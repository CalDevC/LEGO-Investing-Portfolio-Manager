"""
This file holds supporting functions for main.py and scraper.py
"""


def get_dollar_amt(line):
    if (index := line.find('$')) != -1:
        line_start = line[index + 1:]
        return line_start.replace(",", "")
    else:
        return "Not a dollar amount"
