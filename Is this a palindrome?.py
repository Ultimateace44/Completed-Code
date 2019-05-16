#user input
input1 = str(raw_input())

#Return when no input given
if len(input1)<= 0:
  print("Your input is too short")

#return when too much input given
if len(input1)>= 100:
  print("Your input is too long")

#List of letters
letter = []

#for (each letter) in user input
for i in input1:
  
#Takes out spaces from input/letter list  
  if i.strip() == "":
    continue

#Changes any uppercase letters to lower case
  if i == i.upper():
    i = i.lower()

#skips adding letters from input to List of letters if letter already exists in list
  if (i in letter):
    continue

#Adds each letter from input into List of letters
  else:
    letter.append(i)

  
# input contains all 26 letters returns
if len(letter) == 26:
  print("YES this is a palindrome!")

#input does NOT contain all 26 letters, return
else:
  print("Nope, sorry... this isn't a palindrome :(")
