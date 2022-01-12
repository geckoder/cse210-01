"""
Author: Michelle Caceres
W02 Prove: Developer - Solo Code Submission
"""
# Create a class for the game
class PlayTicTacToe:
    # Create initial method to set parameters
    def __init__(self, playerNumber, charType):
        self.player = playerNumber
        self.charType = charType
    # Create playing board array
    def createPlayingBoard(self):
        playingBoard = ["1 | 2 | 3", "----------", "4 | 5 | 6", "----------", "7 | 8 | 9"]
        return playingBoard
    # Display current playing board
    def displayPB(self, playingBoard):
        for row in playingBoard:
            print(row)
    # Mark board where player indicates and return updated board
    def your_turn(self, playingBoard, move, charType):
        # Set variable for player specified index
        selectedIndex = move
        # Split list by "|"
        row1 = playingBoard[0].split(" | ")
        row2 = playingBoard[2].split(" | ")
        row3 = playingBoard[4].split(" | ")
        # Begin conditional statements - if match, replace with "x" or "o"
        if selectedIndex == "1" or selectedIndex == "2" or selectedIndex == "3":
            row1.pop((int(selectedIndex)- 1))
            row1.insert((int(selectedIndex)- 1), charType)
        if selectedIndex == "4" or selectedIndex == "5" or selectedIndex == "6":
            row2.pop((int(selectedIndex)- 4))
            row2.insert((int(selectedIndex)- 4), charType)
        if selectedIndex == "7" or selectedIndex == "8" or selectedIndex == "9":
            row3.pop((int(selectedIndex)- 7))
            row3.insert((int(selectedIndex)- 7), charType)
        # Add "|" back and fix list structure
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
        # Join members of list for each row
        row1 = "".join(row1)
        row2 = "".join(row2)
        row3 = "".join(row3)
        # Create updated board with player choices
        newBoard = []
        newBoard.append(row1)
        newBoard.append(row2)
        newBoard.append(row3)
        newBoard.insert(1, "----------")
        newBoard.insert(3, "----------")
        # Display updated board
        for index in newBoard:
            print(index)
        # Return updated board to variable
        return newBoard
    # Determine winner of game
    def determineWinner(self, playingBoard):
        # Copy updated playing board without messing with in-play board
        winnerBoard = playingBoard.copy()
        # Remove "----------"
        winnerBoard.pop(1)
        winnerBoard.pop(2)
        # Split list by "|" and assign to row number
        row1 = winnerBoard[0].split(" | ")
        row2 = winnerBoard[1].split(" | ")
        row3 = winnerBoard[2].split(" | ")
        # Clear copy board
        winnerBoard.clear()
        # Add newly cleaned lists to winner board
        winnerBoard.append(row1)
        winnerBoard.append(row2)
        winnerBoard.append(row3)
        # Begin conditions for win, if match, win
        if winnerBoard[0][0] == winnerBoard[0][1] and winnerBoard[0][1] == winnerBoard[0][2]:
            winner = "Winner!"
        elif winnerBoard[1][0] == winnerBoard[1][1] and winnerBoard[1][1] == winnerBoard[1][2]:
            winner = "Winner!"
        elif winnerBoard[2][0] == winnerBoard[2][1] and winnerBoard[2][1] == winnerBoard[2][2]:
            winner = "Winner!"
        elif winnerBoard[0][0] == winnerBoard[1][0] and winnerBoard[1][0] == winnerBoard[2][0]:
            winner = "Winner!"
        elif winnerBoard[0][1] == winnerBoard[1][1] and winnerBoard[1][1] == winnerBoard[2][1]:
            winner = "Winner!"
        elif winnerBoard[0][2] == winnerBoard[1][2] and winnerBoard[1][2] == winnerBoard[2][2]:
            winner = "Winner!"
        elif winnerBoard[0][0] == winnerBoard[1][1] and winnerBoard[1][1] == winnerBoard[2][2]:
            winner = "Winner!"
        elif winnerBoard[2][0] == winnerBoard[1][1] and winnerBoard[1][1] == winnerBoard[0][2]:
            winner = "Winner!"
        else:
            winner = "No winner."
        # Return winner to variable
        return winner
# Main function where class and methods are called
def main():
    # Display Welcome Message
    print("Welcome to the Tic Tac Toe Game! It's tic-tac-totally awesome!")
    # Set arguments
    p1 = PlayTicTacToe(1, "x")
    p2 = PlayTicTacToe(2, "o")
    # Create playing board
    playingBoard = p1.createPlayingBoard()
    print()
    # Display playing board
    p1.displayPB(playingBoard)
    print()
    # Default assignment to use later for stopping while loop
    game = "Let's Play!"
    # Loop that continues until someone wins
    while game == "Let's Play!":
        # Display turn - record player's choice
        moveP1 = input("Your turn player one! Please enter a number from 1-9: ")
        print()
        # Update playing board with choice
        playingBoard = p1.your_turn(playingBoard, moveP1, "x")
        # Check if winner
        chickenDinner = p1.determineWinner(playingBoard)
        if chickenDinner == "Winner!":
            print()
            print("Player One Wins!")
            # Stop loop
            break
        print()
        # Display turn - record player's choice
        moveP2 = input("Your turn player two! Please enter a number from 1-9: ")
        print()
        # Update playing board with choice
        playingBoard = p2.your_turn(playingBoard, moveP2, "o")
        # Check if winner
        chickenDinner = p1.determineWinner(playingBoard)
        if chickenDinner == "Winner!":
            print()
            print("Player Two Wins!")
            game = "end"
        print()
# Call to main function
if __name__ == "__main__":
    main()