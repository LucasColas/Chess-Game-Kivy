from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import *
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Rectangle, Color, Ellipse
from kivy.lang.builder import Builder


Width, Height = 800, 800
Window.size = (Width, Height)

#Config.set('graphics', 'resizable', False)
"""
class ChessPieceButton(ButtonBehavior, Image):

    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)

    position_hint = ReferenceListProperty(grid_x, grid_y)
    print("grid_x in class : ", grid_x)
"""
class ChessPiece(ButtonBehavior, Image):
    grid_x = NumericProperty()
    grid_y = NumericProperty()
    id = StringProperty()
    def available_moves(self, pieces):
        pass

class Pawn(ChessPiece):
    """
        Class for Pawn Piece.
    """
    First_use = BooleanProperty()
    def callback(instance, value):
        print("Value of First_use changed", value)

    def available_moves(self, pieces):
        """
            parameters : pieces -> a container with every available pieces in the game.
            Check if it's a white or black pawn.
            Then find if there are available moves.
            Look for pieces to capture (on the left or on the right)
            available moves are stored in a dictionary (available_moves).
            available_moves has 2 keys. The first one contains a tuple with every possible moves.
            A move is a tuple that contains x and y coordinates.
            The second key contains the position of the pieces that can be captured.

            return : available_moves (dictionary)
        """
        if self.id[:5] == "White":
            available_moves = {"available_moves":(), "pieces_to_capture":[]}

            if self.grid_y > 7:
                return available_moves
            if self.First_use:  #if it's the first time a pawn moves
                #origins of the x and y axis are in the bottom left corner.
                #so a white pawn moves forward by incrementing its y coordinate.
                available_moves["available_moves"] = ((self.grid_x, self.grid_y+1), (self.grid_x, self.grid_y+2))
            else:
                available_moves["available_moves"] = ((self.grid_x, self.grid_y+1),)
                print("not first use, available_moves : ",available_moves["available_moves"])




            for piece in pieces:
                #if there is a piece in front of it then it can move forward.
                if piece.grid_y == self.grid_y + 1 and piece.grid_x == self.grid_x:
                    available_moves["available_moves"] = ()

                #Look for pieces to capture. They must be white pieces.
                if piece.id[:5] == "Black" and piece.grid_x == self.grid_x + 1 and piece.grid_y == self.grid_y + 1:
                    available_moves["pieces_to_capture"].append((self.grid_x + 1,self.grid_y + 1))

                if piece.id[:5] == "Black" and piece.grid_x == self.grid_x - 1 and piece.grid_y == self.grid_y + 1:
                    available_moves["pieces_to_capture"].append((self.grid_x - 1,self.grid_y + 1))

            return available_moves

        if self.id[:5] == "Black":
            #print("Black")
            available_moves = {"available_moves":(), "pieces_to_capture":[]}
            if self.First_use: #if it's the first time a pawn moves
                #self.First_use = False
                #print("First Use")
                #a white pawn moves forward by decrementing its y coordinate.
                available_moves["available_moves"] = ((self.grid_x, self.grid_y-1), (self.grid_x,self.grid_y-2))
            else:
                available_moves["available_moves"] = ((self.grid_x, self.grid_y-1),)
            for piece in pieces:
                if piece.grid_y == self.grid_y - 1 and piece.grid_x == self.grid_x:
                    available_moves["available_moves"] = ()

                #Look for pieces to capture. They must be white pieces.
                if piece.id[:5] == "White" and piece.grid_x == self.grid_x + 1 and piece.grid_y == self.grid_y - 1:
                    available_moves["pieces_to_capture"].append((self.grid_x + 1,self.grid_y - 1))

                if piece.id[:5] == "White" and piece.grid_x == self.grid_x - 1 and piece.grid_y == self.grid_y - 1:
                    available_moves["pieces_to_capture"].append((self.grid_x - 1,self.grid_y - 1))

            return available_moves

