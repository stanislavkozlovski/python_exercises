"""
You have a record of N students.
Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
The marks can be floating values.
The user enters some integer N followed by the names and marks for N students.
You are required to save the record in a dictionary data type. The user then enters a student's name.
Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format
The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained
by that student separated by a space. The final line contains the name of a particular student previously listed.

Constraints
2 <= N <= 10
0 <= Marks <= 100

Output Format
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output
56.00
"""

n = int(input())
students = {}  # type: dict
# save the input into the dictionary
for _ in range(n):
    name, maths_grade, physics_grade, chemistry_grade = input().split()
    student_average_grade = (float(maths_grade) + float(physics_grade) + float(chemistry_grade)) / 3
    students[name] = student_average_grade

searched_student_average = input()  # name of the student we want to find the average of
print('{0:.2f}'.format(students[searched_student_average]))