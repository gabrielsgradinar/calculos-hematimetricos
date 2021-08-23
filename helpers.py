from classes import Window
import dearpygui.dearpygui as dpg



def create_new_windows(sender, app_data, user_data):
    other_windows = ["VCM", "HCM", "CHCM", "Objetivo", "Quem somos", "Referências"]

    dpg.hide_item("main_window")

    other_windows.remove(user_data)

    print(other_windows)

    for w in other_windows:
        if dpg.does_item_exist(w):
            dpg.delete_item(w)
    
    new_window = Window(user_data)
    new_window.submit()

    create_menu(parent=new_window._id)

    dpg.set_primary_window(new_window._id, True)


def create_menu(parent):
     with dpg.menu_bar(parent=parent):

        with dpg.menu(label="Calcúlos"):

            dpg.add_menu_item(label="VCM", callback=create_new_windows, user_data="VCM")
            dpg.add_menu_item(label="HCM", callback=create_new_windows, user_data="HCM")
            dpg.add_menu_item(label="CHCM", callback=create_new_windows, user_data="CHCM")


        with dpg.menu(label="Sobre"):

            dpg.add_menu_item(label="Objetivo", callback=create_new_windows, user_data="Objetivo")
            dpg.add_menu_item(label="Quem somos", callback=create_new_windows, user_data="Quem somos")
            dpg.add_menu_item(label="Referências", callback=create_new_windows, user_data="Referências")




