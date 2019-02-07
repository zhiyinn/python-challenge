
#import necessary libraries
import os
import csv
import statistics 

#create lists to store data
month_change= []
date=[]
profit=[]

#set variables intialized at 0 
month_count = 0 
profit_total=0
profit_change=0
initial_profit=0
total_change= 0

#set navigational path
path = os.path.join('../Resources/budget_data.csv')

#read in the csv
with open(path, newline='') as csvfile:
    #skip the header row (titles were causing errors in reading values in as integers)
    csvfile.readline()
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    for row in csvreader:
        #count number of months
        month_count = month_count + 1
        
        #fill list with dates
        date.append(row[0])
        
        #fill lists with profit values
        profit.append(row[1])
                  
        end_profit = int(row[1])
        #calculating profit change
        profit_change = end_profit - initial_profit
        
        #fill list with profit change values
        month_change.append(profit_change)    
       
        #reset value
        initial_profit = end_profit
        
        #calculating total profit, using list 
        #note: values must be read in as integers
        profit_total = profit_total + int(row[1])
        
        #reset value
        initial_profit = end_profit
        
        #calculating total change
        total_change = total_change + profit_change
        initial_profit = int(row[1])
        
        #data summary    
        greatest_inc = max(month_change)
        greatest_dcr = min(month_change)
        avg_change = round(total_change/month_count, 2)
        #avg_change2 = statistics.mean(month_change)
        
        
        #use change values to reference dates of greatest change 
        inc_date = date[month_change.index(greatest_inc)]
        dcr_date = date[month_change.index(greatest_dcr)]

#Output (Financial Analysis)        
print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months:{month_count}")
print(f"Total Profits: ${profit_total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {inc_date} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {dcr_date} (${greatest_dcr})")

#print(avg_change2)

#Export as a Text File 
with open('pybank.txt', 'w')as text: 
    text.write(f'''
    ----------------------------------------------------------
    Financial Analysis
    ----------------------------------------------------------
    Total Months:{month_count}
    Total Profits: ${profit_total}
    Average Change: ${avg_change}
    Greatest Increase in Profits: {inc_date} (${greatest_inc})
    Greatest Decrease in Profits: {dcr_date} (${greatest_dcr})
    '''
              )

