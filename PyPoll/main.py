#import necessary libraries

import os
import csv

#set navigational path
path = os.path.join('../Resources/election_data.csv')

#create lists/variables to store data
count = 0
vote_count = []
votes_for=[]
candidate_dict = {"Khan": 0, "O'Tooley":0,"Li" : 0, "Correy":0 }

#read in the csv
with open(path, newline='') as csvfile:
    #skip the header row when reading in file
    csvfile.readline()
    
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        #count each vote
        count = count + 1
        
        
        #fill list with votes for candidates
        votes_for.append(row[2])
               
        #need to isolate unique values in candidate list
        candidate = row[2]
        candidate_dict[candidate] = candidate_dict[candidate] + 1
        
        winner = max(candidate_dict, key=candidate_dict.get)

print("-------------------------")
print("Election Results")   
print("-------------------------")
print(f"Total Votes : {count}")    
print("-------------------------")
for key, value in candidate_dict.items():
    #calculate the percentage of votes for each candidate 
    percent = (value/count)* 100
    rounded_percent = round(percent, 2)
    print(f"{key}: {rounded_percent}%  ({value})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open('election_results.txt', 'w') as text:
    text.write(f'''
    -------------------------
    Election Results   
    -------------------------
    Total Votes : {count}  
    -------------------------
    ''')
    for key, value in candidate_dict.items():
        #calculate the percentage of votes for each candidate 
        percent = (value/count)* 100
        rounded_percent = round(percent, 2)
        text.write( f'''
        {key}: {rounded_percent}%  ({value})''')
    text.write(f'''
    -------------------------
    Winner: {winner}
    -------------------------''')
    