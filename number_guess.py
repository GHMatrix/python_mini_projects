import random

#setting secret number
secret_number = random.randint(1,50)
print("A secret number between 1 and 50")

guess = None  #Start with no guess

while guess != secret_number:
  guess = int(input("Enter your guess:"))
  print("You guessed: ", guess)

  if guess < secret_number:
    print("Your number is too low")

  elif guess > secret_number:
    print("Your guess is too high")

  else:
    print("Spot on! You guessed the number")