# for item in list_of_items:

fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]

for fruit in fruits:
    print(fruit)


student_score = [150, 123, 146, 132, 144, 77, 88, 92, 93, 68]
total_sum = sum(student_score)
print(total_sum)

sum_of_scores = 0
for score in student_score:
    sum_of_scores += score

print(max(student_score))

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print(max_score)

# ------------------
sum_up_to_101 = 0
for number in range(1, 101):
    sum_up_to_101 += number

print(sum_up_to_101)
