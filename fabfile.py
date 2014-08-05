# -*- encoding: utf-8 -*-

"""
agent.fabfile
~~~~~~~~~~~~~

Build jobs here.
"""

from fablib.db import *


def help():
    from fabric.api import local
    local('fab -l')
