# Setting the game
print("Subtract a square game")
num = 50
turn = 1
while num > 0:
    print("Number = ", num)
    if turn == 1:
        print("Player 1 turn")
        x = int(input("Enter a squared number less than 25: "))
        turn = 2
        if x in [1, 4, 9, 16]:
            num -= x

        else:
            print("number must be squared and less than 25")
            turn = 1

    else:
        print("Player 2 turn")
        x = int(input("Enter a squared number less than 25: "))
        turn = 1
        if x in [1, 4, 9, 16]:
            num -= x
        else:
            print("number must be squared and less than 25")
            turn = 2

if turn == 2:
    print("Player 1 has won")
else:
    print("Player 2 has won")
