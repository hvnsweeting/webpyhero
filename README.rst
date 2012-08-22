-----
Deploying Web.py on Heroku
-----

You must use postgresql as your database. Anything else is not supported.

Sign up Heroku
=====
This easy

Learn some commands
=====
    * heroku login

    * heroku config
        This command to show some environment variables, most important is DATABASE_URL 

    * git push heroku master

Add some Heroku fiel
=====
    * requirements.txt
      contains module you need to installs. If you use web.py with postgres,
      you have to add psycopg2 to this file but no need to import it anywhere
      (because web.py do it for you)
    * Procfile
      provide command you need to run your app


Import database
=====
https://devcenter.heroku.com/articles/import-data-heroku-postgres
    ``$ pg_dump -Fc --no-acl --no-owner my_old_postgres > data.dump``

    ``$ PGPASSWORD=<PASS> pg_restore --verbose
    --clean --no-acl --no-owner -h <HOST> -U <USER> -d <DBNAME> -p <PORT> ~/data.dump``

Use heroku-postgres
=====
If you are using *web.py-0.37* or lower, web.py will not direct support use database URL.

This issue is fixed on development version on Github:

https://github.com/webpy/webpy/issues/171

You can use below function::

    def dburl2dict(url):
        dbn, rest = url.split('://', 1)
        user, rest = rest.split(':', 1)
        pw, rest = rest.split('@', 1)
        host, rest = rest.split(':', 1)
        port, rest = rest.split('/', 1)
        db = rest
        return dict(dbn=dbn, user=user, pw=pw, db=db, host=host)

to get a dict and pass it to web.database()::

    d = dburl2dict(YOUR_DATABASE_URL)
    db = web.database(dbn=d['dbn'], 
                        db=d['db'],
                        user=d['user'],
                        pw=d['pw'],
                        host=d['host'],
                        )
    
YOUR_DATABASE_URL has format: 

``postgres://<USER>:<PASS>@<HOST>:<PORT>/<DBNAME>``

which you can see from ``heroku config`` output
