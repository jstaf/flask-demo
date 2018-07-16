import sqlalchemy
from datetime import datetime
from flask import Flask, request


# has to be top-level or we can't use the @app.route decorator
app = Flask(__name__)
app.config['db'] = 'sqlite:///access_log.db'
db = None


@app.route('/hello')
def default_endpoint():
    '''
    Just prints "Hello <name>!" with whatever name the user throws at it. If no
    name is provided, it will return "Hello stranger!". The timestamp, name,
    and originating ip address are logged to a database.
    '''
    name = request.args.get('name', default='stranger')

    get_db().execute(
        'INSERT INTO logs VALUES (:timestamp, :user, :ip);',
        timestamp=datetime.now(), user=name, ip=request.remote_addr)

    return 'Hello {}!'.format(name)


def get_db():
    '''
    Lazily open a single connection to the database, initializing it if not
    already setup. sqlite only supports single-threaded writes, so there's no
    point in having more than one connection (all we're going to do is write).
    '''
    global db
    if db is None:
        db = sqlalchemy.create_engine(app.config['db']).connect()

        # on first connection, create the table we need if it doesn't already
        # exist.
        db.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                -- primary key is the default autoincremented rowid
                timestamp TEXT NOT NULL,
                user TEXT NOT NULL,
                ip TEXT NOT NULL
            );
        ''')

    return db
