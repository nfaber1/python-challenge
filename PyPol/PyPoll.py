import os
import csv

# create csv path
csvpath = os.path.join('.', 'Resources','election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvfile)

    # skip header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    row_count1 = 0 
    candidate = ""
    khan_percent = 0
    khan_count = 0
    correy_count = 0
    correy_percent = 0
    li_percent = 0
    li_count = 0
    OTooley_percent = 0
    OTooley_count = 0

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
            for row in csvreader == "Khan":
               khan_count += 1
            csvfile.seek(0)
            next(csvreader)
    khan_percent = (khan_count / 3521001) * 100

    for row in csvreader:
        if candidate == "Correy":
            for row in csvreader == "Correy":
               correy_count += 1
            csvfile.seek(0)
            next(csvreader)
    correy_percent = (correy_count / 3521001) * 100

    for row in csvreader:
        if candidate == "Li":
            for row in csvreader == "Li":
               li_count += 1
            csvfile.seek(0)
            next(csvreader)
    li_percent = (li_count / 3521001) * 100

    for row in csvreader:
        if candidate == "O'Tooley":
            for row in csvreader == "O'Tooley":
               OTooley_count += 1
            csvfile.seek(0)
            next(csvreader)
    OTooley_percent = (OTooley_count / 3521001) * 100

    print("Election Results")
    print(f"--------------------")  
    print(f"Total Votes = {row_count1}")
    print(f"--------------------")
    print(f"Khan: {khan_percent}%")
    print(f"Correy: {correy_percent}%")
    print(f"Li: {li_percent}%")
    print(f"O'Tooley: {OTooley_percent}%")