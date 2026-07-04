
#This file serves as the host of the compute_ranks function. The rank of every student
#is calculated based on the skills, availability, and interests of every student. The way
#we calculate this is using frequencies. Students with less frequent skills receive a higher score,
#students with less available days receive a higher score, and students with less frequent skills also
#receive a higher score. 

#The function takes the students' list that was declared in the main file. 
def compute_ranks(students):
    #These are declarations for empty dictionaries. One dictionary for the skill frequency
    #and another dictionary for the interest frequency. These dictionaries store the skills, and
    #interests accordinly, and also the frequency of each one.
    skill_frequency = {}
    interest_frequency = {}

    #These for loops will iterate through each student in the Students list, and will count each 
    #appearance of skills and interests.
    for student in students:
        for skill in student.skills:
            #Every time we find a new skill, the skill gets added to the skill frequency dictionary.
            #The frequency is updated we find a new skill, or if we find a repeated one.
            skill_frequency[skill] = skill_frequency.get(skill, 0) + 1

        #Every time we find a new interest, the interest gets added to the interest_frequency dictionary.
        #The frequency is updated everytime we find a new interest, or if we find a repeated one. 
        for interest in student.interests:
            interest_frequency[interest] = interest_frequency.get(interest, 0) + 1

    #This section helps to compute the rank of every student. 
    #It iterates through every student in the students list. Rarity and interest are set to 0.
    for student in students:
        #The rarity of a skill is computed based on the number of students that have that skill. 
        #If one skill is shared by a lot of students, rarity decreases. If one student has a unique skill,
        #that skill is very rare and the rarity score becomes 1. We calculate the rarity by dividing 1 by
        #the frequency of the skill.
        rarity = 0
        for skill in student.skills:
            rarity += 1 / skill_frequency[skill]

        #The availability score is computed by taking the lenght of the student's availability. The lenght
        #function will count the number of days a student is available. The max function is only to ensure
        #we never divide by zero. We always take the maximum value between 1 and the available days of the 
        #student. 
        availability = 1 / max(1, len(student.availability))

        #The interest score is computed the same way as the availability one. If a student has a very rare
        #interest, the score increases. It decreases otherwise.
        interest = 0
        for i in student.interests:
            interest += 1 / interest_frequency[i]
        
        #The final student rank is computed adding all the scores. 
        student.rank = rarity + availability + interest