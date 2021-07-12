# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

import csv
import os
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate Options and candidate votes.
candidate_options = []
county_options = []
# 1: Create a county list and county votes dictionary.
candidate_votes = {}
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
   
    file_reader = csv.reader(election_data)
    # Read the header
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        #  Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking each candidate's vote count. To create each candidate as a keyfor the dictionary.
            candidate_votes[candidate_name] = 0
        # And begin tracking that candidate's voter count.
        candidate_votes[candidate_name] += 1

        
        if county_name not in county_options:
            county_options.append(county_name)
            #  Begin tracking each candidate's vote count. To create each candidate as a keyfor the dictionary.
            county_votes[county_name] = 0
        # Add a vote to that candidate's count as we iterate through rows.
        county_votes[county_name] += 1

        # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
         # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    
    txt_file.write(election_results) 

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:
        #  Retrieve vote count of a candidate.
        votes = county_votes[county]
        #  Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # print each candidate's name, vote count, and percentage of votes to terminal
        county_election_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_election_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_election_results)
  
        # Determine winning vote count and candidate. Determine if the votes is greater than the winning count.
        if (votes > winning_county_count) and (vote_percentage > winning_county_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_county_count = votes
            winning_county_percentage = vote_percentage
            winning_county = county
    txt_file.write("\n")

    county_results = (
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(county_results, end="")
    txt_file.write(county_results)

     # Save the final candidate vote count to the text file.
    for candidate in candidate_votes:
    # Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
# Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
   # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary) 