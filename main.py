import tkinter as tk
from pages import VCM, HCM, MainPage


pages = (MainPage, VCM, HCM)


class MainApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        tk.Tk.__init__(self, *args, **kwargs)
         
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        self.frames = {} 
  
        for page in pages:
  
            frame = page(container, self)
  
            self.frames[page] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(MainPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
  
# Driver Code
app = MainApp()
app.title("Calculos Hematimétricos")

app.mainloop()