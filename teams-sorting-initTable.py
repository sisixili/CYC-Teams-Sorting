# Create functions to read csv files and initialize tables

import pandas as pd

def readCSV(colnames, csvPath):
    # colnames is a list
    print("Trying to read csv " + csvPath) # print ("error", file = std.err) or smth like that

    # dataframe rawtable includes column names as its first row
    rawtable = pd.read_csv(csvPath, usecols=colnames)

    oldlen = len(rawtable.index) #print(rawtable[rawtable.duplicated(keep = False)])
    rawtable.drop_duplicates(inplace = True) 
    if len(rawtable.index) < oldlen:
        print("Warning: duplicate(s) were detected and removed")

    print("Successfully read CSV")
    
    return rawtable

def initStudent(studInfodf, cursor, dbName):
    query = "INSERT INTO student_info(firstname, lastname, grade, school, email, isIB) VALUES(%s, %s, %s, %s, %s, %s)"
    values = list(studInfodf.itertuples(index=False, name=None)) # List of tuples
    
    cursor.executemany(query, values)
    dbName.commit()
    print("Successfully initialized table student_info")

def initTranking(trankingsdf, cursor, dbName, numThemes):
    query = "INSERT INTO trankings(s_id, t_id, ranking) VALUES(%s, %s, %s)"
    stud_ID = [] # Declare s_id col 1,1,1,1,1,1,...
    theme_ID = [] # Declare t_id col 1,2,3,4,5,6,...
    
    for i in range(len(trankingsdf)*numThemes):
        stud_ID.append(int(i/numThemes + 1))
        theme_ID.append(int(i%numThemes + 1))
    values = list(zip(stud_ID, theme_ID, trankingsdf))  
    
    cursor.executemany(query, values)
    dbName.commit()
    print("Successfully initialized table trankings")
    
def initMemLeads(isTLdf, cursor, dbName):
    teamLeads = []
    members = []
    
    # Based off logic that row # in csv = ID in student_info
    for i in range(len(isTLdf)):
        if isTLdf.iloc[i]['Is Team Lead?'] == "Yes":
            teamLeads.append((i+1,))
        else:
            members.append((i+1,))

    leadQuery = "INSERT INTO teams(lead_id) VALUES(%s)"
    memQuery = "INSERT INTO members(mem_id) VALUES(%s)"
    
    cursor.executemany(leadQuery, (teamLeads))
    cursor.executemany(memQuery, (members))
    dbName.commit()
    print("Successfully initialized tables teams and members")

