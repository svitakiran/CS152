'''Svita Kiran
09/14/23
CS 152 A
Project 01
Code for first project
'''

def ballistic1(t):
    pi = 1
    vi = 11
    a = -10
    pf = pi + (vi * t) + (0.5 * a * t**2)
    return pf

y = ballistic1(0.5)
#print("f(0.5) is", y)
y = ballistic1(1.0)
#print("f(1.0) is", y)


def ballistic2(pi, vi, a, t):
    pf = pi + (vi * t) + (0.5 * a * t**2)
    return pf

y = ballistic2(2, 11, -10, 0.5)
#print("pf is", y)

name = input("What do you want to name your file? ")
fileName = str(name)
def computeAndOutput(pi, vi, a, t):
    y = ballistic2(pi, vi, a, t)
    print(t, ",", y)
    fp = open(fileName, 'a')
    fp.write( str(t) + "," + str(y) + "\n" )
    fp.close()

def trajectory10(pi, v, a, ti):
    computeAndOutput(pi, v, a, ti)
    computeAndOutput(pi, v, a, ti + 0.1)
    computeAndOutput(pi, v, a, ti + 0.2)
    computeAndOutput(pi, v, a, ti + 0.3)
    computeAndOutput(pi, v, a, ti + 0.4)
    computeAndOutput(pi, v, a, ti + 0.5)
    computeAndOutput(pi, v, a, ti + 0.6)
    computeAndOutput(pi, v, a, ti + 0.7)
    computeAndOutput(pi, v, a, ti + 0.8)
    computeAndOutput(pi, v, a, ti + 0.9)

#trajectory10(1, 11, -10, 0)
#trajectory10(1, 11, -10, 1)

def trajectory100(pi, v, a, ti):
    trajectory10(pi, v, a, ti)
    trajectory10(pi, v, a, ti + 1)
    trajectory10(pi, v, a, ti + 2)
    trajectory10(pi, v, a, ti + 3)
    trajectory10(pi, v, a, ti + 4)
    trajectory10(pi, v, a, ti + 5)
    trajectory10(pi, v, a, ti + 6)
    trajectory10(pi, v, a, ti + 7)
    trajectory10(pi, v, a, ti + 8)
    trajectory10(pi, v, a, ti + 9)

#original/given
trajectory100(1, 50, -10, 0)
#jupiter
trajectory100(1, 13.06, 23.12, 0)
#saturn
trajectory100(1, 9.67, 8.96, 0)