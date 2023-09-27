from initTable import *
from sort import *

# Reading CSV
# Themes are currently hardcoded...will have update 'theme' table later
student_cols = ['firstname','lastname','grade','school','email','Is IB?','Caring for the Environment Rank', 
                'Online Tutoring Rank','Caring for Seniors Rank','Anti-Racism Rank','Youth Engagment Rank', 
                'Media and Awareness Rank','Is Team Lead?']
student_path = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/simstudents.csv'

student_table = readCSV(student_cols, student_path)

student_info = student_table[['firstname','lastname','grade','school','email','Is IB?']]
theme_rankings = student_table[['Caring for the Environment Rank','Online Tutoring Rank','Caring for Seniors Rank',
                                'Anti-Racism Rank','Youth Engagment Rank','Media and Awareness Rank']]
isLead = student_table[['Is Team Lead?']]

# Make this into future update
numThemes = 6
minTeamSize = 4
maxTeamSize = 7

# Connecting to CYC database
print("Trying to establish connection to MySQL db")
cycdb = mysql.connector.connect(
  host = "XXX",
  user = "XXX",
  password = "XXX",
  database = "cyc",
  auth_plugin = "mysql_native_password"
)
cursorObj = cycdb.cursor()
print("Successfully established connection")

# Initializing table student_info
initStudent(student_info, cursorObj, cycdb)

# Initializing table trankings (Collapse rankings into 1 col)
initTranking(theme_rankings.stack().reset_index(drop=True), cursorObj, cycdb, numThemes)

# Initializing table teams and table members
initMemLeads(isLead, cursorObj, cycdb)

# Sort
sortTeams(cursorObj, cycdb, minTeamSize, maxTeamSize, numThemes)

cursorObj.close() # needed?
cycdb.close()

print("Program is done")
