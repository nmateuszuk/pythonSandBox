
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

print(states_of_america[0])
print(states_of_america[-1])

states_of_america[0] = "Dellawarre"
print(states_of_america[0])

states_of_america.append("Genovia")
print(states_of_america[-1])

states_of_america.extend(["Brunhildowo", "Lesiowo"])
print(states_of_america[-1])

print(len(states_of_america))

# nested list
# dirty_dozen1 = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
#                 "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
print(dirty_dozen[0])
print(dirty_dozen[1])
