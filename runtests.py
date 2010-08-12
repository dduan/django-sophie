#!/usr/bin/env python

from django.conf import settings

if not settings.configured:
    print 'configuring settings'
    settings.configure(
        DATABASE_ENGINE = 'sqlite3',
        SITE_ID = 1,
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

    )

from os.path import dirname, abspath
import sys

from django.test.simple import run_tests

def runtests(*test_args):
    if not test_args:
        test_args = ['sophie']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    failures = run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])


