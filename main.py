import data_mgr
import console_ui
import file_mgr
import spreadsheet
import vars

ui = console_ui.console_ui()
data = data_mgr.data_mgr()

while (True):
    # Load saved spreadsheet
    current_sheet = spreadsheet.Spreadsheet(sheet=vars.CURRENT_SPREADSHEET)

    # Get user selection
    selection = ui.get_menu_selection()

    # Interpret input
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
        current_sheet = spreadsheet.Spreadsheet()
        current_sheet.updateSheet("A1")
    elif selection == '5':
        current_sheet.fetchSheet()
        # data.update_Prices()
        current_sheet.updateSheet('A3')
    else:
        print("\nInvlaid Selection\n")
