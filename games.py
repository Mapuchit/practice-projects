import random

money = 100

## Game of chance functions:


# Coin flip

def coinflip():
  global money
  # get input for bet (repeats)
  game = "Coin Flip"
  bet = get_bet(game, money)
  # get input for guess
  guess = input("Enter 1 for \"Heads\" or 2 for \"Tails\": ")
  choices = {"1": "Heads", "2": "Tails"}
  # check if the guess is valid
  while guess not in list(choices):
    guess = input("You need to enter 1 or 2. ")
  # display choice
  print("You have placed a £{0} bet on {1}.".format(bet, choices[guess]))
  print("Flipping...")
  # flip the coin
  flip_result = random.choice(list(choices.values()))
  print(flip_result)
  # see if we have won and increment wallet
  if flip_result == choices[guess]:
    return bet # return the bet amount = winnings
  else:
    return bet * -1 # return the negative bet amount = loss


# Cho_Han

def cho_han():
  global money
  # get input for bet (repeats)
  game = "Cho-Han"
  bet = get_bet(game, money)
  # get input for guess
  guess = input("Enter 1 for \"Odd\" or 2 for \"Even\": ")
  choices = {"1": "Odd", "2": "Even"}
  # check if the guess is valid
  while guess not in list(choices):
    guess = input("You need to enter 1 or 2. ")
  # display choice
  print("You have placed a £{0} bet on {1}.".format(bet, choices[guess]))
  # roll the dice
  print("Rolling the first dice...")
  dice1 = random.randint(1, 6)
  print(dice1)
  print("Rolling the second dice...")
  dice2 = random.randint(1, 6)
  print(dice2)
  # add up results
  roll_result = dice1 + dice2
  print("The roll sum is: {0}".format(roll_result))
  # see if we have won and increment wallet
  if roll_result % 2 == 0: # roll sum is Even
    print("That was Even-tful!")
    if guess == "2": # correct guess
      return bet
    else: # wrong guess
      return bet * -1
  else: # roll sum is Odd
    print("That's Odd...")
    if guess == "1": # correct guess
      return bet
    else: # wrong guess
      return bet * -1


# Higher Card

# option to choose how many rounds you want to play. max is 52 / 2 = 26 rounds
# while loop to count rounds and always draw from deck with less cards
# sum up money won in each round
def higher_card():
  global money
  game = "Higher Card"
  # choose how many rounds the user wants to play
  rounds = get_rounds(game)
  # set up a wallet. the user will put money in the wallet from global money,
  # and then use this money to play all rounds and place individual bets per round
  # this will avoid overspending from the global money, which will be updated once all rounds are finished
  wallet = get_bet(game, money)
  # set up the deck
  print("The game will be {0} rounds. You have £{1} in your wallet for this game. Setting up the deck...".format(rounds, wallet))
  colours = ["diamond", "spade", "heart", "club"]
  colour_deck = [] # this list will have each colour 13 times = 52 cards total
  for c in colours:
    for n in range(0, 13):
      colour_deck.append(c)
  number_deck = [] # this list will have 4 number sets of 1-13 = 52 cards total
  for c in range(len(colours)):
    for n in range(1, 14):
      number_deck.append(n)

  # set up a counter for the rounds
  round_counter = 1
  # and a counter for the money won or lost
  money_counter = 0
  while round_counter < rounds + 1:
    # getting the bet before each round, display earnings so user can make better choice
    print("Your winnings this far: {0}".format(money_counter))
    # we place the single round bets from the wallet created for this game
    bet = get_bet(game, wallet)
    # display choice
    print("Round {0}. You have placed a £{1} bet on having the higher card.".format(round_counter, bet))
    # player draw
    print("You are drawing a card from the deck...")
    # pick a colour and remove it from the colour_deck
    colour1 = colour_deck.pop(random.randint(0, len(colour_deck) - 1))
    # pick a number and remove it from the number_deck
    card1 = number_deck.pop(random.randint(0, len(number_deck) - 1))
    print("{0}{1}.".format(colour1, card1))
    # opponent draw
    print("Your opponent is drawing a card from the deck...")
    colour2 = colour_deck.pop(random.randint(0, len(colour_deck) - 1))
    card2 = number_deck.pop(random.randint(0, len(number_deck) - 1))
    print("{0}{1}.".format(colour2, card2))
    # see if we have won and increment wallet
    if card1 > card2: # Your card is higher
      print("You won this round!")
      money_counter += bet
      wallet += bet
    elif card2 > card1: # Your opponents card is higher
      print("No luck :(")
      money_counter += bet * -1
      wallet += bet * -1
    else: # it's a tie
      print("It's a tie!")
    round_counter += 1

  print("Game over! Your total winnings: {0}".format(money_counter))
  # return money won + any remaining money from the wallet
  return money_counter + wallet


# Roulette

def roulette():


# Helper functions

def get_bet(name, wallet):
  # print("Welcome to {0}!".format(name))
  print("You have £{0} in your wallet.".format(wallet))
  bet = None
  while bet is None or not 0 < bet <= wallet:
    try:
      bet = int(input("How much money would you like to bet? Please enter a whole number: "))
      while not 0 < bet <= wallet:
        if bet > wallet:
          print("It looks like you lack the funds. Please enter a smaller bet.")
        if bet <= 0:
          print("Please enter a number greater than 0.")
        bet = int(input("How much money would you like to bet? Please enter a whole number: "))
    except ValueError:
      print("Something's not right. Make sure to enter a whole number.")
  return bet


# create rounds for other games
def get_rounds(name):
  print("Welcome to {0}!".format(name))
  print("You have £{0} in your wallet.".format(money))
  print("You can play for any number of rounds between 1 (a single draw) and 26 (full deck).")
  rounds = None
  while rounds is None or not 0 < rounds <= 26:
    try: # in case user enters a float any type other then int
      rounds = int(input("How many rounds would like to play? "))
      while not 0 < rounds <= 26:
        if rounds > 26: # too many rounds
          print("There are 52 cards in a deck, so you can only play 26 rounds.")
        if rounds <= 0: # negative number or 0
          print("Please enter a number greater than 0.")
        rounds = int(input("How many rounds would like to play? "))
    except ValueError:
      print("Something's not right. Make sure to enter a whole number.")
  return rounds


# this function takes a game function as argument
def play(game):
  print("Hello! Which game would you like to play? Select a number for a game or show game descriptions: ")
  global money
  money += result
  if game > 0: # you won
    print("Woohoo! You have just won £{0}! Your wallet now has £{1}.".format(game, money))
  elif game < 0: # you lost
    print("No luck this time... :( You have  lost -£{0}! Your wallet now has £{1}.".format(game, money))
  else: # result = 0
    print("It's a tie!")
  return

# TESTING AREA #

print(money)

print(higher_card())
print(money)
