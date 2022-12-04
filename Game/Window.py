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

# 0 being off 1 being on as in true / false
Config.set('graphics', 'resizable', True)

class ChessGame(Widget):
    def __init__(self, **kwargs):
        super(ChessGame, self).__init__(**kwargs)
        #print(self.ids)
        self.board = self.ids["chess_board"]
        self.Size = Window.system_size
        print("size : ",self.Size)
        self.board_size = [self.Size[0], self.Size[1]*0.8]
        #print("board size : ", self.board_size)
    def draw_window(self):
        #print("in draw window")
        for i in range(8):
            #print("in the first for loop")
            board_row = BoxLayout(orientation="horizontal")
            for j in range(8):
                #print("in the second for loop")
                board_row.add_widget(Button(background_normal="", background_color=self.get_color(i,j)))
            self.board.add_widget(board_row)

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
