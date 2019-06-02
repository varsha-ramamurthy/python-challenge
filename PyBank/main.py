import os
import csv
print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
budget_csv = os.path.join("..\PyBank","budget_data.csv")
#total number of months
with open(budget_csv, newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    hdr  = next(csvfile)
input_file = open("budget_data.csv","r+")
total_months=len(list(csv.reader(input_file)))
print(total_months)
#net profit/loss total
with open("budget_data.csv") as fin:
    headerline = fin.next()
    net_total=0
    for row in csv.reader(fin):
        net_total += int(row[1])
    print(net_total)