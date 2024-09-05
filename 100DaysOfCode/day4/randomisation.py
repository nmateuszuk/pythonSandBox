import random

rand_number = random.randint(1, 10)
print(f"random number is {rand_number}")


random_number_0_to_1 = random.random()
print(f"random_number_0_to_1 is {random_number_0_to_1}")


random_number_0_to_10 = random.random() * 10
print(f"random_number_0_to_1 is {random_number_0_to_10}")

# range is inclusive
random_float = random.uniform(1, 10)
print(f"random_float is {random_float}")


random_head_tails = random.randint(0, 1)
if random_head_tails == 1:
    print("Heads")
else:
    print("Tails")
