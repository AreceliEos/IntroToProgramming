#estimating population with a LOOP

initialPopulation = int(input("Initial population size: "))
growthRate = float(input("Average growth rate: "))
numberOfYears = int(input("Number of years: "))
population = initialPopulation


print( "\nYears\tEstimated population\n")
for currentYear in range ( 1, numberOfYears + 1):
    print( currentYear, "\t", format( population, ".2f"))
    population = population + (growthRate * population)
   
    
