#This file serves as the host for the build_teams and the team_metric functions.

#The build_teams function will create teams of students using the list of students
#declared in the main file, the matrix of compatibility created in the compatibility
#file, and the team_size that was declared in the main file. 
def build_teams(students, matrix, team_size):

    #This is an empty list where we will store all the teams that we wil form
    teams = []
    #We will iterate for all the students in the students' list.
    for student in students:
       
        #If a student has already been assigned to a team, we will pass it and continue
        #with the next one. This is important so we do not assign the same student to 
        #multiple teams.
        if student.assigned:
            continue

        #This line of code assigns a student to a team.
        student.assigned = True
        #A new team is created using a list, and it contains the student that we just 
        #assigned in the previous line of code.
        team = [student]

        #We will keep iterating until the lenght of the team reaches the team_size that
        #we hardcoded in the main.py file
        while len(team) < team_size:
            #best is used as a placeholder for the best fit for a team memeber. It is 
            #initialized to none. We do not have an ideal candidate yet.
            best = None
            #We initialize the score for best candidate to a very low score.
            best_score = -1

            #This loops sees all students in the students list as a possible candidate for
            #a new member. If a candidate has already been assigned to a team, we pass that
            #student and continue with the next student in the list. We set to 0  the score 
            #for the new candidate
            for candidate in students:
                if candidate.assigned:
                    continue
                score = 0

                #For every member/members in the team, we will add the scores of the candidate.
                #We will store it in score, and if the score is greater than best_score, the new
                #candidate becomes the best candidate. We will try different additions. The greatest
                #score for the team will always be the most ideal team.
                for member in team:
                    score += matrix[member.name][candidate.name]
                if score > best_score:
                    best_score = score
                    best = candidate
            #This piece of code is for checking if there are remaining students waiting to be 
            #assigned. If we do not have a best candidate, we exit the while loop.
            if best is None:
                break
            #The best candidate is labeled as assined, and it cannot be selected again for other teams.
            best.assigned = True
            #We append the student to the team
            team.append(best)
        #The new created team is appended to the teams list.
        teams.append(team)
    #We return all the teams
    return teams


#The team_metrics function computes the average of the ranking of each student
def team_metrics(teams):
    #Initialization for an empty metrics list, for the average metric of every team
    metrics = []

    #For all team in the teams list, we are going to initialize a total to 0, we are
    #going to add the rank scores of every student, and divide the total by the number
    #of students in the team. We will append the average to the metrics list.
    for team in teams:
        total = 0
        for student in team:
            total += student.rank
        metrics.append(total / len(team))
    #We return the average metrics of every team
    return metrics