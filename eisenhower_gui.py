from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout


class EisenhowerGUI(App):
    def build(self):
        # Main layout using FloatLayout for background and logo support
        self.root_layout = FloatLayout()
        
        # Background image
        self.bg_image = Image(source="background.png", allow_stretch=True, keep_ratio=False)
        self.bg_image.size_hint = (1, 1)
        self.bg_image.pos_hint = {'x': 0, 'y': 0}
        self.root_layout.add_widget(self.bg_image)

        # Logo image
        self.logo_image = Image(source="logo.png", allow_stretch=True)
        self.logo_image.size_hint = (1, 1)  # Adjust size hint as needed for your logo
        self.logo_image.pos_hint = {'center_x': 0.5, 'top': 1.2}
        self.root_layout.add_widget(self.logo_image)

        # Overlay GridLayout on FloatLayout
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.greeting = Label(text="Enter your name:",
                              font_size=30,
                              color='#156669')
        self.window.add_widget(self.greeting)

        self.user = TextInput(multiline=False,
                              padding_y=(20, 20),
                              size_hint=(1, 0.5))
        self.window.add_widget(self.user)

        self.button = Button(text="Start planning",
                             size_hint=(1, 0.5),
                             bold=True,
                             background_color='#156669',
                             background_normal='')
        # self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        # Add the GridLayout to the FloatLayout
        self.root_layout.add_widget(self.window)

        return self.root_layout
    
    # def callback(self, instance):
    #     self.greeting.text = "Let's go, " + self.user.text + "!"
    #     self.user.text = ""
    
if __name__ == "__main__":
    EisenhowerGUI().run()
