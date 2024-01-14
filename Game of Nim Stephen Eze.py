from random import randint

def main(): #These print statements are instructions to prospective players to choose what part of the game he/she will want to play
    print("This is a game of Nim, Play to Win!", "\n" + "Lets Go!!!", "\n")
    print("Choose based on the numerical arragement of the game options")
    print("1. Player Vs Player", "\n" + "2. Player Vs Computer", "\n" + "3. Two players with Arbitrary Piles and Tokens", "\n")
    userChoice = int(input("Which game will you want to play 1, 2 or 3? "))
    gameOver = False
    while not gameOver :
        if userChoice == 1: #This executes the two players codes based on the definition
            print(twoPlayerNimGame())

        elif userChoice == 2: #This executes the players Vs Computer codes based on the definition
            print(playerVsComputerNimGame())

        elif userChoice == 3: #This executes the arbitrary token and piles codes based on the definition
            print(abitraryTokenAndPile())
        else:
            print("Please enter a valid Game type", "\n") #This  is executed when a user enters a wrong choice 
            
        tryAgain = input("Do you want to try again y/n? ")# This validates the players choice to either continue playing or quit
        if tryAgain == "n":
           gameOver = True
        else:
            print("Choose based on the numerical arragement of the game options")
            print("1. Player Vs Player", "\n" + "2. Player Vs Computer", "\n" + "3. Two players with Arbitrary Piles and Tokens", "\n")
            userChoice = int(input("Which game will you want to play 1, 2 or 3? "))
           
        
        
        

def abitraryTokenAndPile():
    #This prompts a user for their names and numbers of their choice to represent the number of tokens in two pile
    player1Name = input("Player 1: Enter player name: ")
    player2Name = input("Player 2: Enter player name: ")
    print()
    #This prompts a user for the number of piles they want and the number of tokens within each pile
    pile = ["",]
    userPrompt = int(input("How many piles do you want? "))
    i = 0
    for i in range(0,userPrompt):
        tokenInEachPile = int(input("How many tokens do you want in pile " + str(i + 1) + "? "))
        i = i + 1
        pile.append(tokenInEachPile)

    print("\n" + "Your Token Piles:  Lets Go!!!", "\n")
    #This prints the piles of tokens depending on the number of piles the user wants
    userPromptRange = 0
    numberOfIteration = 0
    for tableIndex in pile[1:]:
        numberOfIteration = numberOfIteration + 1
        pileRepresentation = "*" * tableIndex
        print("Pile ", numberOfIteration, ":",pileRepresentation)
    
    #This block of codes below keeps prompting players to continue with the game until a winner is found.
    roundNumber = 0 # The round number is used to check which players turn it is to play
    tokenList = sum(pile[1:])
    playerList = [player1Name, player2Name]
    done = False
    while not done:
        roundNumber = roundNumber + 1
        if tokenList == 0:
            done = True

        elif roundNumber %2: # Here the user check is implemented to decide which player turn it is
            print(playerList[0].upper(),": Your turn!!!"+"\n")
            userPrompt1 = int(input("Which pile do you want to take from?: "))
            userPrompt2 = int(input("How many tokens do you want to remove?: "))

            #This program is executed when it is the turn of the first player(player1) to play
            #This validates the users choice to ensure itw within the scopt of the game
            if userPrompt1 not in range(numberOfIteration+1) :#This occurs when the users input is invalid
                print("Opps: Sorry you lost your round" + "\n")

            elif userPrompt2 < 0 or userPrompt2 > pile[userPrompt1]:#This occurs when the users input is invalid
                print("Opps: Sorry you lost your round" + "\n")

            else :
                if userPrompt1 in range(numberOfIteration+1) and userPrompt2 >= 0 and userPrompt2 <= pile[userPrompt1]: #This occurs when the user input is valid
                    pile[userPrompt1] = pile[userPrompt1] - userPrompt2 # This updates the list with a new value after the subtraction
                    tokenList = tokenList - userPrompt2
                    numberOfIteration = 0
                    for tableIndex in pile[1:]: # This then prints the token representation of the updated table
                        numberOfIteration = numberOfIteration + 1
                        pileRepresentation = "*" * tableIndex
                        print("Pile ", numberOfIteration, ":",pileRepresentation)

            #This program is executed when it is the turn of the second player(player2) to play
            #This validates the users choice to ensure itw within the scopt of the game

        else:
            print(playerList[1].upper(),": Your turn!!!"+"\n")
            userPrompt1 = int(input("Which pile do you want to take from?: "))
            userPrompt2 = int(input("How many tokens do you want to remove?: "))

            #This program is executed when it is the turn of the first player(player1) to play
            #This validates the users choice to ensure itw within the scopt of the game
            if userPrompt1 not in range(numberOfIteration+1) :#This occurs when the users input is invalid
                print("Opps: Sorry you lost your round" + "\n")

            elif userPrompt2 < 0 or userPrompt2 > pile[userPrompt1]:#This occurs when the users input is invalid
                print("Opps: Sorry you lost your round" + "\n")

            else :
                if userPrompt1 in range(numberOfIteration+1) and userPrompt2 >= 0 and userPrompt2 <= pile[userPrompt1]: #This occurs when the user input is valid
                    pile[userPrompt1] = pile[userPrompt1] - userPrompt2 # This updates the list with a new value after the subtraction
                    tokenList = tokenList - userPrompt2
                    numberOfIteration = 0

                    for tableIndex in pile[1:]: # This then prints the token representation of the updated table
                        numberOfIteration = numberOfIteration + 1
                        pileRepresentation = "*" * tableIndex
                        print("Pile ", numberOfIteration, ":",pileRepresentation)


                # This Checks who removed the last token and declares such player the winner

    if roundNumber %2:
        print(playerList[1].upper(), " Wins the Game" "\n" + "Congratulations!!!")
    else:
        print(playerList[0].upper(), " Wins the Game" "\n" + "Congratulations!!!")

    return("")




