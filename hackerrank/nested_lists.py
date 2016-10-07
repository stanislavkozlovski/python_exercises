"""
Given the names and grades for each student in a Physics class of N students,
 store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically
and print each name on a new line.

Input Format
The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second
 line contains their grade.

Constraints
2 <= N <= 5
There will always be one or more students having the second lowest grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students,
order their names alphabetically and print each one on a new lin
"""
students = []
n = int(input())

# fill the students list
for i in range(0,n*2,2):
    studentName = input()
    studentGrade = float(input())
    students.append([studentName, studentGrade])

min_grade = min(grade for _, grade in students)  # get the lowest grade
second_lowest_grade = min(grade for _, grade in students if grade != min_grade)  # get the second-lowest grade
# get all the students with the second-lowest grade
second_lowest_students = list(filter(lambda x: x[1] == second_lowest_grade, students))
# sort them alphabetically
second_lowest_students.sort(key=lambda x: x[0].lower())

for student in second_lowest_students:
    print(student[0])  # print the name of the student