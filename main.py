import data_mgr
import console_ui
import file_mgr
import spreadsheet
import vars

ui = console_ui.console_ui()
data = data_mgr.data_mgr()
sheet_id = '0'

while(True):
    selection = ui.get_menu_selection()
    if selection.lower() in ['q', 'exit', 'quit', 'done', 'close']:
        exit()
    elif selection == '1':
        data.update_Prices()
    elif selection == '2':
        data.update_total_invested()
    elif selection == '3':
        new_tax_rate = input("Enter the tax rate for your region: ")
        file_mgr.update_var('TAX_RATE', new_tax_rate)
    elif selection == '4':
      spreadsheet = spreadsheet.Spreadsheet()
      spreadsheet.updateSheet("A1")
      spreadsheet.fetchSheet()
    else:
        print("\nInvlaid Selection\n")



