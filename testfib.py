#!/usr/bin/env python

import fib

def test_fib():
    test=5
    result=fib.main(5)
    assert test==result, "result = " + str(result)