def twoPlayerNimGame():
    #This prompts a user for their names and numbers of their choice to represent the number of tokens in two pile
    player1Name = input("Player 1: Enter player name: ")
    player2Name = input("Player 2: Enter player name: ")
    userInput1 = int(input("Player 1: Enter the number of tokens you want in the FIRST pile: "))
    userInput2 = int(input("Player 2: Enter the number of tokens you want in the SECOND pile: "))

    #The program further multiplies the token "*" by the user input according to the prompts to create a pile of tokens
    pile1 = "*" * userInput1
    pile2 =  "*" *userInput2
    print("\n" + "Your Token Piles:  Lets Go!!!", "\n" + "\n" + "Pile 1: " + pile1, "\n" + "Pile 2: " + pile2, "\n")

    #This block of codes below keeps prompting players to continue with the game until a winner is found.

    roundNumber = 0 # The round number is used to check which players turn it is to play
    tokenList = [userInput1, userInput2]
    playerList = [player1Name, player2Name]
    done = False
    while not done:
        roundNumber = roundNumber + 1
        if tokenList[0] == 0 and tokenList[1] == 0:
            done = True

        elif roundNumber %2: # Here the user check is implemented to decide which player turn it is
            print(playerList[0].upper(),": Your turn!!!"+"\n")
            userPrompt1 = input("Which pile do you want to take from (1 or 2): ")
            userPrompt2 = int(input("How many tokens do you want to remove?: "))

        #This program is executed when it is the turn of the first player(player1) to play
        #This validates the users choice to ensure itw within the scopt of the game
            if userPrompt1 == "1" and userPrompt2 >= 0 and userPrompt2 <= tokenList[0]: #This occurs when the user input is valid
                tokenList[0] = tokenList[0] - userPrompt2
                pile1 = "*" * tokenList[0]
                pile2 = "*" * tokenList[1]
                print("\n" + "Pile 1: " + pile1, "\n" + "Pile 2: " + pile2, "\n" )

            elif userPrompt1 == "2" and userPrompt2 >= 0 and userPrompt2 <= tokenList[1]:
                tokenList[1] = tokenList[1] - userPrompt2
                pile2 = "*" * tokenList[1]
                pile1 = "*" * tokenList[0]
                print("\n" + "Pile 1: " + pile1, "\n" + "Pile 2: " + pile2, "\n" )

            elif userPrompt1 != "1" and userPrompt2 < 0 or userPrompt2 > tokenList[0]:#This occurs when the users input is invalid
                print("Opps: Sorry you lost your round" + "\n")

            else:
                print("Opps: Sorry you lost your round" + "\n")

        #This program is executed when it is the turn of the second player(player2) to play
        #This validates the users choice to ensure itw within the scopt of the game

        else:
            print(playerList[1].upper(),": Your turn!!!"+"\n")
            userPrompt1 = input("Which pile do you want to take from (1 or 2): ")
            userPrompt2 = int(input("How many tokens do you want to remove?: "))

            if userPrompt1 == "1" and userPrompt2 >= 0 and userPrompt2 <= tokenList[0]:
                tokenList[0] = tokenList[0] - userPrompt2
                pile1 = "*" * tokenList[0]
                pile2 = "*" * tokenList[1]
                print("\n" + "Pile 1: " + pile1, "\n" + "Pile 2: " + pile2, "\n" )

            elif userPrompt1 == "2" and userPrompt2 >= 0 and userPrompt2 <= tokenList[1]:
                tokenList[1] = tokenList[1] - userPrompt2
                pile2 = "*" * tokenList[1]
                pile1 = "*" * tokenList[0]
                print("\n" + "Pile 1: " + pile1, "\n" + "Pile 2: " + pile2, "\n" )

            elif userPrompt1 != "1" and userPrompt2 < 0 or userPrompt2 > tokenList[0]: #This occurs when the users input is invalid
                print("Opps: Sorry you lost your round" + "\n")

            else:
                print("Opps: Sorry you lost your round" + "\n")

        # This Checks who removed the last token and declares such player the winner
    if roundNumber %2:
        print(playerList[1].upper(), " Wins the Game" "\n" + "Congratulations!!!")

    else:
        print(playerList[0].upper(), " Wins the Game" "\n" + "Congratulations!!!")

    return("")

