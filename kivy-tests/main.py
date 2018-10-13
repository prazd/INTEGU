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
from kivy.uix.gridlayout import GridLayout
# from kivy.graphics.vertex_instructions_line import height
from kivy.core.window import Window
# Window.clearcolor = (166, 237, 181, 1)


class EconomyApp(App):

    def Clear(self, instance):
        self.inpMonthIncome.text = ""
        self.inpWage.text = ""
        self.inpParrentWage.text = ""
        self.inpRent.text = ""
        self.inpAllowance.text = ""
        self.inpCashback.text = ""
        self.inpSaving.text = ""
        self.inpOtherIncome.text = ""
        self.inpMonthExpense.text = ""
        self.inpUtilities.text = ""
        self.inpRentalOfProperty.text = ""
        self.inpLoyalPayment.text = ""
        self.inpEducation.text = ""
        self.inpHealthCare.text = ""
        self.inpNutrion.text = ""
        self.inpClothes.text = ""
        self.inpHousewares.text = ""
        self.inpComm.text = ""
        self.inpPassage.text = ""
        self.inpFines.text = ""
        self.inpOtherExpense.text = ""
    
    def Run(self, instance):
        pass

    def build(self):
        ####################################
        # For up panel 
        self.up = FloatLayout()
        self.info = Label(text="[color=ff3333]Заполните пустые ячейки, впишите в них ежемесячную сумму Вашего дохода и расходов:[/color]",markup=True)
        self.up.add_widget(self.info)

        # For left panel
        #################################
        self.Left = BoxLayout(orientation='vertical')
        # self.intro = Label(text="[color=ff3333]Заполните пустые ячейки, впишите в них ежемесячную сумму Вашего дохода и расходов:[/color]",markup=True)
        self.monthIncome = Label(text=" - Ваш ежемесячный доход:")
        self.wage = Label(text="[color=ff3333]Заработная плата:[/color]",markup=True)
        self.parrentWage = Label(text="[color=33ff41]Если Вы не работаете, укажите ту часть заработной платы родителей,\n которая покрывает лично Ваши расходы[/color]",markup=True)
        self.rent = Label(text="[color=ff33e2]Доход от аренды[/color]",markup=True)
        self.allowance = Label(text="[color=33a8ff]Пособие или иная социальная выплата[/color]",markup=True)
        self.cashback = Label(text="[color=33a8ff]Пассивный доход (кешбэк с операций с кредитными картами,\n продажа в Интернет товаров собственного производства, блогинг и др.)[/color]",markup=True)
        self.saving = Label(text="Сбережения")
        self.otherIncome = Label(text="Иной источник дохода")
        #######################################
        self.monthExpense = Label(text="- Ваши ежемесячные расходы:")
        self.utilities = Label(text="Коммунальные услуги")
        self.rentalOfProperty = Label(text="Аренда Жилья")
        self.loalRepayment = Label(text="Погашение кредита")
        self.education = Label(text="Образование")
        self.healthCare = Label(text="Здравоохранение")
        self.nutrition = Label(text="Питание")
        self.clothes = Label(text="Одежда")
        self.housewares = Label(text="Предметы домашнего обихода")
        self.comm = Label(text="Интернет, телефон")
        self.passage = Label(text="Проезд")
        self.fines = Label(text="Штрафы")
        self.otherExpense = Label(text="Иные расходы")
        ########################################

        # Add all of labels
        self.Left.add_widget(self.monthIncome)
        self.Left.add_widget(self.wage)
        self.Left.add_widget(self.parrentWage)
        self.Left.add_widget(self.rent)
        self.Left.add_widget(self.allowance)
        self.Left.add_widget(self.cashback)
        self.Left.add_widget(self.saving)
        self.Left.add_widget(self.otherIncome)
        self.Left.add_widget(self.monthExpense)
        self.Left.add_widget(self.utilities)
        self.Left.add_widget(self.rentalOfProperty)
        self.Left.add_widget(self.loalRepayment)
        self.Left.add_widget(self.education)
        self.Left.add_widget(self.healthCare)
        self.Left.add_widget(self.nutrition)
        self.Left.add_widget(self.clothes)
        self.Left.add_widget(self.housewares)
        self.Left.add_widget(self.comm)
        self.Left.add_widget(self.passage)
        self.Left.add_widget(self.fines)
        self.Left.add_widget(self.otherExpense)
        ###################################
        # For inputs
        self.inpWidget = BoxLayout(orientation='vertical')

        # custom size
        
        # self.inpOne = TextInput(size_hint=(.3, None),height=30,multiline=False)
        # self.inpTwo = TextInput(size_hint=(.3, None),height=30,multiline=False)
        # self.inpThree = TextInput(size_hint=(.3, None),height=30,multiline=False)
        # self.inpFour = TextInput(size_hint=(.3, None),height=30,multiline=False)

        self.inpMonthIncome = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpWage = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpParrentWage = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpRent = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpAllowance = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpCashback = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpSaving = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpOtherIncome = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpMonthExpense = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpUtilities = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpRentalOfProperty = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpLoyalPayment = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpEducation = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpHealthCare = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpNutrion = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpClothes = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpHousewares = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpComm = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpPassage = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpFines = TextInput(size_hint=(.3, None),height=30,multiline=False)
        self.inpOtherExpense = TextInput(size_hint=(.3, None),height=30,multiline=False)

        # Add
        self.inpWidget.add_widget(self.inpMonthIncome)
        self.inpWidget.add_widget(self.inpWage)
        self.inpWidget.add_widget(self.inpParrentWage)
        self.inpWidget.add_widget(self.inpRent)
        self.inpWidget.add_widget(self.inpAllowance)
        self.inpWidget.add_widget(self.inpCashback)
        self.inpWidget.add_widget(self.inpSaving)
        self.inpWidget.add_widget(self.inpOtherIncome)
        self.inpWidget.add_widget(self.inpUtilities)
        self.inpWidget.add_widget(self.inpRentalOfProperty)
        self.inpWidget.add_widget(self.inpLoyalPayment)
        self.inpWidget.add_widget(self.inpEducation)
        self.inpWidget.add_widget(self.inpHealthCare)
        self.inpWidget.add_widget(self.inpNutrion)
        self.inpWidget.add_widget(self.inpClothes)
        self.inpWidget.add_widget(self.inpHousewares)
        self.inpWidget.add_widget(self.inpComm)
        self.inpWidget.add_widget(self.inpPassage)
        self.inpWidget.add_widget(self.inpFines)
        self.inpWidget.add_widget(self.inpOtherExpense)
        

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
        # root.add_widget(self.up)
        root.add_widget(self.Center)
        root.add_widget(self.layout)

        return root


if __name__ == '__main__':
    EconomyApp().run()