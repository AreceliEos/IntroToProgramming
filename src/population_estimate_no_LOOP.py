import math

initialPopulation = int(input("Intial Population size: "))
growthRate = float(input("Estimated Growth Rate: "))
numberOfYears = int(input("Number of Years: "))
estimatedPopulation = (initialPopulation * math.e**(growthRate * numberOfYears))


print("The estimated population would be" , round(estimatedPopulation, 2),"in", numberOfYears, "years")
