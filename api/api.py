import sqlalchemy
from datetime import datetime
from flask import Flask, request, g


# has to be top-level or we can't use the @app.route decorator
app = Flask(__name__)
app.config['db'] = 'sqlite:///access_log.db'
engine = None


def get_db():
    # lazily initialize the database
    global engine
    if engine is None:
        engine = sqlalchemy.create_engine(app.config['db'])
        with engine.connect() as con:
            con.execute('''
                CREATE TABLE IF NOT EXISTS logs (
                    timestamp TEXT PRIMARY KEY,
                    user TEXT NOT NULL,
                    ip TEXT NOT NULL
                );
            ''')

    if 'db' not in g:
        g.db = engine.connect()

    return g.db


def close_db(_):
    db = g.pop('db', None)
    if db is not None:
        db.close()


# close the database connection when done like a good citizen
app.teardown_appcontext(close_db)


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
