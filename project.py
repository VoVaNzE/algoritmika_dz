from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        self.counter = 0
        vl = BoxLayout(orientation='vertical')
        self.txt = Label(text="Счетчик: 0")
        btn = Button(text="Потапай меня")
        btn.bind(on_press=self.tapanie)
        img = Image(source='i.webp')
        vl.add_widget(self.txt)
        vl.add_widget(btn)
        vl.add_widget(img)
        return vl

    def tapanie(self, instance):
        self.counter += 1
        self.txt.text = f"Счетчик: {self.counter}"


MyApp().run()