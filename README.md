flask-demo
=============================================

[![Build Status](https://travis-ci.org/jstaf/flask-demo.svg?branch=master)](https://travis-ci.org/jstaf/flask-demo)

A quick Flask API demo. Returns `Hello <name>!` for any query against a `/hello`
endpoint, and logs the event to a sqlite database. Also comes with tests! Fun!

## To install

The following steps assume you have Python, git, curl, sqlite3,
and optionally virtualenv already installed.
Any currently supported version of Python will work.
(Please refer to your system's package manager to install these dependencies,
though most Linux distributions will come with these installed.)

```bash
git clone https://github.com/jstaf/flask-demo.git
cd flask-demo

# if you want to do things in a Python virtual environment, run these two lines
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Running the tests

If for some reason you don't trust the
[test results from Travis](https://travis-ci.org/jstaf/flask-demo),
you can run `pytest` to run the test suite.
This package has been tested against every currently supported version of Python.

## To run/use the API

To start the API, execute the following in the `flask-demo` directory:

```bash
FLASK_APP=api/api.py flask run -h 0.0.0.0
```

You can make requests against the API using `curl`:

```bash
curl http://localhost:5000/hello
```
```
Hello stranger!
```

Using the `name` parameter:

```bash
curl http://localhost:5000/hello?name=demonstration
```
```
Hello demonstration!
```

To dump the contents of the `access_log.db` to a csv file:

```bash
sqlite3 access_log.db -csv 'SELECT * FROM logs;'
```
```
timestamp,user,ip
"2018-07-16 19:30:13.800317",stranger,127.0.0.1
"2018-07-16 19:30:17.424712",test,127.0.0.1
```
