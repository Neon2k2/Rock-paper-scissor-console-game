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
print("welcome to the game")
choices = [rock, paper, scissors]

user_choice = int(input("choose 0:rock 1:paper 2: scissor \n"))
print(choices[user_choice])

user_chosen = choices[user_choice]

computer_choice = random.randint(0,2)
print(choices[computer_choice])
computer_chosen = choices[computer_choice]

if(user_choice >=0 and user_choice <=3):
    if(user_choice == 0 and computer_choice ==1):
        print("computer won")
    else if(user_choice == 1 and computer_choice == 2):
        print("computer won")
    else if(user_choice == 2 and computer_choice == 0):
        print("computer won")
    else:
        print("you won")
else:
    print("invalid input")
    