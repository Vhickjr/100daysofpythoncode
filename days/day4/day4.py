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
game_images = [rock, paper, scissors]

print("Welcome to my Rock Paper Scissors game !")
user_choice= int(input("enter a number between 0 and 2 to play: "))

if(user_choice==0):
    print("You chose Rock")
    print(game_images[0])
elif(user_choice==1):
    print("You chose Paper")
    print(game_images[1])
elif(user_choice==2):
    print("You chose Scissors")
    print(game_images[2])
else:
    print("You entered an invalid number")
    
computer_choice= random.randint(0,2)
cc_name= ["Rock", "Paper", "Scissors"]
print(f"Computer chose {cc_name[computer_choice]}:")
print(game_images[computer_choice])

if(user_choice==0 and computer_choice==1):
    print("You lose")
elif(user_choice==0 and computer_choice==2):
    print("You win")
elif(user_choice==1 and computer_choice==0):
    print("You win")
elif(user_choice==1 and computer_choice==2):
    print("You lose")
elif(user_choice==2 and computer_choice==0):
    print("You lose")
elif(user_choice==2 and computer_choice==1):
    print("You win")
elif(user_choice==computer_choice):
    print("It's a draw")
