import os
import csv

total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""

filepath = os.path.join("election_data.csv")
with open(filepath,'r', newline="") as csvelection:
    election_reader = csv.reader(csvelection, delimiter=",")
    next(election_reader)
    for row in election_reader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

dashbreak = "-------------------------"

print("Election Results")
print(dashbreak)
print(f"Total Votes: {total_votes}")
print(dashbreak)
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} ({vote_count})")
print(dashbreak)
print(f"Winner: {winner}")
print(dashbreak)

