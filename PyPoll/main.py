# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
txtpath = os.path.join("Resources", "PyPoll_output.txt")

#Setting up variables
votecount = 0

uniquecandidates_list=[]
votetotals_list=[]
votepercentages_list=[]

mostvotes=0

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)

    #get list of unique names and total votes
    for row in csvreader:
        name=row[2]
        if name not in uniquecandidates_list:
            uniquecandidates_list.append(name)
        votecount=int(votecount)+1

    #number of unique candidates to go through
    candidates_count=int(len(uniquecandidates_list))


    #go through list again for each candidate, this time totalling votes each candidate won
    for candidate in range(candidates_count):
        #reset candidate vote total
        candidatevotetotal=0
        candidatepercentage=0

        with open(csvpath, newline="") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            csv_header=next(csvreader)
            for row in csvreader:
                name=row[2]
                #if this row relates to the candidate in uniquecandidates_list then take info
                if name==uniquecandidates_list[candidate]:
                    candidatevotetotal=candidatevotetotal+1
        #add candidate vote total to list
        votetotals_list.append(candidatevotetotal)
        #then for each candidate, calculate their vote %
        candidatepercentage=candidatevotetotal/votecount
        votepercentages_list.append(candidatepercentage)

        #then see if this candidate has more votes than others
        if candidatevotetotal > mostvotes:
            mostvotes = candidatevotetotal
            winner = uniquecandidates_list[candidate]

#figure out who has the most


#Print summary


##
print(" Election Results")
print("----------------------")

for candidate in range(candidates_count):
    
    print(f"{uniquecandidates_list[int(candidate)]}:{round(votepercentages_list[int(candidate)]*100,2)}%\
        ({votetotals_list[int(candidate)]})")

print("----------------------")
print(f"Winner: {winner}")

# write to txt
File_object = open(txtpath,"r+")
File_object.write(
    " Election Results"+"\n"
    "----------------------"+"\n"
)
for candidate in range(candidates_count):
    (
        File_object.write(
        f"{uniquecandidates_list[int(candidate)]}:{round(votepercentages_list[int(candidate)]*100,2)}% \
            ({votetotals_list[int(candidate)]})"+"\n"
        )
    )

File_object.write(
    "----------------------"+"\n"
    f"Winner: {winner}"
    )
