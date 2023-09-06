# GOAL: Fill in members(team_id) and student_info(ftheme)
import statistics
from statistics import mode
import mysql.connector
import sys

# Manually fill in friends teams

# Select all from members where teams_id is null and the rank of theme_id = 1 is 1.
# If num of students < 4, select (4 - numStudents) of student(s) from members where teams_id is null and rank of theme_id is 2 


def extractCol(list, colIndex):
    newList = []
    for row in list:
        newList.append(row[colIndex])
    return newList

def toList(val, listLen):
    newList = []
    for i in range(listLen):
        newList.append(val)
    return newList

def sortTeams(cursor, dbName, minSize, maxSize, numThemes):
    
    cursor.execute("SELECT COUNT(*) FROM student_info")
    numStuds = cursor.fetchone()[0]
                    
    cursor.execute("SELECT COUNT(*) FROM teams")
    numLeads = cursor.fetchone()[0]
                    
    avgSize = int((numStuds - numLeads)/numLeads)
    if avgSize < minSize - 1: 
        print("Warning: Too many team leads compared to students")
        sys.exit(1)  
    
    #rank1Results = [] # List of lists where row # = theme ID
    unsorted = [] # List of members who can't get current choice
    
    # Going from theme 1 to 6, assign every member rank 1 theme
    for tnum in range (1, numThemes + 1):
        query = "SELECT * FROM members AS m, trankings AS t WHERE m.team_id IS NULL AND m.mem_id = t.s_id AND t.t_id = %s AND t.ranking = %s"
        cursor.execute(query, (tnum, 1))
        result = cursor.fetchall() # row # = theme, col = mem_ids
        mem_ids = extractCol(result, 2)
            
        if len(result) > minSize - 1:
            # Any number > 3 can be assembled with groups of 3,4,5,6
            updateStudent = "UPDATE student_info SET ftheme = %s WHERE ID = %s"
            studVals = list(zip(toList(tnum, len(mem_ids)), mem_ids))
            cursor.executemany(updateStudent, studVals)   
            dbName.commit()  
        else:
            # If num of mems who ranked a theme as 1 < 3, team can't be formed
            unsorted.append(mem_ids)

    # Last Team where some members will not get first choice
    # Set to have most possible # of rank 1's (May require manual adjustment)
    if len(unsorted) != 0:
        # Find theme with most rank 1's
        temp = [len(unsorted)]
        for i,j in enumerate(temp):
            if j == max(temp):
                theme = i + 1

        themeList = []
        flatUnsorted = [item for sublist in unsorted for item in sublist]
        for row in flatUnsorted:
            themeList.append(theme)
        fthemeVals = list(zip(toList(theme, len(flatUnsorted)), flatUnsorted))
        
        query = "UPDATE student_info SET ftheme = %s WHERE ID = %s"
        cursor.executemany(query, fthemeVals)
        dbName.commit()
    
    # Form teams and assign team leads
    
    queryLeads = "SELECT * FROM teams"
    cursor.execute(queryLeads)
    tLeads = cursor.fetchall()

# if len(result) >= numLeads: 
#    # Theme is bigger than ideal => shift students to lower rank
#    unsorted.append(result)
# else: 
#    # Theme is smaller than ideal => move other students of lower rank to this theme
#    cursor.execute("UPDATE student_info SET ftheme = %s LIMIT BY %s", (tnum, minSize-1))
            
    # cursor.excute(query)
    # dbName.commit()

# for index, row in student_info.iterrows():
#     query = "INSERT INTO temp_student_info(firstname, lastname, grade, school, email, isIB) VALUES(%s, %s, %s, %s, %s, %s)"
#     values = tuple(row)
#     cursorObj.execute(query, values)
# cycdb.commit()

# query = "SELECT * FROM student_info LIMIT 5"
# cursorObj.execute(query)

# results = cursorObj.fetchall()

# for val in results:
#     print(val)

