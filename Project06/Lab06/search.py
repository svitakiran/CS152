"""
search.py

Svita Kiran
Fall 2023
10/25/23
CS152 Lab 6

python3 search.py

"""
import random

def searchSortedList(mylist, value):
    done = False
    found = False
    count = 0
    maxIdx = len(mylist) - 1
    minIdx = 0

    while done is not True:
        count += 1
        testIndex = (maxIdx + minIdx) // 2

        if mylist[testIndex] < value:
            minIdx = testIndex + 1
        elif mylist[testIndex] > value:
            maxIdx = testIndex - 1
        else:
            done = True
            found = True

        if maxIdx < minIdx:
            done = True
            found = False

    return (found, count)




def test():
    a = []
    N = 10**6	
    for i in range (N):
        a.append(random.randint(0,N))

    a.append(42)

    a.sort()

    print(searchSortedList(a, 42))

if __name__ == "__main__":
    test()
