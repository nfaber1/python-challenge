import os
import csv

# create csv path
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvfile)

    # skip header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # variables
    totalmonths = 0
    row_count = 0
    net_profitloss = 0
    tot_profit = 0
    profit = 0
    tot_loss = 0
    prev_PL = 0
    current_PL = 0
    tot_months = 0
    finPL = ""
    recent_Change = 0
    total_Change = 0
    greatest_Profit = 0
    greatest_Profit_Mon = 0
    greatest_Loss = 0
    greates_Loss_Mon = 0

    # row count
    for row in csvreader:
        row_count += 1
    csvfile.seek(0)
    next(csvreader)

    # net total P/L
    for row in csvreader:
        profit += int(row[1])
        if tot_months > 1:
           prev_PL - int(row[1])
        else:
           current_PL - int(row[1]) - prev_PL
    # average change in profits / losses
    for row in csvreader:
        if tot_months == 1:
            finPL = int(row[1])
        else:
            recent_Change =int(row[1]) - finPL
            total_Change += recent_Change
            finPL = int(row[1])
    row_count += 1

    # greatest increase in profits
    if recent_Change > greatest_Profit:
        greatest_Profit - recent_Change
        greatest_Profit_Mon = str(row[0])
    elif recent_Change < greatest_Loss:
        greatest_Loss - recent_Change
        greates_Loss_Mon = str(row[0])
average_Change = tot_profit/(row_count-1)
    # print analysis
print("----------------------")
print(f"Total Months: {row_count}")
print(f"Total: ${profit}")
print(f"Average Change: {total_Change} %")
print(f"Greatest Increase in Profits: {greatest_Profit_Mon} ${greatest_Profit}")
print(f"Greatest Loss in Profits: {greates_Loss_Mon} ${greatest_Loss}")