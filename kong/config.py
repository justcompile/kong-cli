import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Config(object):
    def __init__(self):
        self._config = None

    def exists(self):
        return os.path.exists(self.__config_path())

    def load(self):
        self._config = load(open(self.__config_path()), Loader=Loader)
        return self._config

    def save(self, **kwargs):
        data = {}
        path = self.__config_path()
        if self.exists():
            data = self.load()

        data.update(kwargs)
        with open(path, 'w+') as fp:
            fp.write(dump(data, Dumper=Dumper))

    def __config_path(self):
        return os.path.join(
            os.path.expanduser('~'),
            '.kong-cli.conf'
        )
