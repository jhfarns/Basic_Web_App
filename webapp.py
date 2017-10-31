#!/usr/bin/env python

from bottle import run, request, response, template, redirect, post, Bottle, delete
from collections import namedtuple
from utils import random_string 
from bottle.ext import sqlite


app = Bottle()
plugin = sqlite.Plugin(dbfile='webapp.db')
app.install(plugin)


User = namedtuple("User", "id username password email firstname lastname")


def generate_cookie():
    return random_string(16)


def redirect_to_login():
    return redirect('/web/login')


def redirect_to_user():
    return redirect('/web/user')


def redirect_to_root():
    return redirect('/')


def lookup_user_by_username(db, username):
    user_row = db.execute(
        'SELECT id, username, password, email, firstname, lastname FROM users WHERE username=?',
        (username, )).fetchone()
    if user_row is None:
        return None

    return User._make(user_row)


def lookup_user_by_id(db, user_id):
    user_row = db.execute(
        'SELECT id, username, password, email, firstname, lastname FROM users WHERE id=?',
        (user_id, )).fetchone()
    if user_row is None:
        return None

    return User._make(user_row)



def lookup_user_by_session_cookie(db, cookie):
    row = db.execute(
        'SELECT user_id FROM sessions WHERE cookie=?',
        (cookie, )).fetchone()
    if not row:
        return None
    return lookup_user_by_id(db, row['user_id'])


def create_user(db, user):
    db.execute('INSERT INTO users (username, password, email, firstname, lastname) VALUES (?,?,?,?,?)',
               (user.username, user.password, user.email, user.firstname, user.lastname))
    newUser = lookup_user_by_username(db, user.username)
    return newUser


def create_user_session(db, user):
    cookie = generate_cookie()

    db.execute('INSERT INTO sessions (cookie, user_id) VALUES (?, ?)', (cookie, user.id))

    return cookie


def login_required(fn):
    def wrapped(db):
        cookie = request.get_cookie("session")
        if not cookie:
            # no cookie; need to authenticate
            return redirect_to_login()
        user = lookup_user_by_session_cookie(db, cookie)
        if not user:
            # session does not map to a valid user; need to authenticate
            return redirect_to_login()
        return fn(db, user)
    return wrapped


@app.route('/')
@login_required
def root(db, user):
    return redirect_to_user()


@app.get('/web/login')
def create_or_login():
    return template('CreateOrLogin') 


@app.post('/web/login/new')
def login_new(db):
    username = request.forms.get('username')
    password = request.forms.get('password')
    firstname = request.forms.get('firstname')
    lastname = request.forms.get('lastname')
    email  = request.forms.get('email')
    alldata = username, password, email, firstname, lastname

    user = create_user(db, User(id=None,
                                username=username,
                                password=password,      
                                firstname=firstname,
                                lastname=lastname,
                                email=email))

    cookie = create_user_session(db, user)

    response.set_cookie('session', cookie, path='/')
 
    return redirect_to_user()


@app.post('/web/login/existing')
def login_existing(db):
    username = request.forms.get('username')
    password = request.forms.get('password')

    user = lookup_user_by_username(db, username)
    if not user:
        return redirect_to_login()

    if password != user.password:
        return redirect_to_login()

    cookie = create_user_session(db, user)
    response.set_cookie('session', cookie, path='/')
    return redirect_to_root()


@app.get('/web/user/create')
def create_user_page():
    return template('CreateUserPage')


@app.get('/web/user')
@login_required
def get_user(db, user):
    return template('Editable UserPage', user=user)

@app.get('/web/logout')
@login_required
def logout(db, user):
    cookie = request.get_cookie('session')
    response.delete_cookie('session', path='/') 
    db.execute('DELETE FROM sessions WHERE cookie=?', (cookie, ))
    return redirect('/') 

@app.post('/web/update')
@login_required
def updatesql(db, user):
    username = request.forms.get('username')
    firstname = request.forms.get('firstname')
    lastname = request.forms.get('lastname')
    email  = request.forms.get('email')
    
    db.execute('UPDATE users SET username=?, firstname=?, lastname=?, email=? WHERE username = ?', (username, firstname, lastname, email, user.username))
    
    return redirect_to_root()


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
