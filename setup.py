import os
from distutils.core import setup

import sophie

readme = open(os.path.join(os.path.dirname(__file__), 'README.rst'))

ver = sophie.get_version()

setup(
    name = 'django-sophie',
    packages = [ 'sophie', ],
    package_data = {
        'sophie': [
            'sophie/templates/*',
            'sophie/tests/*',
            'sophie/media/*',
            'sophie/fixtures/*',
        ]},
    version = ver,
    description = 'A django-based blog engine that runs on more databases',
    long_description = readme.read(),
    url = 'http://github.com/DaNmarner/django-sophie',
    download_url = 'http://github.com/DaNmarner/django-sophie/zipball/%s' % ver,
    author = 'DaNmarner',
    author_email = 'DaNmarner@gmail.com',
    keywords = ['django', 'blog', 'cms'],
    license = 'BSD',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: BSD License',
    ],
)

readme.close()
