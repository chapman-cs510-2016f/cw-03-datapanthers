#!/usr/bin/env python

import sequences

# this function imports the sequences.py and tests the fibonacci function to check if it returns the expected list. 
def test_fibonacci():
    fib_list=sequences.fibonacci(5)
    test_list=[1,1,2,3,5]
    assert fib_list == test_list

    fib_list=sequences.fibonacci(1)
    test_list=[1]
    assert fib_list == test_list

    fib_list=sequences.fibonacci(10)
    test_list=[1,1,2,3,5,8,13,21,34,55]
    assert fib_list == test_list

    # test to make sure negative input works
    fib_list=sequences.fibonacci(-5)
    test_list=[1,1,2,3,5]
    assert fib_list == test_list