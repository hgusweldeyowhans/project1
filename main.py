import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '/', '*']
        self.last_op = None
        self.last_but = None
        main_layout = BoxLayout(orientation='vertical')
        
        # Text input to display the expression and result
        self.solution = TextInput(multiline=False, readonly=True, halign='right', font_size=55)
        main_layout.add_widget(self.solution)
        
        # Buttons layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "c", "+"],
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': .5, 'center_y': .5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        # Equals button
        equals_button = Button(text="=", pos_hint={'center_x': .5, 'center_y': .5})
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        
        return main_layout

    def on_button_press(self, instance):
        current_text = self.solution.text
        button_text = instance.text

        if button_text == "c":
            # Clear the input
            self.solution.text = ""
        else:
            if current_text and (self.last_op and button_text in self.operators):
                # Avoid appending operators consecutively
                return
            elif current_text == "" and button_text in self.operators:
                # Avoid starting with an operator
                return
            else:
                # Append the button text to the input
                new_text = current_text + button_text
                self.solution.text = new_text
        
        self.last_but = button_text
        self.last_op = button_text in self.operators

    def on_solution(self, instance):
        # Evaluate the expression and display the result
        try:
            result = str(eval(self.solution.text))
            self.solution.text = result
        except Exception as e:
            # Handle errors, such as division by zero or invalid syntax
            self.solution.text = "Error"

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
    # CalculatorApp().run()