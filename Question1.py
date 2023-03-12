num= int(input("Enter Number: ")) #getting a number for the user to print out its multiple
n_num= int(input("Enter Number Of Multiple: ")) #getting range of multiple's to print out

while(num<=n_num): #using a while loop to check if the number is greater than 0
    if(((num+2)%2)==0): #add 2 into and checking if num is an even number
        print(num) #displaying num
    num=num+1 # counter for num
        

