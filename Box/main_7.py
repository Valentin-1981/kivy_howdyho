from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)

class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super(PainterWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 0, 1)
            Ellipse(pos=(100, 100), size=(50, 50))
            Line(points=(100, 100, 150, 200, 200, 100), close=True, width=5)
            self.line = Line(points=(), width=10, joint='bevel', cap='square')

    def on_touch_down(self, touch):
        self.line.points += (touch.x, touch.y)
class MyApp(App):
    def build(self):
        return PainterWidget()


if __name__ == "__main__":
    MyApp().run()
