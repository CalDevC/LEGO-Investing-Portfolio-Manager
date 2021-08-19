import scraper
import file_mgr
import vars

def get_Prices():
    brickfolio = file_mgr.get_brickfolio()
    columns = brickfolio['data']
    headers = brickfolio['headers']

    for i, set_num in enumerate(columns['Set #']):
        url = "https://www.brickeconomy.com/search?query=" + str(set_num)
        set_info = scraper.get_values(url)
        columns['Current Val.'][i] = set_info['current value']
        columns['Retail Price'][i] = set_info['retail value'] #OPTIONAL if you want your retail values filled in
        print('...')

    file_mgr.set_brickfolio(columns, headers)