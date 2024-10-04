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
        size_hint = 0.5,1
        btn = Button(text="Потапай меня",background_normal='i.webp', background_down='i (1).webp', size_hint=size_hint, pos_hint={'x':0.25,'y':0.6})
        btn.bind(on_press=self.tapanie)
        # img = Image(source='i.webp')
        vl.add_widget(self.txt)
        vl.add_widget(btn)
        # vl.add_widget(img)
        return vl

    def tapanie(self, instance):
        self.counter += 1
        self.txt.text = f"Счетчик: {self.counter}"


MyApp().run()
