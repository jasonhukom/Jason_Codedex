# Write code below 💖

ls_guess = []

def main():
  guess = 0
  for i in range(10, 1, -1):
    print(f"You have only {i} guesses")
    if i < 10:
      strguess = str(guess)
      numberofguess(strguess)
    guess = int(input("Guess the number: "))
    for i in range(3):
      print("\n")
    if guess == 7:
      print('CONGRATULATIONS! YOU GUESS THE CORRECT NUMBER!')
      quit()
  print('You lost, try again!')

def numberofguess(n):
  ls_guess.append(n)
  lssep = ', '
  lsseped = lssep.join(ls_guess)
  print("Your previous guesses: ", lsseped)

try:
  main()
except ValueError:
  print("\nWrong input")