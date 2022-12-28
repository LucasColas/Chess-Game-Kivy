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

class Bishop(Widget):
    def __init__(self, square_size):
        self.square_size = square_size
        self.ids.Bishop.pos = (200,200)

class ChessGame(Widget):
    def __init__(self, **kwargs):

        #print(self.ids)
        self.board_backend = gc.Game()
        self.square_size = 0.125*Window.size[0]
        self.board = BoxLayout(orientation='vertical')
        self.Bishop = Bishop(self.square_size)
        self.board_frontend = self.draw_window()
        self.img = []

        print("self board ",self.board)
    def draw_window(self):
        for i in range(8):
            row = BoxLayout(orientation='horizontal')
            for j in range(8):

                row.add_widget(Button(background_normal='', background_color=self.get_color(i,j), width=self.square_size))
                if i == 1:
                    pass
            self.board.add_widget(row)
        return self.board



    def get_color(self, i,j):
        if (i+j)%2 != 0: #white square
            return [1,1,1,1]
        return [0,0,0,1]

    def update_canvas(self):
        self.canvas.clear()
        for i in range(8):
            for j in range(8):
                with self.canvas:
                    if self.board_backend.board[i,j] == 1:
                        pass


class BoxLayoutApp(App):
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
