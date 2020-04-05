#importing mods
import os 
import csv
#filepath
file_csv = os.path.join ( 'Resources',
                        'budget_data.csv') 
#storage
profit = []
totalMonths = []
monthlyChange = []
#format
with open (file_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    print(header[1])
#populating the lists
    for row in csvreader:
        profit.append(int(row[1]))
        totalMonths.append(row[0])
#calculates amnt change from month to month
    for i in range(len(profit)-1):
        monthlyChange.append(profit[i+1] - profit[i])
#getting the max and min for monthly change
max_monthly_change = max(monthlyChange)
min_monthly_change = min(monthlyChange)
#refrencing values index to store max and min month
max_Month_i = monthlyChange.index(max(monthlyChange)) + 1
max_Month_d = monthlyChange.index(min(monthlyChange)) + 1
#starting the print statements
print("Financial Analysis")
print("======================================")
print(f"Total Months: {len(totalMonths)}")
print(f"Total: ${sum(profit)}")
print(f"Average Monthly Change: ${round(sum(monthlyChange) / len(monthlyChange))}")
print(f"Max Increase: {(totalMonths)[max_Month_i]} ${(max_monthly_change)}")
print(f"Max Decrease: {(totalMonths)[max_Month_d]} ${(min_monthly_change)}")
#output the data to a text file
output = os.path.join('Resources','Finanicials.txt')
with open (output, 'w') as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("================================")
    file.write("\n")
    file.write(f"Total Months:{len(totalMonths)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(monthlyChange)/len(monthlyChange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits:{totalMonths[max_Month_i]} (${(str(max_monthly_change))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits:{totalMonths[max_Month_d]} (${(str(min_monthly_change))})")