# My-Diary-V1
The API for my online journal where users can pen down their thoughts and feelings.

## Badges
<a href='https://coveralls.io/github/Bakley/My-Diary-V1?branch=master'><img src='https://coveralls.io/repos/github/Bakley/My-Diary-V1/badge.svg?branch=master' alt='Coverage Status' /></a> 
[![Build Status](https://travis-ci.com/Bakley/My-Diary-V1.svg?branch=develop)](https://travis-ci.com/Bakley/My-Diary-V1)
[![Maintainability](https://api.codeclimate.com/v1/badges/1be49d5566955442e2d8/maintainability)](https://codeclimate.com/github/Bakley/My-Diary-V1/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1be49d5566955442e2d8/test_coverage)](https://codeclimate.com/github/Bakley/My-Diary-V1/test_coverage)

## Prerequisites
* [Python3](https://www.python.org/) (A programming language) 
* [Flask](http://flask.pocoo.org/) (A Python microframework)

* [Virtualenv](https://virtualenv.pypa.io/en/stable/) (Stores all dependencies used in the project)

* [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)

* [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)

* [Vscode](https://code.visualstudio.com/download) (Preffered Code Editor)

* [PostgreSQL](https://www.postgresql.org/) (Relational database management systems)


## Install the Packages from the Ubuntu Repositories
To begin the process, we'll download and install all of the items we need from the Ubuntu repositories. We will use the Python package manager `pip` to install additional components a bit later.
Since we are using Flask with Python 3, type:

```
sudo apt-get update

sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib 
```
This will install pip, the Python development files needed to build Gunicorn later, the Postgres database system and the libraries needed to interact with it.

## Create the PostgreSQL Database and User
Log into an interactive Postgres session by typing:
```
sudo -u postgres psql
```
You will be given a PostgreSQL prompt where we can set up our requirements.

First, create a database for our project:
```
CREATE DATABASE mydiary;
```
Next, create a database user for our project. Make sure to select a secure password:

```
CREATE USER mydiaryuser WITH PASSWORD 'fake_sticker_pyconke17#';
```


```
ALTER ROLE mydiaryuser  SET client_encoding TO 'utf8';
ALTER ROLE mydiaryuser  SET default_transaction_isolation TO 'read committed';
ALTER ROLE mydiaryuser  SET timezone TO 'Africa/Nairobi';
```

Now, we can give our new user access to administer our new database:

```
GRANT ALL PRIVILEGES ON DATABASE mydiary TO mydiaryuser ;
```

When you are finished, exit out of the PostgreSQL prompt by typing:
```
\q
```

## How to get Started ;-)
Hi there, lets start by making a directory where we will work on. 
Simply Open your terminal and then:
```
mkdir myDiary && cd myDiary
```

## Create a Python Virtual Environment for our Project
Since we are using Python 3, create a virtual environment called `venv` by typing:
```
virtualenv -p python3 venv
```
Before we install our project's Python requirements, we need to activate the virtual environment. You can do that by typing:
```
source venv/bin/activate
```

## Clone and Configure a New Flask Project
Login into your github account and open the project folder then follow the instruction on how to clone the existing project. It should be something similar to:
```
git clone https://<github_account>@github.org/<your_github_username>/My-Diary-V1.git
```
Next, install the requirements by typing:
```
pip install -r requirements.txt
```
## How to run the app
Tell your terminal the application to work with by exporting the ```FLASK_APP``` environment variable:

$ export FLASK_APP=route.py
$ flask run
 * Running on http://127.0.0.1:5000/

If you are on Windows you need to use ```set``` instead of ```export```

Alternatively you can use ```python -m flask:```

$ export FLASK_APP=route.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/

 Now head over to http://127.0.0.1:5000/ and check what you see ;-)

