inputFile = input("Enter sales file name: ")
outputFile = input("Enter name for total sales file: ")

filein = open(inputFile, 'r')
lst = []
for line in filein:
    innerlist = []
    line = line.strip().split(" ")
    number1 = float(line[0].replace('$', ''))
    number2 = float(line[1].replace('$', ''))
    s = number1 + number2
    a = s / 2
    innerlist = [number1, number2, s, a]
    lst.append(innerlist)

filein.close()

fileout = open(outputFile, 'w')
for data in lst:
    fileout.write('${:>8} ${:>8} ${:>8} ${:>8}\n'.format(data[0], data[1], data[2], data[3]))

fileout.close()
print('\nDone writing total to', outputFile)
    


        