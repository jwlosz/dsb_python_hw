# read in the CSV and loop through it

import csv
csvpath = "resources/budget_data.csv"

#variables
month_count = 0
total_profit = 0

#variables for changes 
last_month_profit = 0 
changes = []
month_change = []

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header=next(csvreader)
    #print(f"CSV Header: {csv_header}")
    #read each row of data after the header
    for row in csvreader:
        #counting months
        month_count = month_count + 1
         #add profit 
        total_profit = total_profit + int(row[1])

    #calculate changes - last month profit & this month profit
    #subtrack this month profit from last month profit
    #APPEND the change to the list

    #will need to address first row of changes - there is no change
        if (month_count == 1):
        #first row - nothing for changes
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_change.append(row[0])


        #reset for last months profit
        last_month_profit = int(row[1])


avg_change = sum(changes) / len(changes)

max_change = max(changes)
max_month_idx = changes.index(max_change)
max_month = month_change[max_month_idx]

min_change = min(changes)
min_month_idx = changes.index(min_change)
min_month = month_change[min_month_idx]

output = f"""Financial Analysis
----------------------------
Total Months: {month_count}
Total: ${total_profit}
Average Change: ${round(avg_change,2)}
Greatest increase in profits: {max_month} (${max_change})
Greatest decrease in profits: {min_month} (${max_change})"""

print(output)

with(open("Pybank_output.txt", 'w') as f):
    f.write(output)
