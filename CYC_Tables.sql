CREATE TABLE themes (
    theme_id INT PRIMARY KEY AUTO_INCREMENT,
    tname VARCHAR(50) NOT NULL
);
INSERT INTO themes (tname) VALUES 
	("Caring For The Environment"), 
    ("Online Tutoring"), 
    ("Caring For Seniors"),
    ("Anti-Racism"),
    (" Youth Engagement"),
    ("Media and Awareness");
UPDATE themes SET tname = "Youth Engagement" WHERE theme_id = 5;

DROP TABLE student_info; -- Drop table to refresh index
CREATE TABLE student_info (
    ID INT PRIMARY KEY AUTO_INCREMENT, 
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    grade INT,
    school VARCHAR(100),
    email VARCHAR(50),
    isIB VARCHAR(3), -- 1 => Yes, 0 => No
    ftheme VARCHAR(50)
);

DROP TABLE trankings;
CREATE TABLE trankings(
	ID INT PRIMARY KEY AUTO_INCREMENT,
	s_id INT NOT NULL,
    t_id INT NOT NULL,
    ranking INT NOT NULL,
    FOREIGN KEY (s_id) REFERENCES student_info (ID),
    FOREIGN KEY (t_id) REFERENCES themes (theme_id)
);

DROP TABLE teams;
CREATE TABLE teams (
  ID INT PRIMARY KEY AUTO_INCREMENT, -- Becomes Team Name
  lead_id INT NOT NULL,
  FOREIGN KEY (lead_id) REFERENCES student_info (ID)
);

DROP TABLE members;
CREATE TABLE members (
  ID INT PRIMARY KEY AUTO_INCREMENT, -- For printing
  team_id INT,
  mem_id INT NOT NULL,
  FOREIGN KEY (team_id) REFERENCES teams (ID),
  FOREIGN KEY (mem_id) REFERENCES student_info (ID)
);

-- Remember to do checks like memSize + teamSize = 200 

