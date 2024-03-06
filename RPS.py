# AUTHOR - GIOVANNI OHASHIEGBULA

import random

moves = [["r", "R","Rock"], ["s", "S", "Scissors"], ["p", "P", "Paper"], ["e", "E"]]     # array with options

win = [1, 12, 20]       # Symbolise winning positions

Score = [0, 0]          # Score tracking between computer and player

def finish(z):          # Ending function with message
    if z == 0:
        ai = f"That was fun. If you ever feel like losing again, I'm here for you {name}. Bye"
        print(ai)
    else:
        ai = f"How about a win without cheating next time {name}."
        print(ai)

def inmoves(y):         # Function to check if input is in moves array. The return values are used to create error in try and except below
    global uii          # uii - User input index - getting the index for user input if in moves array
    for i in moves:
        if y in i:
            uii = moves.index(i)
            return 1
        else:
            continue
    return 0

def inputcheck(x):      # Function to check validity of user input
    try:
        int(x)
        print("Wrong input type: No numbers Allowed")
        print()
        return True
    except:
        try:
            float(x)
            print("Wrong input type: No floats Allowed")
            print()
            return True
        except:
            try:
                len(x) / (len(x) - 1)        # To check length of user input, error if length of input is greater than one
                print("Wrong input type: One letter only please")
                print()
                return True
            except:
                try:
                    num = inmoves(x)         # Checks if input is in moves array and causes error if not with return value from inmoves function
                    1 / num                  # Error creation from return value
                    False
                except:                      # Cases where user inputs correct length but not in options
                    print("Right input type but wrong input: Enter one of the options")
                    print()
                    return True
                
def compare(a, b, c):   # Compare your answer's index with the computer guess' index
    mat = (a*10) + b    # Easier way to compare, previous method gave me errors
    if a == b:
        return 0   # Tie
    elif mat in c:
        return 11  # Computer wins
    else:
        return 1   # User wins  
    
def game():             # Game function
    i = 1
    while True:         # While loop counting rounds played
        inp = True
        while inp:      # nested while loop for invalid input recovery
            out = f"Round {i}"
            print(out)
            move = input("What's your play: Enter (R/r) for Rock, (P/p) for Paper, (S/s) for Scissors or (E,e) to Exit? ")
            if move in moves[3]:     # Exit without finishing game, message included
                ex = f"Thanks for playing {name}. Bye"
                print(ex)
                exit()
            inp = inputcheck(move)
        guess = random.randint(0,2)    # Computers guess in index format
        result = compare(guess, uii, win)
        if result == 0:
            print("Its a tie. We both guessed",moves[guess][2],". Great minds do think alike.")
            print("Scores - Me:",Score[0], ", You:", Score[1])
            print()
        elif result == 11:
            Score[0]+=1
            print("Loser haha. I guessed",moves[guess][2])
            print("Scores: Me:",Score[0], ", You:", Score[1])
            print()
        else:
            Score[1]+=1
            print("CHEATER, keep your win. I guessed",moves[guess][2])
            print("Scores: Me:",Score[0], ", You:", Score[1])
            print()

        if Score[0] == 3:
            finish(0)
            break
        elif Score[1] == 3:
            finish(1)
            break
        i+=1
    
global name
name = input("Hi there, how can I address you? ")   
txt = f"Hey {name}, come play Rock-Paper-Scissors with me!! First to three"
print(txt)
game()
