# QUESTION
# Write a python program with the following
# descriptive variables
# Indentations
# comparison operators

# A simple voters system program to show descriptive variables, indentations and comparison operators

name = 'Onyiye Adaobi'
age = 23
votableAge = 18
voterCard = True #User use have voters card to vote

if age < votableAge: # we use the less than (<) operator to compare if my age is less than the votable age
    print(name+' you are not eligible to vote') # tells me i'm eligible to vote if my age does not satisfy the above condition
    #We can see a usecase of indentation here to show code blocks 
elif not (voterCard): #We use the not operator here to check if the user does not have a voters card
    print(name +''' you do not own a voters card 
          you are not eligible to vote''')
elif age < votableAge and not (voterCard): #We use the and operator to run two comparisons at the same time by checking voters age and if the user has a voterCard
    print(name+ ''' You are not eligible to vote 
          because you are not upto 18 years of age 
          and you do not have a valid voters card''')
else:
    print(name + ''':
          You are eligible to vote because
          you meet the minimum age requirement to vote
          and you have a valid voter card''')