class Rook(ChessPiece):
    """
        Class for Rook piece.
    """
    First_use = BooleanProperty()
    def available_moves(self, pieces):
        #super(Rook, self).available_moves(pieces)
        available_moves = {"available_moves":[], "pieces_to_capture":[]}
        rows = 8
        cols = 8
        #print("range values rook 0", self.grid_y + 1, rows -  self.grid_y)

        for x in range(int(self.grid_x) + 1, cols):
            found = False
            for piece in pieces:
                if piece.grid_x == x and piece.grid_y == self.grid_y:
                    found = True
                    if piece.id[:5] != self.id[:5]:
                        available_moves["pieces_to_capture"].append((piece.grid_x, piece.grid_y))
                    break
            if found:
                break
            available_moves["available_moves"].append((x, self.grid_y))



        for y in range(int(self.grid_y) + 1, rows):
            found = False
            for piece in pieces:
                #print("coord", piece.grid_x, piece.grid_y, self.grid_x, y)
                #print(piece.grid_x == int(self.grid_x))
                if piece.grid_x == self.grid_x and piece.grid_y == y:
                    found = True
                    if piece.id[:5] != self.id[:5]:
                        available_moves["pieces_to_capture"].append((piece.grid_x, piece.grid_y))
                    break
            if found:
                break
            available_moves["available_moves"].append((self.grid_x, y))

        for x in range(int(self.grid_x) - 1, -1, -1):
            found = False
            for piece in pieces:
                if piece.grid_x == x and piece.grid_y == self.grid_y:
                    found = True
                    if piece.id[:5] != self.id[:5]:
                        available_moves["pieces_to_capture"].append((piece.grid_x, piece.grid_y))
                    break
            if found:
                break
            available_moves["available_moves"].append((x, self.grid_y))

        for y in range(int(self.grid_y) - 1, -1, -1):
            found = False
            for piece in pieces:
                if piece.grid_x == self.grid_x and piece.grid_y == y:
                    found = True
                    if piece.id[:5] != self.id[:5]:
                        available_moves["pieces_to_capture"].append((piece.grid_x, piece.grid_y))
                    break
            if found:
                break
            available_moves["available_moves"].append((self.grid_x, y))

        return available_moves



class Knight(ChessPiece):
    """
        Class for Knight piece.
    """

    def available_moves(self, pieces):
        available_moves = {"available_moves":self.create_moves(), "pieces_to_capture":[]}


        for piece in pieces:
            if self.id[:5] == "White":

                if piece.id[:5] == "White" and (piece.grid_x, piece.grid_y) in available_moves["available_moves"]:
                    available_moves["available_moves"].remove((piece.grid_x, piece.grid_y))

                if piece.id[:5] == "Black" and (piece.grid_x, piece.grid_y) in available_moves["available_moves"]:
                    available_moves["available_moves"].remove((piece.grid_x, piece.grid_y))
                    available_moves["pieces_to_capture"].append((piece.grid_x, piece.grid_y))

            if self.id[:5] == "Black":
                if piece.id[:5] == "Black" and (piece.grid_x, piece.grid_y) in available_moves["available_moves"]:
                    available_moves["available_moves"].remove((piece.grid_x, piece.grid_y))

                if piece.id[:5] == "White" and (piece.grid_x, piece.grid_y) in available_moves["available_moves"]:
                    available_moves["available_moves"].remove((piece.grid_x, piece.grid_y))
                    available_moves["pieces_to_capture"].append((piece.grid_x, piece.grid_y))

        return available_moves


    def create_moves(self):
        moves = [
            (self.grid_x + 2, self.grid_y + 1),
            (self.grid_x + 1, self.grid_y + 2),
            (self.grid_x - 2, self.grid_y + 1),
            (self.grid_x - 1, self.grid_y + 2),

            (self.grid_x + 1, self.grid_y - 2),
            (self.grid_x + 2, self.grid_y - 1),
            (self.grid_x - 2, self.grid_y - 1),
            (self.grid_x - 1, self.grid_y - 2),
        ]
        good_moves = []
        for move in moves:
            if move[0] <= 7 and move[1] <= 7 and move[0] >= 0 and move[1] >= 0:
                good_moves.append((move))


        return good_moves

