#!/usr/bin/env python

from bottle import route, run, request, response
import randGen

value = randGen.randNum()

@route('/hello')
@route('/')
def hello():
    if request.get_cookie('squidge'):
        return 'Squidge welcomes you back to Squindistries!'
    else:
        response.set_cookie('squidge', value)
    return "Squidge welcomes you to Squindistries!"


run(host='localhost', port=8080, debug=True)
