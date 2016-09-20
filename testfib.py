#!/usr/bin/env python

import fib

def test_fib():
    # test when input is 5
    test=5
    result=fib.main(5)
    assert test==result, "result = " + str(result)
    
    # test when input 1
    test=1
    result=fib.main(1)
    assert test==result, "result = " + str(result)
    
    # test when input is 2
    test=1
    result=fib.main(1)
    assert test==result, "result = " + str(result)
    
    # test when input is a negative number
    test=5
    result=fib.main(-5)
    assert test==result, "result = " + str(result)