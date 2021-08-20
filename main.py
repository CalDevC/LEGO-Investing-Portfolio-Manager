import data_mgr
import console_ui
import file_mgr
import vars

ui = console_ui.console_ui()
data = data_mgr.data_mgr()

while(True):
    selection = ui.get_menu_selection()
    if selection.lower() in ['q', 'exit', 'quit', 'done', 'close']:
        exit()
    if selection == '1':
        data.get_Prices()
    if selection == '2':
        new_tax_rate = input("Enter the tax rate for your region: ")
        file_mgr.update_var('TAX_RATE', new_tax_rate)




