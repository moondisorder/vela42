from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    comp_move = "rock" 
if num == 2:
    comp_move = "paper" 
if num == 3:
    comp_move = "scissors" 

# Ask a user to enter their move
user_move = input("Enter your move! ").lower

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if user_move == "rock":
    print(rock)
elif user_move == "paper":
    print(paper)
elif user_move == "scissors":
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print(f"The computer chooses {comp_move}!")
print(comp_move)

# Figure out who wins and print the result!
#if (user_move = "rock") and (comp_move = scissors):
#    print("You win!")
#if (user_move = "paper") and comp_move = rock

