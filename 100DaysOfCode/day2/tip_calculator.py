print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill? $"))
tip = int(input("How much tip in percents?"))
persons = int(input("How many people to split the bill? "))

tip_percent = tip/100

bill = bill_amount*tip_percent/persons + bill_amount

print(f"Bill to pay {bill}")
