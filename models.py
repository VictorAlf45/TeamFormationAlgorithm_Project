#This file serves to create the Student class.
#With this class, we create the Student objects for name, skills
#availability and iterest for every students. 
from dataclasses import dataclass

@dataclass
class Student:
    #Contains the student's name
    name: str
    #This is a list that contains the skills for every student
    skills: list
    #Another list for the days each student is available to work
    availability: list
    #List for stating the students' interest
    interests: list

    #This is a score that will tell us how easy or hard will be to assign each
    #student. 
    rank: float = 0
    #This tells us if a student has already been assigned to a team or not. 
    assigned: bool = False