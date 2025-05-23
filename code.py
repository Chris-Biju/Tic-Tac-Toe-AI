# main.py

import random
import time 
grid = []

for i in range(3):
  row = []
  for j in range(3):
    row.append(" ")
  grid.append(row)

def printBoard(grid):
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if j < 2:
        print(" " + grid[i][j] + " |", end = "")
      else:
        print(" " + grid[i][j] + " ", end = "")
    if i < 2:  
      print("\n–––+–––+–––")
  print("\n")    
#printBoard(grid)


def randomPlayerMove(grid):
  while True:
    randomRow = random.randint(0, 2)
    randomColumn = random.randint(0, 2)
    if (-1 < randomRow and randomRow < 3) and (-1 < randomColumn and randomColumn < 3) and grid[randomRow][randomColumn] == " ":
          break
  return [randomRow, randomColumn]

  
def testWin(board, i, j, player):
  testBoard = []
  
  for a in range(len(board)):
    row = []
    for b in range(len(board)):
      row.append(board[a][b])
    testBoard.append(row)
    
  if testBoard[i][j] != " ":
    return False
  else:
    testBoard[i][j] = player
    return win(testBoard, player)



def testFork(board, i, j, player):
  testBoard = []
  for a in range(len(board)):
    row = []
    for b in range(len(board)):
      row.append(board[a][b])
    testBoard.append(row)
    
    
  testBoard[i][j] = player
  winCount = 0
  
  for p in range(len(board)):
    for l in range(len(board)):
      if testBoard[p][l] == " ":
        testBoard[p][l] = player
        
        if win(testBoard, player):
          winCount += 1
          testBoard[p][l] = " "
        else:
          testBoard[p][l] = " "
  if winCount >= 2:
    return True
  else:
    return False
  '''
  1. create duplicate
  2. play move on duplicate
  3. test for forks by looping through remainining spots and testing for wins
  4. count wins. If wins is > or equal to 2 you have a fork!
  '''
  
def AIplayerMove(board):
  '''
  1. check if Ai has winning moves
  2. block opponents winning moves
  3. If possible play in center
  4. If possible play in corners
  5 if possible play in edges
  6. Plays random move if it cant find anything
  '''
  
  # 1. check if Ai has winning moves
  
  for i in range(3):
    for j in range(3):
      if testWin(board, i, j, "O"):
        return [i,j]
  
  # 2. block opponents winning moves
  
  for i in range(3):
    for j in range(3):
      if testWin(board, i, j, "X"):
        return [i,j]
  
  #Check for forks
  
  for i in range(3):
    for j in range(3):
      if testFork(board, i, j, "O"):
        return [i,j]
  
  #Check for opponents forks

  for i in range(3):
    for j in range(3):
      if testFork(board, i, j, "X"):
        return [i,j]  
  
  # 3. If possible play in center
  if board[1][1] == " ":
    return [1, 1]
  
  corners = [[0, 0], [2, 0], [2, 2], [0, 2]]
  
  # 4. If possible play in corners
  
  for i in range(4):
    if board[corners[i][0]][corners[i][1]] == " ":
      return corners[i]
      
  #5 If nothing else, play random moves
  
  return randomPlayerMove(board)
# check for wins 
def win(board, player):
  #Horizontal win detection
  if board[0][0] == player and board[0][1] == player and board[0][2] == player:
    return True
  if board[1][0] == player and board[1][1] == player and board[1][2] == player:
    return True
  if board[2][0] == player and board[2][1] == player and board[2][2] == player:
    return True
    
    #Vertical win detection
    
  if board[0][0] == player and board[1][0] == player and board[2][0] == player:
   return True
  if board[0][1] == player and board[1][1] == player and board[2][1] == player:
    return True
  if board[0][2] == player and board[1][2] == player and board[2][2] == player:
    return True
    
    #Diagonal win detection
    
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[2][0] == player and board[1][1] == player and board[0][2] == player:
    return True
  return False  

def finish(grid):
  for row in grid:
    for cell in row:
      if cell == " ":
        return False
  return True

isTie = False

Player = "X"

coinFlip = random.randint(1,2)

if coinFlip == 1:
  Player = "O"
  
  print("The coin flip shows that the computer (O) will go first.")
else:
  print("The coin flip shows that you (X) will go first")

begin = input("Press enter to start the game!")





while True:
  '''
  Steps
  1. print board 
  2. Player turn (if statements to check)
  3. Check if someone wins
  4. Check if all spots are taken (tie)
  5. Change turns
  '''


  printBoard(grid)
  if Player == "X":
    while True:
      row = int(input("What is the row of the cell you'd like to add? "))
      column = int(input("What is the column of the cell you'd like to add? "))
      if (-1 < row and row < 3) and (-1 < column and column < 3) and grid[row][column] == " ":
        grid[row][column] = "X"
        break
      print("Sorry. That input was invalid, please try again.")
      
    
  elif Player == "O":
    computerMove = AIplayerMove(grid)
    time.sleep(1)
    grid[computerMove[0]][computerMove[1]] = "O"
    
  
  if win(grid, Player):
    break
  
  if finish(grid):
    isTie = True
    break
  
  if Player == "O":
    Player = "X"
  else:
    Player = "O"

printBoard(grid)

if isTie:
  print("Tie!")
else:
  print(Player + " has won the game!")
