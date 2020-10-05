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
average_Change = tot_profit/(row_count-1)

    # greatest increase in profits

    
    # print analysis
#output_path = os.path.join("Analysis", "PyBankR.txt")
#print("----------------------", file=txtfile)
print(f"Total Months: {row_count}")
    #print(f"Total Months: {row_count}", file=txtfile)
print(f"Total: ${profit}")
print(f"Average Change: $ {total_Change}")
    #print(f"Average Change: $ {total_Change}", file=txtfile)
print(f"Greatest Increase in Profits: ")
print(f"rijfneriugfnre")