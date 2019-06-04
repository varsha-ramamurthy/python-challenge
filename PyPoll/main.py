import os
import csv
print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
election_csv = os.path.join("..\PyPoll","election_data.csv")
with open(election_csv, newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")
# ignore the header
    hdr=next(csv_reader)
    candidate_votes={}

#compute total sumber of votes cast, and list of candidates
    for row in csv_reader:
        candidate_name = row[2]
        num_votes = candidate_votes.get(candidate_name, 0)
        num_votes += 1
        candidate_votes[candidate_name] = num_votes


    print("----------------------Election Results---------------------")
    total_votes = sum(candidate_votes.values())
    print("Total Votes: " + str(total_votes))
    print("---------------------Votes polled by each candidate-----------------------")
    maximum_votes = 0
    for candidate_name in candidate_votes:
        print("   Candidate " + candidate_name + " secured " + str(round((candidate_votes[candidate_name]/total_votes)*100,0)) + "% (" + str(candidate_votes[candidate_name]) + ")")
        if candidate_votes[candidate_name] > maximum_votes:
            winner_name = candidate_name
            maximum_votes = candidate_votes[candidate_name]
    print("-----------------------------------")
    print("Winner: " + winner_name + " wins with " + str(maximum_votes) + " votes")
    