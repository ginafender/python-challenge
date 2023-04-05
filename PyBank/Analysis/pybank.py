# import csv file
import os
import csv

files = "C:/Users/ginav/Desktop/Analysis Projects/Class Activity Files/Module 3/python-challenge/PyBank/Resources/budget_data.csv"
with open(files) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# check if file is working
    # numlines = 5
    # for i in range(numlines):
        # line = next(csvreader)
        # print(line)

    # add variables outside the for loop
    months = 0
    nettotals = 0
    avgchg = 0
    change = 0
    currmonth = 0
    prevmonth = 0 
    totalchange = 0
    greatInc = 0
    greatDec = 0
    # calculate total number of months, and total net profit/loss
    for row in csvreader:
        months += 1
        currmonth = int(row[1])
        nettotals += currmonth
        # calculate change and average change by comparing current month to previous month
        if prevmonth == 0:
            prevmonth = currmonth
        else:
            change = currmonth - prevmonth
            prevmonth = currmonth
            totalchange = totalchange + change
            avgchg = (round(totalchange / 85, 2))
            # calculate the greatest increase and the greatest decrease 
            # by comparing it to the current change
            if change > greatInc:
                greatInc = change
                incMonth = row[0]
            if change < greatDec:
                greatDec = change
                decMonth = row[0]

    # print all statements
    output = ("Financial Analysis \n")
    output = output + ("------------------------------ \n")
    output = output + (f"Total months: {months} \n") 
    output = output + (f"Total: ${nettotals} \n") 
    output = output + (f"Average change: ${avgchg} \n") 
    output = output + (f"Greatest Increase in Profits: {incMonth} ($ {greatInc}) \n") 
    output = output + (f"Greatest Decrease in Profits: {decMonth} ($ {greatDec}) \n")

    #print to terminal
    print(output)
    
    #export to txt file
    file_to_output = os.path.join("budget_analysis.txt")
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)