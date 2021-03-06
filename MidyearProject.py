import random

def miniGames():
    print("What game would you like to play?\n\n\t1 - Coin flipping\n\t2 - Rock Paper Scissors\n\t3 - Rock Paper Scissors Lizard Spock\n\t4 - Tic Tac Toe\n\t5 - One Hundred")
    gameChoice = input()
    while gameChoice != "1" and gameChoice != "2" and gameChoice != "3" and gameChoice != "4" and gameChoice != "5" and gameChoice.lower() != "back":
        gameChoice = input("Invalid answer. Please enter in a valid number.")
    if gameChoice == "1":
        cF()
    elif gameChoice == "2":
        rPS()
    elif gameChoice == "3":
        rPSLSp()
    elif gameChoice == "4":
        tTT()
    elif gameChoice == "5":
        oneHundred()
    elif gameChoice.lower() == "back":
        menu()

def cF():
    coin = random.randint(0, 1)
    print("The coin has been flipped. What do you think it is? Heads, or tails?")
    cfChoice = input()
    while cfChoice.lower() != "heads" and cfChoice.lower() != "tails":
        cfChoice = input("Invalid answer. Please try again. ")
    if cfChoice.lower() == "heads" and coin == 0:
        print("You lost. The coin landed on tails.")
    elif cfChoice.lower() == "heads" and coin == 1:
        print("You won! The coin landed on heads.")
    elif cfChoice.lower() == "tails" and coin == 0:
        print("You won! The coin landed on tails.")
    elif cfChoice.lower() == "tails" and coin == 1:
        print("You lost! The coin landed on tails.")
    cfAgain = input("Again? ")
    while cfAgain.lower() != "yes" and cfAgain.lower() != "no":
        cfAgain = input("Invalid answer. Please try again. ")
    while cfAgain.lower() == "yes":
        cF()
    if cfAgain == "no":
        miniGames()

def rPS():
    battle = random.randint(0, 2)
    rpsChoice = input("Rock paper scissors SAYS.... what? ")
    while rpsChoice.lower() != "rock" and rpsChoice.lower() != "paper" and rpsChoice.lower() != "scissors":
        rpsChoice = input("Invalid answer. Please try again. ")
    if rpsChoice.lower() == "rock" and battle == 0:
        print("You both chose rock. It's a tie.")
    elif rpsChoice.lower() == "rock" and battle == 1:
        print("The computer chose paper. You lose.")
    elif rpsChoice.lower() == "rock" and battle == 2:
        print("The computer chose scissors. You win!")
    elif rpsChoice.lower() == "paper" and battle == 0:
        print("The computer chose rock. You win!")
    elif rpsChoice.lower() == "paper" and battle == 1:
        print("You both chose paper. It's a tie.")
    elif rpsChoice.lower() == "paper" and battle == 2:
        print("The computer chose scissors. You lose.")
    elif rpsChoice.lower() == "scissors" and battle == 0:
        print("The computer chose rock. You lose.")
    elif rpsChoice.lower() == "scissors" and battle == 1:
        print("The computer chose paper. You win!")
    elif rpsChoice.lower() == "scissors" and battle == 2:
        print("You both chose scissors. It's a tie.")
    rpsAgain = input("Again? ")
    while rpsAgain.lower() != "yes" and rpsAgain.lower() != "no":
        rpsAgain = input("Invalid answer. Please try again. ")
    while rpsAgain.lower() == "yes":
        rPS()
    if rpsAgain == "no":
        miniGames()

def rPSLSp():
    battle = random.randint(0, 4)
    rpsChoice = input("Chose rock, paper, scissors, lizard, or Spock. ")
    while rpsChoice.lower() != "rock" and rpsChoice.lower() != "paper" and rpsChoice.lower() != "scissors" and rpsChoice.lower() != "lizard" and rpsChoice.lower() != "spock":
        rpsChoice = input("Invalid answer. Please try again. ")
    if rpsChoice.lower() == "rock" and battle == 0:
        print("You both chose rock. It's a tie.")
    elif rpsChoice.lower() == "rock" and battle == 1:
        print("The computer chose paper. You lose.")
    elif rpsChoice.lower() == "rock" and battle == 2:
        print("The computer chose scissors. You win!")
    elif rpsChoice.lower() == "rock" and battle == 3:
        print("The computer chose lizard. You win!")
    elif rpsChoice.lower() == "rock" and battle == 4:
        print("The computer chose Spock. You lose.")

    elif rpsChoice.lower() == "paper" and battle == 0:
        print("The computer chose rock. You win!")
    elif rpsChoice.lower() == "paper" and battle == 1:
        print("You both chose paper. It's a tie.")
    elif rpsChoice.lower() == "paper" and battle == 2:
        print("The computer chose scissors. You lose.")
    elif rpsChoice.lower() == "paper" and battle == 3:
        print("The computer chose lizard. You lose.")
    elif rpsChoice.lower() == "paper" and battle == 4:
        print("The computer chose Spock. You win!")

    elif rpsChoice.lower() == "scissors" and battle == 0:
        print("The computer chose rock. You lose.")
    elif rpsChoice.lower() == "scissors" and battle == 1:
        print("The computer chose paper. You win!")
    elif rpsChoice.lower() == "scissors" and battle == 2:
        print("You both chose scissors. It's a tie.")
    elif rpsChoice.lower() == "scissors" and battle == 3:
        print("The computer chose lizard. You win!")
    elif rpsChoice.lower() == "scissors" and battle == 4:
        print("The computer chose Spock. You lose.")

    elif rpsChoice.lower() == "lizard" and battle == 0:
        print("The computer chose rock. You lose.")
    elif rpsChoice.lower() == "lizard" and battle == 1:
        print("The computer chose paper. You win!")
    elif rpsChoice.lower() == "lizard" and battle == 2:
        print("The computer chose scissors. You lose.")
    elif rpsChoice.lower() == "lizard" and battle == 3:
        print("You both chose lizard. It's a tie.")
    elif rpsChoice.lower() == "lizard" and battle == 4:
        print("The computer chose Spock. You win!")

    elif rpsChoice.lower() == "spock" and battle == 0:
        print("The computer chose rock. You win!")
    elif rpsChoice.lower() == "spock" and battle == 1:
        print("The computer chose paper. You lose")
    elif rpsChoice.lower() == "spock" and battle == 2:
        print("The computer chose scissors. You win!")
    elif rpsChoice.lower() == "spock" and battle == 3:
        print("The computer chose lizard. You lose.")
    elif rpsChoice.lower() == "spock" and battle == 4:
        print("You both chose Spock. It's a tie.")
    rpsAgain = input("Again? ")
    while rpsAgain.lower() != "yes" and rpsAgain.lower() != "no":
        rpsAgain = input("Invalid answer. Please try again. ")
    while rpsAgain.lower() == "yes":
        rPSLSp()
    if rpsAgain == "no":
        miniGames()