class Bishop(ChessPiece):
    """
        Class for Bishop piece.
    """

    def available_moves(self, pieces):
        #super(Bishop, self).available_moves(pieces)
        available_moves = {"available_moves":[], "pieces_to_capture":[]}
        rows = 8
        cols = 8

        for i in range(1, rows):
            if self.grid_x + i >= rows or self.grid_y + i >= cols:
                break
            found = False
            for piece in pieces:
                if piece.grid_x == self.grid_x + i and piece.grid_y == self.grid_y + i:
                    found = True
                    if piece.id[:5] != self.id[:5]:
                        available_moves["pieces_to_capture"].append((self.grid_x + i, self.grid_y + i))
                    break

            if found:
                break
            available_moves["available_moves"].append((self.grid_x + i, self.grid_y + i))

        for i in range(1, rows):
            print("coord ",self.grid_x - i, self.grid_y + i)
            if self.grid_x - i < 0 or self.grid_y + i >= rows:
                break
            found = False
            for piece in pieces:
                #print(piece.grid_x, piece.grid_y,piece.grid_x == self.grid_x - i and piece.grid_y == self.grid_y + i)
                if piece.grid_x == self.grid_x - i and piece.grid_y == self.grid_y + i:
                    found = True
                    if piece.id[:5] != self.id[:5]:
                        available_moves["pieces_to_capture"].append((self.grid_x - i, self.grid_y + i))
                    break

            if found:
                break
            available_moves["available_moves"].append((self.grid_x - i, self.grid_y + i))

        for i in range(1, rows):
            if self.grid_x - i < 0 or self.grid_y - i < 0:
                break
            found = False
            for piece in pieces:
                if piece.grid_x == self.grid_x - i and piece.grid_y == self.grid_y - i:
                    found = True
                    if piece.id[:5] != self.id[:5]:
                        available_moves["pieces_to_capture"].append((self.grid_x - i, self.grid_y - i))
                    break

            if found:
                break
            available_moves["available_moves"].append((self.grid_x - i, self.grid_y - i))

        for i in range(1, rows):
            if self.grid_x + i >= rows or self.grid_y - i < 0:
                break
            found = False
            for piece in pieces:
                if piece.grid_x == self.grid_x + i and piece.grid_y == self.grid_y - i:
                    found = True
                    if piece.id[:5] != self.id[:5]:
                        available_moves["pieces_to_capture"].append((self.grid_x + i, self.grid_y - i))
                    break

            if found:
                break
            available_moves["available_moves"].append((self.grid_x + i, self.grid_y - i))


        return available_moves



class Queen(Rook, Bishop): #Inherit from Bishop and Rook
    def available_moves(self, pieces):
        #Inherits from Bishop and Rook
        #get the available moves
        #super(Rook, self).available_moves(pieces)
        available_moves1 = Rook.available_moves(self,pieces)
        print("available_moves1", available_moves1)
        available_moves2 = Bishop.available_moves(self,pieces)
        print("available_moves2", available_moves2)
        available_moves = {key: val + available_moves2[key] for key, val in available_moves1.items()}
        return available_moves

