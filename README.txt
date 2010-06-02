django-sophie
=============

Sophie is just another django-based blog engine, that could run on
a bit more database backend than usual.

Design Goals
------------

Here are a few goals of the design of *Sophie*:

    *   Reusability to end users.
    *   Maintain a data structure such that more DB bankends 
        can be used. Specifically, Sophie should be able to
        run on all the database django officially supports,
        plus (for now) Google Bigtable, aka GAE. This means
        this app is Django-future-support-of-NoSQL-DBs aware.
    *   Be usable and hopefully, useful. 

To Developers
-------------

This is a *boring* Django-based project that does nothing more than
simply applying plain Django knowledge found in the official docs as
well as a couple of related books. Feel free to checkout the code and
help out, but expect no technical innovation :).
