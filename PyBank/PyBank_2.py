import os
import csv

csvpath = 'budget_data.csv'

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvfile)
 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    totalmonths = 0
    totalrev=0

    for row in csvfile:
        totalmonths += 1
        totalrev += int(row[1])