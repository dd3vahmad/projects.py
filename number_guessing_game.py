import random

lower = 1
upper = 100
try:
  lowerInput = int(input("Enter the lower boundary (Enter to skip): "))
  if lowerInput: lower = lowerInput

  upperInput = int(input("Enter the upper boundary (Enter to skip): "))
  if upperInput > lower: upper = upperInput
except ValueError:
  print("\n")

value = random.randint(lower, upper)

while True:
  try:
    answer = int(input(f"Guess the number between {lower} and {upper}: "))

    if answer > value:
      print("Too high!")
    elif answer < value:
      print("Too low!")
    else:
      print("Congratulations! You guessed right.")
      break
  except ValueError:
    print("Please input a valid number (integer to be precise)")