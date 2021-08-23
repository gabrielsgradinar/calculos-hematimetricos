import dearpygui.dearpygui as dpg

class Window:

    def __init__(self, label):
        self._children = []
        dpg.set_staging_mode(True)
        self._id = dpg.add_window(label=label)
        dpg.set_staging_mode(False)

    def add_child(self, child):
        dpg.move_item(child._id, parent=self._id)

    def submit(self):
        dpg.unstage_items([self._id])