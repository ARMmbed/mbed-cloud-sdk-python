import itertools
import logging
import random
import six
import threading
import time

from mbed_cloud.subscribe.observer import Observer

from tests.common import BaseCase

DEFAULT_TIMEOUT = 5


class Test(BaseCase):
    def test_subscribe_first(self):
        obs = Observer()
        a = obs.next()
        b = obs.next()
        obs.notify('a')
        obs.notify('b')
        obs.notify('c')
        self.assertNotEqual(a, b)
        self.assertEqual(a.block(DEFAULT_TIMEOUT), 'a')
        self.assertEqual(b.block(DEFAULT_TIMEOUT), 'b')

    def test_notify_first(self):
        obs = Observer()
        obs.notify('a')
        obs.notify('b')
        obs.notify('c')
        a = obs.next()
        b = obs.next()
        self.assertNotEqual(a, b)
        self.assertEqual(a.block(DEFAULT_TIMEOUT), 'a')
        self.assertEqual(b.block(DEFAULT_TIMEOUT), 'b')

    def test_interleaved(self):
        obs = Observer()
        obs.notify('a')
        a = obs.next()
        b = obs.next()
        c = obs.next()
        obs.notify('b')
        d = obs.next()
        obs.notify('c')
        obs.notify('d')
        obs.notify('e')
        e = obs.next()
        self.assertEqual(a.block(DEFAULT_TIMEOUT), 'a')
        self.assertEqual(b.block(DEFAULT_TIMEOUT), 'b')
        self.assertEqual(c.block(DEFAULT_TIMEOUT), 'c')
        self.assertEqual(d.block(DEFAULT_TIMEOUT), 'd')
        self.assertEqual(e.block(DEFAULT_TIMEOUT), 'e')

    def test_stream(self):
        """Looping over the observer with iteration"""
        obs = Observer()
        n = 7
        # we stream some new values
        for i in range(n):
            obs.notify(dict(i=i))
        # and we can read from them asynchronously
        items = []
        for new_item in itertools.islice(obs, 0, n-1):
            items.append(new_item.block(DEFAULT_TIMEOUT).get('i'))
        self.assertEqual(items, list(range(6)))

    def test_threaded_stream(self):
        """Behaviour in threaded environment"""
        obs = Observer()
        n = 15
        start = threading.Event()
        sleepy = lambda: random.randrange(1, 3) / 1000.0

        def add_values():
            start.wait()
            for i in range(n):
                obs.notify(dict(a_key=i))
                time.sleep(sleepy())

        add = threading.Thread(target=add_values)
        add.daemon = True
        add.start()

        def read_values(result):
            start.wait()
            # finite iteration of infinite generator
            for new_item in itertools.islice(obs, 0, n - 1):
                result.append(new_item.block(timeout=DEFAULT_TIMEOUT).get('a_key'))
                time.sleep(sleepy())

        results = []
        read = threading.Thread(target=read_values, args=(results,))
        read.daemon = True
        read.start()

        start.set()
        add.join(timeout=2*DEFAULT_TIMEOUT)
        read.join(timeout=2*DEFAULT_TIMEOUT)

        self.assertFalse(add.isAlive())
        self.assertFalse(read.isAlive())

        # the sequence of values from all the subscribers
        # should be in the same order as the data was added
        self.assertEqual(results, list(range(n-1)))

    def test_callback(self):
        """Callback is triggered on notification"""
        x = dict(a=1)

        def incr(n):
            x['a'] += n

        obs = Observer()
        obs.add_callback(incr)
        obs.notify(3)

        self.assertEqual(x, dict(a=4))

    def test_callback_add_remove_clear(self):
        """Callbacks can be added and removed"""
        f = lambda: 5
        g = lambda: 6
        obs = Observer()
        obs.add_callback(f)
        obs.add_callback(g)

        obs.remove_callback(f)
        self.assertEqual(obs._callbacks, [g])

        obs.clear_callbacks()
        self.assertEqual(obs._callbacks, [])

    def test_overflow(self):
        """Inbound queue overflows"""
        obs = Observer(queue_size=1)
        obs.notify(1)
        if six.PY3:
            with self.assertLogs(level=logging.WARNING):
                obs.notify(1)
        obs.notify(1)
        self.assertTrue(obs.next().defer().get(timeout=DEFAULT_TIMEOUT))

        # The second waiter will never resolve because the queue was too short
        waiter = obs.next().defer()
        waiter.wait(0.05)
        self.assertFalse(waiter.ready())
