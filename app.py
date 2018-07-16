from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def default_endpoint():
    '''
    Just prints "Hello <name>!" with whatever name the user throws at it. If no
    name is provided, it will return "Hello stranger!"
    '''
    name = request.args.get('name', default='stranger')
    return 'Hello {}!'.format(name)
