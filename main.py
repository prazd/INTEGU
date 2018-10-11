#! /usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
# from kivy.graphics.vertex_instructions_line import height
from kivy.core.window import Window
Window.clearcolor = (166, 237, 181, 1)


class EconomyApp(App):

    def Clear(self, instance):
        self.inpOne.text = ""
        self.inpTwo.text = ""
        self.inpThree.text = ""
        self.inpFour.text =  ""
    
    def Run(self, instance):
        pass

    def build(self):
        ####################################
        # For up panel 
        self.Up = BoxLayout()
        self.info = Label(text="[color=ff3333]Привет всем!!!\nВ этой программе надо заполнить поля и типо всякая хрень[/color]",markup=True)
        self.Up.add_widget(self.info)

        # For left panel
        #################################
        self.Left = BoxLayout(orientation='vertical')
        
        self.One = Label(text="[color=ff3333]Введите то[/color]",markup=True)
        self.Two = Label(text="[color=33ff41]Введите сё[/color]",markup=True)
        self.Three = Label(text="[color=ff33e2]Введите это[/color]",markup=True)
        self.Four = Label(text="[color=33a8ff]Введите [/color]",markup=True)

        self.Left.add_widget(self.One)
        self.Left.add_widget(self.Two)
        self.Left.add_widget(self.Three)
        self.Left.add_widget(self.Four)

        ###################################
        # For inputs
        self.inpWidget = BoxLayout(orientation='vertical')

        # custom size
        
        # self.inpOne = TextInput(size_hint=(.3, None),height=30,multiline=False)
        # self.inpTwo = TextInput(size_hint=(.3, None),height=30,multiline=False)
        # self.inpThree = TextInput(size_hint=(.3, None),height=30,multiline=False)
        # self.inpFour = TextInput(size_hint=(.3, None),height=30,multiline=False)

        self.inpOne = TextInput()
        self.inpTwo = TextInput()
        self.inpThree = TextInput()
        self.inpFour = TextInput()


        self.inpWidget.add_widget(self.inpOne)
        self.inpWidget.add_widget(self.inpTwo)
        self.inpWidget.add_widget(self.inpThree)
        self.inpWidget.add_widget(self.inpFour)

        ####################################
        # For center
        self.Center = BoxLayout()
        self.Center.add_widget(self.Left)
        self.Center.add_widget(self.inpWidget)
        

        ###################################
        # For button widget
        self.run = Button(text='Расчитать',
                            on_press=partial(self.Run),background_color= (1,0,1,1))

        self.reset = Button(text='Сбросить',
                            on_press=partial(self.Clear),background_color= (1,0,0,1))

        self.layout = BoxLayout(size_hint=(1, None), height=50)
        self.layout.add_widget(self.run)
        self.layout.add_widget(self.reset)

        ###################################
        # root 
        root = BoxLayout(orientation='vertical')
        root.add_widget(self.Up)
        root.add_widget(self.Center)
        root.add_widget(self.layout)

        return root


if __name__ == '__main__':
    EconomyApp().run()