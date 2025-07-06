"""
optimize.py

Svita Kiran
Fall 2023
10/25/23
CS152 Project 6

This program optimizes parameters in the elephant simulation. It uses a 
binary search method to find a probability in a given range. This program 
runs the binary search and evaluates parameter effects.


python3 optimize.py

"""
import sys
import elephant
import random

# Executes a search to bring the result of the function optfunc to zero.
# min: minimum parameter value to search
# max: maximum parameter value to search
# optfunc: function to optimize
# parameters: optional parameter list to pass to optfunc
# tolerance: how close to zero to get before terminating the search
# maxIterations: how many iterations to run before terminating the search
# verbose: whether to print lots of information or not

def optimize( min, max, optfunc, parameters = None, tolerance =  
             0.001, maxIterations = 20, verbose=False ):
    '''This function does a binary search with the input parameters min, 
    max, optimized function, parameters, tolerance, max iterations, 
    and verbosity and returns the optimized parameter value.'''
    done = False
    while done == False:
        testValue = (max + min) / 2.0
        if verbose:
            print(testValue)

        result = optfunc(testValue, parameters)
        if verbose:
            print(result)

        if result > 0:
            max = testValue
        elif result < 0:
            min = testValue
        else:
            done = True

        if max - min < tolerance:
            done = True

        maxIterations -= 1
        if maxIterations <= 0:
            done = True
    return testValue




# A function that returns x - target
def target(x, pars):
    return x - 0.73542618
    # you could also use return x - 1.0 to get close to 1.0

# Try changing the tolerance to see how that affects the search.
def testTarget():
    '''This function tests the binary search using a simple target function.'''
    res = optimize( 0.0, 1.0, target, tolerance = 0.01, verbose=True)
    print(res)

def testEsim():
    '''This function tests the binary search with the elephant 
    simulation function.'''
    res = optimize(0.0, 0.5, elephant.elephantSim, verbose=True)
    print(res)


def evalParameterEffect(whichParameter, testmin, testmax, teststep, 
                        defaults = None, verbose = False):
    '''This function evaluates the effects of the selected parameter 
    on the dart percentage using the input parameters: which parameter, 
    min test value, max test value, steps to test, defaults, and verbosity.'''
    if defaults is None:
        simParameters = elephant.defaultParameters()
    else:
        simParameters = defaults.copy()
    
    results = []

    if verbose:
        print("Evaluating parameter %d from %.3f to %.3f with step %.3f" % (whichParameter, testmin, testmax, teststep))

    t = testmin
    while t < testmax:
        simParameters[whichParameter] = t
        percDart = optimize(0.0, 0.5, elephant.elephantSim, simParameters, verbose=False)
        results.append((t, percDart))
        if verbose:
            print("%8.3f \t%8.3f" % (t, percDart))
        t += teststep

    if verbose:
        print("Terminating")

    return results


    
if __name__ == "__main__":
    #testEsim()
    evalParameterEffect(elephant.IDXadultSurvivalProb, 0.98, 1.0, 0.001, verbose=True )