def oneHundred():
    turn = random.randint(0, 1)
    cTurn = 0
    sumNum = 0
    validNumber = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    while sumNum < 100:
        if turn == 1:
            cTurn = 1
            comChoice = random.randint(1, 10)
            userChoice = input("What number would you like to add to the sum? (1 to 10) ")
            while userChoice not in validNumber:
                userChoice = input("Invalid answer, please try again. ")
            sumNum += int(userChoice)
            if sumNum < 100:
                cTurn = 0
                comChoice = random.randint(1, 10)
                if sumNum < 89 and sumNum > 78:
                    faith = random.randint(1, 3)
                    sumNum += (89 - sumNum)
                elif sumNum > 89:
                    faith = random.randint(1, 3)
                    sumNum += (100 - sumNum)
                else:
                    faith = random.randint(1, 3)
                    comChoice = random.randint(1, 10)
                    sumNum += comChoice
                if sumNum > 100:
                    sumNum = 100
                if sumNum != 100:
                    print("The computer decided to add %d to the sum. The new sum is %d. " % (comChoice, sumNum))
        else:
            if sumNum > 100:
                sumNum = 100
            cTurn = 0
            comChoice = random.randint(1, 10)
            faith = random.randint(1, 3)
            if sumNum < 89 and sumNum > 78 and faith == 1:
                faith = random.randint(1, 3)
                sumNum += (89 - sumNum)
            elif sumNum > 89 and faith == 1:
                faith = random.randint(1, 3)
                sumNum += (100 - sumNum)
            else:
                faith = random.randint(1, 3)
                comChoice = random.randint(1, 10)
                sumNum += comChoice

            if sumNum > 100:
                sumNum = 100
            if sumNum != 100:
                print("The computer decided to add %d to the sum. The new sum is %d. " % (comChoice, sumNum))
            if sumNum < 100:
                cTurn = 1
                userChoice = input("What number would you like to add to the sum? (1 to 10) ")
                while userChoice not in validNumber:
                    userChoice = input("Invalid answer, please try again. ")
                sumNum += int(userChoice)
    if sumNum == 100 and cTurn == 0:
        print("The game has ended. Since the computer added the last number to reach 100, you lose.")
    else:
        print("The game has ended. Since you added the last number to reach 100, you win!")
    ohAgain = input("Again? ")
    while ohAgain.lower() != "yes" and ohAgain.lower() != "no":
        ohAgain = input("Invalid answer. Please try again. ")
    while ohAgain.lower() == "yes":
        oneHundred()
    if ohAgain == "no":
        miniGames()

