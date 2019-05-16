#Number of characters
#(dont understand why they didnt want me to use len)
input1= input()

#the character themselves
input2= input()

#changes input1 from a str to an int
input1= int(input1)

#this is what i assume to be the constraint
while True: 
    if input1 >= 27:
        raise Exception("Thats too many letters")

    if input1 <= 0:
        raise Exception ("Not Enough Letters")

    else:
        break

#adds input to list
list = []
for i in input2:
    if (i in list):
        continue
    if i == " ":
        continue
    else:
        list.append(i)

#for some reason added a blank space
#between [0] and [2] so i deleted it


#sorts list alphabetically NOT case sensitive
list.sort(key=str.lower)

#prints the list without brackets or commas
print(" ".join(list))
