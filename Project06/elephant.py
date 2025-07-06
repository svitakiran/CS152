"""
elephant.py

Svita Kiran
Fall 2023
10/25/23
CS152 Project 6

This program should have an input of the darting probabily and then will
return the average total elephant population, avg number of calves,
juveniles, adult males and females, and seniors based on the darting
probability given.

python3 elephant.py <darting probability>

"""
import random
import stats
import sys

# put this at the top of your code below the module string and the import statements
IDXCalvingInterval = 0 
IDXdartingProb = 1
IDXjuvenileAge = 2
IDXMaxAge = 3
IDXcalfSurvivalProb = 4
IDXadultSurvivalProb = 5
IDXseniorSurvivalProb = 6
IDXcarryingCap = 7
IDXnumYrs = 8

IDXGender = 0
IDXAge = 1
IDXMonthsPregnant = 2
IDXMonthsContraceptiveRemaining = 3



def test():
  '''This function is a test function for the other functions written'''

  # assign each parameter from the table above to a variable with an informative name
  calvingInt = 3.1
  dartingProb = 0.0
  juvenileAge = 12
  maxAge = 60
  calfSurvivalProb = 0.85
  adultSurvivalProb = 0.996
  seniorSurvivalProb = 0.20
  carryingCap = 10
  numYrs = 200
  
  # make the parameter list out of the variables
  parameters = [calvingInt, dartingProb, juvenileAge, maxAge, 
                calfSurvivalProb, adultSurvivalProb, seniorSurvivalProb, 
                carryingCap, numYrs]
  # print the parameter list
  print(parameters)

  pop = []
  for i in range(10):
   pop.append( newElephant( parameters, random.randint(1, parameters[IDXMaxAge]) ))
  for e in pop:
    print(e)
  
  population = initPopulation(parameters)
  print(population)

  newpop = incrementAge(population)
  print(newpop)

  x = calcSurvival(10, newpop)
  print(x)



def newElephant(parameters, age):
  '''This function makes a random elephant based
  on the parameters and age which are the inputs
  and returns it.'''
  elephant = [0,0,0,0]
  elephant[IDXGender] = random.choice(['m', 'f'])
  elephant[IDXAge] = age
  if elephant[IDXGender] == 'f' and parameters[IDXjuvenileAge] < age < parameters[IDXMaxAge]:
     if random.random() < 1.0 / parameters[IDXCalvingInterval]:
        elephant[IDXMonthsPregnant] = random.randint(1, 22)
  return elephant

def initPopulation(parameters):
  '''This function creates the initial population of elephants by
  calling the previous function (newElephant) and using the input parameters.'''
  carryingCapacity = parameters[IDXcarryingCap]
  population = [newElephant(parameters, random.randint(1, parameters[IDXMaxAge])) for _ in range(carryingCapacity)]
  return population

def incrementAge(population):
  '''This function increases the age of the elephants in the
  population given in the input.'''
  for i in population:
    i[IDXAge] += 1
  return population

def calcSurvival(parameters, population):
  '''This function calculates the survival of elephants in the population
  based on their age and the parameters and returns 
  a new population list depending on the probability of survival.'''
  new_population = []
  for eleph in population:
    age = eleph[IDXAge]
    if age == 1:
      survivalProb = parameters[IDXcalfSurvivalProb]
    elif age <= parameters[IDXMaxAge]:
      survivalProb = parameters[IDXadultSurvivalProb]
    else:
      survivalProb = parameters[IDXseniorSurvivalProb]
      
    if random.random() < survivalProb:
      new_population.append(eleph)
  return new_population

def dartElephants(parameters, population):
  '''This function simulates darting of the female elephants
  based on the input parameters and returns the updated population 
  after applying these measures.'''
  for eleph in population:
    gender = eleph[IDXGender]
    age = eleph[IDXAge]
    if gender == 'f' and parameters[IDXMaxAge] > age > parameters[IDXjuvenileAge]:
      if random.random() < parameters[IDXdartingProb]:
        eleph[IDXMonthsPregnant] = 0
        eleph[IDXMonthsContraceptiveRemaining] = 22
  return population

def cullElephants(parameters, population):
  '''This function simulates elephant culling to keep 
  the population numbers around the carrying capacity given by the 
  parameters from the input and returns the 
  updated population and the number of elephants culled.'''
  carryingCap = parameters[IDXcarryingCap]
  numCulled = len(population) - carryingCap
  if numCulled > 0:
    random.shuffle(population)
    newPopulation = population[:carryingCap]
  else:
    newPopulation = population
  
  return (newPopulation, numCulled)

def controlPopulation(parameters, population):
  '''This function controls the elephant population based on the given
  parameters and returns a tuple with the new population and the 
  number of elephants culled.'''
  # only if 0
  if parameters[IDXdartingProb] == 0:
    newpop, numCulled = cullElephants(parameters, population)
  # if not 0
  else:
    newpop = dartElephants(parameters, population)
    numCulled = 0
  return (newpop, numCulled)

