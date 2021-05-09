# Fotografia Editor

## About
Fotographia was created by Stavros Panakakis, Sophia Tsivoula,
Christos Milios and Dimitris Pramateftakis as an assignment for
their univeristy's python course.


Fotographia is using python flask under the hood and it is
hosted over on Heroku.

## Installation
You should have [Python 3.9](https://www.python.org/downloads/release/python-390/) and [Pip](https://pip.pypa.io/en/stable/installing/) installed.
```
# Clone the repository 
$ git clone https://github.com/Fotographia/fotographia-editor.git

# Navigate to the project's folder
$ cd fotographia-editor

# Install virtualenv
$ pip install virtualenv

# Create a python virtual envinonment
$ python -m virtualenv venv

# Enter the environment
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Export envinonment variables
$ export PORT=5000
$ export FLASK_ENV=development

# Run application
$ python wsgi.py
```