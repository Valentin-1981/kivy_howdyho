from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxApp(App):
    def build(self):
        bl = BoxLayout(orientation='vertical',
                       padding=[0, 50, 100, 0]
                       , spacing=50)
        bl.add_widget(Button(text='Кнопка 1'))
        bl.add_widget(Button(text='Кнопка 2'))
        bl.add_widget(Button(text='Кнопка 3'))
        return bl

if __name__ == "__main__":
    BoxApp().run()