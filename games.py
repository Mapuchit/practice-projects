import random

money = 100

## Game of chance functions:

# Coin flip

def coinflip():
  # will increment money in global wallet
  global money
  # get input for bet and choice
  print("Welcome to Coin Flip!")
  print("You have £{0} in your wallet.".format(money))
  bet = int(input("How much money would you like to bet? Please enter a whole number: "))
  if bet > money:
    bet = int(input("It looks like you lack the funds. Please enter a smaller bet: "))
  pick = input("Enter 1 for \"Heads\" or 2 for \"Tails\": ")
  choices = {"1": "Heads", "2": "Tails"}
  # checl if the pick is valid
  if pick not in list(choices):
    pick = ("You need to enter 1 or 2. ")
  # flip the coin
  print("You have placed a £{0} bet on {1}.".format(bet, choices[pick]))
  print("Flipping...") # delay for suspence
  flip_result = random.choice(list(choices.values()))
  print(flip_result)
  # display results and increment wallet
  if flip_result == choices[pick]:
    money += bet
    return print("Woohoo! You have just won £{0}! Your wallet now has £{1}.".format(bet, money))
  else:
    money -= bet
    return print("No luck this time... :( You have  lost -£{0}! Your wallet now has £{1}.".format(bet, money))





# TESTING AREA #

coinflip()

print(money)

coinflip()

print(money)
