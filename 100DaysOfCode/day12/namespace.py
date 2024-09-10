enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# global scope
player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()

# there is no block scope in python - if, while, for block of code the dont count as creating local scope
game_level = 3
enemies = ["skeleton", "zombie", "alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
