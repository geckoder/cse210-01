"""
Author: Michelle Caceres
W02 Prove: Developer - Solo Code Submission
"""

class PlayTicTacToe:
    def __init__(self, playerNumber, charType):
        self.player = playerNumber
        self.charType = charType
    def createPlayingBoard(self):
        playingBoard = ["1 | 2 | 3", "----------", "4 | 5 | 6", "----------", "7 | 8 | 9"]
        return playingBoard
    def displayPB(self, playingBoard):
        for row in playingBoard:
            print(row)
    def your_turn(self, playingBoard, move, charType):
        selectedIndex = move
        row1 = playingBoard[0].split(" | ")
        row2 = playingBoard[2].split(" | ")
        row3 = playingBoard[4].split(" | ")
        if selectedIndex == "1" or selectedIndex == "2" or selectedIndex == "3":
            row1.pop((int(selectedIndex)- 1))
            row1.insert((int(selectedIndex)- 1), charType)
        if selectedIndex == "4" or selectedIndex == "5" or selectedIndex == "6":
            row2.pop((int(selectedIndex)- 4))
            row2.insert((int(selectedIndex)- 4), charType)
        if selectedIndex == "7" or selectedIndex == "8" or selectedIndex == "9":
            row3.pop((int(selectedIndex)- 7))
            row3.insert((int(selectedIndex)- 7), charType)
        for value in row1[0:2]:
            row1.extend( value + " | ")
        row1.pop(0)
        row1.pop(0)
        row1.insert(9, row1[0])
        row1.pop(0)

        for value in row2[0:2]:
            row2.extend( value + " | ")
        row2.pop(0)
        row2.pop(0)
        row2.insert(9, row2[0])
        row2.pop(0)

        for value in row3[0:2]:
            row3.extend( value + " | ")
        row3.pop(0)
        row3.pop(0)
        row3.insert(9, row3[0])
        row3.pop(0)

        row1 = "".join(row1)
        row2 = "".join(row2)
        row3 = "".join(row3)
        newBoard = []
        newBoard.append(row1)
        newBoard.append(row2)
        newBoard.append(row3)
        newBoard.insert(1, "----------")
        newBoard.insert(3, "----------")
        for index in newBoard:
            print(index)
        

                
        
def main():
    print("Welcome to the Tic Tac Toe Game! It's tic-tac-totally awesome!")
    p1 = PlayTicTacToe(1, "x")
    p2 = PlayTicTacToe(2, "o")

    playingBoard = p1.createPlayingBoard()
    p1.displayPB(playingBoard)
    
    moveP1 = input("Hello player one! Please enter a number from 1-9: ")
    p1.your_turn(playingBoard, moveP1, "x")
    #moveP2 = input("Hello player two! Please enter a number from 1-9: ")
    #p2.your_turn(playingBoard, moveP2)

    

if __name__ == "__main__":
    main()