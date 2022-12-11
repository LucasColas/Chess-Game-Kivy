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
Config.set('graphics', 'resizable', 1)
Window.size = (800, 800)
Window.set_title("Chess")
class ChessGame(GridLayout):
    def __init__(self, **kwargs):
        super(ChessGame, self).__init__(**kwargs)
        #print(self.ids)
        self.board = GridLayout(cols=8, rows=8)
        self.size = Window.system_size
        print("size : ",self.size)
        #self.board_size = min(self.Size[0], self.Size[1])
        #print("board size : ", self.board_size)
    def draw_window(self):
        #print("in draw window")
        #print(1/8*self.board_size[0], 1/8*self.board_size[1])
        #btn1 = Button(text='Hello', size_hint=(.7, 1))
        #btn2 = Button(text='World', size_hint=(.3, 1))
        #self.board.add_widget(btn1)
        #self.board.add_widget(btn2)

        #self.board

        for i in range(8):
            #print("in the first for loop")

            for j in range(8):
                #print("in the second for loop")

                self.board.add_widget(Button(background_color=self.get_color(i,j), width=0.125*self.size[0]))



    def get_color(self, i,j):
        if (i+j)%2 != 0: #white square
            return [1,1,1,1]
        return [0,0,0,1]


def get_color(i,j):
    if (i+j)%2 != 0: #white square
        return [1,1,1,1]
    return [0,0,0,1]

class BoxLayoutApp(App):
    def build(self):
        board = BoxLayout(orientation='vertical')
        for i in range(8):
            row = BoxLayout(orientation='horizontal')
            for j in range(8):
                print(i,j)
                square_size = 0.125*800
                row.add_widget(Button(background_color=get_color(i,j), width=square_size))
            board.add_widget(row)
        return board

game = BoxLayoutApp()
game.run()
