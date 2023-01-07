from kivy.app import App
from kivy.lang.builder import Builder
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.core.image import Image

import src.GameClasse as gc

# 0 being off 1 being on as in true / false
Config.set('graphics', 'resizable', 1)
Window.size = (720, 720)
Window.set_title("Chess")
"""
class Bishop(Widget):
    def __init__(self, square_size):
        self.square_size = square_size
        self.ids.Bishop.pos = (200,200)
"""

class ChessCell(Button):
    pass

class Chessboard(GridLayout):
    def images_dict(self, images_dir):

        images = {4:images_dir+'BlackBishop.png',
                        6:images_dir+'BlackKing.png',
                        3:images_dir+'BlackKnight.png',
                        1:images_dir+'BlackPawn.png',
                        5:images_dir+'BlackQueen.png',
                        2:images_dir+'BlackRook.png',
                        -4:images_dir+'WhiteBishop.png',
                        -6:images_dir+'WhiteKing.png',
                        -3:images_dir+'WhiteKnight.png',
                        -1:images_dir+'WhitePawn.png',
                        -5:images_dir+'WhiteQueen.png',
                        -2:images_dir+'WhiteRook.png'

        }
        return images

    def update_position(self, images_dir, board):
        images = self.images_dict(images_dir)
        ids = {child.id: child for child in self.children}

        for i in range(8):
            for j in range(8):
                if board[i,j] != 0:
                    image = images[board[i,j]]
                else:
                    image = images_dir + 'transparency.png'

                ids[str(i) + "." + str(j)].children[0] = image

class ChessGame(BoxLayout):
    def __init__(self, **kwargs):

        #print(self.ids)
        self.board_backend = gc.Board()
        self.square_size = 0.125*Window.size[0]
        #self.board = BoxLayout(orientation='vertical')
        self.board_frontend = self.draw_board()
        self.img = []

        #print("self board ",self.board)
    def draw_board(self):
        #Add ChessCell
        for i in range(8):
            for j in range(8):
                new_button = ChessCell(id=str(i) + "." + str(j))





    def get_color(self, i,j):
        if (i+j)%2 != 0: #white square
            return [1,1,1,1]
        return [0,0,0,1]

    def update_board(self, board):
        pass


class WindowApp(App):
    def build(self):
        chess_board = ChessGame()

        """
        board = BoxLayout(orientation='vertical')
        for i in range(8):
            row = BoxLayout(orientation='horizontal')
            for j in range(8):
                print(i,j)
                square_size = 0.125*800
                row.add_widget(Button(background_normal='', background_color=get_color(i,j), width=square_size))
            board.add_widget(row)
        return board
        """
        return chess_board.board_frontend

game = BoxLayoutApp()
game.run()
