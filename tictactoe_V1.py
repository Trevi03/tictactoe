def emptPos(x):
    return m[x]== " "
# Checking for an empty spot
# return request another number when spot taken

def returnBoolean(l):
    blist = []
    for i in l:
        blist += [i != " "]
    return blist
        
    

def endGame():
    #1st horizontal
    if (m[0]==m[1] and m[1]==m[2] and m[0]!= " "):
        return "win"
    #2nd horizontal
    elif (m[3]==m[4] and m[4]==m[5] and m[3]!= " "):
        return "win"
    #3rd horizontal
    elif (m[6]==m[7] and m[7]==m[8] and m[6]!= " "):
        return "win"
    #1st vertical
    elif (m[0]==m[3] and m[3]==m[6] and m[0]!= " "):
        return "win"
    #2nd vertical
    elif (m[1]==m[4] and m[4]==m[7] and m[1]!= " "):
        return "win"
    #3rd vertical
    elif (m[2]==m[5] and m[5]==m[8] and m[2]!= " "):
        return "win"
    #diagonal \
    elif (m[0]==m[4] and m[4]==m[8] and m[0]!= " "):
        return "win"
    #diagonal /
    elif (m[6]==m[4] and m[4]==m[2] and m[6]!= " "):
        return "win"
    elif all(returnBoolean(m))==True:
        return "draw"
    #continue on
    else:
        return "running"

def getPos():
    p = input("Now it's " + currentPlayer + "'s turn. Enter your desired position (1-9):")
    while (p not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or emptPos(int(p)-1) == False):
        p = input("Please make sure position is not taken and the number is within range.\nNow it's " + currentPlayer + "'s turn. Enter your desired position (1-9):")
    return p



print("The positions are as follows:\n1|2|3\n-----\n4|5|6\n-----\n7|8|9\n-------------------------------\n")
currentPlayer = "O"
Game = "running"
m = [" "," "," "," "," "," "," "," "," "]
count = -1

print(" | | \n-----\n | | \n-----\n | | ")
while Game == "running":
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"

    n = getPos()
    m[int(n)-1] = currentPlayer
    board = str( m[0] + "|" + m[1] + "|" + m[2] + "\n" + "-----" + "\n" + m[3] + "|" + m[4] + "|" + m[5] + "\n" + "-----" + "\n" +  m[6] + "|" + m[7] + "|" + m[8])
    
    print(board)

    
    Game = endGame()



if Game == "win":
    print("Player " + currentPlayer + " won!")
else:
    print("It's a draw!")


    






        
