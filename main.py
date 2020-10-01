board = ["1","2","3","4","5","6","7","8","9"]

def showBoard():
    print ("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print ("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|" )

def turn1():
    position = int(input("Player X's turn... Choose a position between one to nine: ")) - 1
    
    if board[position] != "O":
        board[position] = "X"
    else:
        print("Position already taken... Try any other position.")
        turn1()
        


def turn2():
    position = int(input("Player O's turn... Choose a position between one to nine: ")) - 1
    
    if board[position] != "X":
        board[position] = "O"
    else:
        print("Position already taken... Try any other position")
        turn2()


def own():
    if (board[0] == board[1] and board[0] == board[2] and board[1] == board[2]) or (board[3] == board[4] and board[4] == board[5] and board[3] == board[5]) or (board[6] == board[7] and board[7] == board[8] and board[6] == board[8]) or (board[0] == board[4] and board[4] == board[8] and board[0] == board[8]) or (board[2] == board[4] and board[4] == board[6] and board[2] == board[6]) or (board[0] == board[3] and board[3] == board[6] and board[0] == board[6]) or (board[1] == board[4] and board[4] == board[7] and board[1] == board[7]) or (board[2] == board[5] and board[5] == board[8] and board[2] == board[8]) :

        return True
    
    return False

def allFilled():
    if ("1" not in board and "2" not in board and "3" not in board and "4" not in board and "5" not in board and "6" not in board and "7" not in board and "8" not in board and "9" not in board):
        return True
    return False

def play():
    while True:
        showBoard()
        if not own() and not allFilled():
            turn1()
        elif not own() and allFilled():
            print("Game tied...")
            break
        else:
            print("Game over player O own...")
            break

        showBoard()
        if not own() and not allFilled():
            turn2()
        elif not own() and allFilled():
            print("Game tied...")
            break
        else: 
            print("Game over Player X own...")
            break


if __name__ == "__main__":

    try:
        play()
    except KeyboardInterrupt:
        exit()
    except Exception :
        print("Invalid position selected... Restarting the game...")
        play()