def tTT():
    turn = random.randint(0, 1)
    s1 = " "
    s2 = " "
    s3 = " "
    s4 = " "
    s5 = " "
    s6 = " "
    s7 = " "
    s8 = " "
    s9 = " "
    archived = []
    isDone = 0
    if turn == 0:
        # 1
        compChoice = random.randint(1, 9)
        print("The computer will go first.")
        if compChoice == 1:
            s1 = "X"
            archived.append("1")
        elif compChoice == 2:
            s2 = "X"
            archived.append("2")
        elif compChoice == 3:
            s3 = "X"
            archived.append("3")
        elif compChoice == 4:
            s4 = "X"
            archived.append("4")
        elif compChoice == 5:
            s5 = "X"
            archived.append("5")
        elif compChoice == 6:
            s6 = "X"
            archived.append("6")
        elif compChoice == 7:
            s7 = "X"
            archived.append("7")
        elif compChoice == 8:
            s8 = "X"
            archived.append("8")
        else:
            s9 = "X"
            archived.append("9")
        print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
        s1, s2, s3, s4, s5, s6, s7, s8, s9))
        # 2
        userChoice = input("Which section would you like to fill in? ")
        while userChoice in archived or (userChoice != "1" and userChoice != "2" and userChoice != "3" and
                                         userChoice != "4" and userChoice != "5" and userChoice != "6" and
                                         userChoice != "7" and userChoice != "8" and userChoice != "9"):
            userChoice = input("Invalid answer. Please try again. ")
        if userChoice == "1" and userChoice not in archived:
            s1 = "O"
            archived.append("1")
        elif userChoice == "2" and userChoice not in archived:
            s2 = "O"
            archived.append("2")
        elif userChoice == "3" and userChoice not in archived:
            s3 = "O"
            archived.append("3")
        elif userChoice == "4" and userChoice not in archived:
            s4 = "O"
            archived.append("4")
        elif userChoice == "5" and userChoice not in archived:
            s5 = "O"
            archived.append("5")
        elif userChoice == "6" and userChoice not in archived:
            s6 = "O"
            archived.append("6")
        elif userChoice == "7" and userChoice not in archived:
            s7 = "O"
            archived.append("7")
        elif userChoice == "8" and userChoice not in archived:
            s8 = "O"
            archived.append("8")
        elif userChoice == "9" and userChoice not in archived:
            s9 = "O"
            archived.append("9")
        # 3
        compChoice = random.randint(1, 9)
        while str(compChoice) in archived:
            compChoice = random.randint(1, 9)
        if compChoice == 1 and str(compChoice) not in archived:
            s1 = "X"
            archived.append("1")
        elif compChoice == 2 and str(compChoice) not in archived:
            s2 = "X"
            archived.append("2")
        elif compChoice == 3 and str(compChoice) not in archived:
            s3 = "X"
            archived.append("3")
        elif compChoice == 4 and str(compChoice) not in archived:
            s4 = "X"
            archived.append("4")
        elif compChoice == 5 and str(compChoice) not in archived:
            s5 = "X"
            archived.append("5")
        elif compChoice == 6 and str(compChoice) not in archived:
            s6 = "X"
            archived.append("6")
        elif compChoice == 7 and str(compChoice) not in archived:
            s7 = "X"
            archived.append("7")
        elif compChoice == 8 and str(compChoice) not in archived:
            s8 = "X"
            archived.append("8")
        elif compChoice == 9 and str(compChoice) not in archived:
            s9 = "X"
            archived.append("9")
        print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
        s1, s2, s3, s4, s5, s6, s7, s8, s9))
        # 4
        userChoice = input("Which section would you like to fill in? ")
        while userChoice in archived or (userChoice != "1" and userChoice != "2" and userChoice != "3" and
                                         userChoice != "4" and userChoice != "5" and userChoice != "6" and
                                         userChoice != "7" and userChoice != "8" and userChoice != "9"):
            userChoice = input("Invalid answer. Please try again. ")
        if userChoice == "1" and userChoice not in archived:
            s1 = "O"
            archived.append("1")
        elif userChoice == "2" and userChoice not in archived:
            s2 = "O"
            archived.append("2")
        elif userChoice == "3" and userChoice not in archived:
            s3 = "O"
            archived.append("3")
        elif userChoice == "4" and userChoice not in archived:
            s4 = "O"
            archived.append("4")
        elif userChoice == "5" and userChoice not in archived:
            s5 = "O"
            archived.append("5")
        elif userChoice == "6" and userChoice not in archived:
            s6 = "O"
            archived.append("6")
        elif userChoice == "7" and userChoice not in archived:
            s7 = "O"
            archived.append("7")
        elif userChoice == "8" and userChoice not in archived:
            s8 = "O"
            archived.append("8")
        elif userChoice == "9" and userChoice not in archived:
            s9 = "O"
            archived.append("9")
        # 5
        compChoice = random.randint(1, 9)
        while str(compChoice) in archived:
            compChoice = random.randint(1, 9)
        if compChoice == 1 and str(compChoice) not in archived:
            s1 = "X"
            archived.append("1")
        elif compChoice == 2 and str(compChoice) not in archived:
            s2 = "X"
            archived.append("2")
        elif compChoice == 3 and str(compChoice) not in archived:
            s3 = "X"
            archived.append("3")
        elif compChoice == 4 and str(compChoice) not in archived:
            s4 = "X"
            archived.append("4")
        elif compChoice == 5 and str(compChoice) not in archived:
            s5 = "X"
            archived.append("5")
        elif compChoice == 6 and str(compChoice) not in archived:
            s6 = "X"
            archived.append("6")
        elif compChoice == 7 and str(compChoice) not in archived:
            s7 = "X"
            archived.append("7")
        elif compChoice == 8 and str(compChoice) not in archived:
            s8 = "X"
            archived.append("8")
        elif compChoice == 9 and str(compChoice) not in archived:
            s9 = "X"
            archived.append("9")
        print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
        s1, s2, s3, s4, s5, s6, s7, s8, s9))
        if ((s1 == "X" and s2 == "X" and s3 == "X") or (s4 == "X" and s5 == "X" and s6 == "X") or
                (s7 == "X" and s8 == "X" and s9 == "X") or (s1 == "X" and s4 == "X" and s7 == "X") or
                (s2 == "X" and s5 == "X" and s8 == "X") or (s3 == "X" and s6 == "X" and s9 == "X") or
                (s1 == "X" and s5 == "X" and s9 == "X") or (s3 == "X" and s5 == "X" and s7 == "X")):
            isDone = 1
            print("You lose.")
        if isDone == 0:
            # 6
            userChoice = input("Which section would you like to fill in? ")
            while userChoice in archived or (userChoice != "1" and userChoice != "2" and userChoice != "3" and
                                             userChoice != "4" and userChoice != "5" and userChoice != "6" and
                                             userChoice != "7" and userChoice != "8" and userChoice != "9"):
                userChoice = input("Invalid answer. Please try again. ")
            if userChoice == "1" and userChoice not in archived:
                s1 = "O"
                archived.append("1")
            elif userChoice == "2" and userChoice not in archived:
                s2 = "O"
                archived.append("2")
            elif userChoice == "3" and userChoice not in archived:
                s3 = "O"
                archived.append("3")
            elif userChoice == "4" and userChoice not in archived:
                s4 = "O"
                archived.append("4")
            elif userChoice == "5" and userChoice not in archived:
                s5 = "O"
                archived.append("5")
            elif userChoice == "6" and userChoice not in archived:
                s6 = "O"
                archived.append("6")
            elif userChoice == "7" and userChoice not in archived:
                s7 = "O"
                archived.append("7")
            elif userChoice == "8" and userChoice not in archived:
                s8 = "O"
                archived.append("8")
            elif userChoice == "9" and userChoice not in archived:
                s9 = "O"
                archived.append("9")
            if ((s1 == "X" and s2 == "X" and s3 == "X") or (s4 == "X" and s5 == "X" and s6 == "X") or
                    (s7 == "X" and s8 == "X" and s9 == "X") or (s1 == "X" and s4 == "X" and s7 == "X") or
                    (s2 == "X" and s5 == "X" and s8 == "X") or (s3 == "X" and s6 == "X" and s9 == "X") or
                    (s1 == "X" and s5 == "X" and s9 == "X") or (s3 == "X" and s5 == "X" and s7 == "X")):
                print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                s1, s2, s3, s4, s5, s6, s7, s8, s9))
                isDone = 1
                print("You lose.")
            elif ((s1 == "O" and s2 == "O" and s3 == "O") or (s4 == "O" and s5 == "O" and s6 == "O") or
                  (s7 == "O" and s8 == "O" and s9 == "O") or (s1 == "O" and s4 == "O" and s7 == "O") or
                  (s2 == "O" and s5 == "O" and s8 == "O") or (s3 == "O" and s6 == "O" and s9 == "O") or
                  (s1 == "O" and s5 == "O" and s9 == "O") or (s3 == "O" and s5 == "O" and s7 == "O")):
                print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                s1, s2, s3, s4, s5, s6, s7, s8, s9))
                isDone = 1
                print("You win.")
            if isDone == 0:
                # 7
                compChoice = random.randint(1, 9)
                while str(compChoice) in archived:
                    compChoice = random.randint(1, 9)
                if compChoice == 1 and str(compChoice) not in archived:
                    s1 = "X"
                    archived.append("1")
                elif compChoice == 2 and str(compChoice) not in archived:
                    s2 = "X"
                    archived.append("2")
                elif compChoice == 3 and str(compChoice) not in archived:
                    s3 = "X"
                    archived.append("3")
                elif compChoice == 4 and str(compChoice) not in archived:
                    s4 = "X"
                    archived.append("4")
                elif compChoice == 5 and str(compChoice) not in archived:
                    s5 = "X"
                    archived.append("5")
                elif compChoice == 6 and str(compChoice) not in archived:
                    s6 = "X"
                    archived.append("6")
                elif compChoice == 7 and str(compChoice) not in archived:
                    s7 = "X"
                    archived.append("7")
                elif compChoice == 8 and str(compChoice) not in archived:
                    s8 = "X"
                    archived.append("8")
                elif compChoice == 9 and str(compChoice) not in archived:
                    s9 = "X"
                    archived.append("9")
                print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                s1, s2, s3, s4, s5, s6, s7, s8, s9))
                if ((s1 == "X" and s2 == "X" and s3 == "X") or (s4 == "X" and s5 == "X" and s6 == "X") or
                        (s7 == "X" and s8 == "X" and s9 == "X") or (s1 == "X" and s4 == "X" and s7 == "X") or
                        (s2 == "X" and s5 == "X" and s8 == "X") or (s3 == "X" and s6 == "X" and s9 == "X") or
                        (s1 == "X" and s5 == "X" and s9 == "X") or (s3 == "X" and s5 == "X" and s7 == "X")):
                    isDone = 1
                    print("You lose.")
                elif ((s1 == "O" and s2 == "O" and s3 == "O") or (s4 == "O" and s5 == "O" and s6 == "O") or
                      (s7 == "O" and s8 == "O" and s9 == "O") or (s1 == "O" and s4 == "O" and s7 == "O") or
                      (s2 == "O" and s5 == "O" and s8 == "O") or (s3 == "O" and s6 == "O" and s9 == "O") or
                      (s1 == "O" and s5 == "O" and s9 == "O") or (s3 == "O" and s5 == "O" and s7 == "O")):
                    isDone = 1
                    print("You win.")
                # 8
                if isDone == 0:
                    userChoice = input("Which section would you like to fill in? ")
                while userChoice in archived and isDone == 0 or (
                        userChoice != "1" and userChoice != "2" and userChoice != "3" and
                        userChoice != "4" and userChoice != "5" and userChoice != "6" and
                        userChoice != "7" and userChoice != "8" and userChoice != "9"):
                    userChoice = input("Invalid answer. Please try again. ")
                if userChoice == "1" and userChoice not in archived:
                    s1 = "O"
                    archived.append("1")
                elif userChoice == "2" and userChoice not in archived:
                    s2 = "O"
                    archived.append("2")
                elif userChoice == "3" and userChoice not in archived:
                    s3 = "O"
                    archived.append("3")
                elif userChoice == "4" and userChoice not in archived:
                    s4 = "O"
                    archived.append("4")
                elif userChoice == "5" and userChoice not in archived:
                    s5 = "O"
                    archived.append("5")
                elif userChoice == "6" and userChoice not in archived:
                    s6 = "O"
                    archived.append("6")
                elif userChoice == "7" and userChoice not in archived:
                    s7 = "O"
                    archived.append("7")
                elif userChoice == "8" and userChoice not in archived:
                    s8 = "O"
                    archived.append("8")
                elif userChoice == "9" and userChoice not in archived:
                    s9 = "O"
                    archived.append("9")
                if ((s1 == "X" and s2 == "X" and s3 == "X") or (s4 == "X" and s5 == "X" and s6 == "X") or
                        (s7 == "X" and s8 == "X" and s9 == "X") or (s1 == "X" and s4 == "X" and s7 == "X") or
                        (s2 == "X" and s5 == "X" and s8 == "X") or (s3 == "X" and s6 == "X" and s9 == "X") or
                        (s1 == "X" and s5 == "X" and s9 == "X") or (s3 == "X" and s5 == "X" and s7 == "X")):
                    print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                    s1, s2, s3, s4, s5, s6, s7, s8, s9))
                    isDone = 1
                    print("You lose.")
                elif ((s1 == "O" and s2 == "O" and s3 == "O") or (s4 == "O" and s5 == "O" and s6 == "O") or
                      (s7 == "O" and s8 == "O" and s9 == "O") or (s1 == "O" and s4 == "O" and s7 == "O") or
                      (s2 == "O" and s5 == "O" and s8 == "O") or (s3 == "O" and s6 == "O" and s9 == "O") or
                      (s1 == "O" and s5 == "O" and s9 == "O") or (s3 == "O" and s5 == "O" and s7 == "O")):
                    print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                    s1, s2, s3, s4, s5, s6, s7, s8, s9))
                    isDone = 1
                    print("You win.")
                # 9
                if isDone == 0:
                    compChoice = random.randint(1, 9)
                    while str(compChoice) in archived:
                        compChoice = random.randint(1, 9)
                    if compChoice == 1 and str(compChoice) not in archived:
                        s1 = "X"
                        archived.append("1")
                    elif compChoice == 2 and str(compChoice) not in archived:
                        s2 = "X"
                        archived.append("2")
                    elif compChoice == 3 and str(compChoice) not in archived:
                        s3 = "X"
                        archived.append("3")
                    elif compChoice == 4 and str(compChoice) not in archived:
                        s4 = "X"
                        archived.append("4")
                    elif compChoice == 5 and str(compChoice) not in archived:
                        s5 = "X"
                        archived.append("5")
                    elif compChoice == 6 and str(compChoice) not in archived:
                        s6 = "X"
                        archived.append("6")
                    elif compChoice == 7 and str(compChoice) not in archived:
                        s7 = "X"
                        archived.append("7")
                    elif compChoice == 8 and str(compChoice) not in archived:
                        s8 = "X"
                        archived.append("8")
                    elif compChoice == 9 and str(compChoice) not in archived:
                        s9 = "X"
                        archived.append("9")
                    print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                    s1, s2, s3, s4, s5, s6, s7, s8, s9))
                    if ((s1 == "X" and s2 == "X" and s3 == "X") or (s4 == "X" and s5 == "X" and s6 == "X") or
                            (s7 == "X" and s8 == "X" and s9 == "X") or (s1 == "X" and s4 == "X" and s7 == "X") or
                            (s2 == "X" and s5 == "X" and s8 == "X") or (s3 == "X" and s6 == "X" and s9 == "X") or
                            (s1 == "X" and s5 == "X" and s9 == "X") or (s3 == "X" and s5 == "X" and s7 == "X")):
                        isDone = 1
                        print("You lose.")
                    elif ((s1 == "O" and s2 == "O" and s3 == "O") or (s4 == "O" and s5 == "O" and s6 == "O") or
                          (s7 == "O" and s8 == "O" and s9 == "O") or (s1 == "O" and s4 == "O" and s7 == "O") or
                          (s2 == "O" and s5 == "O" and s8 == "O") or (s3 == "O" and s6 == "O" and s9 == "O") or
                          (s1 == "O" and s5 == "O" and s9 == "O") or (s3 == "O" and s5 == "O" and s7 == "O")):
                        isDone = 1
                        print("You win.")
                    else:
                        print("It's a tie.")
    else:
        print("You will go first")
        print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
        s1, s2, s3, s4, s5, s6, s7, s8, s9))
        # 1
        userChoice = input("Which section would you like to fill in? ")
        if userChoice == "1":
            s1 = "X"
            archived.append("1")
        elif userChoice == "2":
            s2 = "X"
            archived.append("2")
        elif userChoice == "3":
            s3 = "X"
            archived.append("3")
        elif userChoice == "4":
            s4 = "X"
            archived.append("4")
        elif userChoice == "5":
            s5 = "X"
            archived.append("5")
        elif userChoice == "6":
            s6 = "X"
            archived.append("6")
        elif userChoice == "7":
            s7 = "X"
            archived.append("7")
        elif userChoice == "8":
            s8 = "X"
            archived.append("8")
        elif userChoice == "9":
            s9 = "X"
            archived.append("9")
        # 2
        compChoice = random.randint(1, 9)
        while str(compChoice) in archived:
            compChoice = random.randint(1, 9)
        if compChoice == 1 and str(compChoice) not in archived:
            s1 = "O"
            archived.append("1")
        elif compChoice == 2 and str(compChoice) not in archived:
            s2 = "O"
            archived.append("2")
        elif compChoice == 3 and str(compChoice) not in archived:
            s3 = "O"
            archived.append("3")
        elif compChoice == 4 and str(compChoice) not in archived:
            s4 = "O"
            archived.append("4")
        elif compChoice == 5 and str(compChoice) not in archived:
            s5 = "O"
            archived.append("5")
        elif compChoice == 6 and str(compChoice) not in archived:
            s6 = "O"
            archived.append("6")
        elif compChoice == 7 and str(compChoice) not in archived:
            s7 = "O"
            archived.append("7")
        elif compChoice == 8 and str(compChoice) not in archived:
            s8 = "O"
            archived.append("8")
        else:
            s9 = "O"
            archived.append("9")
        print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
        s1, s2, s3, s4, s5, s6, s7, s8, s9))
        # 3
        userChoice = input("Which section would you like to fill in? ")
        while userChoice in archived or (userChoice != "1" and userChoice != "2" and userChoice != "3" and
                                         userChoice != "4" and userChoice != "5" and userChoice != "6" and
                                         userChoice != "7" and userChoice != "8" and userChoice != "9"):
            userChoice = input("Invalid answer. Please try again. ")
        if userChoice == "1" and userChoice not in archived:
            s1 = "X"
            archived.append("1")
        elif userChoice == "2" and userChoice not in archived:
            s2 = "X"
            archived.append("2")
        elif userChoice == "3" and userChoice not in archived:
            s3 = "X"
            archived.append("3")
        elif userChoice == "4" and userChoice not in archived:
            s4 = "X"
            archived.append("4")
        elif userChoice == "5" and userChoice not in archived:
            s5 = "X"
            archived.append("5")
        elif userChoice == "6" and userChoice not in archived:
            s6 = "X"
            archived.append("6")
        elif userChoice == "7" and userChoice not in archived:
            s7 = "X"
            archived.append("7")
        elif userChoice == "8" and userChoice not in archived:
            s8 = "X"
            archived.append("8")
        elif userChoice == "9" and userChoice not in archived:
            s9 = "X"
            archived.append("9")
        # 4
        compChoice = random.randint(1, 9)
        while str(compChoice) in archived:
            compChoice = random.randint(1, 9)
        if compChoice == 1 and str(compChoice) not in archived:
            s1 = "O"
            archived.append("1")
        elif compChoice == 2 and str(compChoice) not in archived:
            s2 = "O"
            archived.append("2")
        elif compChoice == 3 and str(compChoice) not in archived:
            s3 = "O"
            archived.append("3")
        elif compChoice == 4 and str(compChoice) not in archived:
            s4 = "O"
            archived.append("4")
        elif compChoice == 5 and str(compChoice) not in archived:
            s5 = "O"
            archived.append("5")
        elif compChoice == 6 and str(compChoice) not in archived:
            s6 = "O"
            archived.append("6")
        elif compChoice == 7 and str(compChoice) not in archived:
            s7 = "O"
            archived.append("7")
        elif compChoice == 8 and str(compChoice) not in archived:
            s8 = "O"
            archived.append("8")
        elif compChoice == 9 and str(compChoice) not in archived:
            s9 = "O"
            archived.append("9")
        print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
        s1, s2, s3, s4, s5, s6, s7, s8, s9))
        # 5
        userChoice = input("Which section would you like to fill in? ")

        while userChoice in archived or (userChoice != "1" and userChoice != "2" and userChoice != "3" and
                                         userChoice != "4" and userChoice != "5" and userChoice != "6" and
                                         userChoice != "7" and userChoice != "8" and userChoice != "9"):
            userChoice = input("Invalid answer. Please try again. ")
        if userChoice == "1" and userChoice not in archived:
            s1 = "X"
            archived.append("1")
        elif userChoice == "2" and userChoice not in archived:
            s2 = "X"
            archived.append("2")
        elif userChoice == "3" and userChoice not in archived:
            s3 = "X"
            archived.append("3")
        elif userChoice == "4" and userChoice not in archived:
            s4 = "X"
            archived.append("4")
        elif userChoice == "5" and userChoice not in archived:
            s5 = "X"
            archived.append("5")
        elif userChoice == "6" and userChoice not in archived:
            s6 = "X"
            archived.append("6")
        elif userChoice == "7" and userChoice not in archived:
            s7 = "X"
            archived.append("7")
        elif userChoice == "8" and userChoice not in archived:
            s8 = "X"
            archived.append("8")
        elif userChoice == "9" and userChoice not in archived:
            s9 = "X"
            archived.append("9")
        if ((s1 == "X" and s2 == "X" and s3 == "X") or (s4 == "X" and s5 == "X" and s6 == "X") or (
                s7 == "X" and s8 == "X" and s9 == "X") or
                (s1 == "X" and s4 == "X" and s7 == "X") or (s2 == "X" and s5 == "X" and s8 == "X") or (
                        s3 == "X" and s6 == "X" and s9 == "X") or
                (s1 == "X" and s5 == "X" and s9 == "X") or (s3 == "X" and s5 == "X" and s7 == "X")):
            print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
            s1, s2, s3, s4, s5, s6, s7, s8, s9))
            isDone = 1
            print("You win.")
        if isDone == 0:
            # 6
            compChoice = random.randint(1, 9)
            while str(compChoice) in archived:
                compChoice = random.randint(1, 9)
            if compChoice == 1 and str(compChoice) not in archived:
                s1 = "O"
                archived.append("1")
            elif compChoice == 2 and str(compChoice) not in archived:
                s2 = "O"
                archived.append("2")
            elif compChoice == 3 and str(compChoice) not in archived:
                s3 = "O"
                archived.append("3")
            elif compChoice == 4 and str(compChoice) not in archived:
                s4 = "O"
                archived.append("4")
            elif compChoice == 5 and str(compChoice) not in archived:
                s5 = "O"
                archived.append("5")
            elif compChoice == 6 and str(compChoice) not in archived:
                s6 = "O"
                archived.append("6")
            elif compChoice == 7 and str(compChoice) not in archived:
                s7 = "O"
                archived.append("7")
            elif compChoice == 8 and str(compChoice) not in archived:
                s8 = "O"
                archived.append("8")
            elif compChoice == 9 and str(compChoice) not in archived:
                s9 = "O"
                archived.append("9")
            print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
            s1, s2, s3, s4, s5, s6, s7, s8, s9))
            if ((s1 == "X" and s2 == "X" and s3 == "X") or (s4 == "X" and s5 == "X" and s6 == "X") or
                    (s7 == "X" and s8 == "X" and s9 == "X") or (s1 == "X" and s4 == "X" and s7 == "X") or
                    (s2 == "X" and s5 == "X" and s8 == "X") or (s3 == "X" and s6 == "X" and s9 == "X") or
                    (s1 == "X" and s5 == "X" and s9 == "X") or (s3 == "X" and s5 == "X" and s7 == "X")):
                isDone = 1
                print("You win.")
            elif ((s1 == "O" and s2 == "O" and s3 == "O") or (s4 == "O" and s5 == "O" and s6 == "O") or
                  (s7 == "O" and s8 == "O" and s9 == "O") or (s1 == "O" and s4 == "O" and s7 == "O") or
                  (s2 == "O" and s5 == "O" and s8 == "O") or (s3 == "O" and s6 == "O" and s9 == "O") or
                  (s1 == "O" and s5 == "O" and s9 == "O") or (s3 == "O" and s5 == "O" and s7 == "O")):
                isDone = 1
                print("You lose.")
            if isDone == 0:
                # 7
                userChoice = input("Which section would you like to fill in? ")
                while userChoice in archived or (userChoice != "1" and userChoice != "2" and userChoice != "3" and
                                                 userChoice != "4" and userChoice != "5" and userChoice != "6" and
                                                 userChoice != "7" and userChoice != "8" and userChoice != "9"):
                    userChoice = input("Invalid answer. Please try again. ")
                if userChoice == "1" and userChoice not in archived:
                    s1 = "X"
                    archived.append("1")
                elif userChoice == "2" and userChoice not in archived:
                    s2 = "X"
                    archived.append("2")
                elif userChoice == "3" and userChoice not in archived:
                    s3 = "X"
                    archived.append("3")
                elif userChoice == "4" and userChoice not in archived:
                    s4 = "X"
                    archived.append("4")
                elif userChoice == "5" and userChoice not in archived:
                    s5 = "X"
                    archived.append("5")
                elif userChoice == "6" and userChoice not in archived:
                    s6 = "X"
                    archived.append("6")
                elif userChoice == "7" and userChoice not in archived:
                    s7 = "X"
                    archived.append("7")
                elif userChoice == "8" and userChoice not in archived:
                    s8 = "X"
                    archived.append("8")
                elif userChoice == "9" and userChoice not in archived:
                    s9 = "X"
                    archived.append("9")
                if ((s1 == "X" and s2 == "X" and s3 == "X") or (s4 == "X" and s5 == "X" and s6 == "X") or
                        (s7 == "X" and s8 == "X" and s9 == "X") or (s1 == "X" and s4 == "X" and s7 == "X") or
                        (s2 == "X" and s5 == "X" and s8 == "X") or (s3 == "X" and s6 == "X" and s9 == "X") or
                        (s1 == "X" and s5 == "X" and s9 == "X") or (s3 == "X" and s5 == "X" and s7 == "X")):
                    print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                    s1, s2, s3, s4, s5, s6, s7, s8, s9))
                    isDone = 1
                    print("You win.")
                elif ((s1 == "O" and s2 == "O" and s3 == "O") or (s4 == "O" and s5 == "O" and s6 == "O") or
                      (s7 == "O" and s8 == "O" and s9 == "O") or (s1 == "O" and s4 == "O" and s7 == "O") or
                      (s2 == "O" and s5 == "O" and s8 == "O") or (s3 == "O" and s6 == "O" and s9 == "O") or
                      (s1 == "O" and s5 == "O" and s9 == "O") or (s3 == "O" and s5 == "O" and s7 == "O")):
                    print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                    s1, s2, s3, s4, s5, s6, s7, s8, s9))
                    isDone = 1
                    print("You lose.")
                if isDone == 0:
                    # 8
                    compChoice = random.randint(1, 9)
                    while str(compChoice) in archived:
                        compChoice = random.randint(1, 9)
                if compChoice == 1 and str(compChoice) not in archived:
                    s1 = "O"
                    archived.append("1")
                elif compChoice == 2 and str(compChoice) not in archived:
                    s2 = "O"
                    archived.append("2")
                elif compChoice == 3 and str(compChoice) not in archived:
                    s3 = "O"
                    archived.append("3")
                elif compChoice == 4 and str(compChoice) not in archived:
                    s4 = "O"
                    archived.append("4")
                elif compChoice == 5 and str(compChoice) not in archived:
                    s5 = "O"
                    archived.append("5")
                elif compChoice == 6 and str(compChoice) not in archived:
                    s6 = "O"
                    archived.append("6")
                elif compChoice == 7 and str(compChoice) not in archived:
                    s7 = "O"
                    archived.append("7")
                elif compChoice == 8 and str(compChoice) not in archived:
                    s8 = "O"
                    archived.append("8")
                elif compChoice == 9 and str(compChoice) not in archived:
                    s9 = "O"
                    archived.append("9")
                print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                s1, s2, s3, s4, s5, s6, s7, s8, s9))
                if ((s1 == "X" and s2 == "X" and s3 == "X") or (s4 == "X" and s5 == "X" and s6 == "X") or
                        (s7 == "X" and s8 == "X" and s9 == "X") or (s1 == "X" and s4 == "X" and s7 == "X") or
                        (s2 == "X" and s5 == "X" and s8 == "X") or (s3 == "X" and s6 == "X" and s9 == "X") or
                        (s1 == "X" and s5 == "X" and s9 == "X") or (s3 == "X" and s5 == "X" and s7 == "X")):
                    isDone = 1
                    print("You win.")
                elif ((s1 == "O" and s2 == "O" and s3 == "O") or (s4 == "O" and s5 == "O" and s6 == "O") or
                      (s7 == "O" and s8 == "O" and s9 == "O") or (s1 == "O" and s4 == "O" and s7 == "O") or
                      (s2 == "O" and s5 == "O" and s8 == "O") or (s3 == "O" and s6 == "O" and s9 == "O") or
                      (s1 == "O" and s5 == "O" and s9 == "O") or (s3 == "O" and s5 == "O" and s7 == "O")):
                    isDone = 1
                    print("You lose.")
                if isDone == 0:
                    # 9
                    userChoice = input("Which section would you like to fill in? ")
                    while userChoice in archived or (userChoice != "1" and userChoice != "2" and userChoice != "3" and
                                                     userChoice != "4" and userChoice != "5" and userChoice != "6" and
                                                     userChoice != "7" and userChoice != "8" and userChoice != "9"):
                        userChoice = input("Invalid answer. Please try again. ")
                    if userChoice == "1" and userChoice not in archived:
                        s1 = "X"
                        archived.append("1")
                    elif userChoice == "2" and userChoice not in archived:
                        s2 = "X"
                        archived.append("2")
                    elif userChoice == "3" and userChoice not in archived:
                        s3 = "X"
                        archived.append("3")
                    elif userChoice == "4" and userChoice not in archived:
                        s4 = "X"
                        archived.append("4")
                    elif userChoice == "5" and userChoice not in archived:
                        s5 = "X"
                        archived.append("5")
                    elif userChoice == "6" and userChoice not in archived:
                        s6 = "X"
                        archived.append("6")
                    elif userChoice == "7" and userChoice not in archived:
                        s7 = "X"
                        archived.append("7")
                    elif userChoice == "8" and userChoice not in archived:
                        s8 = "X"
                        archived.append("8")
                    elif userChoice == "9" and userChoice not in archived:
                        s9 = "X"
                        archived.append("9")
                    if ((s1 == "X" and s2 == "X" and s3 == "X") or (s4 == "X" and s5 == "X" and s6 == "X") or
                            (s7 == "X" and s8 == "X" and s9 == "X") or (s1 == "X" and s4 == "X" and s7 == "X") or
                            (s2 == "X" and s5 == "X" and s8 == "X") or (s3 == "X" and s6 == "X" and s9 == "X") or
                            (s1 == "X" and s5 == "X" and s9 == "X") or (s3 == "X" and s5 == "X" and s7 == "X")):
                        print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                        s1, s2, s3, s4, s5, s6, s7, s8, s9))
                        isDone = 1
                        print("You win.")
                    elif ((s1 == "O" and s2 == "O" and s3 == "O") or (s4 == "O" and s5 == "O" and s6 == "O") or
                          (s7 == "O" and s8 == "O" and s9 == "O") or (s1 == "O" and s4 == "O" and s7 == "O") or
                          (s2 == "O" and s5 == "O" and s8 == "O") or (s3 == "O" and s6 == "O" and s9 == "O") or
                          (s1 == "O" and s5 == "O" and s9 == "O") or (s3 == "O" and s5 == "O" and s7 == "O")):
                        print(" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s " % (
                        s1, s2, s3, s4, s5, s6, s7, s8, s9))
                        isDone = 1
                        print("You lose.")
                    else:
                        print("It's a tie.")
    tttAgain = input("\nWould you like to play again? ")
    while tttAgain.lower() != "yes" and tttAgain.lower() != "no":
        tttAgain = input("Invalid answer. Please try again. ")
    while tttAgain.lower() == "yes":
        tTT()
    if tttAgain.lower() == "no":
        miniGames()

miniGames()