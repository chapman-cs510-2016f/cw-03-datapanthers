#!/usr/bin/env python

import fib

def test_fib():
    test_list=[5]
    fib_list=fib()
    assert test_list==fib_list
    print "it is true"
