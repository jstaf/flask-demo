import sqlalchemy
from datetime import datetime
from flask import Flask, request


DB_CON = None


def create_app(db_uri):
    '''
    The initialization function used to start the API.
    '''
    app = Flask(__name__)
    app.config['db'] = db_uri

    # create the table we need if it doesn't already exist
    con = sqlalchemy.create_engine(db_uri).connect()
    con.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            -- primary key is the default autoincremented rowid in this case
            timestamp REAL NOT NULL,
            user TEXT NOT NULL,
            ip TEXT NOT NULL
        );
    ''')
    con.close()

    return app


# has to be top-level or we can't use the @app.route decorator
app = create_app('sqlite:///access_log.db')


@app.route('/hello')
def default_endpoint():
    '''
    Just prints "Hello <name>!" with whatever name the user throws at it. If no
    name is provided, it will return "Hello stranger!". The timestamp, name,
    and originating ip address are logged to a database.
    '''
    name = request.args.get('name', default='stranger')

    # log the access in our database for later analysis
    get_db().execute(
        'INSERT INTO logs VALUES (:timestamp, :user, :ip);',
        timestamp=datetime.now().timestamp(), user=name, ip=request.remote_addr)

    return 'Hello {}!'.format(name)


def get_db():
    '''
    Lazily open a single connection to the database. sqlite only supports
    single-threaded writes, so we don't want a whole bunch of concurrent db
    connections.
    '''
    global DB_CON
    if DB_CON is None:
        DB_CON = sqlalchemy.create_engine(app.config['db']).connect()

    return DB_CON


if __name__ == '__main__':
    app.run()
