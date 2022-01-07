# print("Hello Peter!")
import kivy.app
import re 
from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

Builder.load_file('./calculator.kv')
Window.size =(350,550)

class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text='0'

    def button_value(self,number):
        prev_number=self.ids.input_box.text

        if "!ERROR" in prev_number:
            prev_number =''

        if prev_number=='0':
            self.ids.input_box.text=''
            self.ids.input_box.text=f"{number}"

        else:
            self.ids.input_box.text=f"{prev_number}{number}"

    def sign(self,sign):
        prev_number=self.ids.input_box.text
        self.ids.input_box.text=f"{prev_number}{sign}"

    def remove_last(self):
        back_number = self.ids.input_box.text
        back_number = back_number[:-1]
        self.ids.input_box.text=back_number

    def results(self):
        prev_number =self.ids.input_box.text

        try: 
            result =eval(prev_number)
            self.ids.input_box.text =str(result)
        except: 
            self.ids.input_box.text= "!ERROR"

    def positive_negative(self):
        prev_number=self.ids.input_box.text
        
        if "-" in prev_number:
            self.ids.input_box.text=f"{prev_number.replace('-','')}"
        else:
            self.ids.input_box.text=f"-{prev_number}"

    def dot(self):
        prev_number =self.ids.input_box.text
        num_list =re.split("\+|\*|-|/|%",prev_number)

        if ("+" in prev_number or "-" in prev_number or "/" in prev_number or "*" in prev_number or "%" in prev_number) and "." not in num_list[-1]:
            prev_number =f"{prev_number}."
            self.ids.input_box.text=prev_number

        elif "." in prev_number:
            pass
        else:
            prev_number=f"{prev_number}."
            self.ids.input_box.text=prev_number

class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()
