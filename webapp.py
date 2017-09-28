#!/usr/bin/env python

import bottle
from bottle import run, request, response, template, redirect
from collections import namedtuple
from utils import random_string, random_number

app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='webapp.db')
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


def create_user(db, user):
    # TODO(james):
    # 1) insert the new row into the users table.
    # 2) fill in the id attribute of the user namedtuple with the users id column value
    # 3) return the modified user namedtuple.
    pass

def lookup_user_by_session_cookie(db, cookie):
    # TODO(james):
    # look up the user row where the id column is the same as the
    # sessions row user_id column and the cookie column value matches the cookie passed into
    # this function.
    #
    # fill out a user namedtuple from the results and return it.
    pass


def create_user_session(db, user):
    # TODO(james):
    # generate a new cookie value (via generate_cookie)
    # insert a new sessions row, where the user_id column matches the id of the passed in user
    # and the cookie column matches the generated cookie value.
    # return the cookie value.
    pass


def login_required(fn):
    def wrapped(db):
        # TODO(james):
        # look up user via session cookie
        # pass user into decorated function


        session_id = request.get_cookie("session")
        if not session_id:
            # no cookie; need to authenticate
            return redirect_to_login()
        user_id = sessions.get(session_id)
        if not user_id:
            # session_id isn't valid; need to authenticate
            return redirect_to_login()
        user = users.get(user_id)
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

    # TODO(james):
    # look up the user based on the username
    # validate the password matches
    # create a session for the user and return the session cookie
        
    user_id = usernames.get(username)
    if user_id  ==  None: 
        return 'Wrong Username or Password (1)'

    user = users.get(user_id)
    if not user:
        return "Wrong Username or Password (2)"

    if password != user.password:
        return 'Wrong Username or Password (expected {}, got {})'.format(user.password, password)

    session_id = generate_cookie()
    sessions[session_id] = user_id 
    response.set_cookie('session', session_id, path='/')
    return redirect_to_root()


@app.get('/web/user/create')
def create_user_page():
    return template('CreateUserPage')


@app.get('/web/user')
@login_required
def get_user(db, user):
    return template('UserPage', user=user)


if __main__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
