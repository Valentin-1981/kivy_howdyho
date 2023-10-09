from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter



class MyApp(App):
    def build(self):
        # s = Scatter()
        s = Scatter(size=(600, 600))
        fl = FloatLayout(size=(300, 300), size_hint=(None, None))
        s.add_widget(fl)
        fl.add_widget(Button(text="Это моя первая кнопка!", font_size=12,
                             on_press=self.btn_press,
                             background_color=[1, 0, 0, 1],
                             background_normal='',
                             size_hint=(.5, .25),
                             pos=(100, 100)
                             ))

        return s

    def btn_press(self, instance):
        print('Кнопка нажата!')
        instance.text = "Я нажата!"


if __name__ == "__main__":
    MyApp().run()
