print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
age = int(input("What is your age? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        print("Child ticket is $5")
        bill = 5
    elif age <= 18:
        print("Youth ticket is $7")
        bill = 7
    elif age >= 70 and age <= 90:
        print("Free ride")
    else:
        print("Adult ticket is $12")
        bill = 12

    wants_photo = input("Do you want a photo taken? Y for yes, N for no")

    if wants_photo == 'y':
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    ("Too short to go")

# ----------------------
number_to_check = int(input("What number do you want to check? "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")

# ----------------------
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

# -----------------------------
