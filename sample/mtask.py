#!/usr/bin/env python

#TODO add form validator
import web
import datetime
import model

urls = (
        '/', 'Index'
)

def round_date(delta):
    if delta.seconds > 0:
        return delta.days + 1
    elif delta.days > 0:
        return delta.days
    else:
        return 0


def get_days_left(end_date):
    date_format = "%d-%m-%Y"
    today = datetime.datetime.today()
    return round_date(datetime.datetime.strptime(end_date, date_format) - today)


def check_date_format(datestring):
    date_format = "%d-%m-%Y"
    try:
        datetime.datetime.strptime(datestring, date_format)
        return True
    except ValueError:
        return False


def multi_string(freq, string='*'):
    return freq * string


t_globals = {
        'multi_string' : multi_string,
        }

#template
render = web.template.render('templates', base='base', globals=t_globals)

class Index:

    form = web.form.Form(

            web.form.Textbox('task', web.form.notnull),
            web.form.Textbox('startdate', web.form.Validator('enter dd-mm-yyyy', check_date_format)),
            web.form.Textbox('enddate', web.form.Validator('enter dd-mm-yyyy', check_date_format)),
            web.form.Textbox('priority', web.form.Validator('must < 10', lambda x: int(x)<10)),
            web.form.Button('Add task'),
            )

    def GET(self):
        tasks = model.get_tasks()
        tasks = [dict(task=row['task'], start=row['startdate'], end=row['enddate'], priority=row['priority'], \
                diff=get_days_left(row['enddate']))\
                for row in tasks]
        form = self.form()
        return render.index(tasks, form)

    def POST(self):
        """add new task"""
        form = self.form()

        if not form.validates():
            tasks = model.get_tasks()
            tasks = [dict(task=row['task'], start=row['startdate'], end=row['enddate'], priority=row['priority'], \
                diff=get_days_left(row['enddate']))\
                for row in tasks]
            return render.index(tasks, form)

        model.new_task(form.d.task, form.d.startdate, form.d.enddate, form.d.priority)
        raise web.seeother('/')

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
