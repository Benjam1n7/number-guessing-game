import random
correct_number= random.randint(1, 100)
print(correct_number)
guess= int(input("Guess a number between 1 and 100: "))
print("You guessed:", guess)
if guess == correct_number:
  print("guess correct")
else:
  print("wrong guess")
