#
# Created : 2018-02-03
#
# @author: Eric Lapouyade
#

import doctest
import unittest
from importlib import import_module
from django.template import Context, Template
from datetime import datetime

# These are my modules that contain doctests:
DOCTEST_MODULES = ()

# unittest.TestLoader will call this when it finds this module:
def load_tests(*args, **kwargs):
    test_all_doctests = unittest.TestSuite()
    for m in DOCTEST_MODULES:
        mod = import_module(m)
        test_all_doctests.addTest(
            doctest.DocTestSuite(mod,globs=globals())
        )
    return test_all_doctests
