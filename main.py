#This file serves as the main control for the whole algorithm.
#It imports the Student class from models, and the compute_ranks, compatibility_matrix,
#build_teams, and team_metrics functions from the ranking, compatibility, and teams files. 

from models import Student
from ranking import compute_ranks
from compatibility import compatibility_matrix
from teams import build_teams, team_metrics


#reset students function: This function helps with reseting
#the students to its original values. If all the estudents have been
#assigned, this fuction resets them to "no assigned" so we can run the algorithm
#again
def reset_students(students):
    #iterates to through all students
    for s in students:
        #resets the students assignment to "not assigned"
        s.assigned = False
        #resets student ranking again to zero
        s.rank = 0

#print teams helper function: This function prints the team number, the students'
#names, the rank of every student, and the average of the team of every student.
def print_teams(teams, metrics):
    #iterates through teams, and gives a number to every team
    #prints the teams
    for i, team in enumerate(teams):
        print(f"\nTeam {i+1}")
        #This prints the name of each student, and also the ranking score for every
        #student up to two decimal places. 
        for student in team:
            print(f"  {student.name} (Rank: {student.rank:.2f})")
        #prints the average of the teams
        print(f"Average Team Metric: {metrics[i]:.2f}")


#Data from 10 students
#This consists in a list of 10 students, and each student has a name, a skill,
#the days in which each student is available to work, and interests of every student
students = [
    Student("Jesus",   ["Python"],  ["Monday", "Wednesday"], ["AI", "VideoGames"]),
    Student("Alonso", ["Java"], ["Monday", "Tuesday"], ["VideoGames", "Football"]),
    Student("Ernesto", ["UI"], ["Wednesday", "Thurday"],  ["Design", "Music"]),
    Student("Elliot", ["Databases"],    ["Tuesday", "Thurday"], ["AI", "Movies"]),
    Student("Salvador", ["Python"], ["Monday", "Friday"], ["Music", "Art"]),
    Student("Rodolfo",  ["Networking"], ["Wednesday", "Friday"], ["Sports", "Travelling"]),
    Student("Andres",["Java"], ["Tuesday", "Wednesday"],  ["Movies", "VideoGames"]),
    Student("Lizeth", ["UI"], ["Thurday", "Friday"],["Art", "Travelling"]),
    Student("Emma", ["Databases"],  ["Monday", "Thurday"], ["AI", "Music"]),
    Student("Jessica", ["Networking"], ["Tuesday", "Friday"], ["Basketball", "Movies"])]

#This is a hard coded constant for the team size.
#This is used to it is easier to control the team size every time
#we run the algorithm, and we can see the output more easily. 
TEAM_SIZE = 3


#Algorithm
#This is the way the whole algorithm flows. First we compute the ranks for every student in the list.
#Then a compatibility matrix is created to save the compatibility score of every unassigned student.
#After that, we build every team based in the students with higher rankings. Students with higher rankings
#are assigned first, and after that, the students with better compatibility score are assigned to corresponding 
#teams. 
#In the metrics we calculate the average metric for every team.

#imported from ranking
compute_ranks(students)
#imported from compatibility
matrix = compatibility_matrix(students)
#imported from teams
teams = build_teams(students, matrix, TEAM_SIZE)
#imported from teams
metrics = team_metrics(teams)
print_teams(teams, metrics)