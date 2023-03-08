#A tic-tac-toe game
import turtle
import random
def main():
    try:
        #sets the turtle up and declares some of the variables
        pencil = turtle.Turtle()
        pencil.hideturtle()
        gridNumbers = list()
        gridNumbers += 1,2,3,4,5,6,7,8,9
        gridChords = list()
        drawGrid(pencil)
        putGridNumbers(pencil , gridNumbers , gridChords)
        playGame(pencil , gridChords)
        turtle.done()
    except:
        print("ummm, things happened")
        turtle.done()

def drawGrid(pencil):
    #draws the game board
    pencil.penup()
    pencil.goto(-50 , 100)
    pencil.pendown()
    pencil.goto(-50 , -50)
    pencil.penup()
    pencil.goto(50 , 100)
    pencil.pendown()
    pencil.goto(50 , -50)
    pencil.penup()
    pencil.goto(-100 , 50)
    pencil.pendown()
    pencil.goto(100 , 50)
    pencil.penup()
    pencil.goto(-100 , 0)
    pencil.pendown()
    pencil.goto(100 , 0)
    
def putGridNumbers(pencil , gridNumbers , gridChords):
    #Lables each square to more easaly play the game
    pencil.penup()
    x = 0
    xc = -100
    yc = 100
    ca = pencil.position()
    z = 0
    for i in range(9):
        pencil.goto(xc , yc)
        pencil.write(gridNumbers[x])
        xc += 100
        x +=1
        ca = pencil.position() - (0,15.5)
        gridChords.insert(z,ca)
        z+=1
        if xc == 200:
            xc = -100
            yc -= 65
    return gridChords
    
def playGame(pencil , gridChords):
    #plays the full game with a simple ai
    choicesAvalibale = list()
    choicesAvalibale += 1,2,3,4,5,6,7,8,9
    playerChoice = 0
    computerChoice = 0
    gridOptions = list()
    gridOptions += (0 , 0 , 0 ,0 , 0 , 0 ,0 , 0 , 0)
    roundsPlayed = 0
    while roundsPlayed <= 9:
        playerRound(playerChoice , gridOptions , gridChords , pencil , choicesAvalibale)
        roundsPlayed = checkForWin(roundsPlayed , gridOptions , pencil)
        if roundsPlayed != 100:
            computerRound(choicesAvalibale , computerChoice , gridChords , pencil , gridOptions)
            roundsPlayed = checkForWin(roundsPlayed , gridOptions , pencil)

def playerRound(playerChoice , gridOptions , gridChords , pencil , choicesAvalibale):
    #Gets player move abd then plots the move
    playerChoice = int(turtle.numinput("choice" , "Chose a square 1-9 " , '' , 1 , 9))
    gridOptions[(playerChoice-1)] = -1
    itemToDelete = choicesAvalibale.index(playerChoice)
    del choicesAvalibale[itemToDelete]
    putChoicePlayer(playerChoice , pencil , gridChords)
    return gridOptions , choicesAvalibale

def computerRound(choicesAvalibale , computerChoice , gridChords , pencil , gridOptions):
    #A simple AI using a random number generated
    x = True
    while x == True:
        if computerChoice not in choicesAvalibale:
            computerChoice = random.randint(1, 9)
        else:
            x = False
    itemToDelete = choicesAvalibale.index(computerChoice)
    del choicesAvalibale[itemToDelete]
    gridOptions[(computerChoice-1)] = 1
    putComputerChoice(computerChoice , gridChords , pencil)
    return gridOptions , choicesAvalibale
    
def putChoicePlayer(playerChoice , pencil , gridChords):
    #Plots the player choice onto the board
    pencil.shape("turtle")
    pencil.color("blue")
    pencil.penup()
    pencil.goto(gridChords[playerChoice - 1])
    pencil.stamp()
    
def putComputerChoice(computerChoice , gridChords , pencil):
    #Plots the computer move onto the board
    pencil.shape("circle")
    pencil.color("red")
    pencil.penup()
    pencil.goto(gridChords[computerChoice - 1])
    pencil.stamp()    
    
def checkForWin(roundsPlayed , gridOptions , pencil):
        #Checks to see if the player won the game
        squareOne = 0
        offsetOne = 1
        offsetTwo = 2
        itemsChecked = 0
        for i in range(8):
            #adds the square values to see if they are in a wining senario, if not, checks other options
            rowTotal = gridOptions[squareOne] + gridOptions[(squareOne + offsetOne)] + gridOptions[(squareOne + offsetTwo)]
            if rowTotal == -3:
                roundsPlayed = 100
                pencil.color("black")
                pencil.goto(-20 , 125)
                pencil.write("You Win!!!")
                return roundsPlayed
            elif rowTotal == 3:
                roundsPlayed = 100
                pencil.color("black")
                pencil.goto(-20 , 125)
                pencil.write("You Lost:(")
                return roundsPlayed
            elif roundsPlayed == 8:
                roundsPlayed = 100
                pencil.color("black")
                pencil.goto(-20 , 125)
                pencil.write("It's  A Tie!")
                return roundsPlayed                
            else:
                if squareOne == 6:
                    squareOne = 0
                    offsetOne = 3
                    offsetTwo = 6
                    itemsChecked = 1
                elif squareOne == 2:
                    squareOne = 0
                    offsetOne = 4
                    offsetTwo = 8
                    itemsChecked = 2
                elif itemsChecked == 2:
                    squareOne = 2
                    offsetOne = 2
                    offsetTwo = 4
                else:
                    if (itemsChecked == 0):
                        squareOne += 3
                    elif (itemsChecked == 1):
                        squareOne += 1
        roundsPlayed += 1
        return roundsPlayed       
    
main()