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
items = [rock,paper,scissors]

my_choice = int(input("what do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
computer_choice = random.randint    (0,2)
keep_running = True
while keep_running:

 if my_choice== 0 and computer_choice == 1:
     print("You chose")
     print(items[0])
     print("Computer chose")
     print(items[computer_choice])
     print("You Lose")
 elif my_choice== 0 and computer_choice== 2:
    print("You chose")
    print(items[0])
    print("Computer chose")
    print(items[computer_choice])
    print("You win")
 elif my_choice == 1 and computer_choice == 0:
    print("You chose")
    print(items[1])
    print("Computer chose")
    print(items[computer_choice])
    print("You win")
 elif my_choice == 1 and computer_choice == 2:
    print("You chose")
    print(items[1])
    print("Computer chose")
    print(items[computer_choice])
    print("You lose")
 elif my_choice == 2 and computer_choice == 0:
    print("You chose")
    print(items[2])
    print("Computer chose")
    print(items[computer_choice])
    print("You lose")
 elif my_choice == 2 and computer_choice == 1:
    print("You chose")
    print(items[2])
    print("Computer chose")
    print(items[computer_choice])
    print("You win")

 elif my_choice > 2:
     print("Invalid entry")

 else:
    print("It's a draw")
 keep_running = False