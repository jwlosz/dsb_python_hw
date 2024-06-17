import csv
csvpath = "resources/election_data.csv"

#variables
votes_count = 0
canadiate_dic = {}

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#tested to make sure csv is read in correctly - headers printed below

    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")

    #read each row of data after the headee
    for row in csvreader:
        votes_count = votes_count + 1

        #read to the dictionary
        row_canadiate = row[2]
        if row_canadiate in canadiate_dic.keys():
            canadiate_dic[row_canadiate] += 1
        else:
            canadiate_dic[row_canadiate] = 1


output = f"""Election Results
----------------------------
Total Votes: {votes_count}
----------------------------\n"""

max_can = ""
maxvote = 0

for candiate in canadiate_dic.keys():
    votes = canadiate_dic[candiate]
    percent = 100 * (votes / votes_count)

    line = f"{candiate}: {round(percent, 3)}% ({votes})\n"
    output += line

    if votes > maxvote:
        max_can = candiate
        maxvote = votes

last_line = f"""------------------
Winner: {max_can}
---------------------"""

output += last_line

with(open("PyPoll_output.txt", 'w') as f):
    f.write(output)

print(output)
