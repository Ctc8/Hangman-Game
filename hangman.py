import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


print("WELCOME TO HANGMAN... REQUIRES 2 PEOPLE TO PLAY.\n")

word = input("Get someone to type in a word for you (case sensitive): ")
blank = "_" * len(word)

print(blank)
cls()


print(len(word), "letters")
for x in word:
  print("_ ", end="")

print("")
  

guessedLetters = []

misses = 0
while True:
  guess = input("Type in a letter: ")
  guessedLetters.append(guess)

  doneYet = True
  for letter in word:
    if not(letter in guessedLetters):
      doneYet = False

  
  if doneYet == True:
    break

  
  if not(guess in word):
    misses = misses + 1
    
  for letter in word:
    if letter in guessedLetters:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  print("\nGuess another letter.")

print("The word was", word + "!")
print("You had a total of", misses, "incorrect guesses.")
