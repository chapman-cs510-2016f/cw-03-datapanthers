#takes all files from sequences.py
import sequences

def main(n):
    x=sequence.fibonacci(n)
    #prints the last element of the fibonacci sequence 
    print x[-1]

#checks to make sure that user input is valid
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        #if user input invalid prints error message with a default argument of 5 
        print("Error:did not input a number. Will set a default argument of 5")
        main(5)
    else:
        main(int(argv[1]))

