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

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)


### ----------------------------------------------------------------------------------

### Open file using with statement
# with open(file_to_save, "w") as txt_file:

    ### Write some data to the file
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

### ----------------------------------------------------------------------------------
