# PyBank Homework
# Your task is to create a Python script that analyzes the records to calculate 
# each of the following:
    # The total number of months included in the dataset [the count of rows]
    # The total amount of revenue gained over the entire period [the sum of Revenue column]
    # The average change in revenue between months over the entire period [sum / count]
    # The greatest increase in revenue (date and amount) over the entire period [If conditional, both Keys]
    # The greatest decrease in revenue (date and amount) over the entire period [If conditional, both Keys]

import os
import csv
import datetime

csvpath = ("raw_data/budget_data_1.csv")

totalMonths = 0		# a variableis a dynamic state object
totalRevenue = 0
prevRevenue = 0		# create a variable to track steps in the revenue loop
revChange = 0		# create a variable to store change in rev from one cell to next
revChangeList = []  # create a list to evaluate revenue changes over time
greatestInc = 0		# a variable to hold the highest positive change in revenue
greatestDec = 0		# a variable to hold the highest negative change in revenue
monthInc = 0		# a variable to hold the month with highest increase in revenue
monthDec = 0		# a variable to hold the month with highest decrease in revenue

with open(csvpath, newline = "") as csvfile:
    statsDict = csv.DictReader(csvfile, delimiter = ',')

    for row in statsDict:
        totalMonths = totalMonths + 1
        totalRevenue = totalRevenue + int(row["Revenue"])
        revChange = int(row["Revenue"]) - prevRevenue  # create a variable to track revenue change
        prevRevenue = int(row["Revenue"])
        revChangeList.append(revChange)    # add each revChange increment to the list

        if revChange > greatestInc:		# set conditional to test for an increase in Revenue
            greatestInc = revChange   	# for each higher change in Revenue, update greatestInc
            monthInc = row["Date"]		# pair the highest Revenue change with its Date
            
        if revChange < greatestDec:		# do the same but for greatest decrease in Revenue 
            greatestDec = revChange
            monthDec = row["Date"]

revAverage = sum(revChangeList) / len(revChangeList)   # evaluate the averge revenue change sum/number 

print("The average change in revenue between months is " + "$" + str(round(revAverage,2)))
print("The total number of months included in this dataset is " + str(totalMonths))
print("Total revenue is " + "$" + str(totalRevenue))			
print("The greteast increase in revenue was " + "$" + str(greatestInc) + " " + "in " + str(monthInc))
print("The greteast decrease in revenue was " + "$" + str(greatestDec) + " " + "in " + str(monthDec))
