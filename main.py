from sorting import Sorter
from data_structures import *
from searching import Searcher
import time

def main() -> None:
    """The main function for this script.
    Used for testing the algos created in this repo."""
    data = readData('data/basic.txt', 'int')
    # print("Unsorted Data: {}".format(data))
    sorter = Sorter()
    data = sorter.mergeSort(data)
    print("Sorted data: {}".format(data))
    ll = LinkedList()
    for e in data:
        ll.addStart(e)
        ll.addEnd(e)
    print(ll.export())
    for e in data:
        ll.delStart()
        ll.delEnd()
        print(ll.export())


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