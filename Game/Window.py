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
from kivy.graphics import Rectangle, Color
from kivy.lang.builder import Builder


Width, Height = 800, 800
Window.size = (Width, Height)

#Config.set('graphics', 'resizable', False)
class ChessPieceButton(ButtonBehavior, Image):

    grid_x = NumericProperty(0)
    grid_y = NumericProperty(0)
    position_hint = ReferenceListProperty(grid_x, grid_y)
    print("grid_x in class : ", grid_x)


class ChessBoard(RelativeLayout):

    def on_touch_down(self, touch):
        print("mouse ")
        grid_x = int(touch.pos[0] / self.width * 8)
        grid_y = int(touch.pos[1] / self.height * 8)
        for child in self.children:
            #print(child.id)
        anim = Animation(grid_x=grid_x, grid_y=grid_y, t='in_quad', duration=0.5)
        #anim.start(self.children[0])

    def on_size(self, *_):
        self.draw_board()

    def update(self):
        pass

    def on_pos(self, *_):
        self.draw_board()

    def draw_board(self):
        black = 0.5, 0.5, 0.5
        white = 1, 1, 1
        is_white = False
        grid_size_x = self.width / 8
        grid_size_y = self.height / 8
        with self.canvas.before:
            for y in range(8):
                for x in range(8):
                    if is_white:
                        Color(rgb=white)
                    else:
                        Color(rgb=black)
                    Rectangle(pos=(grid_size_x * x, grid_size_y * y), size=(grid_size_x, grid_size_y))
                    is_white = not is_white
                is_white = not is_white

class ChessPiece(ButtonBehavior, Image):
    grid_x = NumericProperty()
    grid_y = NumericProperty()
    id = StringProperty()

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
        for row in range(8):
            for col in range(8):
                if row == 1:
                    board.add_widget(ChessPiece(id="WhitePawn_"+str(col),source="Assets\PNG\WhitePawn.png",grid_x=col, grid_y=row))
                elif row == 6:
                    board.add_widget(ChessPiece(id="BlackPawn_"+str(col),source="Assets\PNG\BlackPawn.png",grid_x=col, grid_y=row))

                elif row == 0:

                    if col == 0:
                        board.add_widget(ChessPiece(id="WhiteRook_"+str(0),source="Assets\PNG\WhiteRook.png",grid_x=col, grid_y=row))
                    elif col == 7:
                        board.add_widget(ChessPiece(id="WhiteRook_"+str(1),source="Assets\PNG\WhiteRook.png",grid_x=col, grid_y=row))

                    elif col == 1:
                        board.add_widget(ChessPiece(id="WhiteKnight_"+str(0),source="Assets\PNG\WhiteKnight.png",grid_x=col, grid_y=row))
                    elif col == 6:
                        board.add_widget(ChessPiece(id="WhiteKnight_"+str(1),source="Assets\PNG\WhiteKnight.png",grid_x=col, grid_y=row))

                    elif col == 2:
                        board.add_widget(ChessPiece(id="WhiteBishop_"+str(0),source="Assets\PNG\WhiteBishop.png",grid_x=col, grid_y=row))
                    elif col == 5:
                        board.add_widget(ChessPiece(id="WhiteBishop_"+str(1),source="Assets\PNG\WhiteBishop.png",grid_x=col, grid_y=row))

                    elif col == 3:
                        board.add_widget(ChessPiece(id="WhiteKing",source="Assets\PNG\WhiteKing.png",grid_x=col, grid_y=row))

                    else:
                        board.add_widget(ChessPiece(id="WhiteQueen",source="Assets\PNG\WhiteQueen.png",grid_x=col, grid_y=row))

                elif row == 7:
                    if col == 0:
                        board.add_widget(ChessPiece(id="BlackRook_"+str(0),source="Assets\PNG\BlackRook.png",grid_x=col, grid_y=row))
                    elif col == 7:
                        board.add_widget(ChessPiece(id="BlackRook_"+str(1),source="Assets\PNG\BlackRook.png",grid_x=col, grid_y=row))

                    elif col == 1:
                        board.add_widget(ChessPiece(id="BlackKnight_"+str(0),source="Assets\PNG\BlackKnight.png",grid_x=col, grid_y=row))
                    elif col == 6:
                        board.add_widget(ChessPiece(id="BlackKnight_"+str(1),source="Assets\PNG\BlackKnight.png",grid_x=col, grid_y=row))

                    elif col == 2:
                        board.add_widget(ChessPiece(id="BlackBishop_"+str(0),source="Assets\PNG\BlackBishop.png",grid_x=col, grid_y=row))
                    elif col == 5:
                        board.add_widget(ChessPiece(id="BlackBishop_"+str(1),source="Assets\PNG\BlackBishop.png",grid_x=col, grid_y=row))

                    elif col == 3:
                        board.add_widget(ChessPiece(id="BlackKing",source="Assets\PNG\BlackKing.png",grid_x=col, grid_y=row))

                    else:
                        board.add_widget(ChessPiece(id="BlackQueen",source="Assets\PNG\BlackQueen.png",grid_x=col, grid_y=row))



        return board

if __name__ == '__main__':
    ChessApp().run()
