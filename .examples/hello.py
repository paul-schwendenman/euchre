from bottle import get, post, route, run, static_file, error, debug, request

def check_login(user, password):
    def hash(str):
        return str
    a = {"user":"password","paul":"shit"}
    result = 0
    if user in a:
        if a[user] == hash(password):
            result = 1
    return result

@route('/')
@route('/index.html')
def index():
    return """<a href='/hello'>Hello</a><br />
            <a href='/login'>Login</a>"""
    
@route('/hello')
def hello():
    return "Hello World!"
    
@route('/hello/:name')
def hello(name):
    return "Hello %sjoe !" % name    

#@route('/login')
@get('/login')
def login_form():
    return '''<form method="POST" action="">
                <input name="name"     type="text" /><br />
                <input name="password" type="password" /><br />
                <input name="button" type="button" /><br />
                <input name="submit"   type="submit" />
              </form>'''

#@route('/login', method='POST')
@post('/login')
def login_submit():
    name     = request.forms.get('name')
    password = request.forms.get('password')
    if check_login(name, password):
        return "<p>Your login was correct</p>"
    else:
        return "<p>Login failed</p>"
#@route('/button')
@get('/button')
def button():
    return '''<form method="POST" action="">
                <input name="button" type="button" /><br />
                <input name="sub1"   type="submit" />
                <input name="sub2"   type="submit" />
              </form>'''

#@route('/button', method='POST')
@post('/button ')
def button():
    submit     = request.forms.get('submit')
    button1     = request.forms.get('button')
    print button1, submit
@route('/static/:path#.+#')
def server_static(path):
    return static_file(path, root='/path/to/your/static/files')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/images/:filename#.*\.png#')
def send_image(filename):
    return static_file(filename, root='/path/to/image/files', mimetype='image/png')

@route('/download/:filename')
def download(filename):
    return static_file(filename, root='/path/to/static/files', download=filename)

if __name__ == '__main__':
    debug()
    run(host='localhost', port=8080)
    

