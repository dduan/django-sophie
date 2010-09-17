from sophie.utils import blog_bit, page_bit

class PluginMount(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)


class URLStructure:
    __metaclass__ = PluginMount
    urlpatterns = ()
    pagination_suffix = False
    blog_prefix = True

    @classmethod
    def get_patterns(cls):
        if cls.blog_prefix:
            cls._add_blog_prefix()
        if cls.pagination:
            cls._add_pagination_suffix()
        return cls.urlpatterns

    @classmethod
    def _add_blog_prefix(cls):
        for p,i in enumerate(cls.urlpatterns):
            cls.urlpatterns[i] = blog_bit + p

    @classmethod
    def _add_pagination_suffix(cls):
        for i in range(len(cls.urlpatterns)):
            cls.urlpatterns[i] += page_bit


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
