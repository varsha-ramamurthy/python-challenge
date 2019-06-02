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
    votes_khan=0
    votes_correy=0
    votes_otooley=0
    votes_li=0
    percent_khan=0
    percent_correy=0
    percent_otooley=0
    percent_li=0
    most_votes=0
    winner=""
#compute total sumber of votes cast, and list of candidates
    for row in csv_reader:
        total_votes+=1
        candidates.append(row[2])
        if row[2]=="Khan":
            votes_khan+=1
        elif row[2]=="Correy":
            votes_correy+=1
        elif row[2]=="O'Tooley":
            votes_otooley+=1
        else:
            votes_li+=1

    percent_khan=(votes_khan/total_votes)*100
    percent_correy=(votes_correy/total_votes)*100
    percent_otooley=(votes_otooley/total_votes)*100
    percent_li=(votes_li/total_votes)*100
    most_votes=max(votes_correy,votes_khan,votes_li,votes_otooley)
    if most_votes==votes_correy:
        winner="Correy"
    elif most_votes==votes_khan:
        winner="Khan"
    elif most_votes==votes_li:
        winner="Li"
    else:
        winner="O'Tooley"

    unique_candidates=set(candidates)
    print("Election Results")
    print("--------------------------------------")
    print("Total Votes: " + str(total_votes))
    print("Khan: " + str(round(percent_khan,0)) + "%")
    print("Correy: " + str(round(percent_correy,0)) + "%")
    print("O'Tooley: " + str(round(percent_otooley,0)) + "%")
    print("Li: " + str(round(percent_li,0)) + "%")
    print("Winner: " + winner)  
