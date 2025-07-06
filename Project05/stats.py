"""
stats.py

Svita Kiran
Fall 2023
10/18/23
CS152 Project 5

python3 stats.py

"""

def sum(numbers):
    # adds up the sum of all the numbers
    sum = 0.0
    for x in numbers:
        sum = sum + x
    return sum
    
def test():
    # test function to run other functions
    x = [1, 2, 3, 3, 4]
    result = sum(x)
    result2 = mean(x)
    result3 = min(x)
    result4 = max(x)
    result5 = variance(x)
    result6 = mode(x)
    print(result)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)


def mean(data):
    # calculates mean of the numbers in the data
    total = sum(data)
    x = len(data)
    return total/x

def min(data):
    # finds the lowest value in the data
    min = 1000
    for n in data:
        if n < min:
            min = n
    return min

def max(data):
    # finds the maximum value in the data
    max = -1000
    for n in data:
        if n > max:
            max = n
    return max

def variance(data):
    # finds the variance value in the numbers
    total = 0
    items = len(data)
    for n in data:
        diff = mean(data) - n
        diffsq = diff**2
        total = total + diffsq
    variance = total / (items - 1)
    return variance

def mode(data):
    # finds the mode in the data or the number repeated the most
    frq = {}
    maxfrq = 0
    x = []
    for i in data:
        for i in frq:
            frq[i] += 1
        else:
            frq[i] = 1

        if frq[i] > maxfrq:
            maxfrq = frq[i]
    for i, z in frq.items():
        if z == maxfrq:
            x.append(i)
    return x

#def standard_deviation(data):



if __name__ == "__main__":
    test()