'''
Make sure the API actually works...
'''


def test_endpoint_no_arg(client):
    r = client.get('/hello')
    assert b'Hello stranger!' in r.data


def test_endpoint_with_arg(client):
    r = client.get('/hello?name=user')
    assert b'Hello user!' in r.data