class King(ChessPiece):
    First_use = BooleanProperty()
    def available_moves(self, pieces):
        available_moves = self.create_moves()
        rows, cols = 8,8
        good_available_moves = []
        for move in available_moves["available_moves"]:

            if move[0] < cols and move[1] < rows and move[1] >= 0 and move[0] >= 0:

                good_available_moves.append(move)
                #print("in King : ", available_moves)

        available_moves["available_moves"] = good_available_moves
        #print("in King : ", available_moves)

        for piece in pieces:
            if (piece.grid_x, piece.grid_y) in available_moves["available_moves"]:
                if piece.id[:5] != self.id[:5]:
                    available_moves["pieces_to_capture"].append((piece.grid_x, piece.grid_y))

                available_moves["available_moves"].remove((piece.grid_x, piece.grid_y))

        if self.First_use:
            available_moves["castling"] = self.castling(pieces)

        return available_moves


    def create_moves(self):
        available_moves = {"available_moves":[], "pieces_to_capture":[]}

        available_moves["available_moves"].append((self.grid_x, self.grid_y+1))

        available_moves["available_moves"].append((self.grid_x-1, self.grid_y+1))

        available_moves["available_moves"].append((self.grid_x+1, self.grid_y+1))

        available_moves["available_moves"].append((self.grid_x-1, self.grid_y))

        available_moves["available_moves"].append((self.grid_x-1, self.grid_y-1))

        available_moves["available_moves"].append((self.grid_x+1, self.grid_y))

        available_moves["available_moves"].append((self.grid_x+1, self.grid_y-1))

        available_moves["available_moves"].append((self.grid_x, self.grid_y-1))

        return available_moves

    def castling(self, pieces):
        if self.First_use:
            print("castling First use")
            no_piece_left = True
            no_piece_right = True
            for piece in pieces:
                #Problem with if : if there's an ennemy piece it may work
                if piece.grid_y == self.grid_y and piece.grid_x > self.grid_x and (piece.id[5:9] != "Rook" or self.id[:5] != piece.id[:5]):
                    print("no_piece_right False : ", piece.grid_y, piece.grid_x, piece.id)
                    no_piece_right = False

                elif piece.grid_y == self.grid_y and piece.grid_x < self.grid_x and (piece.id[5:9] != "Rook" or self.id[:5] != piece.id[:5]):
                    print("no_piece_left False : ", piece.grid_y, piece.grid_x, piece.id)
                    no_piece_left = False

            if no_piece_right and no_piece_left:
                return [(self.grid_x-2, self.grid_y),(self.grid_x+2, self.grid_y)]

            if no_piece_right:
                return [(self.grid_x+2, self.grid_y)]

            if no_piece_left:
                return [(self.grid_x-2, self.grid_y)]
        return []

