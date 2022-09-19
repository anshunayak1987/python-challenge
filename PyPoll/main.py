import os
import csv
pypoll_csv = os.path.join(".", "Resources", "election_data.csv")
#declaring total number of vote variable
total_number_of_vote = 0
#declaring total vote variable
total_vote = 0
#creating election data list
election_data = []
#opening the file for reading
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")
    #Read through each row of data after the header
    for row in csv_reader:
          election_data.append(row[2])
          #print (row)        
          total_number_of_vote = total_number_of_vote + 1
         
          
      #print(total_number_of_vote)
   
  #initialize a unique null list      
unique_list = []
#creating a function to identifie the unique candidate
def unique(list1):
  
    # initialize a null list
    #unique_list = []
  
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    #for x in unique_list:
        #print(x)
unique(election_data)
#unique_list
unique_list1 =[]
#creating the list of votes for candidate1
for x in election_data:
        # check if exists in unique_list or not
        if x == unique_list[0]:
            unique_list1.append(x)
            
unique_list2 =[]
#creating the list of votes for candidate2
for x in election_data:
        # check if exists in unique_list or not
        if x == unique_list[1]:
            unique_list2.append(x)
unique_list3 =[]
#creating the list of votes for candidate3
for x in election_data:
        # check if exists in unique_list or not
        if x == unique_list[2]:
            unique_list3.append(x)           
            #print(per_vote_charles)
num_vote_charles = len(unique_list1)
per_vote_charles = (num_vote_charles/total_number_of_vote) * 100
#print(per_vote_diana)
num_vote_diana = len(unique_list2)
per_vote_diana =(num_vote_diana/total_number_of_vote) * 100
#print(per_vote_raymon)
num_vote_raymon = len(unique_list3)
per_vote_raymon =(num_vote_raymon/total_number_of_vote) * 100
#print(num_vote_charles,num_vote_diana,num_vote_raymon)

#identifying the winner
if num_vote_charles > num_vote_diana and num_vote_charles > num_vote_raymon:
    winner = "Charles Casper Stockham"
elif num_vote_diana > num_vote_charles and num_vote_diana > num_vote_raymon:
    winner = "Diana DeGette"
elif num_vote_raymon > num_vote_diana and num_vote_raymon >  num_vote_charles:
    winner = "Raymon Anthony Doane"
else :
    winner = "none"
#printing the summary for terminal
print("Election Results"+ "\n")
print("-------------------------"+ "\n")
print("Total Vote: " + str(total_number_of_vote)+ "\n")
print("-------------------------"+ "\n")
print("Charles Casper Stockham: " + str(round(per_vote_charles,3)) + "% (" + str(num_vote_charles)+")" + "\n")
print("Diana DeGette: " + str(round(per_vote_diana,3)) + "% (" + str(num_vote_diana)+")" + "\n")
print("Raymon Anthony Doane:  " + str(round(per_vote_raymon,3)) + "% (" + str(num_vote_raymon)+")" + "\n")
print("-------------------------"+ "\n")
print("Winner: " + winner+ "\n")
print("-------------------------"+ "\n")
# Specify the file to write to
output_path = os.path.join(".", "analysis","election_result.txt")
with open(output_path, "w") as text_file:
    #wrting the summary in file
    text_file.write("Election Results"+ "\n"+ "\n")
    text_file.write("----------------------------"+ "\n"+ "\n")
    text_file.write("Total Vote: " + str(total_number_of_vote)+ "\n"+ "\n")
    text_file.write("-------------------------"+ "\n"+ "\n")
    text_file.write("Charles Casper Stockham: " + str(round(per_vote_charles,3)) + "% (" + str(num_vote_charles)+")" + "\n"+ "\n")
    text_file.write("Diana DeGette: " + str(round(per_vote_diana,3)) + "% (" + str(num_vote_diana)+")" + "\n"+ "\n")
    text_file.write("Raymon Anthony Doane:  " + str(round(per_vote_raymon,3)) + "% (" + str(num_vote_raymon)+")" + "\n"+ "\n")
    text_file.write("-------------------------" + "\n"+ "\n")
    text_file.write("Winner: " + winner +"\n"+ "\n")
    text_file.write("-------------------------")

