from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class BoxApp(App):
    def build(self):
        bl = GridLayout(rows=3, padding=[30], spacing=3)
        for x in range(6):
            bl.add_widget(Button(text='X'))
        return bl

if __name__ == "__main__":
    BoxApp().run()