class ChessBoard(RelativeLayout):
    """
        Relative Layout for the whole chess board.
    """
    piece_pressed = False
    id_piece_ = None
    available_moves = {"available_moves":(), "pieces_to_capture":[]}
    turn_ = "White"
    piece_index = None
    def on_touch_down(self, touch):
        rows, cols = 8,8
        #get the position
        grid_x = int(touch.pos[0] / self.width * rows)
        grid_y = int(touch.pos[1] / self.height * cols)

        for id, child in enumerate(self.children):
            if not ChessBoard.piece_pressed:
                #Find if a player clicked on a piece
                #TODO : check the turn
                #TODO: do the 3 special moves
                if grid_x == child.grid_x and grid_y == child.grid_y and child.id[:5] == ChessBoard.turn_: #The player clicked on a piece
                    ChessBoard.piece_pressed = True
                    ChessBoard.piece_index = id
                    #Get available_moves
                    print(child.id)
                    ChessBoard.available_moves = child.available_moves(self.children)
                    self.draw_moves()
                    print(ChessBoard.available_moves)
                    ChessBoard.id_piece_ = child.id
                    break
            elif ChessBoard.piece_pressed and grid_x == child.grid_x and grid_y == child.grid_y and ChessBoard.id_piece_[:5] == child.id[:5]:
                ChessBoard.available_moves = child.available_moves(self.children)
                print(child.id)
                self.draw_moves()
                print("in elif",ChessBoard.available_moves)
                ChessBoard.id_piece_ = child.id
                break

            elif ChessBoard.piece_pressed and child.id == ChessBoard.id_piece_:
                if (grid_x, grid_y) in ChessBoard.available_moves["available_moves"]:

                    anim = Animation(grid_x=grid_x, grid_y=grid_y, t='in_quad', duration=0.5)
                    anim.start(self.children[id])



                    ChessBoard.piece_pressed = False
                    ChessBoard.available_moves = {"available_moves":(), "pieces_to_capture":[]}
                    if child.id[5:9] == "Pawn" and child.First_use:
                        child.First_use = False
                    self.draw_moves()
                    self.turn()

                elif (grid_x, grid_y) in ChessBoard.available_moves["pieces_to_capture"]:
                    for enemy in self.children:
                        if enemy.grid_x == grid_x and enemy.grid_y == grid_y:

                            anim = Animation(grid_x=grid_x, grid_y=grid_y, t='in_out_expo', duration=0.5)
                            anim.start(self.children[id])
                            self.remove_widget(enemy)
                            ChessBoard.piece_pressed = False
                            ChessBoard.available_moves = {"available_moves":(), "pieces_to_capture":[]}
                            if child.id[5:9] == "Pawn" and child.First_use:
                                child.First_use = False
                            self.draw_moves()
                            self.turn()
                            break

            elif ChessBoard.piece_pressed and ChessBoard.id_piece_[5:] == "King" and (grid_x, grid_y) in ChessBoard.available_moves["castling"] and child.id[:5] == ChessBoard.id_piece_[:5] and child.id[5:-2] == "Rook":
                if child.grid_x == grid_x + 1:
                    anim = Animation(grid_x=grid_x-1, grid_y=grid_y, t='in_out_expo', duration=0.5)
                    anim.start(self.children[id])

                elif child.grid_x == grid_x - 1:
                    anim = Animation(grid_x=grid_x+1, grid_y=grid_y, t='in_out_expo', duration=0.5)
                    anim.start(self.children[id])
                anim = Animation(grid_x=grid_x, grid_y=grid_y, t='in_out_expo', duration=0.5)
                anim.start(self.children[ChessBoard.piece_index])
                ChessBoard.piece_pressed = False
                child.First_use = False
                self.children[ChessBoard.piece_index].First_use = False
                ChessBoard.available_moves = {"available_moves":(), "pieces_to_capture":[]}
                self.turn()
                self.draw_moves()



            #print(ChessBoard.id_piece_[5:], child.id[:5], ChessBoard.id_piece_[:5], child.id[5:-2])


    def turn(self):
        if ChessBoard.turn_ == "White":
            ChessBoard.turn_ = "Black"

        else:
            ChessBoard.turn_ = "White"

    def draw_moves(self):

        """
        Draw available moves.
        Moves are circles. They are added in a group.
        We can delete this group and so delete the ellipses.
        """
        grid_size_x = self.width / 8
        grid_size_y = self.height / 8
        Blue = (0, 0, 1)
        Green = (0, 1, 0)
        #self.canvas.clear()

        with self.canvas:
            #self.canvas.remove_group()
            #print("draw")
            self.canvas.remove_group("moves") #remove previous moves drawn
            size = (0.2*grid_size_x, 0.2*grid_size_y) #size of a circle that represents an available move
            #moves = InstructionGroup() #Group where we store every circles

            for idx, moves in enumerate(ChessBoard.available_moves.values()): #available_moves and pieces_to_capture
                print("moves in draw_moves : ", moves)
                if idx == 0:
                    Color(rgb=Blue)
                    for move in moves:
                        Ellipse(pos=(grid_size_x * move[0]+grid_size_x/2 - size[0]/2, grid_size_y * move[1] + grid_size_y/2 - size[1]/2), size=size, group="moves")
                elif idx == 1:
                    Color(rgb=Green)
                    for move in moves:
                        Ellipse(pos=(grid_size_x * move[0]+grid_size_x/2 - size[0]/2, grid_size_y * move[1] + grid_size_y/2 - size[1]/2), size=size, group="moves")



        #print("moves : ",self.canvas.get_group('moves'))

    def on_size(self, *_):
        #update the board
        self.draw_board()
        self.draw_moves()

    def update(self):
        pass

    def on_pos(self, *_):
        #update the board
        self.draw_board()
        self.draw_moves()

    def draw_board(self):
        green = 0.18, 0.70, 0.24
        white = 1, 1, 1
        is_white = False
        grid_size_x = self.width / 8
        grid_size_y = self.height / 8
        #self.canvas.clear()
        with self.canvas.before:
            #draw the board.
            for y in range(8):
                for x in range(8):
                    if is_white:
                        Color(rgb=white)
                    else:
                        Color(rgb=green)
                    Rectangle(pos=(grid_size_x * x, grid_size_y * y), size=(grid_size_x, grid_size_y))
                    is_white = not is_white
                is_white = not is_white



