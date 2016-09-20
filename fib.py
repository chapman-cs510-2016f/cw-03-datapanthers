#takes all files from sequences.py
import sequences

"""Module Description
This function uses the fibonacci function from sequences.py
to find the n squences of the fibonacci series. 
The function then returns the last number of the sequences and
outputs it. 
This script only needs to be called as a module and does not run any code.

"""

def main(n):
    x=sequences.fibonacci(n)
    #prints the last element of the fibonacci sequence 
    print x[-1]
    return x[-1]

#checks to make sure that user input is valid
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        #if user input invalid prints error message with a default argument of 5 
        print("Error:did not input a number. Will set a default argument of 5")
        main(5)
    else:
        # checks to see if 
        n = int(argv[1])
        if n < 0:
            print("Error: Negative number. Will convert to positive counterpart")
            n = -n
        main(n)

