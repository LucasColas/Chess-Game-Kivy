from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window


class ChessPieceButton(Button):
    def __init__(self, piece_image, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source=piece_image, allow_stretch=True))
        self.bind(size=self.update_image_pos)

    def update_image_pos(self, instance, size):
        for child in self.children:
            if isinstance(child, Image):
                child.size = size
                child.pos = (0, 0)

class ChessBoardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 8
        self.cols = 8
        self.sizes = Window.size
        self.width = self.sizes[0]
        self.height = self.sizes[1]
        self.cell_w = self.width // self.cols
        self.cell_h = self.width // self.rows
        with self.canvas:
            for i in range(self.rows):
                for j in range(self.cols):
                    if (i + j) % 2 == 0:
                        Color(rgba=(0, 0, 0, 1))
                        Rectangle(pos=(i*self.cell_w, j*self.cell_w), size=(self.cell_w, self.cell_h))
                    else:
                        Color(rgba=(1, 1, 1, 1))
                        Rectangle(pos=(i*self.cell_w, j*self.cell_w), size=(self.cell_w, self.cell_h))
            #Rectangle(pos=(0, 0), size=(50, 50))
class ChessApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ChessBoardScreen(name='board'))
        return sm

if __name__ == '__main__':
    ChessApp().run()
