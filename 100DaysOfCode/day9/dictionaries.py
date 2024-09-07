programing_dictionary = {
    "Bug": "an error in program",
    "Function": " a piece of code you can call to do something",
}

print(programing_dictionary["Bug"])
programing_dictionary["Loop"] = " action of doing something over again"
print(programing_dictionary)


empty_dictionary = {}

# wipe existing dictionary
programing_dictionary = {}
print(programing_dictionary)


programing_dictionary["Loop"] = " action of doing something over again"
programing_dictionary["Loop"] = "edit this entry"


# loop through a dictionary
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])
