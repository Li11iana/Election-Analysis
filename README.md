# Election Analysis
## Overview
For this project the election results for 3 counties: Denver, Arapahoe, and Jefferson. Every vote was registered in an Excel file. Using Python to automate the election result count and obtain a visual summary of all relevant data insights to facilitate the election commission's work.

## Election Audit Result
The characteristics of the data analysis will be reviewed below:

![Terminal_output](https://github.com/Li11iana/Election_Analysis_Python/blob/main/Resources/Terminal_output.png)


* A total of 369,711 votes were cast for the congressional election.
* Counties Breakdown
The county of Jefferson had 10.5% of the total votes with 38,855 votes emited.
The county of Denver had 82.8% of the total votes with 306,055 votes emited.
The county of Arapahoe had 6.7% of the total votes with 11,606 votes emited.
The county of Denver had the largest number of votes (82.8% of the total votes).
* Candidates Breakdown
Candidate Charles Casper Stockham obtained 23.0% of all the votes (85,213 votes).
Candidate Diana DeGette obtained 73.8% of all the votes (272,892 votes).
Candidate Raymon Anthony Doane obtained 3.1% of all the votes (11,606 votes).
* Winner summary
Candidate Diana DeGette was the winner of the congressional election with a total vote count of 272,892 representing the 73.8% of all emited votes.

## Election Audit Summary

The code simplifies the election analysis and its adequate for variable input since it can adapt to data sources with different counties and candidates, extracting this information and using it to elaborate the summaries so the code can be resuse with minimal to no refactoring. For example, if another country loads its election information in csv format the code would automatically iterate to generate a candidate and county from that data and assigning it to variables. This would make it very simple to obtain the counties, candidates and winner breakdown as long as the csv file follows the same format. If that is not the case, then the code would have to be refactored so that data collection adapts to the source file.
An improvement that could be added is more checking points for the analyst, this could be easily configured by printing the list and dictionaries used in order to confirm that all the information is being properly assessed.
