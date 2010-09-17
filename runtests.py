#!/usr/bin/env python

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE = 'sqlite3',
        TEMPLATE_LOADERS = (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
        ),
        INSTALLED_APPS = (
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'django.contrib.sitemaps',
            'sophie',
        ),
        ROOT_URLCONF = 'sophie.tests.base_urls',
        SOPHIE_ENABLES_MULTIBLOG = True,
        SITE_ID = 1,
    )

from os.path import dirname, abspath
import sys

from django.test.simple import run_tests

def runtests(*test_args):
    if not test_args:
        test_args = ['sophie']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=1)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])


