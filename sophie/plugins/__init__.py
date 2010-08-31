class PluginMount(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)


class URLStructure:
    __metaclass__ = PluginMount

# Auto-discover the modules under this directory.

from os import listdir
from os.path import basename, dirname

for mod in listdir(dirname(__file__)):
    mod = basename(mod)
    if mod.endswith('.py'):
        if mod == '__init__.py':
            # To prevent duplicate excution of the code in this file
            continue
        mod = mod[:-3]

    try:
        # The code in dicovered modules gets excuted by being imported here
        __import__(mod, globals(), locals(), [], -1)
    except ImportError:
        pass
