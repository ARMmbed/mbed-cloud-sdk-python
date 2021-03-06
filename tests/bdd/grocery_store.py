"""Fetch some Gherkins"""
import logging
import os
import subprocess

import dotenv


def copy_ignore(src, contents):
    return [c for c in contents if not os.path.exists(c)]


def run():
    """Fetches all the cucumbers

    Basically the same as using a submodule. We should probably just use those.
    https://git-scm.com/book/en/v2/Git-Tools-Submodules
    """
    logging.basicConfig(level=logging.INFO)
    dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True, raise_error_if_not_found=False))
    gh_token = os.getenv("GITHUB_TOKEN")
    grocery_store = os.getenv(
        "GROCERY_STORE",
        "https://{GITHUB_TOKEN}@github.com/ARMmbed/mbed-cloud-sdk-bdd.git",
    )
    logging.info("using token: ***%s", gh_token[-4:])
    grocery_store = grocery_store.format(GITHUB_TOKEN=gh_token)
    bdd_root = os.path.dirname(__file__)
    checkout_dir = os.path.join(bdd_root, "user_stories")
    if not os.path.exists(checkout_dir):
        os.makedirs(checkout_dir)
        subprocess.check_call(["git", "init"], cwd=checkout_dir)
    # subprocess.check_call(['git', 'clone', grocery_store, checkout_dir])
    subprocess.check_call(["git", "pull", "--ff", grocery_store], cwd=checkout_dir)
    logging.info("repository cloned to %s", checkout_dir)
    subprocess.check_call(['python', '-m', 'behave', bdd_root])



__name__ == "__main__" and run()
