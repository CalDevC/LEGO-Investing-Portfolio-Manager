import csv
from collections import defaultdict
import vars

def get_brickfolio():
    columns = defaultdict(list)

    with open("Brickfolio.csv", "r") as FILE:
        reader = csv.reader(FILE, delimiter=',')
        headers = next(reader)
        column_nums = range(len(headers))
        for row in reader:
            for i in column_nums:
                columns[headers[i]].append(row[i])
    return {'data': columns, 'headers': headers}

def set_brickfolio(columns, headers):
    with open("Brickfolio.csv", "w", newline="") as FILE:
        row_list = []

        writer = csv.writer(FILE, lineterminator='\n')
        FILE.seek(0)
        writer.writerow(headers)
        for i in range(len(columns[headers[0]])):
            for header in headers:
                row_list.append(columns[header][i])
            writer.writerow(row_list)
            row_list = []
