import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
emojis = { ROCK: "✊", PAPER: "📄", SCISSORS: "✂️" }
choices = tuple(emojis.keys());

def get_user_choice():
  choice = input(f"Rock, Paper or Scissors ({ROCK}/{PAPER}/{SCISSORS}): ")

  if choice not in choices:
    print("Invalid choice ({ROCK}/{PAPER}/{SCISSORS})")
    return
  
  return choice

def display_choices(user_choice, computer_choice):
  print(f'''
    Your chose {emojis[user_choice]}\n
    Computer chose {emojis[computer_choice]}
  ''')

def check_winner(user_choice, computer_choice):
  if computer_choice == user_choice:
    print("It's a tie")
  elif computer_choice == ROCK and user_choice == PAPER:
    print("You won!")
  elif computer_choice == PAPER and user_choice == SCISSORS:
    print("You won!")
  elif computer_choice == SCISSORS and user_choice == ROCK:
    print("You won!")
  else:
    print("You lost!")

def play_game():
  while True:
    user_choice = get_user_choice()

    computer_choice = random.choice(choices)
    
    display_choices(user_choice, computer_choice)

    check_winner(user_choice, computer_choice)

    option = input("Continue? (Y/n): ").lower()
    if option == "n":
      break

play_game()