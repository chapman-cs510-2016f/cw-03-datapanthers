#!/usr/bin/env python

import sequences

def test_fibonacci():
    fib_list=sequences.fibonacci(5)
    test_list=[1,1,2,3,5]
    assert fib_list == test_list
    print "test 1 true"
    
    fib_list=sequences.fibonacci(1)
    test_list=[1]
    assert fib_list == test_list
    print "test 2 true"

    fib_list=sequences.fibonacci(10)
    test_list=[1,1,2,3,5,8,13,21,34,55]
    assert fib_list == test_list
    print "test 3 true"
