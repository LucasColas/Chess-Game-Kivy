import numpy as np

class Board():
    def __init__(self):
        self.n_row = 8
        self.n_col = 8
        self.board = self.initialize_board()


    def create_board(self):
        #2D numpy array with zeros.
        return np.zeros((8,8))

    def initialize_board(self):
        """
        initialize the board.
        value from -6 to 6.
        abs(1): pawn
        abs(2): rook
        abs(3): knight
        abs(4): bishop
        abs(5): queen
        abs(6): king

        if x > 0: it represents a black piece. If x < 0 it represents a white piece.

        First row : top of the board. So there are black rooks, black bishops...
        Last row : bottom of the board. So there are white rooks, white bishops...
        """
        #create the board
        board = self.create_board()

        #initialize pawns
        board[1,:] = np.ones((1,8))
        board[self.n_row-2,:] = -1

        #initialize other pieces
        for j in range(self.n_col):
            if j == 0 or j == self.n_col-1:
                board[0, j] = 2
                board[self.n_col-1, j] = -2
            if j == 1 or j == self.n_col-2:
                board[0, j] = 3
                board[self.n_col-1, j] = -3

            if j == 2 or j == self.n_col-3:
                board[0, j] = 4
                board[self.n_col-1, j] = -4

            if j == 3:
                board[0,j] = 5
                board[self.n_col-1, j] = -5

            if j==4:
                board[0,j] = 6
                board[self.n_col-1, j] = -6


        return board


newG = Board()
