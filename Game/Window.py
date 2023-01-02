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

class Chessboard(GridLayout):
    def images_dict(self, images_dir):

        images = {'Black-Bishop':images_dir+'BlackBishop.png'
                        'Black-King':images_dir+'BlackKing.png'
                        'Black-Knight':images_dir+'BlackKnight.png'
                        'Black-Pawn':images_dir+'BlackPawn.png'
                        'Black-Queen':images_dir+'BlackQueen.png'
                        'Black-Rook':images_dir+'BlackRook.png'
                        'White-Bishop':images_dir+'WhiteBishop.png'
                        'WhiteKing':images_dir+'WhiteKing.png'
                        'WhiteKnight':images_dir+'WhiteKnight.png'
                        'WhitePawn':images_dir+'WhitePawn.png'
                        'WhiteQueen':images_dir+'WhiteQueen.png'
                        'WhiteRook':images_dir+'WhiteRook.png'

        }
        return images

class ChessGame(BoxLayout):
    def __init__(self, **kwargs):

        #print(self.ids)
        self.board_backend = gc.Game()
        self.square_size = 0.125*Window.size[0]
        #self.board = BoxLayout(orientation='vertical')
        self.board_frontend = self.draw_board()
        self.img = []

        #print("self board ",self.board)
    def draw_board(self):
        #Add ChessCell



    def get_color(self, i,j):
        if (i+j)%2 != 0: #white square
            return [1,1,1,1]
        return [0,0,0,1]

    def update_board(self):
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
