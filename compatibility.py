#This files serves as a host for the compatibility_matrix function. This function
#will calculate a compatibility score, and based on the students that have already 
#been assigned to teams, the non-assigned students will be paired with the most 
#compatible assigned students. 

def compatibility_matrix(students):
    #This is the initialization of an empty dictionary that will be used to store the compatibility scores
    #of all students. 
    matrix = {}

    #This chunk compares every student a to any other student b.
    for a in students:
        #For every student a, this will create a matrix with the score of all the students b and their names.
        matrix[a.name] = {}
        for b in students:

            #This is for not comparing a student with themselves. If we find out that one student is compared 
            #with the same one, we will continue with the next student in the compatibility matrix.
            if a == b:
                continue

            #Initialization of compatibility score to 0. 
            score = 0
            
            #This line is for comparing the common skills between students a and b. Each skills sublist for two
            #distinct students get converted into a set. The & operator serves to find an intersection between 
            #the two sets, and the lenght function just counts the number of items intersected. 
            common_skills = len(set(a.skills) & set(b.skills))

            #If two students do not have shared skills. The score is increased by 50 points. If there is a
            #shared skill, there is an increase in 20 points for every skill shared. 
            if common_skills == 0:
                score += 50
            else:
                score += 20

            #This piece of code is for comparing the common availability between students ab and b. Each availability 
            #sublist for two different students get converted into a set. The & operaror helps finding the intersection
            #between sets. The lenght function counts the number of items that intersect. 
            common_availability = len(set(a.availability) & set(b.availability))
            #The number of common available days are added to the score as individual points. 
            score += common_availability

            #This is for converting common interests into scores. We find the intersection of interests between two 
            #two students just as we did for skills and availability. This time, the number of common interest are 
            #multiplied by a factor of 5, and the number is added to the score. 
            common_interests = len(set(a.interests) & set(b.interests))
            score += common_interests * 5

            #The compatibility score between students a and b is added to the matrix.
            matrix[a.name][b.name] = score
            
    #We return the whole matrix
    return matrix