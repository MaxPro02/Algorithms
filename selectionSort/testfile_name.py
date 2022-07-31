from random import randint, random
from selectionSort import selectionSort
from time import time
 
averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)
 
def test_selectionSortWorst():
    start= time()
    assert selectionSort(worstcase) == bestcase
    print(time()-start)
 
def test_selectionSortBest():
    start= time()
    assert selectionSort(bestcase) == bestcase
    print(time()-start)
 
def test_selectionSortAvg():
    start= time()
    assert selectionSort(averagecase) == bestcase
    print(time()-start) 
