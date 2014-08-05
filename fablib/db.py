# -*- encoding: utf-8 -*-

"""
lunaport_agent.fablib.db
~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import sqlite3
from fabric.operations import local

DEFAULT_DB_PATH = './agent_dev_deb.sqlite3'
DEFAULT_SCHEMA_PATH = './deploy/sql/schema.sql'


def db_populate(db_path=DEFAULT_DB_PATH, schema_path=DEFAULT_SCHEMA_PATH):
    """
    Crate new database file with schema and fixture data.
    """
    if os.path.isfile(db_path):
        msg = [
            db_path,
            'db file allready exists, overwrite it? (y/n)',
        ]
        should_rewrite = raw_input('\n'.join(msg))
        if should_rewrite.lower() != 'y':
            print 'Doing nothing'
            return
        else:
            os.unlink(db_path)

    sql = open(schema_path, 'r+').read()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.executescript(sql)
    c.close()
    print 'Db successfully populated: {}'.format(db_path)
