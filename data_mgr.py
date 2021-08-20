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
    
    def update_Prices(self):
        self.get_current_data()

        for i, set_num in enumerate(self.columns['Set #']):
            print(f'...updating set #{set_num}')
            url = "https://www.brickeconomy.com/search?query=" + str(set_num)
            set_info = scraper.get_values(url)
            self.columns['Current Val.'][i] = set_info['current value']
            self.columns['Retail Price'][i] = set_info['retail value'] #OPTIONAL if you want your retail values filled in
            if self.columns['Current Val.'][i] == 'Available at retail':
                self.columns['Highest Val.'][i] = set_info['retail value']
            else:
                self.columns['Highest Val.'][i] = max(self.columns['Highest Val.'][i], self.columns['Current Val.'][i])

        file_mgr.set_brickfolio(self.columns, self.headers)

    def update_total_invested(self):
        self.get_current_data()
        sum = 0

        for i, row in enumerate(self.columns['Set #']):
            purchase_price = float(self.columns['Purchase Price'][i].strip('$'))
            quantity = float(self.columns['Qty.'][i])

            self.columns['Total Invested'][i] = purchase_price * quantity * vars.TAX_RATE
            sum += self.columns['Total Invested'][i]

        self.columns['Current Invested'][0] = sum
        file_mgr.set_brickfolio(self.columns, self.headers)
