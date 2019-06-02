import os
import csv
print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
budget_csv = os.path.join("..\PyBank","budget_data.csv")

with open(budget_csv, newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
    # ignore the header
    hdr=next(csv_reader)

    total_months = 0
    net_total = 0
    net_average=0
    total_net_change = 0
    greatest_increase=0
    greatest_decrease=0
    profit_loss_change=0
    greatest_increase_month=""
    greatest_decrease_month=""
    for row in csv_reader:
        #increment total months, net_total 
        total_months += 1
        net_total += int(row[1])
        # Computations for average change in Profit/Loss
        if total_months != 1 :
            profit_loss_change=int(row[1]) - prev_net
            total_net_change += profit_loss_change
            if(profit_loss_change>greatest_increase):
                greatest_increase=profit_loss_change
                greatest_increase_month=str(row[0])
            if(profit_loss_change<greatest_decrease):
                greatest_decrease=profit_loss_change
                greatest_decrease_month=str(row[0])
        prev_net = int(row[1])
    #calculate average change in profit/loss rounded to 2 decimal places
    net_average=round(total_net_change/(total_months-1),2)    
print("Financial Analysis")
print("-------------------------------------------")
print(f"Total Months:" + str(total_months))
print(f"Total:" + str(net_total))
print(f"Average Change: $"+ str(net_average))
print(f"Greatest Increase in Profits: $" + str(greatest_increase) + " in" + greatest_increase_month)
print(f"Greatest Decrease in Profits: $" + str(greatest_decrease) + " in" + greatest_decrease_month)



