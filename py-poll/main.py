import pandas as pd

df = pd.read_csv('election_data.csv')

Total = df['Voter ID'].value_counts()
Total_Votes = Total.sum()

Candidates = df.Candidate.unique()

Khan_Count = df.loc[df.Candidate == 'Khan', 'Candidate'].count()

c = df.groupby(['Candidate']).size()
c = pd.Series.to_frame(c, name = "Count")

s = df['Candidate'].value_counts(normalize=True)*100
s = pd.Series.to_frame(s, name = "Percentage")
s["Candidate"] = s.index

t = pd.merge(c,s, on="Candidate")

winner = t.loc[t["Percentage"].idxmax()]

print("Election Results")
print('------------------')
print("Total Votes:" ,(Total_Votes))
print('------------------')
print(t)
print('------------------')
print(winner)
print('------------------')
