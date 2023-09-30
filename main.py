from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        self.lbl1 = Label(text='Введите первое число:')
        self.lbl2 = Label(text='Введите второе число:')
        self.lbl3 = Label(text='Сумма двух чисел:')
        self.ti1 = TextInput(multiline=False)
        self.ti2 = TextInput(multiline=False)
        self.calc_btn = Button(text='Вычислить сумму', font_size=20)
        self.calc_btn.bind(on_press=self.calculate)
        layout.add_widget(self.lbl1)
        layout.add_widget(self.ti1)
        layout.add_widget(self.lbl2)
        layout.add_widget(self.ti2)
        layout.add_widget(self.lbl3)
        layout.add_widget(self.calc_btn)
        return layout

    def calculate(self, instance):
        first = int(self.ti1.text)
        second = int(self.ti2.text)
        total = first + second
        self.lbl3.text = str(total)


if __name__ == '__main__':
    MyApp().run()