from PIL import Image #From PIL a Library known as Pillow we import a module called Image that has a method for displaying pictures
print("This is my Bio-data") # displaying the tittle of the program
#My Bio-Data stored in descriptive variables
names = 'Emeka Sandra Oshama' # this is my name stored in a string variable
age = 22 # this is my age stored in an Integer variable
regNo = '20/BCH/147' # this is my MAT number stored in a string variable
gender = 'Female' # this is my gender stored in a string variable
department = 'Biochemistry' # this is my department stored in a string variable
faculty = 'Physical Science' # this is my faculty stored in a string variable
passport = Image.open("123.jpeg") # this is the path to my picture stores on my laptop, stored in a string variable that is passed to the image method as a parameter...
#Printing my Bio-data 
print("Name:",names) 
print("Age:",age)  
print("Registration Number:",regNo) 
print("Gender:",gender)             
print("Department:",department)       
print("Faculty:",faculty)
passport.show() # using the show method of the Image module to display my passport

#End of Program

