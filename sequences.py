#!/usr/bin/env python

#
### INSTRUCTOR COMMENTS:
# Note that the phrases "Module description" and "Function docstring" should not
# actually appear in docstrings. Instead, you should put the name and/or brief
# description of what the function/module does.
#

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
    #
    ### INSTRUCTOR COMMENT:
    # Make sure your docstrings are good English. I think you mean that the function takes
    # an integer n and returns a sequence of the first n fibonacci numbers. It does not return
    # multiple sequences. You also don't need to explain the logic of the code in a docstring,
    # just the purpose, expected inputs, and output. Saying that a positive integer is expected
    # as an input is sufficient.
    #
    if n < 0:
        print ("The number is negative. Will change to a positive number")
        #
        ### INSTRUCTOR COMMENT:
        # Automatically correcting inputs like this is a bad idea. It can hide errors.
        # Instead, raise an exception if the input is actually bad.  Something like:
        #    if not (isinstance(n, int) and n > 0):
        #        raise TypeError("Not a positive integer")
        # Then a user is informed forcibly if they misuse your code, rather than having their
        # error hidden from view.
        #
        # Also, it is usually bad to mix print statements with running code like this.
        # There is no guarantee that this code will be running somewhere where you can see a
        # print statement. It is much better to raise an exception in the event of an error.
        #
        n = -n
    
    #
    ### INSTRUCTOR COMMENTS:
    # Good. However, this logic is very long. Can you see any way to shorten it?
    # The danger with long chains of logic like this is that it can be difficult to read later
    # and understand exactly what is happening. Your good comments help with that, but it's even
    # better to write shorter (but still clear) code if possible.
    #
    
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
    #
    ### INSTRUCTOR COMMENT:
    # This naming is problematic.  sys.argv is a list of strings,
    # so naming something argv makes a reader think it's a list of strings.
    # Here, you have already converted it to a single int, but you wouldn't
    # know that without reading the rest of the code. It is much better to
    # use names that suggest what is actually happening. For example: main(n)
    # would make it more clear that n is not a list of strings. A docstring
    # on the function main would then clarify exactly what it is expected to be.
    #
    print (fibonacci(argv))

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        #
        ### INSTRUCTOR COMMENT:
        # This is one possible error. But the check done above was just that the length
        # wasn't 2. It didn't actually check whether a number was input.  Make sure your
        # error messages actually match the checks being done in the code.
        #
        print ("Error: did not input a number. Will set a default argument of 5")
        main(5)
    else:
        #
        ### INSTRUCTOR COMMENT:
        # For example, int() here could raise an exception if it cannot convert to an int
        #
        main(int(argv[1]))



