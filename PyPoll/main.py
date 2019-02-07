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
        #create output as set instead of list
        candidates = set()
        for x in votes_for:
            candidates.add(x)
#             #count number of votes for each candidate
#             [num_votes= votes_for.count(x)]<--this line appears to be problematic
#             #put number of votes in a list
#             vote_count.append(num_votes)
            
#             #calculate the percentage of votes for each candidate 
#             percent = (num_votes/count) * 100