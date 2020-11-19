print("Welcome to the Investment Doubler!: ")

while 1:
    try:
        investment = int(input("Enter your investment: "))
        rate = int(input("Enter your interest rate: "))
        break
    except:
        print("Please enter proper values")
rate = (rate / 100)
rate = (rate / 10)
inv = investment
c = 0.0
while (inv < (2 * investment)):
    inv = inv + (inv * rate)
    c = c + 0.1

print("It will take", round(c,1), "years to double your investment to $" + str(2 * investment))
