# Subscripting
print("Hello"[0])
print("Hello"[-1])


# String concatinating
print("123"+"456")

# Integer= whole number
print(123+456)

# large intigers
print(123_456_789)

# float =  floating point number
print(3.14)

# Boolean
print(True)
print(False)

# Lists list Ordered sequence of objects:   [10,"hello",200.3]
# Dictionaries dict Unordered Key:Value pairs:  {"mykey" : "value" , "name" : "Frankie"}
# Tuples tup Ordered immutable sequence of objects: (10,"hello",200.3)
# Sets set Unordered collection of unique objects:  {"a","b"}

# Python uses Dynamic Typing -->This means you can reassign variables to different data types.


# you can convert to int() float() str() bool()
length = len(input("Enter your name "))
print(type(length))
print(type("Number of letters in your name: "))
print("Number of letters in your name: " + str(length))
