import scraper
import file_mgr
from collections import defaultdict
import vars

class data_mgr:
    
    def __init__(self):
        self.columns = defaultdict(list)
        self.headers = []

    def get_current_data(self):
        brickfolio = file_mgr.get_brickfolio()
        self.columns = brickfolio['data']
        self.headers = brickfolio['headers']
    
    def get_Prices(self):
        self.get_current_data()

        for i, set_num in enumerate(self.columns['Set #']):
            url = "https://www.brickeconomy.com/search?query=" + str(set_num)
            set_info = scraper.get_values(url)
            self.columns['Current Val.'][i] = set_info['current value']
            self.columns['Retail Price'][i] = set_info['retail value'] #OPTIONAL if you want your retail values filled in
            print('...')

        file_mgr.set_brickfolio(self.columns, self.headers)

    def update_total_invested(self):
        self.get_current_data()

        for i, set_num in enumerate(self.columns['Set #']):
            purchase_price = float(self.columns['Purchase Price'][i].strip('$'))
            quantity = float(self.columns['Qty.'][i])

            self.columns['Total Invested'][i] = purchase_price * quantity * vars.TAX_RATE

        file_mgr.set_brickfolio(self.columns, self.headers)
