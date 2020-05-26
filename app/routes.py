from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app
from app.forms import ExampleForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ExampleForm()
    post = ''
    if form.validate_on_submit():
        post = form.field.data
        flash(f'Accepted! Content: {post}')
        return redirect(url_for('index'))
        # Your job is to add to database. This is just a simple kickstarter
    
    return render_template('index.html', title='Home', form=form,
                           posts=post)

@app.route('/page2', methods=['GET', 'POST'])
def page2():   
    return 'Comming Soon!'