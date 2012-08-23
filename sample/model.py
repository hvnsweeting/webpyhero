import web
#import psycopg2

#postgres://mgzdqjxltjjfbs:TEoACC6-iEkBi8KBudnK3MAI2y@ec2-107-22-163-230.compute-1.amazonaws.com:5432/d8g05oiv7f32o2

def dburl2dict(url):
    dbn, rest = url.split('://', 1)
    user, rest = rest.split(':', 1)
    pw, rest = rest.split('@', 1)
    host, rest = rest.split(':', 1)
    port, rest = rest.split('/', 1)
    db = rest
    return dict(dbn=dbn, user=user, pw=pw, db=db, host=host)

d = dburl2dict("postgres://mgzdqjxltjjfbs:TEoACC6-iEkBi8KBudnK3MAI2y@ec2-107-22-163-230.compute-1.amazonaws.com:5432/d8g05oiv7f32o2")

db = web.database(dbn=d['dbn'], 
                    db=d['db'],
                    user=d['user'],
                    pw=d['pw'],
                    host=d['host'],
                    )

def get_tasks():
	return db.select('tasks', order='enddate, priority DESC')

def new_task(task, startdate, enddate, priority):
	db.insert('tasks', task=task, startdate=startdate, enddate=enddate, priority=priority)
