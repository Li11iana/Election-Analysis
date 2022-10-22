#Repetition statements
#   Condition controlled loop WHILE   
#   CAREFUL WITH INFINITE LOOPS!
print("\n While Loop")
x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7

while count < 1:
    print("Hello World")


#   Count controlled loop FOR   
print("\n For Loop")

counties = ["El Paso","Jefferson","Denver","Arapahoe"] 
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

#built in function range() creates an iterable object or a list
for num in range(5):
    print(num)

#indexing to iterate (needs len when its string)
for i in range(len(counties)):
    print(counties[i])

#iterate through a dictionary
print("\n Dictionary")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

print("\n Keys")
for county in counties_dict.keys():
    print(county)

print("\n values")
for voters in counties_dict.values():
    print(voters)

print("\n")
for county in counties_dict:
    print(counties_dict[county])

print("\n get")   
for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

print("\n key-value pair")  
for county, voters in counties_dict.items():
    print(county, voters)

#SKILL DRILL
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#use the range function to iterate over the list of dictionaries and print the counties in voting_data
for i in range(len(voting_data)):
      print(voting_data[i]['county'])

#range(number) :: for x in range(3)
for county in range(len(voting_data)):
     print(county)

#How would you retrieve the number of registered voters from each dictionary?
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#1
for county_dict in voting_data:  
     print(county_dict.values())

#1.2
for item in voting_data:  
     print(item.values())

#2
for county_dict in voting_data:    
   for value in county_dict:      
       print(value)
#3
for county_dict in voting_data:
     print(county_dict['registered_voters'])

#4
for county_dict in voting_data:
     for key, value in county_dict.items():
         print(value)

#we only want to print the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])

#F-strings USES f"whatever {variable or operation} whatever"
#before
print("\nPrinting formats \n")
    #my_votes = int(input("How many votes did you get in the election? "))
    #total_votes = int(input("What is the total votes in the election? "))
    #percentage_votes = (my_votes / total_votes) * 100
    #print("I received " + str(percentage_votes)+"% of the total votes.")

    #after
    #my_votes = int(input("How many votes did you get in the election? "))
    #total_votes = int(input("What is the total votes in the election? "))
    #print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#f-strings can be used with dictionaries too
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
    
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multiline F-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)


#changing precision of the value (decimals)
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#SKILL DRILL Print each county and registered voter from the dictionary using f strings
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = ['{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}']
election_summary = (
    f"The county of {'county'} has {'registered_voters'} registered voters"
)

print(election_summary)
