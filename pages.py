from helpers import LARGEFONT
import tkinter as tk
from tkinter import ttk
  
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        logo = ttk.Label(self, text ="Logotipo", font = LARGEFONT)

        oq_sao_indices = ttk.Label(
            self, 
            text ="O que são os índices hematimétricos", 
            font = LARGEFONT
        )

        vcm = ttk.Button(
            self, 
            text ="VCM",
            command = lambda : controller.show_frame(Page1)
        )

        hcm = ttk.Button(
            self, 
            text ="HCM",
            command = lambda : controller.show_frame(Page2)
        )

        chcm = ttk.Button(
            self, 
            text ="CHCM",
            command = lambda : controller.show_frame(Page2)
        )

        objetivo = ttk.Button(
            self, 
            text ="Objetivo",
            command = lambda : controller.show_frame(Page2)
        )

        quem_somos = ttk.Button(
            self, 
            text ="Quem somoss",
            command = lambda : controller.show_frame(Page2)
        )

        referencias = ttk.Button(
            self, 
            text ="Referências",
            command = lambda : controller.show_frame(Page2)
        )


        logo.grid(row = 0, column = 0, columnspan=3, padx = 10, pady = 10)
        oq_sao_indices.grid(row = 1, column = 0, columnspan=3, padx = 10, pady = 10)

        vcm.grid(row = 2, column = 0, padx = 10, pady = 10)
        hcm.grid(row = 2, column = 1, padx = 10, pady = 10)
        chcm.grid(row = 2, column = 2, padx = 10, pady = 10)

        objetivo.grid(row = 3, column = 0, padx = 10, pady = 10)
        quem_somos.grid(row = 3, column = 1, padx = 10, pady = 10)
        referencias.grid(row = 3, column = 2, padx = 10, pady = 10)
  
          
  
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(MainPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(MainPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)