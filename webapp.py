#!/usr/bin/env python

from bottle import get, post, route, run, request, response, template, redirect
from utils import random_string, random_number

users = {92:'values', 1: 'this is the voice'}

users1 = {}

def generate_cookie():
    return random_string(16)

def generate_number():
    return random_number()

@route('/hello')
@route('/')
def hello():
    if request.get_cookie('squidge'):
        return template('Welcomeback')
    else:
        response.set_cookie('squidge', generate_cookie())
    return template('LoginPage') 


@get('/web/user/create')
def create_user_page():
    return template('LoginPage')


@get('/web/user/<id:int>')
def get_user(id):

    return users1[id]

    # TODO(james):
    # 1) look up the user in the in-memory dict using the id you got from
    #    bottle.
    # 2) if found, return a rendered user page, passing the user object into
    #    the template so you can fill out the template with user information.
    # 3) if not found, return a rendered page that says "user not found" or
    #    whatever.
    pass


@post('/api/user')
def create_user():
    firstname = request.forms.get('firstname')
    lastname = request.forms.get('lastname')
    email = request.forms.get('email')
    username = request.forms.get('username')
    password = request.forms.get('password')
    user_id = generate_number()

    global users1 

    users1.setdefault(user_id, [])
    
    for addData in (firstname, lastname, email, username, password):
        users1[user_id].append(addData)


    return redirect('/web/user/' + str(user_id))

    # TODO(james):
    # 1) generate a random id for the new user
    # 2) store the new user in some in-memory dict that maps from the id
    #    to their user info.
    # 3) return a response that redirects the browser to the /web/user/<id>
    #    page for that user.


run(host='0.0.0.0', port=8080, debug=True)
