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
            command = lambda : controller.show_frame(VCM)
        )

        hcm = ttk.Button(
            self, 
            text ="HCM",
            command = lambda : controller.show_frame(HCM)
        )

        chcm = ttk.Button(
            self, 
            text ="CHCM",
            command = lambda : controller.show_frame(HCM)
        )

        objetivo = ttk.Button(
            self, 
            text ="Objetivo",
            command = lambda : controller.show_frame(HCM)
        )

        quem_somos = ttk.Button(
            self, 
            text ="Quem somoss",
            command = lambda : controller.show_frame(HCM)
        )

        referencias = ttk.Button(
            self, 
            text ="Referências",
            command = lambda : controller.show_frame(HCM)
        )


        logo.grid(row = 0, column = 0, columnspan=3, padx = 10, pady = 10)
        oq_sao_indices.grid(row = 1, column = 0, columnspan=3, padx = 10, pady = 10)

        vcm.grid(row = 2, column = 0, padx = 10, pady = 10)
        hcm.grid(row = 2, column = 1, padx = 10, pady = 10)
        chcm.grid(row = 2, column = 2, padx = 10, pady = 10)

        objetivo.grid(row = 3, column = 0, padx = 10, pady = 10)
        quem_somos.grid(row = 3, column = 1, padx = 10, pady = 10)
        referencias.grid(row = 3, column = 2, padx = 10, pady = 10)


class VCM(tk.LabelFrame):
     
    def __init__(self, parent, controller):
         
        tk.LabelFrame.__init__(self, parent, text="VCM")


        label = ttk.Label(self, text ="Dados explicativos sobre o VCM", font = LARGEFONT)
        atalhos = ttk.Label(self, text ="Textos asdasdasdasdad", font = LARGEFONT)

        button1 = ttk.Button(
            self, 
            text ="Menu Principal",
            command = lambda : controller.show_frame(MainPage)
        )
     
        button2 = ttk.Button(
            self, 
            text ="Page 2",
            command = lambda : controller.show_frame(HCM)
        )

        label.grid(row = 0, column = 0, columnspan=3, rowspan=4, padx = 10, pady = 10)
        atalhos.grid(row = 0, column = 4, padx = 10, rowspan=3, pady = 10)
        button1.grid(row = 5, column = 0, padx = 10, pady = 10)
        button2.grid(row = 6, column = 0, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class HCM(tk.LabelFrame):
    def __init__(self, parent, controller):
        tk.LabelFrame.__init__(self, parent, text='HCM')
        label = ttk.Label(self, text ="HCM", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="VCM",
                            command = lambda : controller.show_frame(VCM))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Menu Principal",
                            command = lambda : controller.show_frame(MainPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)