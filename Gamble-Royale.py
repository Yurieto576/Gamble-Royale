# Name: Gamble Royale
# Creator: Bill Johnson

import random
import time

money = random.randrange(100, 350)
name = input("Hello. This is a game medley Royale Software. What is your name? ")
time.sleep(2.84375978435726554287)
# First Game
def Craps(money):
  diceFace = random.randrange(1,6)
  dicFace2 = random.randrange(1,6)
  finalCombo = diceFace + dicFace2
  virtualmoney = 30

  print("The roll for you comes out to be", finalCombo)
  if finalCombo == 7 or finalCombo == 11:
    print("holy ****, you actually won this time. Your rolls came out as", diceFace, "and ", dicFace2)
    virtualmoney += 1
    print(virtualmoney)
    print()
  elif finalCombo != 7 or finalCombo != 11:
    virtualmoney -= 1
    print("HAHA! I am now richer than you. You got some lousy", diceFace, "and ", dicFace2, "for rolls! ")
    print(virtualmoney)
    print() 
    if virtualmoney == 0:
      print("I own you now. ")
      print()
      quit("You are now his slave. ")
  # Rewind time
  redo = input("Do you wanna try again? y or n. ")
  if redo == "y":
    print()
    print()  
    print("Let's do this. ")
    return Craps(money)
  elif redo == "n":
    print() 
    print("Goodbye. ")
    return Greetings()

# Second Game
def Roulette(money):
  money = 30
  green = 0
  red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36)
  black = (2, 4, 6, 8, 10, 11, 13, 15,17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35)
  even = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,34, 36)
  odd = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35)
  rollup = random.randint(1, 36)
  psyche = input("What color and number do you think will win big? Red | Black | or Green? ")
  if psyche == rollup:
    money += 10
    print("You win this time. ")
    print("Your current total here is: ", money)
  if psyche != rollup:
    money -= 10
    print("Sorry. Better luck next time")
    print("Your current total so far is: ", money)
    print("YOU GOT.... ", rollup)
    print("------------------------------------------------------")
    time.sleep(3)
    print("HAHAHAHAHAHAHA!!!!!!!!")
    print()
    time.sleep(4)
    print("I am now richer than you. ")
  if money == 0:
    print("You are officialy out og money. ")
    print()   
    time.sleep(3)
    print("GET OUT OF MY CASINO!!!!! ")
    quit()
  redo = input("DO you want to try it again? yes. or no. ")
  if redo == "yes" or redo == "y":
    print() 
    return Roulette(money)
  elif redo == "no" or redo == "n":
    print("Depart from my casino at once. ")
    time.sleep(2)
    return Greetings()
  
  if (rollup) == even:
    money + 2
    print("You win ")
  elif (rollup) == odd:
    money + 2
    print("You win. ")
  elif (rollup) == red: 
    money + 2
    print("You win. ")
  elif (rollup) == black:
    money + 2
    print("You win. ")
  elif (rollup) == green: 
    money + 2
    print("You win. ")

# Final Game
def BlackJack():
  money = 800
  print() 
  offering = int(input("How much money will you part with to play?  THE MAXIMUM is 800. "))
  newMoney = money +- offering
  gamble = input("This is an irreversible command. Do you want to proceed? ")
  if gamble == "sure" or gamble == "meh, I guess so":
    print("Let's play. Note this: The goal here is to get as close to 21 without going over 21. ")
    dealer_cards = []
    player_cards = []
    while len(dealer_cards) != 2:
      dealer_cards.append(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]))  
      if len(dealer_cards) == 2:
        print("Dealer has X &", dealer_cards[1])

        while len(player_cards) != 2:
            player_cards.append(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]))
        if len(player_cards) == 2:
            print("You have: ", player_cards)       
        if sum(dealer_cards) == 21:
            money -= offering
            print("Dealer has 21. It's a shame you lost. ")
        elif sum(dealer_cards) > 21:
            print("Dealer bust")
        while sum(player_cards) < 21:
            action_taken = str(input("Do you want to stay or hit? "))
            if action_taken == "hit":
                player_cards.append(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]))
                print(player_cards[-1])
            elif action_taken == "stay":
                print("you have", sum(player_cards))
                break
        print("Dealer has", sum(dealer_cards))    
        if sum(player_cards)>21:
            money -= offering
            print("you have: ", sum(player_cards), "you busted")
            print("Your total now is; ", newMoney)
        else:
            if sum(player_cards)>sum(dealer_cards):
                money += offering
                print("Damn. You won.")
            elif sum(player_cards)<sum(dealer_cards):
                print("hahahahahahahahahahahahahahahahahahahahahahahahaha. Give me you money!!!!!")
  elif gamble == "no":
    print("RIP. Maybe later.")
    return Greetings()
  else:
    print("NO. I'm bored now with your incompetent decision-making.")

def Greetings():
  print()    
  print("01000101, ", name)
  print()
  time.sleep(3)
  startfunct = input("We have a number of games that will have us playing common games using math. The options are: BlackJack | Roulette | Craps. ")

  if startfunct == "craps" or startfunct == "Craps":
    Craps(money)
  if startfunct == "roulette" or startfunct == "Roulette":
    Roulette(money)
  if startfunct == "blackjack" or startfunct == "Blackjack":
    BlackJack()

Greetings()
