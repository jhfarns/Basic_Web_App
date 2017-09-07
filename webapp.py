#!/usr/bin/env python

from bottle import route, run, request, response, template, TEMPLATE_PATH
from utils import random_string

def generate_cookie():
    return random_string(16)

@route('/hello')
@route('/')
def hello():
    if request.get_cookie('squidge'):
        return template('Welcomeback')
    else:
        response.set_cookie('squidge', generate_cookie())
    return template('LoginPage') 


run(host='localhost', port=8080, debug=True)
