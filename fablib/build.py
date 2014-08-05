# -*- encoding: utf-8 -*-

"""
lunaport_agent.fablib.build
~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from fabric.operations import local, abort

def say_hello():
    """
    just say hello
    """
    local('ls -lt')
    print 'Ya yA'
