#imports
import csv
import os

#set path
csvpath = os.path.join("Resources", "election_data.csv")

#variables
total_votes = 0
candidates = []
percentages = [0.0, 0.0, 0.0, 0.0]
votes = [0, 0, 0, 0]
winner = ""

#read csv
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #read out header line
    csv_header = next(csvreader)
    #read data
    for row in csvreader:
        #count total votes
        total_votes += 1
        #list candidates
        if str(row[2]) not in candidates:    
            candidates.append(str(row[2]))
    #re-read data
    csvfile.seek(0)
    csvreader = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader)
    #find votes per candidates
    for row in csvreader:
        for i in range(0,4):
            if str(row[2]) == str(candidates[i]):
                vote_value = votes[i]
                vote_value += 1
                votes[i] = vote_value
#find percentages
for j in range(0,4):
    vote_value = votes[j]
    percent = round((vote_value / total_votes) * 100, 4)
    percentages[j] = percent
#find winner
for x in percentages:
    index = percentages.index(max(percentages))
    winner = candidates[index]

print("'''text\n")
print("Election Results\n")
print("-------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("-------------------------\n")
for candidate in candidates:
    index = candidates.index(candidate)    
    print(f"{candidate}:  {percentages[index]}% ({votes[index]})\n")
print("-------------------------\n")
print(f"Winner: {winner}")
print("-------------------------\n")
print("'''")

#open/create output file
f= open("analysis/output_PyPoll.txt","w+")

#write data to file
f.write("'''text\n")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write(f"Total Votes: {total_votes}\n")
f.write("-------------------------\n")
for candidate in candidates:
    index = candidates.index(candidate)    
    f.write(f"{candidate}:  {percentages[index]}% ({votes[index]})\n")
f.write("-------------------------\n")
f.write(f"Winner: {winner}")
f.write("-------------------------\n")
f.write("'''")