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
    if form.validate_on_submit():
        post = form.field.data
        flash('Your post is now live!')
        return redirect(url_for('index'))
    
    #page = request.args.get('page', 1, type=int)
    return render_template('index.html', title='Home', form=form,
                           post=post)