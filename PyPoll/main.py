import os 
import csv
#filepath
file_csv = os.path.join ( 'Resources',
                        'election_data.csv') 
total_votes = 0
otooley_votes = 0
correy_votes = 0
khan_votes = 0
li_votes = 0
#format
with open (file_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    #print (header)
    for row in csvreader:
#adding the total votes based on rows
        total_votes += 1
        if row[2] == "O'Tooley":
            otooley_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Li":
            li_votes += 1
    #candidates = ["O'Tooley","Correy","Khan","Li"]
    #votes = [otooley_votes, correy_votes, khan_votes, li_votes]
Stats = {"O'Tooley": otooley_votes,"Correy": correy_votes,
        "Khan": khan_votes,"Li": li_votes}
#voteCount = F.values()
StatsNew = [max(Stats, key=Stats.get)]
otooley_percent = (otooley_votes / total_votes) * 100
correy_percent = (correy_votes / total_votes) * 100
khan_percent = (khan_votes / total_votes) * 100
li_percent = (li_votes / total_votes) * 100
#print statements
print(f"Election Stats")
print(f"======================")
print(f"Total Number of Votes:{(total_votes)}")
print(f"O'Tooley:{otooley_percent:.3f}% ({otooley_votes})")
print(f"Correy:{correy_percent:.3f}% ({correy_votes})")
print(f"Khan:{khan_percent:.3f}% ({khan_votes})")
print(f"Li:{li_percent:.3f}% ({li_votes})")
print(f"Winner: {StatsNew}")
output = os.path.join("Analysis","Election_results.txt")
with open(output,"w") as file:
    file.write(f"Election Stats")
    file.write("\n")
    file.write(f"======================")
    file.write("\n")
    file.write (f"Total Number of Votes:{(total_votes)}")
    file.write("\n")
    file.write(f"O'Tooley:{otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"Correy:{correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Khan:{khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Li:{li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"Winner: {StatsNew}")
