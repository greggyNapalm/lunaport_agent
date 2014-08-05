#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
lunaport_agent.wgi
~~~~~~~~~~~~~~~~~~

Describes  WSGI application.
"""

import os

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from flask.ext.sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config.from_envvar('LUNAPORT_AGENT_CFG')
app.wsgi_app = ProxyFix(app.wsgi_app)  # Fix for old proxyes
db = SQLAlchemy(app)

if os.environ.get('LUNAPORT_ENV') == 'production':
    sentry = Sentry(app, dsn=app.config.get('SENTRY_DSN'))
    sentry.init_app(app)

from plugg_views import User, Job
from helpers import auth_required

user_ident = auth_required(User.UserIdent.as_view('user_ident'))
user_view = auth_required(User.User.as_view('user'))
job_view = auth_required(Test.Test.as_view('test'))

app.add_url_rule('/api/v1.0/userident/', view_func=user_ident, methods=['GET'])
app.add_url_rule('/api/v1.0/user/', defaults={'login': None}, view_func=user_view, methods=['GET'])
app.add_url_rule('/api/v1.0/user/', view_func=user_view, methods=['POST'])
app.add_url_rule('/api/v1.0/user/<login>', view_func=user_view, methods=['GET', 'PATCH'])

app.add_url_rule('/api/v1.0/job/', defaults={'job_id': None}, view_func=test_view, methods=['GET'])
app.add_url_rule('/api/v1.0/job/', view_func=test_view, methods=['POST'])
app.add_url_rule('/api/v1.0/job/<int:job_id>', view_func=test_view, methods=['GET', 'PATCH', 'DELETE'])
