#! /usr/bin/env python
# -*- coding: utf-8 -*-
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.8.0') # replace with your current kivy version !
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
# Window.clearcolor = (1, 1, 1, 1)

Window.size = (800,800)

from kivy.uix.boxlayout import BoxLayout    
class LblTxt(BoxLayout):
    from kivy.properties import ObjectProperty
    theTxt = ObjectProperty(None)

class MyApp(App):
    def build(self):
        self.textAndInput = Builder.load_file('simpleForm.kv')
        self.task = Label(text="[color=33ff41]Заполните пустые ячейки, впишите в них ежемесячную сумму Вашего дохода и расходов:[/color]",markup=True)
        self.root = BoxLayout(orientation="vertical")
        self.root.add_widget(self.task)
        self.root.add_widget(self.textAndInput)
        return self.root

if __name__ == '__main__':
    MyApp().run()
