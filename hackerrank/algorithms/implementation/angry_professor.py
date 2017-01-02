"""
A Discrete Mathematics professor has a class of N students.
Frustrated with their lack of discipline, he decides to cancel class
    if fewer than K students are present when class starts.
Given the arrival time of each student, determine if the class is canceled.

Input Format

The first line of input contains T, the number of test cases.

Each test case consists of two lines.
    The first line has two space-separated integers, N (students in the class) and K (the cancelation threshold).
    The second line contains N space-separated integers (A0...An-1) describing the arrival times for each student.

Note: Non-positive arrival times (a<=0) indicate the student arrived early or on time;
positive arrival times (a>0) indicate the student arrived 'a' minutes late.
"""

test_count = int(input())

for _ in range(test_count):
    n, min_students = [int(part) for part in input().split()]
    students_on_time = 0
    will_be_canceled = True

    student_arrivals = (int(arrival) for arrival in input().split())  # generator to optimize time/memory when unneeded

    for arrival in student_arrivals:
        if arrival <= 0:
            students_on_time += 1
            if students_on_time == min_students:
                will_be_canceled = False
                break

    print('YES' if will_be_canceled else 'NO')