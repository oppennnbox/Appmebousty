from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# Небольшая адаптация под телефоны
Window.clearcolor = (0.1, 0.1, 0.15, 1)


class CounterApp(App):
    def build(self):
        self.count = 0

        layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=20
        )

        self.label = Label(
            text="Нажми на кнопку!",
            font_size='26sp',
            halign='center',
            valign='middle'
        )
        layout.add_widget(self.label)

        btn = Button(
            text="Нажми меня",
            font_size='22sp',
            size_hint=(1, 0.3),
            background_color=(0.2, 0.6, 0.9, 1)
        )
        btn.bind(on_press=self.increment)
        layout.add_widget(btn)

        reset_btn = Button(
            text="Сброс",
            font_size='20sp',
            size_hint=(1, 0.2),
            background_color=(0.9, 0.3, 0.3, 1)
        )
        reset_btn.bind(on_press=self.reset)
        layout.add_widget(reset_btn)

        return layout

    def increment(self, instance):
        self.count += 1
        self.label.text = f"Нажато: {self.count}"

    def reset(self, instance):
        self.count = 0
        self.label.text = "Нажми на кнопку!"


if __name__ == "__main__":
    CounterApp().run()
