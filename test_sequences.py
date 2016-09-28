#!/usr/bin/env python

import sequences

# this function imports the sequences.py and tests the fibonacci function to check if it returns the expected list. 
def test_fibonacci():
    fib_list=sequences.fibonacci(5)
    test_list=[1,1,2,3,5]
    assert fib_list == test_list
    
    #
    ### INSTRUCTOR COMMENT:
    # It is better to have each assert run in a separate test function. They are really separate tests that way.
    # Also, it may be more clear in this case to skip defining so many intermediate variables:
    #     assert sequences.fibonacci(1) == [1]
    #
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
