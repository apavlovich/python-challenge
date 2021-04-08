import os
import csv
from pathlib import Path

os.chdir(os.path.dirname(__file__))

CSVfile = os.path.join("..","Resources","PyPoll_PollingData.csv")

total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

with open(CSVfile,newline="",encoding="utf-8") as elections:
    csvreader = csv.reader(elections,delimiter=",")
    header = next(csvreader)

    for row in csvreader:

        total_votes += 1

        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1

candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan, correy, li, otooley]

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

khanPercent = (khan/total_votes) * 100
correyPercent = (correy/total_votes) * 100
liPercent = (li/total_votes) * 100
otooleyPercent = (otooley/total_votes) * 100

if khanPercent > correyPercent and khanPercent > liPercent and khanPercent > otooleyPercent:
    winner = "Khan"
if correyPercent > khanPercent and correyPercent > liPercent and correyPercent > otooleyPercent:
    winner = "Correy"
if liPercent > khanPercent and liPercent > correyPercent and liPercent > otooleyPercent:
    winner = "Li"
if otooleyPercent > khanPercent and otooleyPercent > correyPercent and otooleyPercent > liPercent:
    winner = "O'Tooley"


print(f"Election Results")
print(f"---------------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------------")
print(f"Khan: {khanPercent:.3f}% ({khan})")
print(f"Correy: {correyPercent:.3f}% ({correy})")
print(f"Li: {liPercent:.3f}% ({li})")
print(f"O'Tooley: {otooleyPercent:.3f}% ({otooley})")
print(f"--------------------------------")
print(f"Winner: {winner}")

output = Path("..","Analysis","Election_Summary_Results.txt")

with open(output,"w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"---------------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"---------------------------------")
    file.write("\n")
    file.write(f"Khan: {khanPercent:.3f}% ({khan})")
    file.write("\n")
    file.write(f"Correy: {correyPercent:.3f}% ({correy})")
    file.write("\n")
    file.write(f"Li: {liPercent:.3f}% ({li})")
    file.write("\n")
    file.write(f"O'Tooley: {otooleyPercent:.3f}% ({otooley})")
    file.write("\n")
    file.write("---------------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")