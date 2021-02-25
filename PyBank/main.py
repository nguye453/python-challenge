#imports
import csv
import os

#set path
csvpath = os.path.join("Resources", "budget_data.csv")

#variables
total_months = 0
total_amount = 0.00
average_change = 0
greatest_increase_date = ""
greatest_increase = 0.00
greatest_decrease_date = ""
greatest_decrease = 0.00

#read csv
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #read out header line
    csv_header = next(csvreader)
    #read data
    for row in csvreader:
        total_months += 1
        total_amount += float(row[1])
        average_change = total_amount / total_months
        if float(row[1]) > greatest_increase:
            greatest_increase = float(row[1])
            greatest_increase_date = row[0]
        elif float(row[1]) < greatest_decrease:
            greatest_decrease = float(row[1])
            greatest_decrease_date = row[0]
    print("''text")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_amount}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} {greatest_increase}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} {greatest_decrease}")
    print("'''")

#open/create output file
f= open("analysis/output_PyBank.txt","w+")

#write data to file
f.write("'''text\n")
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(f"Total Months: {total_months}\n")
f.write(f"Total: {total_amount}\n")
f.write(f"Average Change: {average_change}\n")
f.write(f"Greatest Increase in Profits: {greatest_increase_date} {greatest_increase}\n")
f.write(f"Greatest Decrease in Profits: {greatest_decrease_date} {greatest_decrease}\n")
f.write("'''")