def simulateMonth(parameters, population):
  '''This function simulates one month of the elephant population
  using the input parameters.'''
  for e in population:
    # assign indexes to variables
    gender = e[IDXGender]
    age = e[IDXAge]
    monthsPregnant = e[IDXMonthsPregnant]
    monthsContraceptive = e[IDXMonthsContraceptiveRemaining]
    if gender == 'f' and age > parameters[IDXjuvenileAge]:
      if monthsContraceptive > 0:
        e[IDXMonthsContraceptiveRemaining] -= 1
      elif monthsPregnant > 0:
        if monthsPregnant >= 22:
          newEleph = newElephant(parameters, 1)
          population.append(newEleph)
          e[IDXMonthsPregnant] = 0
        else:
          e[IDXMonthsPregnant] += 1
      else:
        if random.random() < 1.0 / ((parameters[IDXCalvingInterval] * 12) - 22):
          e[IDXMonthsPregnant] = 1
  return population

def simulateYear(parameters, population):
  '''This function simulates one year of the elephant population and
  returns the updated population after the simulation.'''
  pop = calcSurvival(parameters, population)
  # replace variable pop
  pop = incrementAge(pop)
  x = 0
  while x < 12:
    pop = simulateMonth(parameters, pop)
    x += 1
  return pop

def calcResults(parameters, population, numCulled):
  '''This function calculates the distribution of 
  the elephant population including the number of calves, juveniles, 
  adult males, adult females, and seniors and then returns the total 
  population and the number of elephants culled.'''
  calves = 0
  juveniles = 0
  adultMales = 0
  adultFemales = 0
  seniors = 0

  for eleph in population:
    if eleph[IDXAge] == 1:
      calves += 1
    elif eleph[IDXAge] <= parameters[IDXjuvenileAge]:
      juveniles += 1
    elif parameters[IDXjuvenileAge] < eleph[IDXAge] < parameters[IDXMaxAge]:
      if eleph[IDXGender] == 'm':
        adultMales += 1
      else:
        adultFemales += 1
    else:
      seniors += 1
  totalPop = len(population)
  
  return [totalPop, calves, juveniles, adultMales, adultFemales, seniors, numCulled]

def runSimulation(parameters):
  '''This function runs the elephant population simulation and 
  returns a list of results at the end. If the population is greater than 
  ten times the carrying capacity or goes extinct, the simulation 
  terminates early.'''
  popsize = parameters[IDXcarryingCap]
  # init the population
  population = initPopulation(parameters)
  [population, numCulled] = controlPopulation(parameters, population)
  # run the simulation for N years, storing the results
  results = []
  for i in range(parameters[IDXnumYrs]):
    population = simulateYear(parameters, population)
    [population, numCulled] = controlPopulation(parameters, population)
    results.append(calcResults(parameters, population, numCulled))
    if results[i][0] > 10 * popsize or results[i][0] == 0:
      # cancel early, out of control
      print('Terminating early')
      break
  return results

def defaultParameters():
  '''This function returns the default parameters for the simulation.'''
  calvingInt = 3.1
  probDart = 0.0
  juvAge = 12
  maxAge = 60
  probCalfSurvival = 0.85
  probAdultSurvival = 0.996
  probSeniorSurvival = 0.2
  carryingCapacity = 1000
  numYears = 200
  parameters = [calvingInt, probDart, juvAge, maxAge, probCalfSurvival, 
                probAdultSurvival, probSeniorSurvival, carryingCapacity, 
                numYears]
  return parameters

def elephantSim(probDart, inputParameters = None):
  '''This function simulates the elephant population and returns
  the difference between the carrying capacity and the average 
  total population.'''
  if inputParameters is None:
    parameters = defaultParameters()
  else:
    parameters = inputParameters

  parameters[IDXdartingProb] = probDart
  results = []
  for i in range(5):
    results += runSimulation(parameters)
  avgTotalPop = sum(result[0] for result in results) / len(results)
  diff = parameters[IDXcarryingCap] - int(avgTotalPop)
  return diff

  



def main(argv):
  '''This function takes the command-line argument from the
  terminal for the darting probability. It sets up the parameters for 
  the simulation, calls the runSimulation function, and then
  calculates and prints the average results.'''
  if len(argv) < 2:
    print('usage: python3 elephant.py dartingProb')
    sys.exit(1)
  dartingProb = float(argv[1])
  calvingInt = 3.1
  juvenileAge = 12
  maxAge = 60
  calfSurvivalProb = 0.85
  adultSurvivalProb = 0.996
  seniorSurvivalProb = 0.20
  carryingCap = 7000
  numYrs = 200

  parameters = [calvingInt, dartingProb, juvenileAge, maxAge, 
                calfSurvivalProb, adultSurvivalProb, seniorSurvivalProb, 
                carryingCap, numYrs]
  results = runSimulation(parameters)
  #print(results[-1][0])

  #print("Total Population in the Last Year:", results[-1][0])

  total_population = [i[0] for i in results]
  calves = [i[1] for i in results]
  juveniles = [i[2] for i in results]
  adult_males = [i[3] for i in results]
  adult_females = [i[4] for i in results]
  seniors = [i[5] for i in results]

  avgTotalPop = stats.mean(total_population)
  avgCalves = stats.mean(calves)
  avgJuveniles = stats.mean(juveniles)
  avgAdultMales = stats.mean(adult_males)
  avgAdultFemales = stats.mean(adult_females)
  avgSeniors = stats.mean(seniors)

  print("Average Results:")
  print("Average total population:", avgTotalPop)
  print("Average number of calves:", avgCalves)
  print("Average number of juveniles:", avgJuveniles)
  print("Average number of adult males:", avgAdultMales)
  print("Average number of adult females:", avgAdultFemales)
  print("Average number of seniors:", avgSeniors)



if __name__ == "__main__":
  #test()
  main(sys.argv)