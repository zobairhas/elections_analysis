# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add dependencies
import csv
import os

# Variable to load file via indirect method
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable via indirect method
file_to_save = os.path.join("analysis", "election_analysis.txt")

# new list for candidate names
candidate_options = []

# Set total votes variable to 0
total_votes = 0

# new dictionary
candidate_votes = {}

# empty string value for winning candidate
winning_candidate = ""

winning_count = 0
winning_percentage = 0

# opens the file; election_data is just another random variable
with open(file_to_load) as election_data:

    # csv.read() lets you read the CSV file
    file_reader = csv.reader(election_data)
        
    # next(file_reader) reads the header rows
    headers = next(file_reader)
        
    # loops through rows
    for row in file_reader:
      
      # add total vote count
      total_votes += 1

      # print candidate name from each row
      candidate_name = row[2]

      # using not in operator to determine if candiate_name column does not match existing candidate
      # we are basically saying that if the candidate (column 3 row 3) is not in the dictionary then add it to the dictionary
      if candidate_name not in candidate_options:

        # add the candidate name to the candidate list
        candidate_options.append(candidate_name)

        # in order to track candidates vote count set the value equal to 0 first
        candidate_votes[candidate_name] = 0

      # for every single candidate name that's on the sheet, add a +1 to the total
      candidate_votes[candidate_name] += 1


# candidate_votes is the dictionary and candidate_name is the rows that we're looping through to get the name
for candidate_name in candidate_votes:

    # retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    # calculate actual percentage
    vote_percentage = float(votes) / float(total_votes) * 100

    print(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



# print(candidate_votes)





### ----------------------------------------------------------------------------------

### Open file using with statement
# with open(file_to_save, "w") as txt_file:

    ### Write some data to the file
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

### ----------------------------------------------------------------------------------
