print("A Program to calculate the average of 6 numbers") #Display the program title
#We collect 6 different Numbers from the user, using the input method and typecast what ever value we recieve to Integer.
num1= int(input("Enter First Number: ")) #Prompt User to Enter first Number
num2= int(input("Enter Second Number: ")) #Prompt User to Enter Second Number
num3= int(input("Enter Third Number: ")) #Prompt User to Enter Third Number
num4= int(input("Enter Fourth Number: ")) #Prompt User to Enter Fourth Number
num5= int(input("Enter Fifth Number: ")) #Prompt User to Enter Fifth number
num6= int(input("Enter Sixth Number: ")) #Prompt User to Enter Sixth Number
total= num1 + num2 + num3 + num4 + num5 + num6 #add all numbers together into a variable called total
#The formular for calculating the average is sum of numbers divided by the number of values.

answer = total/6 # we divide our total number by the number of values and store it in a variable called answer

print('Your answer is:',answer) #Prints the total from adding the two numbers

#Program Terminates here