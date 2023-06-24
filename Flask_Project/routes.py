from app import app,db
from flask import render_template,redirect,url_for
import forms
from models import Task
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    tasks=Task.query.all()
    return render_template("index.html",tasks=tasks)


@app.route('/add',methods=['GET','POST'])
def add():
    form=forms.AddTask()
    if form.validate_on_submit():
        t=Task(title =form.title.data,date =datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html",form=form)

@app.route('/base')
def base():
    return render_template("base.html")
