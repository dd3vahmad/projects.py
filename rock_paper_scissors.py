import random

choices = ("r", "p", "s");
emojis = { "r": "✊", "p": "📄", "s": "✂️" }

while True:
  user_choice = input("Rock, Paper or Scissors (r/p/s): ")

  if user_choice not in choices:
    print("Invalid choice (r/p/s)")
    continue

  computer_choice = random.choice(choices)
  print(f'''
    Your chose {emojis[user_choice]}\n
    Computer chose {emojis[computer_choice]}
  ''')

  if computer_choice == user_choice:
    print("It's a tie")
  elif computer_choice == "r" and user_choice == "p":
    print("You won!")
  elif computer_choice == "p" and user_choice == "s":
    print("You won!")
  elif computer_choice == "s" and user_choice == "r":
    print("You won!")
  else:
    print("You lost!")

  option = input("Continue? (Y/n): ").lower()
  if option == "n":
    break