import math

numberOfBaseballs = int(input("Enter number of baseballs to be manufactured: "))
diameterOfBaseball = float(input("Enter the diameter of each baseball in inches: "))
volume = (4 / 3) * math.pi * math.pow(( diameterOfBaseball / 2 ), 3)    
print("You will need", format(volume, ".2f"), "inches cubed of filler.")

