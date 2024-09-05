print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S,M or L: ").upper()
peperoni = input("Do you want peperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0

if size == 'S':
    print(" Small pizza is 10")
    bill = 10
elif size == 'M':
    print(" Medium pizza is 15")
    bill = 15
elif size == 'L':
    print("Large pizza is 25")
    bill = 25
else:
    print("wrong input")

if peperoni == 'Y':
    if size == 'S':
        bill += 3
        print("Adding pepperoni")
    else:
        bill += 5
        print("Adding pepperoni")

if extra_cheese == 'Y':
    bill += 2
    print("Adding extra cheese")

print(f"Final bill is ${bill}")
