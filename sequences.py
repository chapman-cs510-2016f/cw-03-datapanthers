#!/usr/bin/env python

"""Module Description
This function takes the input the user puts in, n, and outputs
the first n sequences of the Fibonacci number sequences
For example, putting in the number 5 will yield the list 1, 1, 2, 3, 5

Please do not input a negative number.  

"""

def fibonacci(n):
    """Function Docstring
    fibonacci(int) -> list 
    
    this function will take in an integer n and finds the n sequences of fibonacci
    and will return the list of the n sequences.
    """
    if n < 0:
        print ("The number is negative. Will change to a positive number")
        n = -n
        
    #setting our initial conditions
    a1, a2 = 1, 1
    final_list = [1]
    counter = 3

    if n == 1:
	    return final_list
    elif n == 2:
        final_list.append(1)
        return final_list
    else:
        final_list.append(1)
        while counter <= n:
            new_num = a1 + a2
            final_list.append(new_num)
            
            # resets the previous number variables
            a1 = a2
            a2 = new_num
            counter = counter + 1
    
    return final_list

def main(argv):
    print (fibonacci(argv))

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print ("Error: did not input a number. Will set a default argument of 5")
        main(5)
    else:
        main(int(argv[1]))



