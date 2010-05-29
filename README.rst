django-sophie
=============

Sophie is just another django-based blog engine.

Here are a few goals of the design of *Sophie*:

    *   Follow Django Applications' pluggability convention.
    *   Maintain a data structure such that more db bankends 
        can be used. Specifically, Sophie should be able to
        run on all the database django officially supports,
        plus (for now) Google Bigtable, aka GAE. This means
        this app is Django-future-support-of-NoSQL-dbs aware.
    *   Be usable and hopefully, useful. 
        
