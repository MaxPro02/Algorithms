from random import randint, random
from mergeSort import mergeSort
from time import time
 
averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)
 
def test_mergeWorst():
    start= time()
    assert mergeSort(worstcase) == bestcase
    print(time()-start)
 
def test_mergeBest():
    start= time()
    assert mergeSort(bestcase) == bestcase
    print(time()-start)
 
def test_mergeAvg():
    start= time()
    assert mergeSort(averagecase) == bestcase
    print(time()-start) 
