import statistics

# input for the student's name
f_name = input("Student's first name: ")
s_name = input("Student's surname: ")

# subjects
agri = int(input("Agriculture: "))
math = int(input("Mathematics: "))
chic = int(input("Chichewa: "))
eng = int(input("English: "))
l_s = int(input("Life Skills: "))
phy = int(input("Physics: "))
chem = int(input("Chemistry: "))
soc = int(input("Social Studies: "))
bio = int(input("Biology: "))
b_k = int(input("Bible Knowledge: "))
s_marks = agri + math + chic + eng + l_s + phy + chem + soc + bio + b_k
m_marks = s_marks/10
print(" ")

# calculating total marks of a students
if agri > 100 or math > 100 or chic > 100 or eng > 100 or l_s > 100 or phy > 100 or chem > 100 or soc > 100 or bio > 100 or b_k > 100:
    print("Marks for each subject shouldn't be more than 100")
else:
    print(s_name +" " + f_name + " "  + "total marks: " + str(s_marks))
    print("Average marks:" + str(m_marks))

# giving a student grades
if agri > 100 or math > 100 or chic > 100 or eng > 100 or l_s > 100 or phy > 100 or chem > 100 or soc > 100 or bio > 100 or b_k > 100:
    print("Can't give grades if one of the subjects marks are more than 100")
elif m_marks >= 85 and m_marks <=100:
    print("Grade A")
elif m_marks >= 75 and m_marks < 85:
    print("Grade B")
elif m_marks >= 60 and m_marks < 75:
    print("Grade C")
elif m_marks >= 40 and m_marks < 60:
    print("Grade D")
elif m_marks < 40:
    print("Grade F")