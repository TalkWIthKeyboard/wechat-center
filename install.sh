#!/usr/bin/env bash
pip install virtualenv
virtualenv flask
flask/bin/pip install --upgrade pip
flask/bin/pip install setuptools --no-use-wheel --upgrade
flask/bin/pip install flask==0.9
flask/bin/pip install APScheduler
flask/bin/pip install uwsgi
flask/bin/pip install flask_mongoengine
flask/bin/pip install flask_apscheduler
