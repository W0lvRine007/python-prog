import random

rock = '''              Stone
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''             Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''              Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]
user_choice = int(
    input("What do you choose?. Type 0 for Rock, 1 for Paper, 2 Scissors\n"))
comp_choice = random.randint(0, 2)

if user_choice > 3 or user_choice < 0:
    print("You entered invalid number, You lose")

else:

    print("You choose :")
    print(game_image[user_choice])

    print("Computer choose :")
    print(game_image[comp_choice])

    if user_choice == 2 and comp_choice == 0:
        print("You lose!")
    elif user_choice > comp_choice:
        print("You win")
    elif user_choice == comp_choice:
        print("It's a draw!")
    elif user_choice == 0 and comp_choice == 1:
        print("You lose!")
    elif user_choice == 0 and comp_choice == 2:
        print("You win!")
    
    elif user_choice == 1 and comp_choice == 2:
        print("You lose!")
