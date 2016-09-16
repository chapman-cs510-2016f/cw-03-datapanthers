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
    and will return the list of the n sequences. This function has a catch to see if the user
    input is a negative number, in which an error message will display, the number converted
    to its non-negative equivalent, and then the function runs with the new positive input.
    """
    if n < 0:
        print ("The number is negative. Will change to a positive number")
        n = -n
        
    #setting our initial condition variables, list, and counter variable at 3
    a1, a2 = 1, 1
    final_list = [1]
    counter = 3

    #first checks if the user input was numbers 1 or 2 as those are part of our initial conditons 
    #then returns the list appropriately
    if n == 1:
	    return final_list
    elif n == 2:
        final_list.append(1)
        return final_list
    #if the inputed number is greater than 2, we initiate our code to calculate the fibonacci sequences
    else:
    # append 1 to the list, 
    # now our lists starts with two 1s, per our initial conditions
        final_list.append(1)
        #while our counter is less than or equal to the user input, we add the previous two numbers
        #of the list, append it to our list, then reset our variables
        while counter <= n:
            a1, a2 = a2, a1 + a2 
            final_list.append(a2)
            
            # push up the counter
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



