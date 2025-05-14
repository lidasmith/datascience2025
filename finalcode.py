import csv
import time
#Importing functions

line_count = 0
n = 1
a = 0
row_total = []
ans = []
your_dog = []
#Declaring variables

with open('breed_traits.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for i in range(194):
        row_total.append(i)
    for i in row_total:
        if i > 0:
            row_total[i] = 0
    for i in range(17):
        ans.append(i)
    #setting up list variables
    for i in range(4):
        print("")
    ans[1] = int(input("On a scale of 1-5, how important is it for your dog to be affectionate with family? "))
    ans[2] = int(input("On a scale of 1-5, how important is it for your dog to be good with young children? "))
    ans[3] = int(input("On a scale of 1-5, how important is it for your dog to be good with other dogs? "))
    ans[4] = int(input("On a scale of 1-5, how important is it for your dog to NOT shed very often? "))
    ans[5] = int(input("On a scale of 1-5, how important is it for your dog to NOT need to be groomed often? "))
    ans[6] = int(input("On a scale of 1-5, how important is it for your dog to NOT drool much? "))
    print("Please capitalize following answers.")
    time.sleep(1)
    print("Dog fur types: Corded, Curly, Double, Hairless, Rough, Silky, Smooth, Wavy, Wiry")
    time.sleep(2)
    ans[7] = input("What fur type would you prefer to have on a dog? ")
    ans[8] = input("What length do you prefer the dog's coat to be? (Short, Medium, Long) ")
    ans[9] = int(input("On a scale of 1-5, how important is it for your dog to be welcoming to strangers? "))
    ans[10] = int(input("On a scale of 1-5, how important is it for your dog to be playful? "))
    ans[11] = int(input("On a scale of 1-5, how important is it for your dog to possess traits of a watchdog? "))
    ans[12] = int(input("On a scale of 1-5, how important is it for your dog to be adaptable to changes? "))
    ans[13] = int(input("On a scale of 1-5, how important is it for your dog to be easy to train? "))
    ans[14] = int(input("On a scale of 1-5, how important is it for your dog to have a high energy level? "))
    ans[15] = int(input("On a scale of 1-5, how important is it for your dog NOT to bark much? "))
    ans[16] = int(input("On a scale of 1-5, how important is it for your dog NOT to need lots of mental stimulation? "))
    print("calculating...")
    time.sleep(2)
    #Collecting data from user input

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        #This if statement is to skip the title row.
        else:
            for i in range(3):
                if int(ans[n]) <= int(row[n]):
                    row_total[a] += 1
                n += 1
            #This loop calculates the first half of the values.
            for i in range(3):
                if int(ans[n]) <= 6 - int(row[n]):
                    row_total[a] += 1
                n += 1
            #Reverse coding

            if row[7] == ans[7]:
                row_total[a] += 3
            if row[8] == ans[8]:
                row_total[a] += 3
            n += 2
            #These transcribe the coat types into numbers.

            for i in range(6):
                if int(ans[n]) <= int(row[n]):
                    row_total[a] += 1
                n += 1
            for i in range(2):
                if int(ans[n]) <= 6 - int(row[n]):
                    row_total[a] += 1
                n += 1
            #This is the second half of the values.
            if row_total[a] == int(max(row_total)):
                your_dog += [row[0]]
            #The selected dog will be the last in this list.
            line_count += 1
            n = 1
            a += 1
print("")
print("The dog breed that would best suit you are " + str(your_dog[-1]) + "!")
time.sleep(2)
print("If you would like to learn more about them, check out the AKC website.")


#type: ignore