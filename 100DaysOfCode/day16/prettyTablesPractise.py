from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table. add_column("Type", ["electric", "water", "fire"])
table.align = "l"


print(table)
