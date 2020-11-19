# pcost.py
#
# Exercise 1.27

# f = open('Data/portfolio.csv', 'rt')
import csv
import sys

def portfolio_cost(filename):

    try:
        f = open(filename, 'rt')
        rows = csv.reader(f)
        headers = next(rows)
        total = 0

        for row in rows:
            total += int(row[1]) * float(row[2])
        
        return total
    except ValueError:
        "Error message"

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

total = portfolio_cost(filename)
print('Total cost:',total)
