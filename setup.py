import os
from distutils.core import setup

from sophie import VERSION

readme = open(os.path.join(os.path.dirname(__file__), 'README.txt'))

setup(
    name = 'django-sophie',
    packages = ['sophie'],
    version = '.'.join(map(str, VERSION)),
    description = 'Just another django-based blog engine',
    long_description = readme.read(),
    author = 'DaNmarner',
    author_email = 'DaNmarner@gmail.com',
    key_words = ['django', 'blog', 'cms'],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

readme.close()
