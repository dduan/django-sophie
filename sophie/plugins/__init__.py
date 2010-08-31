class PluginMount(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)


class URLStructure:
    __metaclass__ = PluginMount

from os import listdir
from os.path import basename, dirname, isdir

for mod_path in listdir(dirname(__file__)):
    mod_path = basename(mod_path)
    if isdir(mod_path):
        mod_name = mod_path
    elif mod_path.endswith('.py'):
        if basename(mod_path) == '__init__.py':
            continue
        mod_name = mod_path[:-3]
    else:
        continue

    try:
        __import__(basename(mod_name))
    except ImportError:
        pass
