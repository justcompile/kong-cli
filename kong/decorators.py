from __future__ import unicode_literals
from functools import update_wrapper
from click import echo, prompt

from kong.config import Config


def verify_config(f):
    def new_func(*args, **kwargs):
        c = Config()

        if not c.exists():
            value = prompt('Please enter the base url for your Kong Admin interface')
            c.save(base_url=value)

        if args[0].obj is not {}:
            args[0].obj = {}

        args[0].obj['base_url'] = c.load()['base_url']

        return f(*args, **kwargs)
    return update_wrapper(new_func, f)
