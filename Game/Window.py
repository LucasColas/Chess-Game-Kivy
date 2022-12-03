from kivy.app import App
from kivy.lang.builder import Builder
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.floatlayout import FloatLayout

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)

class ChessGame(Widget):

    def draw_window(self):
        board = self.ids.chess_board
        for i in range(8):
            board_row = BoxLayout(orientation="horizontal")
            for j in range(8):
                board_row.add_widget(Button(background_normla="", background_color=self.get_color(i,j)))
            board.add_widget(board_row)

    def get_color(self, i,j):
        if (i+j)%2 != 0: #white square
            return [1,1,1,1]
        return [0,0,0,1]

class WindowApp(App):

    def build(self):
        game = ChessGame()
        game.draw_window()
        return game


app = WindowApp()
app.run()
