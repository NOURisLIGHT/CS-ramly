# Define the function to check the winner
def is_win():
    global winner
    a,b,c,d,e,f,g,h=[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,5,7],[4,3,8],[4,5,6]
    if ((all(x in x_list for x in a)) or (all(x in x_list for x in b))or (all(x in x_list for x in c))or(all(x in x_list for x in d))or (all(x in x_list for x in e))or (all(x in x_list for x in f))or (all(x in x_list for x in g))or (all(x in x_list for x in h))):
        winner = True
        print("X has won!")
    elif ((all(x in y_list for x in a)) or (all(x in y_list for x in b))or (all(x in y_list for x in c))or(all(x in y_list for x in d))or (all(x in y_list for x in e))or (all(x in y_list for x in f))or (all(x in y_list for x in g))or (all(x in y_list for x in h))):
        winner = True
        print("Y has won!")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x_list = []
y_list = []
winner = False
turn = 1

while (nums != [] and winner == False):
    print(nums)
    print("\n")
    #if turn is even, then x choose
    if (turn % 2 == 0):
        x = int(input("Player X choose from 1 to 9 & not chosen: "))
        if x in nums:
            x_list.append(x)
            nums.remove(x)
        else:
            x = int(input("The num is taken, enter another one: "))
            x_list.append(x)
            nums.remove(x)
        is_win()

    
    #if turn is odd, then y choose
    else:
        y = int(input("Player Y choose from 1 to 9 & not chosen: "))
        if y in nums:
            y_list.append(y)
            nums.remove(y)
        else:
            y = int(input("The num is taken, enter another one: "))
            y_list.append(y)
            nums.remove(y)
        is_win()
    turn += 1


if (nums == [] and winner == False):
    print("It is a tie")