# A message to tell the user the input the program is expecting
print("Enter correct Score for Assesment and Exam for CSC2101")
# getting assesmentScore of the student via input
assesmentScore = int(input("Enter Score for Assesment: "))
# getting examScore of the student via input
examScore = int(input("Enter Score for Exam: "))
# calculating totalScore of the student for both assestment and exams
totalScore = assesmentScore + examScore

# A Nested if statement block to check if the totalScore of the student is within a certain grade and output the grade with a remark
if totalScore >= 70:
    print("Grade => A, pass")  # output the student grade and a remark
elif totalScore >= 60:
    print("Grade => B, pass")  # output the student grade and a remark
elif totalScore >= 50:
    print("Grade => C, pass")  # output the student grade and a remark
elif totalScore >= 40:
    print("Grade => D, pass")  # output the student grade and a remark
elif totalScore >= 30:
    print("Grade => E, pass")  # output the student grade and a remark
elif totalScore < 30:
    print("Grade => F, Carry over")  # output the student grade and a remark

# End of program
