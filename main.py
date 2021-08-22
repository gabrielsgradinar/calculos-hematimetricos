import dearpygui.dearpygui as dpg


def print_me(sender, data):
    print(f"Menu Item: {sender}")

with dpg.window(label="Calcúlos Hematimétricos", id="main_window"):

    with dpg.menu_bar():

        with dpg.menu(label="Calcúlos"):

            dpg.add_menu_item(label="VCM", callback=print_me)
            dpg.add_menu_item(label="HCM", callback=print_me)
            dpg.add_menu_item(label="CHCM", callback=print_me)

        with dpg.menu(label="Sobre"):

            dpg.add_menu_item(label="Objetivo", callback=print_me)
            dpg.add_menu_item(label="Quem somos", callback=print_me)
            dpg.add_menu_item(label="Referências", callback=print_me)


dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()