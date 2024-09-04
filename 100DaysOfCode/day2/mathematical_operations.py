print("My age: " + str(33))
print(123+456)
print(7-3)
print(3*2)
print(type(6/3))  # implicit type casting
# // to force it to be int --> doing first / and then get rid of numbers after dot
print(type(6//3))
print(2**3)  # 2 power of 3

# PEMDAS L->R
# ()
# **
# * OR /
# + OR -
print(3*3+3/3-3)


height = 1.65
weight = 84
bmi = weight/(height*height)
print(bmi)

print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

score = 1
score -= 1
print(score)
print("your score is " + str(score))

is_winning = True

# fstring
print(f"your score is= {score}, your height is {
      height}. You are winning {is_winning}")
