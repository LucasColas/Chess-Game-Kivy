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

import src.GameClasse as gc

# 0 being off 1 being on as in true / false
Config.set('graphics', 'resizable', 1)
Window.size = (800, 800)
Window.set_title("Chess")

class ChessGame(Widget):
    def __init__(self, **kwargs):

        #print(self.ids)
        self.board_backend = gc.Game()
        self.board_frontend = self.draw_window()
        self.img = []

    def draw_window(self):
        board = BoxLayout(orientation='vertical')
        for i in range(8):
            row = BoxLayout(orientation='horizontal')
            for j in range(8):
                #print(i,j)
                square_size = 0.125*800

                row.add_widget(Button(background_normal='', background_color=self.get_color(i,j), width=square_size))
            board.add_widget(row)
        return board



    def get_color(self, i,j):
        if (i+j)%2 != 0: #white square
            return [1,1,1,1]
        return [0,0,0,1]

    def update(self):
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
        return chess_board.draw_board

game = BoxLayoutApp()
game.run()
