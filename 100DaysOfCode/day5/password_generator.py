import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_of_letters = int(input(
    "Welcome to the PyPassword Generator\n How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols do you want? "))
number_of_numbers = int(input("How many numbers do you want? "))

password_list = []

for char in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, number_of_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, number_of_numbers + 1):
    password_list += random.choice(numbers)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
