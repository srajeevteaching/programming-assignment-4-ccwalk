def userHand():
    playerHand = []
    for i in deckOfCards:
       #This chooses the players inital hand, removes those cards from deck and adds to player hand
       card1 = random.choice(deckOfCards)
       card2 = random.choice(deckOfCards)
       deckOfCards.remove(card1)
       deckOfCards.remove(card2)
       playerHand.append(card1)
       playerHand.append(card2)
    return playerHand
def computer():
    dealerHand = []
    for i in deckOfCards:
        dealerCard = random.choice(deckOfCards)
        draw = dealerHand.append(dealerHand)

def main():
    points = 0
    userHand()
    # Need to have if statement to calculate the points of the cards and add them to points
    for i in deckOfCards:
        while points < 21:
            userPrompt = input("Hit or Stop?")
            userPrompt = userPrompt.strip().lower()
            if (userPrompt == "hit"):
                random.randint(0, deckOfCards.index(i))
                hand = deckOfCards.remove(i)
                playerHand.append(hand)
            elif (userPrompt == "stop"):
                computer()
            else:
                print("invalid, try again")
main()
