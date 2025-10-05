import random

number_of_dice = 2
roll_times = 0

number_of_dice = int(input("How many dice(s) do you want to roll?: "))

while True:
  choice = input("Roll the dice? (y/n): ").lower()

  if choice == "y":
    dice = []
    for i in range(number_of_dice):
      die = random.randint(1, 6)
      dice.append(die)
    print("Result: ", dice);
    roll_times += 1
    print("Roll count: ", roll_times);
  elif choice == "n":
    print("Thank you for playing");
    break
  else:
    print("Invalid choice!")