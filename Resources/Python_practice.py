print("Hello World")
a = 5 + 2 * 3
b = 8 // 5 - 3
c = 8 + 22 * 2 - 4
d = 16 - 3 / 2 + 7 - 1
e = 3 ** 3 % 5
f= 5 + 9 * 3 / 2 - 4
g = 5 + (9 * 3 / 2 - 4)
h = 5 + (9 * 3 / (2 - 4))

calculations = [a,b,c,d,e,f,g,h]

print(calculations)

print(type(calculations))

print(type(calculations[3]))

print(calculations)

#list are mutable change an element using list(index-element-to-change) = new element
calculations[2] = 'left'
print(calculations)



print('LISTS')

counties = ["Arapahoe","Denver","Jefferson"]

print(counties[1:])
#add element ad the end of the list: my_list.append()
counties.append('El Paso')
print(counties)

#add element at specific indez: my_list.insert(where,what)
counties.insert(2, 'El Paso')
print(counties)

#eliminate a element from a list my_list.remove(element-to-eliminate) or my_list.pop(element-to-delete-INDEX)
counties.pop(2)
print(counties)

counties.remove('Arapahoe')
print(counties)

print("new list")
counties1 = ["Arapahoe","Denver","Jefferson"]
counties1.insert(1, 'El Paso')
counties1.remove('Arapahoe')
counties1.remove('Denver')
counties1.insert(2, 'Denver')
counties1.append('Arapahoe')

print(counties1)

#TUPLES are inmutable no adding removing nothing
print('TUPLES')
counties_tuple = ("Arapahoe","Denver","Jefferson")
counties_tuple[1]

print(counties_tuple[1:2])

#Dictionaries: creates an empty dictionary and add key county + number-of-votes
print('DICTIONARIES')
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438


print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get('Arapahoe'))
counties_dict['Arapahoe'] 

counties_dict.get("Arapahoe")  

print(counties_dict['Arapahoe'])  

print(counties_dict.get("Arapahoe")) 

#new empty dictionary where keys will have more than 1 value associated 
#[{key1:value1, key2:value2}, {key1:value3, key2:value4}]
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)
#add another set of values in the second position
voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})

#Remove “Arapahoe” and its registered voters from voting_data. 
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})

#Make “Denver” and its registered voters the third item in voting_data, but keep “Jefferson” and its registered voters as the second item.   
voting_data.remove({"county":"Denver", "registered_voters": 463353})
voting_data.insert(2, {"county":"Denver", "registered_voters": 463353})

#Add “Arapahoe” and its registered voters to voting_data.
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

print(voting_data)


print('DECISION STATEMENT')
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")


counties = ["Arapahoe","Denver","Jefferson"]
if counties[0] != 'Denver':
    print(counties[2])



#If-else statements
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#NESTED IF-ELSE
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

print('all good!')


#IF ELIF ELSE 
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

print('even better!!')


#Membership operators

counties = ["Arapahoe","Denver","Jefferson"] 
if "Arapahoe" in counties: 
    print("True") 
else: print("False")


if "El Paso" not in counties: 
    print("True") 
else: print("False")


if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


#Logical operators + if statements

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

#or
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

#and
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")





