from sorting import Sorter
from data_structures import BST
from searching import Searcher
import time

def main() -> None:
    """The main function for this script."""
    rawData = readData('input.txt', 'int')
    # print("Unsorted Data: {}".format(rawData))
    sorter = Sorter()
    sorter.quickSort(rawData)
    # print("\nSorted data: {}".format(rawData))
    searcher = Searcher()
    startTime = time.time()
    for data in rawData:
        searcher.binarySearch(rawData, data)
    endTime = time.time()
    print(endTime-startTime)
    startTime = time.time()
    for data in rawData:
        searcher.iterativeSearch(rawData, data)
    endTime = time.time()
    print(endTime-startTime)

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