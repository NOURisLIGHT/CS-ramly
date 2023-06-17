#create the dictionary
#ask the user which option does he want? Wether listing all cities, or asking for a particular city, or adding a new city
#IN Listing we will use dict.items() to loop in the dict then append it to a list, 
#IN asking we will print the key and the value of the city he asked for
#IN adding we will use dict[city] = value

dictionary = {
    "cairo" : 0,
    "Giza" : 15,
    "Alex" : 200,
    "Sina" : 500,
    "Marsa Alam" : 800
}

while True:
    user_input = input("Enter the operation you want to do, wether (list or ask or add):  ")
    if user_input == "list":
        lst = []
        lst.append(dictionary)
        print(lst)
        
        play_again = input("Would you like to play again? Type y or n: ").lower()
        if play_again == "y":
            continue
        else:
            break


    elif user_input == "ask":
        city = input("Enter the city you want, choose from dictionary: ")
        if city in dictionary:
            print(dictionary[city], "kilometers from cairo")
        else:
            print(f"{city} is not in the dictionary")

        play_again = input("Would you like to play again? Type y or n: ").lower()
        if play_again == "y":
            continue
        else:
            break

    elif user_input == "add":
        city_add = input("Enter the city you want to add: ")
        distance = int(input("Enter its distance from Cairo: "))
        dictionary[city_add] = distance
        print_dict = input("Would you like to print the dicionary? Type y/n: ").lower()
        if print_dict == "y" or print_dict == "yes":
            print(dictionary)
        else:
            print("As you like")

        play_again = input("Would you like to play again? Type y or n: ").lower()
        if play_again == "y":
            continue
        else:
            break

    else:
        print("Invalid input! Try again...")

    


 
