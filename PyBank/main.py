import os
import csv
pybank_csv = os.path.join(".", "Resources", "budget_data.csv")

#Open and read csv
#creating month variable
number_of_month = 0
#creating amount variable
total_amount = 0
#creating profit loss list
prev_profit_loss = []
#creating budget data list
budget_data = []

#creating reading statment
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")
    #Read through each row of data after the header
    for row in csv_reader:
        prev_profit_loss.append(row[1])
        budget_data.append(row)
        #print (row)        
        number_of_month = number_of_month + 1
        total_amount = total_amount + int(row[1])
       
    #print(number_of_month)
    #print(total_amount)
    #print(budget_data)
#declaring the list to capture changes profit and loss
change = []
#for loop for getting the change 
for x in range(number_of_month):
    # Print each number in the range
    #calculating the change in profit and loss
    if x>0:
        z = int(prev_profit_loss[x]) - int(prev_profit_loss[x-1])
        #print(z)
        change.append(z)
#calculating the average
average=sum(change)/len(change)    
#print(average)

#calculate the Greatest increase in Profits
max_value = max(change)
#Getting the index Greatest increase in Profits
max_index = change.index(max_value)
#print(max_value,max_index)


#Calculate the Greatest Decrease in Profits
min_value = min(change)
#Getting the index Greatest Decrease in Profits
min_index = change.index(min_value)
#print(min_value,min_index)


#Generate Output Summary
print("Finacial Analysis"+ "\n")
print("----------------------------"+ "\n")
print("Total Month: "+ str(number_of_month)+ "\n")
print("Total:" + " $"+ str(total_amount)+ "\n")
print("Average Change:" + " $" + str(round(average,2))+ "\n")
print("Greatest Increase in Profits " + budget_data[max_index+1][0] +" ($"+ str(max_value) + ")"+ "\n")
print("Greatest Decrease in Profits " + budget_data[min_index+1][0] +" ($"+ str(min_value) + ")"+ "\n")

# Specify the file to write to
output_path = os.path.join(".", "analysis", "budget_data_Output.txt")
with open(output_path, "w") as text_file:
    #printing the result in text file
    text_file.write("Finacial Analysis"+ "\n"+ "\n")
    text_file.write("----------------------------"+ "\n"+ "\n")
    text_file.write("Total Month: "+ str(number_of_month)+ "\n"+ "\n")
    text_file.write("Total:" + " $"+ str(total_amount)+ "\n"+ "\n")
    text_file.write("Average Change:" + " $" + str(round(average,2))+ "\n"+ "\n")
    text_file.write("Greatest Increase in Profits " + budget_data[max_index+1][0] +" ($"+ str(max_value) + ")" + "\n"+ "\n")
    text_file.write("Greatest Decrease in Profits " + budget_data[min_index+1][0] +" ($"+ str(min_value) + ")"+ "\n")
    