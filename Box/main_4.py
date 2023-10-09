from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class BoxApp(App):
    def build(self):
        bl = AnchorLayout(anchor_x='left', anchor_y='top')
        bl.add_widget(Button(text='X', size_hint=[.5, .5]))
        return bl

if __name__ == "__main__":
    BoxApp().run()