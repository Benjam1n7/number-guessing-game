import random
correctnumber= random.randint(1, 100)
print(correctnumber)
guess= int(input("Guess a number between 1 and 100: "))
print("You guessed:", guess)
if guess == correctnumber:
  print("guess correct")
else:
  print("wrong guess")