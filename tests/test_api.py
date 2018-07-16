'''
Make sure the API actually works...
'''


def test_endpoint_no_arg(client):
    r = client.get('/hello')
    assert b'Hello stranger!' in r.data


def test_endpoint_with_arg(client):
    r = client.get('/hello?name=user')
    assert b'Hello user!' in r.data


def test_db_insert(client, db):
    client.get('/hello?name=database')
    results = db.execute('SELECT * FROM logs WHERE user="database";').fetchall()
    assert results[0][1] == 'database'


def test_db_sql_inject(client, db):
    client.get('/hello?name=DROP TABLE logs; --')
    results = db.execute('SELECT * FROM logs WHERE user LIKE "DROP%";').fetchall()
    assert results[0][1] == 'DROP TABLE logs; --'
