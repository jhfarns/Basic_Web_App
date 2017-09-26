#!/usr/bin/env python

from bottle import get, post, route, run, request, response, template, redirect
from collections import namedtuple
from utils import random_string, random_number


User = namedtuple("User", "first_name last_name email username password")


# dict from user_id to user object
users = {}
users[1234] = User(first_name='andrew',
                   last_name='harding',
                   username='andrew',
                   email= 'andrew@isnotcool.com',
                   password='hunter3')

# dict from session_id to user_id
sessions = {}

#dict from usernames to user_id object
usernames = {}
usernames['andrew'] = 1234


def create_user():
    pass


def login():

    validate_username = usernames.get(username)

    if validate_username  ==  None: 
        return 'Wrong Username or Password'
    else:
        mapped_user_id = usernames[username]
    if password != users[mapped_user_id]['Password']:
        return 'Wrong Username or Password'
    else:
        session_id = generate_cookie()
        sessions[session_id] = validate_username 
        response.set_cookie('session', session_id)
        redirect_to_root()


def generate_cookie():
    return random_string(16)


def generate_number():
    return random_number()
    

def redirect_to_login():
    return redirect('/web/login')


def redirect_to_user():
    return redirect('/web/user')


def redirect_to_root():
    return redirect('/')


def login_required(fn):
    def wrapped():
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
        return fn(user)
    return wrapped


@route('/')
@login_required
def root(user):
    return redirect_to_user()


@get('/web/login')
def create_or_login():
    return template('CreateOrLogin') 


@post('/web/login/new')
def login_new():
    username = request.forms.get('username')
    password = request.forms.get('password')
    firstname = request.forms.get('firstname')
    lastname = request.forms.get('lastname')
    email  = request.forms.get('email')

    user_id = generate_number()
    users[user_id] = User(first_name=firstname,
                          last_name=lastname,
                          email=email,
                          username=username,
                          password=password)
    usernames[username] = user_id
    session_id = generate_cookie()
    sessions[session_id] = user_id 
    response.set_cookie('session', session_id, path='/')
 
    return redirect_to_user()


@post('/web/login/existing')
def login_existing():
    username = request.forms.get('username')
    password = request.forms.get('password')
        
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


@get('/web/user/create')
def create_user_page():
    return template('CreateUserPage')


@get('/web/user')
@login_required
def get_user(user):
    return template('UserPage', user=user)


if __main__ == '__main__':
    run(host='localhost', port=8080, debug=True)
