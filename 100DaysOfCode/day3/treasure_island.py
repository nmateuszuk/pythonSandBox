print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.\n Yor mission is to find a treasure.\n You ar eon a cross road. Where do you want to go?")
left_or_right = input("Type \"left\" or \"right\"").lower()
if left_or_right == 'left':
    smim_or_wait = input(
        "Do you want to swim or wait?\n Type \"swim\" or \"wait\"").lower()
    if smim_or_wait == 'wait':
        door = input(
            "Which door to you pick?\n Type \"Red\" or \"Yellow\" or \"Blue\"").lower()
        if door == 'red':
            print("Burned by fire.\n Game Over")
        elif door == 'yellow':
            print("You win!")
        elif door == 'blue':
            print("Eaten by the beasts.\n Game Over")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\n Game Over")

else:
    print("Fall into a hole.\n Game Over")
