from helpers import create_menu
import dearpygui.dearpygui as dpg


with dpg.window(label="Calcúlos Hematimétricos", id="main_window"):
   create_menu(parent='main_window')
   dpg.add_text("Hello, world")


dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()