"""Computes the mean and standard deviation of some data

    * given a tab-delimited file of integers and a specified column number,
      returns the mean and standard deviation of the data

Parameters
----------
--file_name : the input file containing the data to do statistics on
              Must be a tab-delimited file of integers.

--column_number : the column number of the input file specifying
                  the column of data to be analyzed
                  Must be a positive integer that corresponds to a
                  column index in input file 'file_name'.

Returns
-------
mean : Arithmetic mean of the values in column "column_number"
       of file "file_name"

stdev : The standard deviation of the values in column
        "column_number" of file "file_name"


Errors
------
'File was not able to be opened' : issue opening the file

'Column number could not be read' : issue with column number

'Could not calculate the mean' : issue calculating the mean

'Could not calculate the standard deviation' : issue calculating
                                               the standard deviation


"""


import sys
import math
import argparse

parser = argparse.ArgumentParser(description='Do statistics'
                                             ' on a column of integers.')

parser.add_argument('--file_name', type=str,
                    help='Name of the file', required=True)

parser.add_argument(
                    '--column_number', type=str,
                    help='The column number', required=True)

args = parser.parse_args()


try:
    f = open(args.file_name, 'r')
except FileNotFoundError:
    print('File was not able to be opened')
    sys.exit(1)

V = []

try:
    int(args.column_number)
except ValueError:
    print('Column number could not be read')
    sys.exit(1)

try:
    for l in f:
        A = [int(x) for x in l.split()]
        V.append(A[int(args.column_number)])
except IndexError:
    print('File was not able to be read')
    sys.exit(1)
except ValueError:
    print('File was not able to be read')
    sys.exit(1)

try:
    mean = sum(V)/len(V)
except ArithmeticError:
    print('Could not calculate the mean')
    sys.exit(1)

try:
    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
except ArithmeticError:
    print('Could not calculate the standard deviation')
    sys.exit(1)


def main():
    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    main()
