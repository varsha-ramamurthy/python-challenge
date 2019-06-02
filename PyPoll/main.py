import os
import csv
print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
election_csv = os.path.join("..\PyPoll","election_data.csv")
with open(election_csv, newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
# ignore the header
    hdr=next(csv_reader)

    total_votes=0
    candidates=[]
#compute total sumber of votes cast, and list of candidates
    for row in csv_reader:
        total_votes+=1
        candidates.append(row[2])

    unique_candidates=set(candidates)
    
#calculating candidate vote stats    