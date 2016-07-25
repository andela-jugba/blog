from flask import render_template, url_for, redirect, session, request
from datetime import datetime
from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            # db.session.commit() #not needed of the config sets SQLALCHEMY_COMMIT_ON_TEARDOWN == True
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.index'))

    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', current_date=datetime.utcnow(), form=form, name=session.get('name'),
                           known=session.get('known', False))

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
