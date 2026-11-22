from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=12, spacing=8, **kwargs)

        self.display = TextInput(
            text="0",
            font_size=32,
            readonly=True,
            halign="right",
            size_hint=(1, 0.22),
        )
        self.add_widget(self.display)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"],
        ]

        for row in buttons:
            layout = BoxLayout(spacing=8)
            for label in row:
                layout.add_widget(Button(text=label, on_press=self.press))
            self.add_widget(layout)

    def press(self, button):
        label = button.text

        if label == "C":
            self.display.text = "0"
        elif label == "=":
            try:
                result = str(eval(self.display.text))
                self.display.text = result
            except (ZeroDivisionError, SyntaxError):
                self.display.text = "Error"
        elif self.display.text in ("0", "Error"):
            self.display.text = label
        else:
            self.display.text += label


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()
