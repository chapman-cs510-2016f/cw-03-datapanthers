#!/bin/bash

##----------------------------------------------------------------------------
## This script uses the python function fib.py, which uses the fibonacci function
## from sequences.py, to find a fibonacci sequence and get the last number of the sequence
## Taking a for loop statement from the numbers 1 to 10000, this script creates an array, 
## calls the fib.py python script for each number in the loop, redirects the output to a 
## comma-separated-value file. This script also has error messages and codes in case 
## a csv file already exists, and if a backup file exists as well
##----------------------------------------------------------------------------

# Create an empty array to store our numbers
array=()

# For loop implementing our fib.py for each number in 1 to 10000
# and storing the numbers into the array
for i in $(seq 10000); do

    va=$(python fib.py $i 2>&1)
    array+=($va)
done

# Combining all the values in our array, separated by a comma
csv_combine=$(IFS=,; echo "${array[*]}")

# Creating variables to check for previously saved csv files
file="./fibs.csv"
back_file="./fibs.csv.bak"

# Checking to see if a back up file and if a copy of the file already exists
# if so, will save accordingly, and if not, then will save a new file fibs.csv
if [ -e "$back_file" ]
then
    echo "Backup exists. Cannot overwrite, program will exit"
    :
elif [ -e "$file" ]
then
    echo "fibs.csv exits. Saving as backup fibs.csv.back"
    echo $csv_combine >> fibs.csv.bak
else
    echo $csv_combine >> fibs.csv
fi
    


## Ignore, these were test functions I tried while writing
## this code and I want to keep for future references
#PYTHON="/usr/bin/python"
#SCRIPT_PATH="fib.py"
#$PYTHON $SCRIPT_PATH $i
#x=$ python fib.py $i 
#x=$(python -c 'import fib; fib.last(5)')

