import dearpygui.dearpygui as dpg


# def print_me(sender, data):
#     print(f"Menu Item: {sender}")

# with dpg.window(label="Calcúlos Hematimétricos", id="main_window"):

#     with dpg.menu_bar():

#         with dpg.menu(label="Calcúlos"):

#             dpg.add_menu_item(label="VCM", callback=print_me)
#             dpg.add_menu_item(label="HCM", callback=print_me)
#             dpg.add_menu_item(label="CHCM", callback=print_me)

#         with dpg.menu(label="Sobre"):

#             dpg.add_menu_item(label="Objetivo", callback=print_me)
#             dpg.add_menu_item(label="Quem somos", callback=print_me)
#             dpg.add_menu_item(label="Referências", callback=print_me)


# dpg.set_primary_window("main_window", True)
# dpg.start_dearpygui()


import dearpygui.dearpygui as dpg

with dpg.window(label="Tutorial"):

    with dpg.table(header_row=False):

        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()

        for i in range(0, 4):
            with dpg.table_row():
                for j in range(0, 3):
                    dpg.add_text(f"Row{i} Column{j}")

dpg.start_dearpygui()