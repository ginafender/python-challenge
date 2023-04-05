# import csv file
import os
import csv

files = "C:/Users/ginav/Desktop/Analysis Projects/Class Activity Files/Module 3/python-challenge/PyPoll/Resources/election_data.csv"
with open(files) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #variables needed
    currCand = 0
    percVotes = 0
    totalVotes = 0
    votes = 0
    #count the total number of votes cast
    cand_dict = {}
    for row in csvreader:
        totalVotes += 1
        currCand = row[2]
        if not currCand in cand_dict.keys():
            cand_dict[currCand] = 1
        else:
            cand_dict[currCand] += 1
    output = ("Election Results \n")
    output = output + ("----------------------------\n")
    output = output + (f"Total Votes: {totalVotes}\n")
    output = output + ("----------------------------\n") 

    #calculate the percentage of votes
    for cand, votes in cand_dict.items():
        percVotes = (votes / totalVotes)*100
        output = output + (f"{cand}: {round(percVotes, 3)}% ({votes})\n")
        max_value = max(cand_dict.values())
        max_key = max(cand_dict, key=cand_dict.get)
    output = output + ("----------------------------\n")
    output = output + (f"Winner: {max_key}\n")
    output = output + ("----------------------------\n")

    #print to terminal
    print(output)

    #export to txt file
    file_to_output = os.path.join("election_analysis.txt")
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)