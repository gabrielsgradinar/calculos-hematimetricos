from dearpygui.core import *
from dearpygui.simple import *


def print_me(sender, data):
    log_debug(f"Menu Item: {sender}")


show_logger()

with window("Calcúlos Hematimétricos"):

    with menu_bar("Menu"):

        with menu("Calcúlos"):

            add_menu_item("VCM", callback=print_me)
            add_menu_item("HCM", callback=print_me)
            add_menu_item("CHCM", callback=print_me)

        with menu("Sobre"):

            add_menu_item("Objetivo", callback=print_me)
            add_menu_item("Quem somos", callback=print_me)
            add_menu_item("Referências", callback=print_me)

start_dearpygui()