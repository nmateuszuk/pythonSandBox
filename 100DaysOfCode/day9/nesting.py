capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nested list in dictionary

travel_log = {
    "France": ["Paris", "Lyon", "Nantes", "Marseille"],
    "Germany": ["Munich", "Hamburg", "Frankfur am Main"],
}

print(travel_log["France"][0])


nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# ------------------------------

travel_log2 = {
    "France": {"num_times_visited": 8, "cities_visited": ["Paris", "Lyon", "Nantes", "Marseille"]},
    "Germany": {"num_times_visited": 4, "cities_visited": ["Munich", "Hamburg", "Frankfur am Main"]},
}

print(travel_log2["Germany"]["cities_visited"][0])
