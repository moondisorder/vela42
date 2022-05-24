##toothpick game attempt 

num_left = 13
player1_name = input("Input player1 name!")
player2_name = input("Input player2 name!")
current_player=player1_name

while True:
    print("|"*num_left)
    print(f"There are {num_left} toothpicks left")
    choice = int(input(f"{current_player}, how many toothpicks do you take?"))
    num_left -= choice
    if num_left <=0:
        print(f"{current_player} wins the game!")
        break
    if current_player == player1_name:
        current_player = player2_name
    else:
        current_player = player1_name
print("GAME OVER!")