def playerVsComputerNimGame():
    #This prompts a user for their names and numbers of their choice to represent the number of tokens in two pile
    player1Name = input("Player 1: Enter player name: ")
    player2Name = "Computer"
    userInput1 = int(input("Enter the number of tokens you want in the FIRST pile: "))
    userInput2 = int(input("Enter the number of tokens you want in the SECOND pile: "))

    #The program further multiplies the token "*" by the user input according to the prompts to create a pile of tokens
    pile1 = "*" * userInput1
    pile2 =  "*" *userInput2
    print("\n" + "Your Token Piles:  Lets Go!!!", "\n" + "\n" + "Pile 1: " + pile1, "\n" + "Pile 2: " + pile2, "\n")

    #This block of codes below keeps prompting players to continue with the game until a winner is found.

    roundNumber = 0 # The round number is used to check which players turn it is to play
    tokenList = [userInput1, userInput2]
    playerList = [player1Name, player2Name]
    done = False
    while not done:
        roundNumber = roundNumber + 1
        if tokenList[0] == 0 and tokenList[1] == 0:
            done = True

        elif roundNumber %2: # Here the user check is implemented to decide which player turn it is
            print(playerList[0].upper(),": Your turn!!!"+"\n")
            userPrompt1 = input("Which pile do you want to take from (1 or 2): ")
            userPrompt2 = int(input("How many tokens do you want to remove?: "))

        #This program is executed when it is the turn of the first player(player1) to play
        #This validates the users choice to ensure itw within the scopt of the game
            if userPrompt1 == "1" and userPrompt2 >= 0 and userPrompt2 <= tokenList[0]: #This occurs when the user input is valid
                tokenList[0] = tokenList[0] - userPrompt2
                pile1 = "*" * tokenList[0]
                pile2 = "*" * tokenList[1]
                print("\n" + "Pile 1: " + pile1, "\n" + "Pile 2: " + pile2, "\n" )

            elif userPrompt1 == "2" and userPrompt2 >= 0 and userPrompt2 <= tokenList[1]:
                tokenList[1] = tokenList[1] - userPrompt2
                pile2 = "*" * tokenList[1]
                pile1 = "*" * tokenList[0]
                print("\n" + "Pile 1: " + pile1, "\n" + "Pile 2: " + pile2, "\n" )

            elif userPrompt1 != "1" and userPrompt2 < 0 or userPrompt2 > tokenList[0]:#This occurs when the users input is invalid
                print("Opps: Sorry you lost your round" + "\n")

            else:
                print("Opps: Sorry you lost your round" + "\n")

        #This block of code is executed when it is the turn of the second player(computer) to play
        #This validates the computers choice by giving it a range for it to pick a random number
        else:
            print(playerList[1].upper(),"Played"+"\n")

            computerRandomPileChoice = randint(1,2)
            computerRandomTokenChoiceInPile1 = randint(0, tokenList[0])
            computerRandomTokenChoiceInPile2 = randint(0, tokenList[1])

            if computerRandomPileChoice == 1 :
                tokenList[0] = tokenList[0] - computerRandomTokenChoiceInPile1
                pile1 = "*" * tokenList[0]
                pile2 = "*" * tokenList[1]
                print("I removed ", computerRandomTokenChoiceInPile1, " from pile 1")
                print("\n" + "Pile 1: " + pile1, "\n" + "Pile 2: " + pile2, "\n" )

            else:
                tokenList[1] = tokenList[1] - computerRandomTokenChoiceInPile2
                pile2 = "*" * tokenList[1]
                pile1 = "*" * tokenList[0]
                print("I removed ", computerRandomTokenChoiceInPile2, " from pile 2")
                print("\n" + "Pile 1: " + pile1, "\n" + "Pile 2: " + pile2, "\n" )

        # This Checks who removed the last token and declares such player the winner
    if roundNumber %2:
        print("OOPS!!!" "\n","\n" + playerList[1].upper(), " Wins the Game" )

    else:
        print(playerList[0].upper(), " Wins the Game" "\n" + "Congratulations!!!")

    return("")
        

main()            
            
                
                

            
                
                

                    
                
                
       
        
            
            
                
                

