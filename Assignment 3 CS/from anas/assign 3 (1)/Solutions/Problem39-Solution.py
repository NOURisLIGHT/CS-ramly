egy_cities = {"Cairo": 7000000, "Alex": 4000000, "Giza": 250000, "Port Said": 500000,
              "suez": 450000, "Luxor": 400000, "Asyut": 400000, "Tanta": 400000,
              "Fayom": 300000, "Ismailia": 250000}


print("'a' to get the population of a city\n"
      "'b' to add a city's population\n"
      "'c' to list all the city's populations")
choice = input("chose (a, b, c): ")
if choice == "a":
    city = input("Enter the city: ")
    print("The population of the city is", egy_cities[city])
elif choice == "b":
    city = input("Enter the city: ")
    pop = input("Enter the population")
    egy_cities[city] = pop
elif choice == "c":
    for i in egy_cities:
        print(i, ": ", egy_cities[i])
else:
    print("a, b, c only allowed")
