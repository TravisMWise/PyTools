from sorting import Sorter
from data_structures import *
from searching import Searcher
import time

def main() -> None:
    """The main function for this script.
    Used for testing the algos created in this repo."""
    data = readData('data/basic.txt', 'int')
    print("Unsorted Data: {}".format(data))
    sorter = Sorter()
    sorter.quickSort(data)
    print("Sorted data: {}".format(data))
    searcher = Searcher()
    # stack = Stack()
    # for e in data:
    #     stack.push(e)
    #     print(stack.export())
    # for e in data:
    #     stack.pop()
    #     print(stack.export())
    queue = Queue()
    for e in data:
        queue.enqueue(e)
        print(queue.export())
    for e in data:
        queue.dequeue()
        print(queue.export())


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