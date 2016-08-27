# A Python script to play Tic-Tac-Toe with computer.

import os,time,sys,random

# 'printPattern' function determines how the tic-tac board will be displayed.
def printPattern(tempdict):
    print(' '*20+tempdict[0]+' '+'|'+tempdict[1]+' '+'|'+tempdict[2]+' ')
    print(' '*20+'--|--|--')
    print(' '*20+tempdict[3]+' '+'|'+tempdict[4]+' '+'|'+tempdict[5]+' ')
    print(' '*20+'--|--|--')
    print(' '*20+tempdict[6]+' '+'|'+tempdict[7]+' '+'|'+tempdict[8]+' ')
    print('\n\n')


# 'winCondition' function checks if there are 3 consequtive 'O' or 'X' in a row, column or diagonally.
# If either of the following conditions are ssatisfied , the it returns 1 , indication a possible win situation .
def winCondition(tempdict):
    if tempdict[0]==tempdict[1]==tempdict[2]=='O' or tempdict[0]==tempdict[1]==tempdict[2]=='X':
        return(1)
    elif tempdict[3]==tempdict[4]==tempdict[5]=='O' or tempdict[3]==tempdict[4]==tempdict[5]=='X':
        return(1)
    elif tempdict[6]==tempdict[7]==tempdict[8]=='O' or tempdict[6]==tempdict[7]==tempdict[8]=='X':
        return(1)
    elif tempdict[0]==tempdict[4]==tempdict[8]=='O' or tempdict[0]==tempdict[4]==tempdict[8]=='X':
        return(1)
    elif tempdict[2]==tempdict[4]==tempdict[6]=='O' or tempdict[2]==tempdict[4]==tempdict[6]=='X':
        return(1)
    elif tempdict[0]==tempdict[3]==tempdict[6]=='O' or tempdict[0]==tempdict[3]==tempdict[6]=='X':
        return(1)
    elif tempdict[1]==tempdict[4]==tempdict[7]=='O' or tempdict[1]==tempdict[4]==tempdict[7]=='X':
        return(1)
    elif tempdict[2]==tempdict[5]==tempdict[8]=='O' or tempdict[2]==tempdict[5]==tempdict[8]=='X' :
        return(1)
    else:
        return(0)
# 'instructionList' is a function to print the instruction headers and the game progress , after each iteration.
def instructionList():
    initialList=['0','1','2','3','4','5','6','7','8']
    print('WELCOME TO TIC TAC TOE !!\n\n'.center(55))
    print('Instructions:- Player 1 is denoted by O and Player 2 by X.')
    print('               Enter the spot numbers as indicated in the ')
    print('               below sample to indicate your choice .     ')
    print('               BEST OF LUCK !!\n')
    printPattern(initialList)

# 'playerTurnUpdate' function is used to input 'X' or 'O' in a certain spot determined by the user.
# If the spot is already occupied or it doesn't exist , then a message is displayed and prompts the user to re-enter a new spot.
# In, case of the computer's turn , the script automatically chooses and blank spot.
# It, checks if the 'winCondition' is satisfied . If satisfied , then it return 1.
def playerTurnUpdate(t,symbol,spotDic):
    win=0
    while True:
        randomList=[]
        if t==0:
            print('Player  choose your spot:')
            userChoice=int(input())
        else:
            for z in spotDic.keys():
                if spotDic[z]==' ':
                    randomList.append(z)
            k=random.choice(randomList)
            userChoice=int(k)
        if (userChoice>=0 and userChoice<=8):
            if spotDic[userChoice]==' ':
                spotDic[userChoice]=symbol
                win=winCondition(spotDic)
                if win==1:
                    return(1)
                break
            else:
                print('The spot is already occupied')
                continue
        else:
            print('The spot does not exist.')
            continue

# It displays the current game progress.
def display():
    os.system('cls')
    instructionList()
    print('Match Progress :-')
    printPattern(spotDict)

# 'spotDict' dictionary is used to store the contents of each spots.
# 'isWon'=1 indicates a win situation .
# 'turn' variable randomnly determines who goes first .
# If 'turn'=0 , then player goes first . If turn=1 ,  the computer goes first.
# The first player takes 'O' input and the second one takes 'X'.
spotDict={0:' ',1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' '}
isWon=0
finish=0
turn=random.randint(0,1)
if turn==0:
    display()
    print('\nPlayer get ready to start. . .')
    time.sleep(4)
else:
    display()
    print('\nComputer starts. . .')
    time.sleep(4)
indicator=0

while finish<=8:
    display()
    if turn==0:
        choice='O'
        isWon=playerTurnUpdate(turn,choice,spotDict)
        if isWon==1:
            display()
            print('PLAYER HAS WON\n\n'.center(50))
            sys.exit()
            
    else:
        choice='X'
        print('Computer choosing a spot. . . .')
        time.sleep(3)
        isWon=playerTurnUpdate(turn,choice,spotDict)
        if isWon==1:
            display()
            print('COMPUTER HAS WON!!\n\n'.center(50))
            sys.exit()
            
    # The following 'if-else' code is used to change the turn .
    if turn==0:
        turn=1
        choice='X'
        
    else:
        turn=0
        choice='O'
        
    finish+=1
    
# If no player wins , then a ' MATCH IS A TIE !' message is displayed.
display()
print('MATCH IS A TIE !\n\n'.center(50))

