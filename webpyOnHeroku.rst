-----
Deploying Web.py on Heroku
-----

You must use postgresql as your database. Anything else is not supported.

Sign up Heroku
=====

Learn some commands
=====
    heroku login

    heroku config
        This command to show some environment variables, most important is DATABASE_URL 

    git push heroku master

Import database
=====
https://devcenter.heroku.com/articles/import-data-heroku-postgres
    `$ pg_dump -Fc --no-acl --no-owner my_old_postgres > data.dump`
    `$ PGPASSWORD=<PASS> pg_restore --verbose --clean --no-acl --no-owner -h <HOST> -U <USER> -d <DBNAME> -p <PORT> ~/data.dump`

Use heroku-postgres
=====
If you are using web.py-0.37 or lower, web.py will not direct support use database URL.
This issue is fix on development version on Github:

https://github.com/webpy/webpy/issues/171

You can use below function:

    def dburl2dict(url):
        dbn, rest = url.split('://', 1)
        user, rest = rest.split(':', 1)
        pw, rest = rest.split('@', 1)
        host, rest = rest.split(':', 1)
        port, rest = rest.split('/', 1)
        db = rest
        return dict(dbn=dbn, user=user, pw=pw, db=db, host=host)

to get a dict and pass it to web.database():

    d = dburl2dict("postgres://mgzdqjxltjjfbs:TEoACC6-iEkBi8KBudnK3MAI2y@ec2-107-22-163-230.compute-1.amazonaws.com:5432/d8g05oiv7f32o2")
    
    db = web.database(dbn=d['dbn'], 
                        db=d['db'],
                        user=d['user'],
                        pw=d['pw'],
                        host=d['host'],
                        )
    
