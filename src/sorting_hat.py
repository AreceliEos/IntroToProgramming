import sys

print("Welcome to Hogwarts!")
print("Now, tell me your situation and I'll recommend a house")
print()

magical = str(input("Do you have magical powers (y/n)?: "))


if magical == "n":
    print("Ah, you are a muggle.")
    sys.exit()

else:
    score = int(input("What is your magical score?: "))
print()
print("Ahh...right then...better be...")

if score in range(0, 25):
    print("Gryffindor!")
elif score in range(25, 50):
    print("Slytherin!")
elif score in range(50, 75):
    print("Ravenclaw!")
elif score in range(75, 101):
    print("Hufflepuff!")

