
import random

def input_choice():
  game_list = ['Rock', 'Paper', 'Scissors']
  
  while True:
    try:
      user_choice = int(input("What do you choose? please type 0 for Rock, 1 for Paper or 2 for Scissors. "))
      if user_choice in [0, 1, 2]:
        print("You chose:", game_list[user_choice])
        return user_choice
      else:
        print("Invalid number, please enter the correct number.")
    except ValueError:
      print("Invalid input, please enter the correct number.")
      
def machine_choice(game_list):
  computer_choice = random.randint(0, 2)
  print("The computer chose:", game_list[computer_choice])
  return computer_choice


def different_conditions(user_choice, computer_choice):
  
  if user_choice == 0 and computer_choice == 1:
    print("You lost!")
  elif user_choice == 0 and computer_choice == 2:
    print("You won!")
  elif user_choice == computer_choice:
    print("It's a draw!") 
  elif user_choice == 1 and computer_choice == 2:
    print("You lost!")
    
  
  
    
if __name__ == "__main__":
  user_choice = input_choice()
  computer_choice =machine_choice(['Rock', 'Paper', 'Scissors'])
  different_conditions(user_choice, computer_choice)

