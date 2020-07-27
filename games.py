import random

money = 100

## Game of chance functions:


# Coin flip

def coinflip():
  # will increment money in global wallet
  global money
  # get input for bet (repeats)
  print("Welcome to Coin Flip!")
  print("You have £{0} in your wallet.".format(money))
  bet = int(input("How much money would you like to bet? Please enter a whole number: "))
  if bet > money:
    bet = int(input("It looks like you lack the funds. Please enter a smaller bet: "))
  # get input for guess
  guess = input("Enter 1 for \"Heads\" or 2 for \"Tails\": ")
  choices = {"1": "Heads", "2": "Tails"}
  # check if the guess is valid
  if guess not in list(choices):
    guess = input("You need to enter 1 or 2. ")
  # display choice
  print("You have placed a £{0} bet on {1}.".format(bet, choices[guess]))
  print("Flipping...")
  # flip the coin
  flip_result = random.choice(list(choices.values()))
  print(flip_result)
  # see if we have won and increment wallet
  if flip_result == choices[guess]:
    money += bet
    return print("Woohoo! You have just won £{0}! Your wallet now has £{1}.".format(bet, money))
  else:
    money -= bet
    return print("No luck this time... :( You have  lost -£{0}! Your wallet now has £{1}.".format(bet, money))


# Cho_Han

def cho_han():
  # will increment money in global wallet
  global money
  # get input for bet (repeats)
  print("Welcome to Cho_Han!")
  print("You have £{0} in your wallet.".format(money))
  bet = int(input("How much money would you like to bet? Please enter a whole number: "))
  if bet > money:
    bet = int(input("It looks like you lack the funds. Please enter a smaller bet: "))
  # get input for guess
  guess = input("Enter 1 for \"Odd\" or 2 for \"Even\": ")
  choices = {"1": "Odd", "2": "Even"}
  # check if the guess is valid
  if guess not in list(choices):
    guess = input("You need to enter 1 or 2. ")
  # display choice
  print("You have placed a £{0} bet on {1}.".format(bet, choices[guess]))
  print("Rolling the first dice...")
  # roll the dice
  dice1 = random.randint(1, 6)
  print(dice1)
  print("Rolling the second dice...")
  dice2 = random.randint(1, 6)
  print(dice2)
  roll_result = dice1 + dice2
  print("The roll sum is: {0}".format(roll_result))
  # see if we have won and increment wallet
  if roll_result // 2 ==0: # roll sum is Even
    print("That was Even-tful!")
    if guess == "2": # correct guess
      money += bet
      return print("Woohoo! You have just won £{0}! Your wallet now has £{1}.".format(bet, money))
    else: # wrong guess
      money -= bet
      return print("No luck this time... :( You have  lost -£{0}! Your wallet now has £{1}.".format(bet, money))
  else: # roll sum is Odd
    print("That's Odd...")
    if guess == "1": # correct guess
      money += bet
      return print("Woohoo! You have just won £{0}! Your wallet now has £{1}.".format(bet, money))
    else: # wrong guess
      money -= bet
      return print("No luck this time... :( You have  lost -£{0}! Your wallet now has £{1}.".format(bet, money))




# TESTING AREA #

# coinflip()
print(money)

cho_han()
print(money)
