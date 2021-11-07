import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)
rps = [rock, paper, scissors]
if player_choice >=3 or player_choice < 0:
    print("Invalid choice. You Lose!")
    exit(0)
else:
    print(f"your Choice:\n{rps[player_choice]}")
    print(f"Computer Choice:\n{rps[comp_choice]}")
    if player_choice == comp_choice:
        print("Its a Draw!")
    elif player_choice == 0 and comp_choice == 2:
        print("You Win!")
    elif player_choice == 2 and comp_choice == 0:
        print("you Lose!")
    elif player_choice > comp_choice:
        print("You Win!")
    elif player_choice < comp_choice:
        print("You Lose!")

