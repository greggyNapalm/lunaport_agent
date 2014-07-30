# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
import unittest

import lunaport_agent

class DummyCase(unittest.TestCase):
    def test_module_version(self):
        '''
        Smoke test, just importing module.
        '''
        self.assertTrue(getattr(lunaport_agent, '__version__') is not None)
