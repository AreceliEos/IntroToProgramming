numberOfDays = int(input("Number of days with scores: "))
total = 0
for currentDay in range(1, numberOfDays + 1):
    dailyScore = float(input("The score for day " + str(currentDay) + " : "))
    total += dailyScore

average = total/numberOfDays

print("The total score of the", numberOfDays, "days is", total)
print("The average of the", numberOfDays, "days is", format(average, ".2f"))
    