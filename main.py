# Imports
import time

# Modules
from sorting import Sorter
from data_structures import *
from searching import Searcher
from algorithms import AlgoHelper

def main() -> None:
    """The main function for this script.
    Used for testing the algos created in this repo."""
    data = readData('data/basic.txt', 'int')
    print("Data: {}".format(data))
    AH = AlgoHelper()
    perm = AH.pemutation(data)
    print("Permutations:")
    for e in perm:
        print(e)
    comb = AH.combination(data)
    print("Combinations:")
    for e in comb:
        print(e)

def readData(filename, type) -> list:
    """Read in data from a text file. 
    Input the filename and the type of file to read.
    Return a list of the data read in."""
    if type == 'int':
        with open(filename) as file:
            lines = file.readlines()
        ret = []
        for line in lines:
            ret.append(int(line))
        return ret
    
if __name__== '__main__':
    main()