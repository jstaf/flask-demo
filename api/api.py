from flask import Flask, request


def create_app():
    '''
    The initialization function used to start the API.
    '''
    app = Flask(__name__)
    return app


# has to be top-level or we can't use the @app.route decorator
app = create_app()


@app.route('/hello')
def default_endpoint():
    '''
    Just prints "Hello <name>!" with whatever name the user throws at it. If no
    name is provided, it will return "Hello stranger!"
    '''
    name = request.args.get('name', default='stranger')
    return 'Hello {}!'.format(name)


if __name__ == '__main__':
    app.run()
