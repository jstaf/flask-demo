flask-demo
=============================================

A quick Flask API demo. Returns `Hello <name>!` for any query against a `/hello`
endpoint, and logs the event to a sqlite database. Also comes with tests! Fun!

## To install

The following steps assume you have Python, git, curl,
and optionally `virtualenv` already installed.

```bash
git clone https://github.com/jstaf/flask-demo.git
cd flask-demo

# if you want to do things in a virtual environment, run these two lines
virtualenv --python=python3 venv
source venv/bin/activate

pip install -r requirements.txt
```

## To run/use the API

To start the API, execute the following in the `flask-demo` directory:

```bash
FLASK_APP=api/api.py flask run
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
1531782629.28172,stranger,127.0.0.1
1531782634.38134,demonstration,127.0.0.1
```

## Running the tests

Just run `pytest` to run the test suite.
