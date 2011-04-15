#!/usr/bin/env python
from bottle import route, run, get, post, view, debug, static_file, request

if __name__ != '__main__':
    import os
    os.chdir(os.path.dirname(__file__))
    import sys
    sys.path = ['.'] + sys.path


import basics
from player.web import *

#@route('/index')
@get('/')
@view('index')
def index():
    msg = request.GET.get('msg')
    data = {}
    if not msg:
        msg = "all"
    cards = [basics.card("A","S"), basics.card("J","S")]
    played_cards = [basics.card("9","C"), basics.card("J","D"), basics.card("Q","C"), basics.card("A","H")]

    show = {'msg':msg, 'played_cards':played_cards, 'cards':cards, 'suits':1, 'yesno':1, 'next':1}
    if 'error' in data:
        show['error'] = data['error']
    return show	


#@route('/index', method='POST')
@post('/')
@view('index')
def index():
    result = request.forms.get('result')
    msg = request.forms.get('msg')
    data = {}
    cards = [basics.card("A","S"), basics.card("J","S")]
    played_cards = [basics.card("9","C"), basics.card("J","D"), basics.card("Q","C"), basics.card("A","H")]
    show = {'msg': msg, 'result': result, 'played_cards':played_cards, 'cards':cards, 'suits':1, 'yesno':1, 'next':1}
    
    if 'error' in data:
        show['error'] = data['error']
    return show	
@route('/game')
def game():
    msg = "up? "
    result = 99
    if (msg[:7] == "The win"): # Results
        result = 4
    elif (msg[-6:] == "play? "): # Play
        result = 3
    elif (msg[-4:] == "up? "):#Bid
        result = 0
    elif (msg[-6:] == "Pass? "): # Bid
        result = 1
    elif (msg[-9:] == "discard? "): # Pick it Up
        result = 2
    else: # Bad
        pass
    return result

@route('/favicon.ico')
def send_image():
    return static_file('favicon.ico', root='./pics', mimetype='image/x-icon')

@route('/static/:filename#.*\.gif#')
def send_image(filename):
    return static_file(filename, root='./pics', mimetype='image/gif')
    
@route('/static/:filename')
def send_static(filename):
    return static_file(filename, root='./static')

if __name__ == '__main__':
    debug(True)
    run(host='0.0.0.0', port=8181, reloader=True)
    
else:
    from bottle import default_app
    application=default_app()

