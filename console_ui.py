import os

class console_ui:
    __menu = """
             ===== Main Menu =====

             1 - Get current values
             2 - Update total invested
             3 - Set tax rate
             4 - Make into Google Sheet
             q - Quit
             """

    def __init__(self):
        pass

    def get_menu_selection(self):
        print(self.__menu)
        selection = input("Choose a menu option: ")
        return selection