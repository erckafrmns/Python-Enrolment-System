# General Usage
MICSColor1 = '#7E0202'  # Equivalent to (126, 2, 2) <MAROON>
MICSColor2 = '#F1EAD5'  # Equivalent to (241, 234, 213) <BEIGE>
MICSColor3 = '#472213'
MICSColor4 = '#861D1D' #Slightly maroon
fontc1 = "black"

headFont = 'Arial 15 bold'
subheadFont = 'Arial 12 bold'
subheadFont1 = 'Arial 11 bold'
font1 = 'Arial 10 bold'
font2 = 'Arial 10'
font3 = 'Arial 8'
font4 = 'Arial 7'

axu = "0123756812"
axp = "micsadministrator"
acp = "781230148192"

class StudentPosition: # For student's current position in the list
    __instance = None

    @classmethod
    def get_instance(cls): # Singleton pattern
        if cls.__instance is None:
            cls.__instance = StudentPosition()
        return cls.__instance
    
    def __init__ (self):
        self.stud_pos = None
    
    def set_stud_pos (self, value): # Set student position
        self.stud_pos = value

    def get_stud_post (self): # Return student position
        return self.stud_pos

# SUBJECT DESCRIPTIONS
def subj_def(course_code):
    if course_code == "CC113":
        return "INTRODUCTION TO COMPUTING"
    elif course_code == "CC131L":
        return "COMPUTER PROGRAMMING 1, Lab"
    elif course_code == "CC132":
        return "COMPUTER PROGRAMMING 1, Lec"
    elif course_code == "MATHA05S":
        return "FUNDAMENTALS OF MATH ANALYSIS"
    elif course_code == "CC141L":
        return "COMPUTER PROGRAMMING 2, Lab"
    elif course_code == "CC142":
        return "COMPUTER PROGRAMMING 2, Lec"
    elif course_code == "CC103":
        return "DISCRETE STRUCTURES"
    elif course_code == "CS123":
        return "LINEAR ALGEBRA"
    elif course_code == "MATHA35":
        return "DIFFERENTIAL AND INTEGRAL CALCULUS"
    elif course_code == "CC211L":
        return "DATA STRUCTURES AND ALGORITHM, Lab"
    elif course_code == "CC212":
        return "DATA STRUCTURES AND ALGORITHM, Lec"
    elif course_code == "CS213":
        return "HUMAN COMPUTER INTERACTION"
    elif course_code == "CS233":
        return "COMBINATORICS AND GRAPH THEORY"
    elif course_code == "CS251L":
        return "OBJECT ORIENTED PROGRAMMING, Lab"
    elif course_code == "CS252":
        return "OBJECT ORIENTED PROGRAMMING, Lec"
    elif course_code == "CS251L":
        return "OBJECT ORIENTED PROGRAMMING, Lab"
    elif course_code == "CS271L":
        return "COMPUTER ARCHITECTURE AND ORGANIZATION, Lab"
    elif course_code == "CS272":
        return "COMPUTER ARCHITECTURE AND ORGANIZATION, Lec"
    elif course_code == "CC201L":
        return "INFORMATION MANAGEMENT, Lab"
    elif course_code == "CC202":
        return "INFORMATION MANAGEMENT, Lec"
    elif course_code == "CC223":
        return "APPLICATIONS DEVELOPMENT AND EMERGING TECHNOLOGIES"
    elif course_code == "CS201L":
        return "OPERATING SYSTEMS, Lab"
    elif course_code == "CS202":
        return "OPERATING SYSTEMS, Lec"
    elif course_code == "CS221L":
        return "PROGRAMMING LANGUAGE (DESIGN AND IMPLEMENTATION), Lab"
    elif course_code == "CS222":
        return "PROGRAMMING LANGUAGE (DESIGN AND IMPLEMENTATION), Lec"
    elif course_code == "CS243":
        return "DESIGN AND ANALYSIS OF ALGORITHMS"
    elif course_code == "CS261L":
        return "NETWORK AND COMMUNICATIONS, Lab"
    elif course_code == "CS262":
        return "NETWORK AND COMMUNICATIONS, Lec"
    elif course_code == "MATHSTAT03":
        return "PROBABILITY AND STATISTICS"
    elif course_code == "CSE1":
        return "CS PROFESSIONAL ELECTIVE 1"
    elif course_code == "CSE2":
        return "CS PROFESSIONAL ELECTIVE 2"
    elif course_code == "CSE3":
        return "CS PROFESSIONAL ELECTIVE 3"
    elif course_code == "CSE4":
        return "CS PROFESSIONAL ELECTIVE 4"
    elif course_code == "CS373":
        return "PARALLEL AND DISTRIBUTED COMPUTING"
    elif course_code == "CS351L":
        return "SOFTWARE ENGINEERING 1, Lab"
    elif course_code == "CS352":
        return "SOFTWARE ENGINEERING 1, Lec"
    elif course_code == "CS333":
        return "DATA ANALYTICS"
    elif course_code == "CS313":
        return "INFORMATION ASSURANCE AND SECURITY"
    elif course_code == "CC311L":
        return "WEB DEVELOPMENT, Lab"
    elif course_code == "CC312":
        return "WEB DEVELOPMENT, Lec"
    elif course_code == "CC303":
        return "METHODS OF RESEARCH IN COMPUTING"
    elif course_code == "CS303":
        return "AUTOMATA AND FORMAL LANGUAGE"
    elif course_code == "CS321L":
        return "ARTIFICIAL INTELLIGENCE, Lab"
    elif course_code == "CS322":
        return "ARITIFICIAL INTELLIGENCE, Lec"
    elif course_code == "CS343":
        return "MODELING AND SIMULATION"
    elif course_code == "CS361L":
        return "SOFTWARE ENGINEERING 2, Lab"
    elif course_code == "CS362":
        return "SOFTWARE ENGINEERING 2, Lec"
    elif course_code == "CS413":
        return "THESIS WRITING 1"
    elif course_code == "CS433":
        return "SOCIAL AND PROFESSIONAL ISSUES"
    elif course_code == "CS403":
        return "SUPERVISED INDUSTRIAL TRAINING"
    elif course_code == "CS423":
        return "THESIS WRITING 2"
    