class ChessBoardScreen(Screen):
    def __init__(self, **kwargs):
        super(ChessBoardScreen, self).__init__(**kwargs)
        #self.board = ChessBoard()
        #self.add_widget(self.board)
        self.game = ChessGame()
        self.add_widget(self.game)



class ChessApp(App):
    def build(self):
        #sm = ScreenManager()
        #sm.add_widget(ChessBoardScreen(name='board'))
        board = ChessBoard()
        #Add every piece.
        for row in range(8):
            for col in range(8):
                if row == 1:
                    board.add_widget(Pawn(id="WhitePawn_"+str(col),source="Assets\PNG\WhitePawn.png",grid_x=col, grid_y=row))
                elif row == 6:
                    board.add_widget(Pawn(id="BlackPawn_"+str(col),source="Assets\PNG\BlackPawn.png",grid_x=col, grid_y=row))

                elif row == 0:

                    if col == 0:
                        board.add_widget(Rook(id="WhiteRook_"+str(0),source="Assets\PNG\WhiteRook.png",grid_x=col, grid_y=row))
                    elif col == 7:
                        board.add_widget(Rook(id="WhiteRook_"+str(1),source="Assets\PNG\WhiteRook.png",grid_x=col, grid_y=row))

                    elif col == 1:
                        board.add_widget(Knight(id="WhiteKnight_"+str(0),source="Assets\PNG\WhiteKnight.png",grid_x=col, grid_y=row))
                    elif col == 6:
                        board.add_widget(Knight(id="WhiteKnight_"+str(1),source="Assets\PNG\WhiteKnight.png",grid_x=col, grid_y=row))

                    elif col == 2:
                        board.add_widget(Bishop(id="WhiteBishop_"+str(0),source="Assets\PNG\WhiteBishop.png",grid_x=col, grid_y=row))
                    elif col == 5:
                        board.add_widget(Bishop(id="WhiteBishop_"+str(1),source="Assets\PNG\WhiteBishop.png",grid_x=col, grid_y=row))

                    elif col == 3:
                        board.add_widget(Queen(id="WhiteQueen",source="Assets\PNG\WhiteQueen.png",grid_x=col, grid_y=row))

                    else:
                        board.add_widget(King(id="WhiteKing",source="Assets\PNG\WhiteKing.png",grid_x=col, grid_y=row))

                elif row == 7:
                    if col == 0:
                        board.add_widget(Rook(id="BlackRook_"+str(0),source="Assets\PNG\BlackRook.png",grid_x=col, grid_y=row))
                    elif col == 7:
                        board.add_widget(Rook(id="BlackRook_"+str(1),source="Assets\PNG\BlackRook.png",grid_x=col, grid_y=row))

                    elif col == 1:
                        board.add_widget(Knight(id="BlackKnight_"+str(0),source="Assets\PNG\BlackKnight.png",grid_x=col, grid_y=row))
                    elif col == 6:
                        board.add_widget(Knight(id="BlackKnight_"+str(1),source="Assets\PNG\BlackKnight.png",grid_x=col, grid_y=row))

                    elif col == 2:
                        board.add_widget(Bishop(id="BlackBishop_"+str(0),source="Assets\PNG\BlackBishop.png",grid_x=col, grid_y=row))
                    elif col == 5:
                        board.add_widget(Bishop(id="BlackBishop_"+str(1),source="Assets\PNG\BlackBishop.png",grid_x=col, grid_y=row))

                    elif col == 3:
                        board.add_widget(Queen(id="BlackQueen",source="Assets\PNG\BlackQueen.png",grid_x=col, grid_y=row))

                    else:
                        board.add_widget(King(id="BlackKing",source="Assets\PNG\BlackKing.png",grid_x=col, grid_y=row))



        return board

if __name__ == '__main__':
    ChessApp().run()
