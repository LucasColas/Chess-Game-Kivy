from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config


# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)

class ChessGame():
    def __init__(self, **kwargs):
        pass

    def draw_window(self):
        pass

class WindowApp(App):

    def build(self):
        return ChessGame()
