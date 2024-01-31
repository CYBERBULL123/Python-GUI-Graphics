from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.text input import TextInput
class AgeCalculator(App):
    def build(self):
        self.window = GridLayout()
    return self.window
    
if __name__ == "__main__":
 AgeCalculator().run()
 self.window.cols = 1
 self.window.add_widget(Image(source("logo_image.png")))
 self.ageRequest = Label(text = "Enter your year of birth...")
  self.window.add_widget(self.ageRequest)

self.date = TextInput(multiline=False)
self.window.add_widget(self.date)
self.date = TextInput()
self.button = Button(text = "Calculate Age")
self.button.bind(on_press = self.getAge)
self.window.add_widget(self.button)
def getAge(self, event):
    today = datetime.today().year 
    dob = self.date.text
    age = int(today) - int(dob) 
    self.ageRequest.text = "You are " + str(int(age)) + " years old"
    def build(self):
    self.window = GridLayout()
    self.window.cols = 1
    self.window.size_hint = (0.6, 0.7)
    self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
    self.window.add_widget(Image(source("logo_image.png")))


    self.ageRequest = Label(
        text = "Enter your date of birth...", 
        font_size = 50,
        color = "#ffffff",
        bold = True
    )
    self.window.add_widget(self.ageRequest)
    
    self.date = TextInput(
        multiline=False,
        padding_y = (30, 30),
        size_hint = (1, 0.7),
        font_size = 30
    )
    self.window.add_widget(self.date)

    self.button = Button(
        text = "Calculate Age",
        size_hint = (0.5, 0.5),
        bold = True,
        font_size = 30
    )
    self.button.bind(on_press = self.getAge)
    self.window.add_widget(self.button)

    return self.window
