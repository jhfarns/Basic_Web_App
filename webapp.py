#!/usr/bin/env python

from bottle import get, post, route, run, request, response, template, redirect
from utils import random_string, random_number


# dict from user_id to user object
users = {}
users[1234] = {'First Name':'andrew','Last Name': 'harding', 'Email':'andrew@iscool.com','User Name': 'andrew','Password': 'hunter3'}

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


def redirect_to_user(user_id):
    return redirect('/web/user/{}'.format(user_id))


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
        fn(user)
    return wrapped


@route('/')
@login_required
def root(user):
    return redirect_to_user(sessions[request.get_cookie('session')])
#    if request.get_cookie('squidge'):
#        return template('LoginPage')
#    else:
#        response.set_cookie('squidge', generate_cookie())
#        return template('WelcomePage')


@get('/web/login')
def Either_Or():
    return template('CreateOrLogin') 

@post('/web/login')
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    created_username = request.forms.get('created_username')
    created_password = request.forms.get('create_password')
    firstname = request.forms.get('firstname')
    lastname = request.forms.get('lastname')
    email  = request.forms.get('email')
    #update variables with the request.forms.get() for both forms
        
    if email  == None:
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
            response.set_cookie('session', session_id, path='/')
            redirect_to_root()
    else: 
        user_id = generate_number()
        users[user_id] = {'First Name': firstname, 'Last Name': lastname, 'Email': email,
                      'Password': password, 'User Name': username}
        usernames[username] = user_id
        session_id = generate_cookie()
        sessions[session_id] = user_id 
        response.set_cookie('session', session_id, path='/')
 
        return redirect('/web/user/{}'.format(user_id))

    

    # todo(james):
    # 0) change your user [] into a {}
    # 1) look up user by username (requires you building
    #    a mapping between username and users
    # 2) if user doesn't exist, return an error
    # 3) check password against user
    # 4) if password doesn't match, return an error
    # 5) if password matches, create new session id and
    #    store the mapping between session id and user id
    #    in the sessions dict.
    # 6) set a cookie with the session id
    # 7) redirect back to /

#    username = request.forms.get('username') 
#    password = request.forms.get('password')
#
#    list_of_keys = users.keys()
#
#    for a in list_of_keys:
#        if username in users[a]:
#            if password in users[a]:
#                return redirect('/web/user/' + str(a))
#
    return 'user not found'


@get('/web/user/create')
def create_user_page():
    return template('CreateUserPage')


@get('/web/user/<id:int>')
def get_user(id):
    
    validate = users.get(id)
    
    if validate == []:
        return redirect('/')
    else:
        return template('UserPage', name=users[id]['First Name'], lastname=users[id]['Last Name'], email =users[id]['Email'], username=users[id]['User Name']) 


    # todone:
    # 1) look up the user in the in-memory dict using the id you got from
    #    bottle.
    # 2) if found, return a rendered user page, passing the user object into
    #    the template so you can fill out the template with user information.
    # 3) if not found, return a rendered page that says "user not found" or
    #    whatever.


#@post('/api/user')
#def create_user():
#    
#    firstname = request.forms.get('firstname')
#    lastname = request.forms.get('lastname')
#    email = request.forms.get('email')
#    username = request.forms.get('username')
#    password = request.forms.get('password')
#    user_id = generate_number()
#
#    global users 
#
#    users[user_id] = {'First Name': firstname, 'Last Name': lastname, 'Email': email,
#                      'Password': password, 'User Name': username}
#    usernames[username] = user_id
#
##    users.setdefault(user_id, [])
##    
##    for addData in (firstname, lastname, email, username, password):
##        users[user_id].append(addData)
##
#
#    return redirect('/web/user/' + str(user_id))
#
#    # TODONE:
#    # 1) generate a random id for the new user
#    # 2) store the new user in some in-memory dict that maps from the id
#    #    to their user info.
#    # 3) return a response that redirects the browser to the /web/user/<id>
#    #    page for that user.
#

run(host='0.0.0.0', port=8080, debug=True)
