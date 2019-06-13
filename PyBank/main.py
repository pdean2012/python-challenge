# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("Resources", "PyBank_output.txt")

#Setting up count variables
rowcount = 0
currprofit=0
prevprofit=0
profitchange=0
greatestincrease=0
greatestdecrease=0
cumulativeprofit=0
cumulativeprofitchanges=0

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    for row in csvreader:
        
        #make currprofit = to profit in this row
        currprofit=row[1]
        #calculate change in profit from previous row
        #need the if stmt so that for the first month, it won't count the "zero to start" as a profit change
        if rowcount != 0:
            profitchange=int(currprofit)-int(prevprofit)
        #increase row count (number of months present)
        rowcount = int(rowcount)+1

        #increase cumulative profit change
        cumulativeprofitchanges=cumulativeprofitchanges+profitchange
        #increase total profit
        cumulativeprofit=int(cumulativeprofit)+int(currprofit)
        #record month
        month=row[0]
        #record new greatest increase, if applicable
        if profitchange > greatestincrease:
            greatestincrease = profitchange
            increasemonth=month
        #record new greatest decrase, if applicable
        if profitchange < greatestdecrease:
            greatestdecrease = profitchange
            decreasemonth=month
        #change prevprofit to be this row's profit (i.e., next row will use this row's profit as prevprofit)
        prevprofit = currprofit


    
    #calculating "averaged" change of each change
    avgchange=int(cumulativeprofitchanges/rowcount)

    #Print summary
    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months: {rowcount}")
    print(f"Total: ${cumulativeprofit}")
    print(f"Average change: ${avgchange}")
    print(f"Greatest increase in profits: {increasemonth} ${greatestincrease}")
    print(f"Greatest decrease in profits: {decreasemonth} ${greatestdecrease}")


# write to txt
File_object = open(txtpath,"r+")
File_object.write(
    "Financial Analysis" + '\n'
    "----------------------"+ '\n'
    f"Total Months: {rowcount}"+ '\n'
    f"Total: ${cumulativeprofit}"+ '\n'
    f"Average change: ${avgchange}"+ '\n'
    f"Greatest increase in profits: {increasemonth} ${greatestincrease}"+ '\n'
    f"Greatest decrease in profits: {decreasemonth} ${greatestdecrease}"
    )