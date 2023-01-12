#Author: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 01/10/23
#The purpose of this code is to take a list of student's grades and find the mean, median, and mode using a statisitics module

import statistics

class Student:
    """creates class of students that initializes their names and grades, then will get grade values"""
    def __init__(self, name, grade):
#initializing name and grade
        self._name= name

        self._grade= grade

    def get_grade(self):
#method to get grade from given list
        return self._grade


def basic_stats(student):
    all_grades=[]
#gathers total of all grades from the students
    for s in student:
    #iterates through students and adds grades to list for statistics module to use
        all_grades.append(s.get_grade())
    #using imported statistics module to determine mean, median, and mode of students grades that were compiled
    mean=statistics.mean(all_grades)

    median=statistics.median(all_grades)

    mode=statistics.mode(all_grades)

    student_stats = (mean, median, mode)

    return student_stats

#s1 = Student("Kyoungmin", 73)
#s2 = Student("Mercedes", 74)
#s3 = Student("Avanika", 78)
#s4 = Student("Marta", 74)

#student_list = [s1, s2, s3, s4]
#print(basic_stats(student_list))  # should print a tuple of three values

