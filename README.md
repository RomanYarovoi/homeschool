# homeschool

An app for homeschool planning

## Setup

Create a virtual environment.

```bash
$ python -m venv venv
```

Activate the virtual environment.

```bash
$ source venv/bin/activate
```

Install developer and application packages.

Note: `pygraphviz` requires `graphviz`
so you may need to install that first.
On homebrew on a Mac,
you can install that tool
with `brew install graphviz`.

```bash
$ pip install -r requirements-dev.txt
$ pip install -r requirements.txt
```

Install [Heroku CLI tools](https://devcenter.heroku.com/articles/heroku-cli).

Bootstrap the local database.

```bash
$ ./manage.py migrate
```

Create a superuser account.

```bash
$ ./manage.py createsuperuser
```

Start the local web server.

```bash
$ make
```
