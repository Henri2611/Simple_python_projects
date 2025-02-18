
secret_number = 10
max_attempts = 5
counter = 0

print("Welcome to the Number Guessing Game!")
while counter < max_attempts:
  user_guess= int(input("Guess a number between 0 and 10: "))
  counter += 1
  if user_guess == secret_number:
    print("Congratulation you guessed correctly!")
    break
  elif user_guess > secret_number:
    print("Too High")
  else:
    print("Too Low")


else:
  print("You've exceeded the maximum attempts. The secret number was", secret_number)







