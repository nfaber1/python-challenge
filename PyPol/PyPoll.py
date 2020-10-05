import os
import csv

# create csv path
csvpath = ('election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvfile)

    # skip header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    row_count1 = 0 
    candidate = ""

    for row in csvreader:
        row_count1 += 1
    csvfile.seek(0)
    next(csvreader)

    def print_percentages(election_data):
        voter_ID = int(election_data[0])
        county = str(election_data[1])
        candidate = str(election_data[2])

    for row in csvreader:
        if candidate == "Khan":
            

    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    #khan_percent = (khan_win / row_count1) * 100

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    #loss_percent = (losses / total_matches) * 100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    #draw_percent = (draws / total_matches) * 100


    #print("Election Results")
    #print(f"--------------------")
    #print(f"Total Votes = {row_count1}")
    #print(f"--------------------")
    #print(f"Khan: %")
    #print(f"Correy: %")
    #print(f"Li: %")
    #print(f"O'Tooley: %")