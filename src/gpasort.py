from gpa import Student, makeStudent

def howToSort(): #to categorize the user input choice
    choices = ['name', 'GPA', 'credit hours']
    while True:
        try:
            sortChoice = input("Do you wish to sort by name, GPA, or credit hours?: ")
        except (ValueError, SyntaxError, TypeError):
            print("Invalid choice")
            continue
        if sortChoice in choices:
            break
        else:
            print("Do you wish to sort by name, GPA, or credit hours?: ")
            continue
        return sortChoice

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".
              format(s.getName(), s.gpa(), s.getHours()),
            file = outfile)
    outfile.close()
 
def gpaSort(filename):
    data = readStudents(filename)
    data.sort(key = Student.gpa)
    return data

def nameSort(filename):
    data = readStudents(filename)
    data.sort(key = Student.getName)
    return data

def creditHourSort(filename):
    data = readStudents(filename)
    data.sort(key = Student.getHours)
    return data

def sortCategory(sortChoice, filename): #defining available choices
    if sortChoice == 'name':
        data = nameSort(filename)
    elif sortChoice == 'GPA':
        data = gpaSort(filename)
    else:
        data = creditHourSort(filename)
    return data


def main():
    print("This program will sort students by Name, GPA, or Credit Hours")
    filename = input("Enter the name of desired data file: ")
    direction = input("Would you like the data to be sorted in ascending or descending order?: ")
    if direction == "descending":
        reverse = True
    else:
        reverse = False
    sortChoice = howToSort()
    data = sortCategory(sortChoice, "unofficial-student-data.txt")
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been transferred to", filename)
    
if __name__ == '__main__':
    main()
    
    