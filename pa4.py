#Programmers: Callie Walker
#Programming Assignment: 4
#Course: CS151, Dr. Rajeev
#Programming Input: User choice for cards
#Programming Outputs: What the user's cards are and if its over 21, computer's hand
import random
deckOfCards = ["1c", "1d", "1h", "1s","2c","2d","2h","2s", "3c", "3d", "3h", "3s", "4c", "4d", "4h", "4s,", "5c","5d", "5h", "5s", "6c", "6d", "6h", "6s", "7c", "7d", "7h", "7s", "8c", "8d", "8h", "8s", "9c", "9d", "9h", "9s", "10c", "10d", "10h", "10h", "11c", "11d", "11h", "11h", "12c", "12d", "12h", "12s", "13c", "13d", "13h", "13s"]
playerHand = []
card1 = random.choice(deckOfCards)
points = 0
def deck(list):
    # A function that generates shuffled deck
    for i in list:
        list.sort()
    for i in list:
        random.shuffle(list)
    print(list)
def cardDescription(card):
    cardName = " "
    for i in deckOfCards:
        #Prints description for cards values 2-9
        if(len(card) == 2 and not card[0] == "1"):
            if(card[-1] == "c" ):
                print(card[0], "of clubs")
            elif(card[0] == "d" ):
                print(card[0], "of diamonds")
            elif(card[-1] == "h" ):
                print(card[0], "of hearts")
            elif(card[-1] == "s" ):
                print(card[0], "of spades")
        elif (len(card) == 2 and card[0] == "1"):
            if (card[-1] == "c"):
                print("Ace of clubs")
            elif (card[0] == "d"):
                print("Ace of diamonds")
            elif (card[-1] == "h"):
                print("Ace of hearts")
            elif (card[-1] == "s"):
                print("Ace of spades")
        #Description for values of 10-11
        elif(len(card) == 3 and card[0:2]== "10" or card[0:2]== "11"):
            if (card[-1] == "c"):
                print(card[:2], "of clubs")
            elif (card[0] == "d"):
                print(card[:2], "of diamonds")
            elif (card[-1] == "h"):
                print(card[:2], "of hearts")
            elif (card[-1] == "s"):
                print(card[:2], "of spades")
        #Evaluates King and Queen value descriptions
        elif (len(card) == 3 and card[0:2] == "12"):
            if (card[-1] == "c"):
                print("Queen of clubs")
            elif (card[0] == "d"):
                print("Queen of diamonds")
            elif (card[-1] == "h"):
                print("Queen of hearts")
            elif (card[-1] == "s"):
                print("Queen of spades")
        elif (len(card) == 3 and card[0:2] == "13"):
            if (card[-1] == "c"):
                print("King of clubs")
            elif (card[0] == "d"):
                print("King of diamonds")
            elif (card[-1] == "h"):
                print("King of hearts")
            elif (card[-1] == "s"):
                print("King of spades")

def generateHand(handList, card):
    for i in handList:
        cardDescription(card)
        handList.append(card)
    return handList
def pointSystem(hand, card):
    points = 0
    for i in deckOfCards:
        card = hand[i]
        if(card[0:2] == "12" or card[0:2] == "13"):
            points += 10
        elif(len(hand(i)) == 3):
            points += card[0:2]
        elif(len(card) == 2 and card[0:1] == "1"):
            points += 11
        elif (len(card) == 2 and not card[0:1] == "1"):
            points += card[0:1]

    return points
def computer():
    dealerHand = []
    for i in deckOfCards:
        dealerCard = random.choice(deckOfCards)
        draw = dealerHand.append(dealerHand)
        while points <=17:
            dealerCard = random.choice(deckOfCards)
            draw = dealerHand.append(dealerHand)
    print("busted")

def main():
    deck(deckOfCards)
    for i in playerHand:
        cardInHand = playerHand[i]
        pointSystem(playerHand, cardInHand)
    for i in deckOfCards:
        # This chooses the players inital hand, removes those cards from deck and adds to player hand
        card1 = random.choice(deckOfCards)
        card2 = random.choice(deckOfCards)
        deckOfCards.remove(card1)
        deckOfCards.remove(card2)
        playerHand.append(card1)
        playerHand.append(card2)
        while points < 21:
            userPrompt = input("Hit or Stop? ")
            userPrompt = userPrompt.strip().lower()
            if (userPrompt == "hit"):
                newCard = random.choice(deckOfCards)
                #generateHand(playerHand, newCard)
                hand = deckOfCards.remove(i)
                cardDescription(playerHand)
            elif (userPrompt == "stop"):
                computer()
            else:
                print("invalid, try again")

main()
