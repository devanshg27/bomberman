class Display(object):
    # This class initializes the display and implements method that render the
    # board with the data passed.
    def __init__(self, game):
        # This method is the constructor and it initializes the screen.
        # Switch the screen to alternate buffer.
        print("\033[?1049h\033[H")
        # Hide the cursor
        print("\033[?25l")
        self.__game = game

    def render(self, board):
        # This method renders the board with the data passed.
        # Move the cursor to (1, 1) and loop through all the rows of data.
        print("\033[1;1H", end='')
        for i in range(0, len(board)):
            print(board[i])

    def close(self, infoText):
        # Display the cursor and switch back to the normal buffer.
        print("\033[?25h\033[?1049l", end='')
        print(infoText)
