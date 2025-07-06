"""
Svita Kiran
Fall 2023
CS 152
10/04/05

Simulates and plots CEPD data

python3 penguin.py

"""
import random
import sys
import matplotlib.pyplot as plt

def initPopulation(N, probFemale):
    # calculates the population of males/females in standard/el nino year
    population = []
    for i in range(N):
        num = random.random()
        if num < probFemale:
            population.append('f')
        else:
            population.append('m')
    return population

def simulateYear(pop, elNinoProb, stdRho, elNinoRho, probFemale, maxCapacity):
    # simulates one single year
    elNinoYear = False  # Assume it's not an El Nino year initially
    if random.random() < elNinoProb:
        elNinoYear = True
    newpop = []
    for penguin in pop:
        if len(newpop) >= maxCapacity:
            break

        if elNinoYear:
            if random.random() < elNinoRho:
                newpop.append(penguin)
        else:
            newpop.append(penguin)
            if random.random() < (stdRho - 1.0):
                if random.random() < probFemale:
                    newpop.append('f')
                else:
                    newpop.append('m')
    return newpop

def runSimulation( N,            # numb of years to run the simulation
                   initPopSize,  # initial population size
                   probFemale,   # prob a penguin is female
                   elNinoProb,   # prob El Nino occurs in a given year
                   stdRho,       # pop growth in non-El Nino year
                   elNinoRho,    # pop growth in an El Nino year
                   maxCapacity,  # max carrying capacity of ecosystem 
                   minViable ):  # min viable population
    # returns the year of extinction 
    population = initPopulation(N, probFemale)
    endDate = N
    #print(N)
    for date in range(N):
        newPopulation = simulateYear(population, elNinoProb, stdRho, elNinoRho, probFemale, maxCapacity)
        males = population.count('m')
        females = population.count('f')
        if len(population) < minViable and males >= 0 and females >= 0:
            endDate = date
            break
        population = newPopulation
        #print(date, len(population))
    return endDate
 
def computeCEPD(results, N):
    # takes result of the sim and calculates CEPD 
    # part1
    CEPD = []
    for i in range(N):
        CEPD.append(0)
    # part2
    for i in results:
        if i < N:
            for k in range(i, N):
                CEPD[k] += 1
    # part3
    numSims = len(results)
    for i in range(N):
        CEPD[i] /= numSims

    return CEPD

#EXT
def plotCEPD(sims, years, parameters):
    # to process CEPD values and return data in a format to be plotted
    results = []
    for i in range(sims):
        # * means expanded --- use default parameter when called
        result = runSimulation(years, *parameters)
        results.append(result)
    return results

def main(argv):
    #A usage statement
    if len(argv) < 3:
        print('usage: python3 penguin.py numSims yrsBtwnElNino')
        sys.exit(1)
    
    #B extract values from cmd line args
    numSim = int(argv[1])
    yrsBtwnEN = int(argv[2])

    #C set up local vars
    N = 201
    initPopSize = 500
    probFemale = 0.5
    elNinoProb = 1/7
    stdRho = 1.188
    elNinoRho = 0.41
    maxCapacity = 2000
    minViable = 10
    results = []

    #D main loop to run sims
    for i in range(numSim):
        result = runSimulation(N, initPopSize, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable)
        results.append(result)
    
    #E calc prob of survival after N years
    extinct = sum(1 for result in results if result < N)
    prob = extinct / numSim
    print('prob: ' + str(prob))

    '''
    CEPD = computeCEPD(results, N)
    for i in range(0, len(CEPD), 10):
        print(CEPD[i])
    '''

    # EXT   
    sims = 1000
    #ask number of plots to be made
    plots = int(input('How many plots of the CEPD do you want? '))
    # same parameters - the default
    parameters = (initPopSize, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable)
    run = 0
    for i in range(plots):
        # calling reformatted data
        final = plotCEPD(sims, N, parameters)
        '''calculate CEPD and print - taken from instructions and
        moved and reformatted into extension'''
        CEPD = computeCEPD(final, N)
        for i in range(0, len(CEPD), 10):
            print(CEPD[i])
        run += 1
        plt.plot(range(N), CEPD, label=f"Run " + str(run))
    plt.xlabel("Years")
    plt.ylabel("CEPD")
    plt.grid()
    # shows all plots and corresponding colors
    plt.legend()
    plt.show()





def test():
    # testing the initial pop, simulate year, and run simulation functions
    popsize = 10
    probFemale = 0.5

    pop = initPopulation(popsize, probFemale)

    print( pop )

    newpop = simulateYear(pop, 1.0, 1.188, 0.41, 0.5, 2000)
    print( "El Nino year" )
    print( newpop )
    newpop = simulateYear(pop, 0.0, 1.188, 0.41, 0.5, 2000)
    print( "Standard year" )
    print( newpop )

    runSimulation(201, 500, 0.5, 1/7, 1.188, 0.41, 2000, 10)



if __name__ == "__main__":
    #test()
    main(sys.argv)