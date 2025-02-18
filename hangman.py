import random

word_list = ["Lion", "antelope", "cat", "cow", "dog"]
selected_word = random.choice(word_list).lower()
guessed_letters = []
attempts = 6
display_word = ['_'] * len(selected_word)

while attempts > 0 and '_' in display_word:
  print("Welcome to the hangman game.Try to guess some animal words")
  print(f"Current state of the word: {' '.join(display_word)}")
  print(f"Attempts remaining: {attempts}")
  player_guess = input("Guess a letter: ").lower()

  if player_guess in guessed_letters:
    print("You already guessed that letter. Try again")

  elif player_guess in selected_word:
    guessed_letters.append(player_guess)
    display_word = [letter if letter in guessed_letters else '_' for letter in selected_word]

  else:
    guessed_letters.append(player_guess)
    attempts -= 1
    print("Incorrect guess!")

if '_' not in display_word:
  print("Congratulations, you guessed correctly!")
else:
  print(f"Sorry, you lost. The secret word was: {selected_word}")