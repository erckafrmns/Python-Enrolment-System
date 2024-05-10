# User-Defined Imports
from config import * # For miscellaneous functions and variable configuration details
from students import *
from entry import *
from file_handling import *
from enrollment import *
from protection import *

# Built-in Imports
from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import shutil
import os
import datetime
from fpdf import FPDF
from pathlib import Path
import datetime

#GLOBAL VARIABLES
stuProfile = None
imglabel = None
navbar = None
root = None
current_student = None
currStu_id = None
currStu_lName = None
currStu_fName = None
currStu_mName = None
currStu_yr = None
currStu_sem = None
currStu_pass = None
currStu_status = None
currStu_sex = None
currStu_dob = None
currStu_num = None
currStu_email = None
currStu_address = None
currStu_gEmail = None
currStu_gNum = None

# Get the parent folder of the root folder
parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#IMAGES (that are use often) DIRECTORY
prevPath = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "prevBtn.png")
nextPath = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "nextBtn.png")
mainPath = os.path.join(parent_folder, "main.py")
imgPath = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "MICSlogo.png")
img1Path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "CHED_LOGO.png")

sys_list = SystemList()

def main__menu(): # Function to display the MAIN_MENU and the navigation tools in it
    global root, navbar, currStu_id, currStu_lName, currStu_fName, currStu_mName, currStu_yr, currStu_sem, currStu_pass, current_student
    global currStu_status, currStu_sex, currStu_dob, currStu_num, currStu_email, currStu_address, currStu_gEmail, currStu_gNum
    
    # CURRENT STUDENT DETAILS (Currently encrypted)
    current_student = sys_list.get_current_student()
    currStu_id = current_student[0]
    currStu_lName = current_student[1]
    currStu_fName = current_student[2]
    currStu_mName = current_student[3]
    currStu_yr = current_student[4]
    currStu_sem = current_student[5]
    currStu_pass = current_student[6]
    currStu_status = current_student[7]
    currStu_sex = current_student[8]
    currStu_dob = current_student[9]
    currStu_num = current_student[10]
    currStu_email = current_student[11]
    currStu_address = current_student[12]
    currStu_gEmail = current_student[13]
    currStu_gNum = current_student[14]

    current_datetime = datetime.datetime.now()
    sys_list.add_to_stud_log([currStu_id, encrypt_w_ok("Log-in"), 
                              encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])
    
    #WINDOW FRAME
    root = Tk()
    root.geometry("800x500") # Set size of frame
    root.configure(bg = MICSColor2)
    root.resizable(False, False)
    root.title("Manila Institute of Computer Studies - Main Menu")
    iconPath = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "MICSlogo.ico")
    root.iconbitmap(iconPath)
    
    #LEFT NAVIGATION BAR FRAME
    navbar = Frame(root, width= 250, height=500, relief=GROOVE, bg = MICSColor1)
    navbar.place(x=0, y=0)
    
    # Draw a vertical line on the right side of the navbar
    canvas = Canvas(navbar, width=2, bg= MICSColor1, highlightthickness=0)
    canvas.place(x=248, y=0, height=500)
    canvas.create_line(1, 0, 1, 500, fill='black')
           
    #-----BUTTONS------
    uploadBtn = Button(navbar, text="Upload Image", font = font1, fg=MICSColor1, command=uploadImage)
    uploadBtn.place(x=42, y=168, width= 170, height=25) 
    
    displayBtn = Button(navbar, text="View Grades", font = font1, fg=MICSColor1, bg= MICSColor2, command=displayGrades)
    displayBtn.place(x=32, y=275, width= 190, height=30)
    
    updateBtn = Button(navbar, text="Student Information", font = font1, fg=MICSColor1, bg= MICSColor2, command= updateInfo)
    updateBtn.place(x=32, y=310, width= 190, height=30)

    enrollBtn = Button(navbar, text="Enroll", font = font1, fg=MICSColor1, bg= MICSColor2, command= enroll)
    enrollBtn.place(x=32, y=345, width= 190, height=30)
    
    accountBtn = Button(navbar, text="Account Settings", font = font1, fg=MICSColor1, bg= MICSColor2, command= accountSettings)
    accountBtn.place(x=32, y=380, width= 190, height=30)

    logOutBtn = Button(navbar, text="LOG-OUT", font = font1,fg=MICSColor2, bg= MICSColor3, command= logOut)
    logOutBtn.place(x=32, y=415, width= 190, height=30)
    
    retrieve_student_image()
    updateProfileImage()

    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName[0]) + ". " + decrypt(currStu_lName )
    currStuName = Label(navbar, text= fullName, font = subheadFont1, fg=MICSColor2, bg=MICSColor1 )
    currStuID = Label(navbar, text= decrypt(currStu_id), font = subheadFont1, fg=MICSColor2, bg=MICSColor1 )
    currStuName.place(x=0, y=202, width= 250)
    currStuID.place(x=0, y=230, width = 250)

    for item in SystemList().return_stud_tor_req_list():
        if currStu_id == item[0]:
            if decrypt(item[5]) == "APPROVED":
                messagebox.showinfo("TOR REQUEST APPROVED", "You can now download your Transcript of Records at the ACCOUNT SETTINGS tab")
            elif decrypt(item[5]) == "DECLINED":
                messagebox.showwarning("TOR REQUEST DECLINED", "Request for Transcript of Records declined")
                delete_tor_request()

    mainWindow()

    root.mainloop()

#MAIN WINDOW OR HOME
def mainWindow():
    frame = Frame(root, width= 550, height= 500, relief = GROOVE, bg = MICSColor2)
    frame.place(x=250, y=0)
    
    #HEADER
    header = Label(frame, text= "MANILA INSTITUTE OF COMPUTER STUDIES", font = headFont, fg=MICSColor1, bg=MICSColor2)
    header.place(x=0, y=20, width= 550)

    img = Image.open(imgPath)
    img = img.resize((48, 48))
    logo = ImageTk.PhotoImage(img)
    logolabel = Label(frame, image=logo, bg= MICSColor2)
    logolabel.place(x=5, y=6)
    logolabel.image = logo
    
    img1 = Image.open(img1Path)
    img1 = img1.resize((38, 38))
    logo1 = ImageTk.PhotoImage(img1)
    logo1label = Label(frame, image=logo1, bg= MICSColor2)
    logo1label.place(x=500, y=10)
    logo1label.image = logo1
    
    #CUSTOM FONT AND COLOR
    f1 = "Arial 11 bold"
    c1= "black"
    
    #LABELS
    courseLabel = Label(frame, text = "Course:", font= f1, fg= MICSColor1, bg= MICSColor2)
    courseLabel.place(x=20, y=75)
    statusLabel = Label(frame, text="Scholastic Status:", font= f1, fg= MICSColor1, bg= MICSColor2)
    statusLabel.place(x=20, y=100)
    yrLabel = Label(frame, text="Year:", font= f1, fg= MICSColor1, bg= MICSColor2)
    yrLabel.place(x=330, y=100)
    semLabel = Label(frame, text="Sem:", font= f1, fg= MICSColor1, bg= MICSColor2)
    semLabel.place(x=400, y=100)
    
    crsCodeLabel = Label(frame, text="Course Code", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsCodeLabel.place(x=15, y=130, width = 110, height= 30)
    crsUnitLabel = Label(frame, text="Unit", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsUnitLabel.place(x=125, y=130, width = 60, height= 30)
    facultyLabel = Label(frame, text="Faculty", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    facultyLabel.place(x=185, y=130, width = 205, height= 30)
    scheduleLabel = Label(frame, text="Schedule", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    scheduleLabel.place(x=390, y=130, width = 145, height= 30)

    #LABEL INPUT
    crsLBL = Label(frame, text= "BSCS - Bachelor of Science in Computer Science", font= font1, fg= c1, bg= MICSColor2)
    crsLBL.place(x=88, y=76)
    statLBL = Label(frame, text = decrypt(currStu_status), font= font1, fg= c1, bg= MICSColor2)
    statLBL.place(x=155, y=101)
    yrLBL = Label(frame, text = decrypt(currStu_yr), font= font1, fg= c1, bg= MICSColor2)
    yrLBL.place(x=380, y=101)
    semLBL = Label(frame, text= decrypt(currStu_sem), font= font1, fg= c1, bg= MICSColor2)
    semLBL.place(x=450, y=101)

    #DISPLAY CURRENT COURSE LISTS
    currCrsList = sys_list.get_curr_course_list()

    for index, course in enumerate(currCrsList):
        course_day = ""
        if decrypt(course[4]) == "MONDAY":
            course_day = "M"
        elif decrypt(course[4]) == "TUESDAY":
            course_day = "T"
        elif decrypt(course[4]) == "WEDNESDAY":
            course_day = "W"
        elif decrypt(course[4]) == "THURSDAY":
            course_day = "TH"
        elif decrypt(course[4]) == "FRIDAY":
            course_day = "F"
        elif decrypt(course[4]) == "SATURDAY":
            course_day = "SA"
        elif decrypt(course[4]) == "SUNDAY":
            course_day = "SU"
            
        schedule =  course_day + " " + decrypt(course[5])
        
        crsCodeLBL = Label(frame, text = decrypt(course[0]), font=font2, fg= c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Code
        crsCodeLBL.place(x=15, y=160 + index * 25, width=110, height=25)
        
        crsUnitLBL = Label(frame, text = decrypt(course[1]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Units
        crsUnitLBL.place(x=125, y=160 + index * 25, width=60, height=25)
        
        facultyLBL = Label(frame, text = decrypt(course[3]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Faculty Name
        facultyLBL.place(x=185, y=160 + index * 25, width=205, height=25)
        
        scheduleLBL = Label(frame, text= schedule, font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Schedule
        scheduleLBL.place(x=390, y=160 + index * 25, width=145, height=25)
    
    #SAVE BUTTON
    saveBtn = Button(frame, text="SAVE SCHEDULE", font = font1, fg=MICSColor2, bg= MICSColor1, command= saveSchedule)
    for item in currCrsList:
        if item[3] == "" or item[4] == "" or item[5] == "":
            saveBtn.config(state = "disabled")
            break

    saveBtn.place(x=415, y=450, width= 120, height=30)

#RETRIEVE CURRENT STUDENT IMAGE    
def retrieve_student_image():
    global stuProfile
    file_extensions = [".jpg", ".jpeg", ".png"]  # Add more extensions if needed
    
    encrypted_stud_num = ""

    i = 1
    for char in decrypt(currStu_id):
        if i < 5:
            new_char = chr(ord(char) + 3)
            encrypted_stud_num += new_char
        else:
            new_char = chr(ord(char) + 17)
            encrypted_stud_num += new_char

        i += 1

    for extension in file_extensions:
        file_name = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "2", encrypted_stud_num + extension)
        if os.path.exists(file_name):
            stuProfile = file_name
            break
        else: #IF NEW STUDENT AND HAVE NO PROFILE PICTURE YET
            defaultImg = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "defaultProfile.jpg")
             # Set the new profile image file path
            stuProfile = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "2", f"{encrypted_stud_num}{os.path.splitext(defaultImg)[1]}")
        
            try:
                shutil.copy2(defaultImg, stuProfile) #Copy the new image file to the file path
                updateProfileImage()
                
            except Exception as e:
                print("Error uploading image:", e)

    if stuProfile:
        print("Image file found:", stuProfile)
    else:
        print("Image file not found.")

#OPEN FILE DIALOG, LET USER CHOOSE NEW PROFILE, AND SAVE THE NEW PROFILE
def uploadImage():
    global stuProfile
    newImg = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select New Image",
                                        filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    
    encrypted_stud_num = ""

    i = 1
    for char in currStu_id:
        if i < 5:
            new_char = chr(ord(char) + 3)
            encrypted_stud_num += new_char
        else:
            new_char = chr(ord(char) + 17)
            encrypted_stud_num += new_char

        i += 1

    if newImg:
        if os.path.exists(stuProfile):
            os.remove(stuProfile) # Delete the existing profile image file if it exists

        # Set the new profile image file path
        stuProfile = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "2", f"{encrypted_stud_num}{os.path.splitext(newImg)[1]}")
    
        try:
            shutil.copy2(newImg, stuProfile) #Copy the new image file to the file path
            updateProfileImage()

            current_datetime = datetime.datetime.now()
            sys_list.add_to_stud_log([currStu_id, encrypt_w_ok("Update profile image"), 
                                      encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])
            
        except Exception as e:
            print("Error uploading image:", e)

#DISPLAY CURRENT STUDENT PROFILE/IMAGE
def updateProfileImage():
    global stuProfile, imglabel

    if imglabel is not None:
        imglabel.destroy()

    try:
        img = Image.open(stuProfile)
        img = img.resize((164, 150))
        stuImg = ImageTk.PhotoImage(img)

        imglabel = Button(navbar, image=stuImg, command=mainWindow)
        imglabel.place(x=42, y=15)
        imglabel.image = stuImg
    except Exception as e:
        print("Error opening image file:", e)

#VIEW GRADES
def displayGrades():

    topFrame = Frame(root, width=550, height=50, relief=GROOVE)
    topFrame.place(x=250, y=0)
    
    sframe = Frame(root, width= 550, height= 450, relief = GROOVE, bg = MICSColor2)
    sframe.place(x=250, y=50)    

    #HEADER
    lb = Label(topFrame, text= "Manila Institute of Computer Studies", font = headFont, fg= MICSColor2, bg = MICSColor1)
    lb.place(x=0, y=0, width= 550, height= 50)
    lb.config(highlightthickness=1, highlightbackground=MICSColor1)
    
    img = Image.open(imgPath)
    img = img.resize((45, 45))
    logo = ImageTk.PhotoImage(img)
    logolabel = Label(topFrame, image=logo, bg= MICSColor1)
    logolabel.place(x=25, y=0)
    logolabel.image = logo
    
    img1 = Image.open(img1Path)
    img1 = img1.resize((35, 35))
    logo1 = ImageTk.PhotoImage(img1)
    logo1label = Label(topFrame, image=logo1, bg= MICSColor1)
    logo1label.place(x=475, y=5)
    logo1label.image = logo1
    
    #CUSTOM FONT AND COLOR
    f1 = "Arial 11 bold"
    c1= "black"
     
    total_grade = 0
    total_units = 0

    currCrsList = sys_list.get_curr_course_list()
    for course in currCrsList:
        x = float(decrypt(course[2])) * int(decrypt(course[1]))

        # Update the total grade points and total units
        total_grade += x
        total_units += int(decrypt(course[1]))

    # Calculate the GPA
    gpa = total_grade / total_units
    gpa = round(gpa, 2)
    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName)
     
    #LABELS
    stuNameLabel = Label(sframe, text="Student's Name:", font= f1, fg= MICSColor1, bg= MICSColor2)
    stuNameLabel.place(x=10, y=20)
    stuNumLabel = Label(sframe, text="Student No:", font= f1, fg= MICSColor1, bg= MICSColor2)
    stuNumLabel.place(x=10, y=40)
    stuYrLabel = Label(sframe, text="Year:", font= f1, fg= MICSColor1, bg= MICSColor2)
    stuYrLabel.place(x=332, y=40)
    stuSemLabel = Label(sframe, text="Sem:", font= f1, fg= MICSColor1, bg= MICSColor2)
    stuSemLabel.place(x=400, y=40)
    statusLabel = Label(sframe, text="Scholastic Status:", font= f1, fg= MICSColor1, bg= MICSColor2)
    statusLabel.place(x=10, y=60)
    gpaLabel = Label(sframe, text="GPA:", font= f1, fg= MICSColor1, bg= MICSColor2)
    gpaLabel.place(x=350, y=60)   
    
    #LABEL INPUT
    stuNameInput = Label(sframe, text= fullName, font= font1, fg= c1, bg= MICSColor2)
    stuNameInput.place(x=135, y=21) 
    stuNumInput = Label(sframe, text= decrypt(currStu_id), font= font1, fg= c1, bg= MICSColor2)
    stuNumInput.place(x=105, y=41) 
    stuYrInput = Label(sframe, text= decrypt(currStu_yr), font= font1, fg= c1, bg= MICSColor2)
    stuYrInput.place(x=380, y=41) 
    stuSemInput = Label(sframe, text= decrypt(currStu_sem), font= font1, fg= c1, bg= MICSColor2)
    stuSemInput.place(x=448, y=41) 
    statusInput = Label(sframe, text= decrypt(currStu_status), font= font1, fg= c1, bg= MICSColor2)
    statusInput.place(x=145, y=61) 
    gpaInput = Label(sframe, text= gpa, font= font1, fg= c1, bg= MICSColor2)
    gpaInput.place(x=398, y=61) 
    
    
    #DISPLAYING GRADES OF CURRENT COURSES
    crsCodeLabel = Label(sframe, text="Course Code", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsCodeLabel.place(x=15, y=95, width = 110, height= 30)
    crsUnitLabel = Label(sframe, text="Unit", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsUnitLabel.place(x=125, y=95, width = 60, height= 30)
    crsGradeLabel = Label(sframe, text="Grade", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsGradeLabel.place(x=185, y=95, width = 65, height= 30)
    facultyLabel = Label(sframe, text="Faculty", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    facultyLabel.place(x=250, y=95, width = 195, height= 30)
    remarksLabel = Label(sframe, text="Remarks", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    remarksLabel.place(x=445, y=95, width = 90, height= 30)   
    
    currCrsList = sys_list.get_curr_course_list()
    for index, course in enumerate(currCrsList):
        yPos=index *22
        
        if float(decrypt(course[2])) == 0.00 or float(decrypt(course[2])) == 0 or float(decrypt(course[2])) == 0.0:
            remarks = "-"
        elif float(decrypt(course[2])) <= 3.00 :
            remarks = "PASSED"
        else:
            remarks = "FAILED"
        
        crsCodeLBL = Label(sframe, text = decrypt(course[0]), font=font2, fg= c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Code
        crsCodeLBL.place(x=15, y=125 + yPos, width=110, height=22)
            
        crsUnitLBL = Label(sframe, text = decrypt(course[1]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Units
        crsUnitLBL.place(x=125, y=125 + yPos, width=60, height=22)
            
        crsGradeLBL = Label(sframe, text = decrypt(course[2]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Grade
        crsGradeLBL.place(x=185, y=125 + yPos, width=65, height=22)
            
        facultyLBL = Label(sframe, text = decrypt(course[3]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Faculty Name
        facultyLBL.place(x=250, y=125 + yPos, width=195, height=22)

        remarksLBL = Label(sframe, text = remarks, font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Remarks
        remarksLBL.place(x=445, y=125 + yPos, width=90, height=22)

    
    
    #FIRST YEAR - SECOND SEM
    if int(decrypt(currStu_yr)) == 1 and int(decrypt(currStu_sem)) == 2:
            
            #BUTTONS
            prev = Image.open(prevPath)
            prev = prev.resize((30, 30))
            prevIcon = ImageTk.PhotoImage(prev)
            prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = fYr_fSem)
            prevBtn.place(x= 140, y=395, width= 30, height=30)
            prevBtn.config(highlightthickness=1, highlightbackground='black')
            prevBtn.image = prevIcon
            
            next = Image.open(nextPath)
            next = next.resize((30, 30))
            nextIcon = ImageTk.PhotoImage(next)
            nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = fYr_fSem)
            nextBtn.place(x= 378, y=395, width= 30, height=30)
            nextBtn.config(highlightthickness=1, highlightbackground='black')
            nextBtn.image = nextIcon
    
    #SECOND YEAR - FIRST SEM
    elif int(decrypt(currStu_yr)) == 2 and int(decrypt(currStu_sem)) == 1:
            
            #BUTTONS
            prev = Image.open(prevPath)
            prev = prev.resize((30, 30))
            prevIcon = ImageTk.PhotoImage(prev)
            prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = fYr_fSem)
            prevBtn.place(x= 140, y=395, width= 30, height=30)
            prevBtn.config(highlightthickness=1, highlightbackground='black')
            prevBtn.image = prevIcon
            
            next = Image.open(nextPath)
            next = next.resize((30, 30))
            nextIcon = ImageTk.PhotoImage(next)
            nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = fYr_sSem)
            nextBtn.place(x= 378, y=395, width= 30, height=30)
            nextBtn.config(highlightthickness=1, highlightbackground='black')
            nextBtn.image = nextIcon                 
    
    #SECOND YEAR - SECOND SEM
    elif int(decrypt(currStu_yr)) == 2 and int(decrypt(currStu_sem)) == 2:
            
            #BUTTONS
            prev = Image.open(prevPath)
            prev = prev.resize((30, 30))
            prevIcon = ImageTk.PhotoImage(prev)
            prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = fYr_fSem)
            prevBtn.place(x= 140, y=395, width= 30, height=30)
            prevBtn.config(highlightthickness=1, highlightbackground='black')
            prevBtn.image = prevIcon
            
            next = Image.open(nextPath)
            next = next.resize((30, 30))
            nextIcon = ImageTk.PhotoImage(next)
            nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = sYr_fSem)
            nextBtn.place(x= 378, y=395, width= 30, height=30)
            nextBtn.config(highlightthickness=1, highlightbackground='black')
            nextBtn.image = nextIcon
    
    #THIRD YEAR - FIRST SEM
    elif int(decrypt(currStu_yr)) == 3 and int(decrypt(currStu_sem)) == 1:
            
            #BUTTONS
            prev = Image.open(prevPath)
            prev = prev.resize((30, 30))
            prevIcon = ImageTk.PhotoImage(prev)
            prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = fYr_fSem)
            prevBtn.place(x= 140, y=395, width= 30, height=30)
            prevBtn.config(highlightthickness=1, highlightbackground='black')
            prevBtn.image = prevIcon
            
            next = Image.open(nextPath)
            next = next.resize((30, 30))
            nextIcon = ImageTk.PhotoImage(next)
            nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = sYr_sSem)
            nextBtn.place(x= 378, y=395, width= 30, height=30)
            nextBtn.config(highlightthickness=1, highlightbackground='black')
            nextBtn.image = nextIcon
    
    #THIRD YEAR - SECOND SEM
    elif int(decrypt(currStu_yr)) == 3 and int(decrypt(currStu_sem)) == 2:
            
            #BUTTONS
            prev = Image.open(prevPath)
            prev = prev.resize((30, 30))
            prevIcon = ImageTk.PhotoImage(prev)
            prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = fYr_fSem)
            prevBtn.place(x= 140, y=395, width= 30, height=30)
            prevBtn.config(highlightthickness=1, highlightbackground='black')
            prevBtn.image = prevIcon
            
            next = Image.open(nextPath)
            next = next.resize((30, 30))
            nextIcon = ImageTk.PhotoImage(next)
            nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = tYr_fSem)
            nextBtn.place(x= 378, y=395, width= 30, height=30)
            nextBtn.config(highlightthickness=1, highlightbackground='black')
            nextBtn.image = nextIcon
    
    #FOURTH YEAR - FIRST SEM
    elif int(decrypt(currStu_yr)) == 4 and int(decrypt(currStu_sem)) == 1:
            
            #BUTTONS
            prev = Image.open(prevPath)
            prev = prev.resize((30, 30))
            prevIcon = ImageTk.PhotoImage(prev)
            prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = fYr_fSem)
            prevBtn.place(x= 140, y=395, width= 30, height=30)
            prevBtn.config(highlightthickness=1, highlightbackground='black')
            prevBtn.image = prevIcon
            
            next = Image.open(nextPath)
            next = next.resize((30, 30))
            nextIcon = ImageTk.PhotoImage(next)
            nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = tYr_sSem)
            nextBtn.place(x= 378, y=395, width= 30, height=30)
            nextBtn.config(highlightthickness=1, highlightbackground='black')
            nextBtn.image = nextIcon
    
    #FOURTH YEAR - SECOND SEM        
    elif int(decrypt(currStu_yr)) == 4 and int(decrypt(currStu_sem)) == 2:
            
            #BUTTONS
            prev = Image.open(prevPath)
            prev = prev.resize((30, 30))
            prevIcon = ImageTk.PhotoImage(prev)
            prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = fYr_fSem)
            prevBtn.place(x= 140, y=395, width= 30, height=30)
            prevBtn.config(highlightthickness=1, highlightbackground='black')
            prevBtn.image = prevIcon
            
            next = Image.open(nextPath)
            next = next.resize((30, 30))
            nextIcon = ImageTk.PhotoImage(next)
            nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = foYr_fSem)
            nextBtn.place(x= 378, y=395, width= 30, height=30)
            nextBtn.config(highlightthickness=1, highlightbackground='black')
            nextBtn.image = nextIcon
    elif int(decrypt(currStu_yr)) == 1 and currStu_sem == 1:
        pass
    else:
        print("Invalid")  #SINCE IT IS ONLY A 4 YEAR COURSE       
                         
    contBtn = Button(sframe, text="BACK TO MAIN MENU", font = font1, fg=MICSColor2, bg= MICSColor1, command= mainWindow)
    contBtn.place(x=190, y=395, width= 170, height=30)
    
#UPDATE STUDENT INFORMATIONS    
def updateInfo():
    frame = Frame(root, width= 550, height= 500, relief = GROOVE, bg = MICSColor2)
    frame.place(x=250, y=0)
    
    lb = Label(frame, text= "Update Student Information", font = headFont, fg= MICSColor2, bg = MICSColor1)
    lb.place(x=0, y=0, width= 550, height= 50)
    lb.config(highlightthickness=1, highlightbackground=MICSColor1)
    
    #LABELS
    stuName = Label(frame, text="Student's Name:", font= font1, fg= fontc1, bg= MICSColor2)
    stuName.place(x=10, y=65, width= 120, height= 25)
    lLabel = Label(frame, text="Last Name", font= font3, fg= fontc1, bg= MICSColor2)
    lLabel.place(x=20, y=120, width= 160, height= 25)
    fLabel = Label(frame, text="First Name", font= font3, fg= fontc1, bg= MICSColor2)
    fLabel.place(x=190, y=120, width= 160, height= 25)
    mLabel = Label(frame, text="Middle Name", font= font3, fg= fontc1, bg= MICSColor2)
    mLabel.place(x=360, y=120, width= 160, height= 25)
    sex = Label(frame, text="Sex:", font= font1, fg= fontc1, bg= MICSColor2)
    sex.place(x=15, y=160, height= 25)
    dob = Label(frame, text="Date of Birth [MM-DD-YYYY]:", font= font1, fg= fontc1, bg= MICSColor2)
    dob.place(x=190, y=160, height= 25)
    email = Label(frame, text="Email Address:", font= font1, fg= fontc1, bg= MICSColor2)
    email.place(x=15, y=200, height= 25)
    phoneNo = Label(frame, text="Mobile Number:", font= font1, fg= fontc1, bg= MICSColor2)
    phoneNo.place(x=300, y=200, height= 25)
    address = Label(frame, text="Student's Address:", font= font1, fg= fontc1, bg= MICSColor2)
    address.place(x=15, y=270, height= 25)
    gEmail = Label(frame, text="Guardian Email Address:", font= font1, fg= fontc1, bg= MICSColor2)
    gEmail.place(x=15, y=340, height= 25)
    gPhoneNo = Label(frame, text="Guardian Mobile Number:", font= font1, fg= fontc1, bg= MICSColor2)
    gPhoneNo.place(x=300, y=340, height= 25)
    
    #ENTRY VALUE
    lnameValue = StringVar()
    fnameValue = StringVar()
    mnameValue = StringVar()
    dobValue = StringVar()
    emailValue = StringVar()
    phoneNoValue = StringVar()
    addressValue = StringVar()
    gEmailValue = StringVar()
    gPhoneNoValue = StringVar()
    
    if decrypt(currStu_sex) == 'F':
        gender = 'Female'
    else:
        gender = 'Male'

    #SET VALUE
    lnameValue.set(decrypt(currStu_lName)) 
    fnameValue.set(decrypt(currStu_fName))
    mnameValue.set(decrypt(currStu_mName)) 
    dobValue.set(decrypt(currStu_dob))
    emailValue.set(decrypt(currStu_email))
    phoneNoValue.set(decrypt(currStu_num))
    addressValue.set(decrypt(currStu_address))
    gEmailValue.set(decrypt(currStu_gEmail))
    gPhoneNoValue.set(decrypt(currStu_gNum))
     
    
    #INPUT ENTRY
    lnameEntry = Entry(frame, textvariable= lnameValue, font = font2, bd= 2, state= "readonly")
    lnameEntry.place(x=20, y=95, width= 160, height= 25) 
    fnameEntry = Entry(frame, textvariable= fnameValue, font = font2, bd= 2, state= "readonly")
    fnameEntry.place(x=190, y=95, width= 160, height= 25) 
    mnameEntry = Entry(frame, textvariable= mnameValue, font = font2, bd= 2, state= "readonly")
    mnameEntry.place(x=360, y=95, width= 160, height= 25) 
    genderEntry= Combobox(frame, values=['Female', 'Male'], font= font2,  state="disabled")
    genderEntry.set(gender) 
    genderEntry.place(x=60, y= 160, width= 100, height= 25)
    dobEntry = Entry(frame, textvariable= dobValue, font = font2, bd= 2, state= "readonly")
    dobEntry.place(x=380, y=160, width= 130, height= 25) 
    emailEntry = Entry(frame, textvariable= emailValue, font = font2, bd= 2, )
    emailEntry.place(x=20, y=230, width= 245, height= 25) 
    phoneNoEntry = Entry(frame, textvariable= phoneNoValue, font = font2, bd= 2, )
    phoneNoEntry.place(x=305, y=230, width= 160, height= 25) 
    addressEntry = Entry(frame, textvariable= addressValue, font = font2, bd= 2, )
    addressEntry.place(x=20, y=305, width= 470, height= 25) 
    gEmailEntry = Entry(frame, textvariable= gEmailValue, font = font2, bd= 2, )
    gEmailEntry.place(x=20, y=375, width= 245, height= 25) 
    gPhoneNoEntry = Entry(frame, textvariable= gPhoneNoValue, font = font2, bd= 2, )
    gPhoneNoEntry.place(x=305, y=375, width= 180, height= 25) 
    
    def submitChanges():
        global currStu_email, currStu_num, currStu_address, currStu_gEmail, currStu_gNum

        # Get the updated values from the entry widgets
        new_email = emailValue.get()
        new_phone = phoneNoValue.get()
        new_address = addressValue.get()
        new_gEmail = gEmailValue.get()
        new_gPhone = gPhoneNoValue.get()
        
        # Update the variables with the new values
        currStu_num = encrypt_w_ok(new_phone)
        currStu_email = encrypt_w_ok(new_email)
        currStu_address = encrypt_w_ok(new_address)
        currStu_gEmail = encrypt_w_ok(new_gPhone)
        currStu_gNum = encrypt_w_ok(new_gPhone)
        
        current_student[10] = encrypt_w_ok(new_phone)
        current_student[11] = encrypt_w_ok(new_email)
        current_student[12] = encrypt_w_ok(new_address)
        current_student[13] = encrypt_w_ok(new_gPhone)
        current_student[14] = encrypt_w_ok(new_gPhone)

        current_datetime = datetime.datetime.now()
        sys_list.add_to_stud_log([currStu_id, encrypt_w_ok("Update student information"), 
                                  encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])

        messagebox.showinfo("Success", "Changes Submitted Successfully!")
        mainWindow()
    
    #BUTTONS
    submitBtn = Button(frame, text= "SUBMIT", font = font1, fg=MICSColor2, bg= MICSColor1, command= submitChanges)
    submitBtn.place(x=290, y=430, width= 100, height=30)
    backBtn = Button(frame, text="BACK", font = font1, fg=MICSColor2, bg= MICSColor1, command= mainWindow)
    backBtn.place(x=140, y=430, width= 100, height=30)

def enroll():
    
    enrollment_check = 1

    frame = Frame(root, width= 550, height= 500, relief = GROOVE, bg = MICSColor2)
    frame.place(x=250, y=0)
    
    lb = Label(frame, text= "Enrollment", font = headFont, fg= 'white', bg = MICSColor1)
    lb.place(x=0, y=0, width= 550, height= 35)
    lb.config(highlightthickness=1, highlightbackground=MICSColor1)
    
    #CUSTOM FONT AND COLOR
    f1 = "Arial 11 bold"
    c1= "black"
     
    total_grade = 0
    total_units = 0

    currCrsList = sys_list.get_curr_course_list()
    for course in currCrsList:
        x = float(decrypt(course[2])) * int(decrypt(course[1]))

        # Update the total grade points and total units
        total_grade += x
        total_units += int(decrypt(course[1]))

    # Calculate the GPA
    gpa = total_grade / total_units
    gpa = round(gpa, 2)
    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + ". " + decrypt(currStu_lName)
     
    #LABELS
    stuNameLabel = Label(frame, text="Student's Name:", font= f1, fg= MICSColor1, bg= MICSColor2)
    stuNameLabel.place(x=10, y=40)
    stuNumLabel = Label(frame, text="Student No:", font= f1, fg= MICSColor1, bg= MICSColor2)
    stuNumLabel.place(x=10, y=60)
    stuYrLabel = Label(frame, text="Year:", font= f1, fg= MICSColor1, bg= MICSColor2)
    stuYrLabel.place(x=332, y=60)
    stuSemLabel = Label(frame, text="Sem:", font= f1, fg= MICSColor1, bg= MICSColor2)
    stuSemLabel.place(x=400, y=60)
    statusLabel = Label(frame, text="Scholastic Status:", font= f1, fg= MICSColor1, bg= MICSColor2)
    statusLabel.place(x=10, y=80)
    gpaLabel = Label(frame, text="GPA:", font= f1, fg= MICSColor1, bg= MICSColor2)
    gpaLabel.place(x=350, y=80)   
    
    #LABEL INPUT
    stuNameInput = Label(frame, text= decrypt(fullName), font= font1, fg= c1, bg= MICSColor2)
    stuNameInput.place(x=135, y=41) 
    stuNumInput = Label(frame, text= decrypt(currStu_id), font= font1, fg= c1, bg= MICSColor2)
    stuNumInput.place(x=105, y=61) 
    stuYrInput = Label(frame, text= decrypt(currStu_yr), font= font1, fg= c1, bg= MICSColor2)
    stuYrInput.place(x=380, y=61) 
    stuSemInput = Label(frame, text= decrypt(currStu_sem), font= font1, fg= c1, bg= MICSColor2)
    stuSemInput.place(x=448, y=61) 
    statusInput = Label(frame, text= decrypt(currStu_status), font= font1, fg= c1, bg= MICSColor2)
    statusInput.place(x=145, y=81) 
    gpaInput = Label(frame, text= gpa, font= font1, fg= c1, bg= MICSColor2)
    gpaInput.place(x=398, y=81) 
    
    
    #DISPLAYING GRADES OF CURRENT COURSES
    crsCodeLabel = Label(frame, text="Course Code", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsCodeLabel.place(x=15, y=115, width = 110, height= 30)
    crsUnitLabel = Label(frame, text="Unit", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsUnitLabel.place(x=125, y=115, width = 60, height= 30)
    crsGradeLabel = Label(frame, text="Grade", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsGradeLabel.place(x=185, y=115, width = 65, height= 30)
    facultyLabel = Label(frame, text="Faculty", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    facultyLabel.place(x=250, y=115, width = 195, height= 30)
    remarksLabel = Label(frame, text="Remarks", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    remarksLabel.place(x=445, y=115, width = 90, height= 30)   
    
    currCrsList = sys_list.get_curr_course_list()
    for index, course in enumerate(currCrsList):
        grade = float(decrypt(course[2]))
    
        yPos = index * 22

        if grade == 0.00:
            enrollment_check = -1
        
        if grade == 0.00 or grade == 0 or grade == 0.0:
            remarks = "-"
        elif grade <= 3.00 :
            remarks = "PASSED"
        else:
            remarks = "FAILED"
        
        crsCodeLBL = Label(frame, text= decrypt(course[0]), font=font2, fg= c1, bg=MICSColor2, borderwidth=1, relief="solid")
        crsCodeLBL.place(x=15, y=145 + yPos, width=110, height=22)
            
        crsUnitLBL = Label(frame, text= decrypt(course[1]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        crsUnitLBL.place(x=125, y=145 + yPos, width=60, height=22)
            
        crsGradeLBL = Label(frame, text= "{:.2f}".format(grade), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        crsGradeLBL.place(x=185, y=145 + yPos, width=65, height=22)
            
        facultyLBL = Label(frame, text= decrypt(course[3]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        facultyLBL.place(x=250, y=145 + yPos, width=195, height=22)

        remarksLBL = Label(frame, text= remarks, font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        remarksLBL.place(x=445, y=145 + yPos, width=90, height=22)

    enrlBtn = Button(frame, text = "ENROLL", font = font1, fg=MICSColor2, bg= MICSColor1)

    def enroll_student(event):
        select_new_subs()
        enroll()

        cframe = Toplevel()
        cframe.geometry("500x150")

        global currStu_yr
        global currStu_sem

        stud_det = sys_list.get_current_student()
        syear = stud_det[4]
        ssem = stud_det[5]

        currStu_yr = syear
        currStu_sem = ssem

        congratsText = "Congratulations! You are now enrolled for\nYear " + decrypt(syear)

        if decrypt(ssem) == 1:
            congratsText += " - 1st Semester"
        else:
            congratsText += " - 2nd Semester"

        cgrts = Label(cframe, text = congratsText, font = ('Arial Bold', 15), bg = MICSColor2, fg = MICSColor1)
        cgrts.place(x = 50, y = 25, width = 400, height = 60)

        okBtn = Button(cframe, text = "CONFIRM", font = ('Arial Bold', 10), bg = MICSColor3, fg = MICSColor2)

        def exit_cframe(event):

            current_datetime = datetime.datetime.now()
            sys_list.add_to_stud_log([currStu_id, encrypt_w_ok("Enroll for YEAR " + decrypt(currStu_yr) + " - SEMESTER " + decrypt(currStu_sem)), 
                                      encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])

            cframe.destroy()

        okBtn.bind("<Button-1>", exit_cframe)
        okBtn.place(x = 175, y = 110, width = 150, height = 30)

        # Frame attributes (Tkinter)
        cframe.configure(bg = MICSColor2)
        cframe.resizable(False, False)
        cframe.mainloop()

    enrlBtn.place(x = 415, y = 450, width = 120, height=30)

    if enrollment_check == -1:
        enrlBtn.config(state = "disabled")
    else:
        enrlBtn.config(state = "normal")
        enrlBtn.bind("<Button-1>", enroll_student)

    contBtn = Button(frame, text = "BACK TO MAIN MENU", font = font1, fg=MICSColor2, bg= MICSColor1, command= mainWindow)
    contBtn.place(x = 15, y = 450, width= 170, height=30)

#DISPLAY ACCOUNT SETTINGS    
def accountSettings():
    frame = Frame(root, width= 550, height= 500, relief = GROOVE, bg = MICSColor2)
    frame.place(x=250, y=0)
    
    x = 'Arial 20 bold'
    
    lb = Label(frame, text= "Manila Institute of Computer Studies", font = headFont, fg= MICSColor2, bg = MICSColor1)
    lb.place(x=0, y=0, width= 550, height= 70)
    lb.config(highlightthickness=1, highlightbackground=MICSColor1)
    
    img = Image.open(imgPath)
    img = img.resize((65, 65))
    logo = ImageTk.PhotoImage(img)
    logolabel = Label(frame, image=logo, bg= MICSColor1)
    logolabel.place(x=25, y=0)
    logolabel.image = logo
    
    img1 = Image.open(img1Path)
    img1 = img1.resize((52, 52))
    logo1 = ImageTk.PhotoImage(img1)
    logo1label = Label(frame, image=logo1, bg= MICSColor1)
    logo1label.place(x=470, y=7)
    logo1label.image = logo1
    
    acc = Label(frame, text= "ACCOUNT SETTINGS", font= x, fg= MICSColor1, bg= MICSColor2)
    acc.place(x= 125, y= 120)
    
    
    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName)
    nameLabel = Label(frame, text= "STUDENT NAME:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    nameLabel.place(x= 30, y= 200)
    name = Label(frame, text= fullName, font= font2, fg= MICSColor1, bg= "white")
    name.place(x= 200, y= 197, width= 300, height= 30)
    
    idLabel = Label(frame, text= "USERNAME:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    idLabel.place(x= 65, y= 250)
    id = Label(frame, text= decrypt(currStu_id), font= font2, fg= MICSColor1, bg= "white")
    id.place(x= 200, y= 247, width= 300, height= 30)
    
    # Create the modified password string with the first letter and asterisks
    first_letter = decrypt(currStu_pass)[0]
    asterisk_string = '*' * (len(currStu_pass) - 1)
    hidden_pass = first_letter + asterisk_string
    
    PassLabel = Label(frame, text= "PASSWORD:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    PassLabel.place(x= 65, y= 300)
    Pass = Label(frame, text= hidden_pass, font= font2, fg= MICSColor1, bg= "white")
    Pass.place(x= 200, y= 297, width= 300, height= 30)
    
    
    #BUTTONS
    chPassBtn = Button(frame, text= "CHANGE PASSWORD", font = font1, fg=MICSColor2, bg= MICSColor1, command= changePass)
    chPassBtn.place(x=288, y=370, width= 200, height=35)
    reqTORBtn = Button(frame, text= "REQUEST TOR", font = font1, fg=MICSColor2, bg= MICSColor1, command= reqTOR)
    reqTORBtn.place(x=62, y=370, width= 200, height=35)
    backBtn = Button(frame, text="BACK TO MAIN MENU", font = font1, fg=MICSColor2, bg= MICSColor3, command= mainWindow)
    backBtn.place(x=165, y=420, width= 220, height=30)
     
#CHANGE PASSWORD    
def changePass():
    frame = Frame(root, width= 550, height= 500, relief = GROOVE, bg = MICSColor2)
    frame.place(x=250, y=0)
    
    f1 = 'Arial 20 bold'
    f2 = 'Arial 11 bold'
    
    lb = Label(frame, text= "Manila Institute of Computer Studies", font = headFont, fg= MICSColor2, bg = MICSColor1)
    lb.place(x=0, y=0, width= 550, height= 70)
    lb.config(highlightthickness=1, highlightbackground=MICSColor1)
    
    img = Image.open(imgPath)
    img = img.resize((65, 65))
    logo = ImageTk.PhotoImage(img)
    logolabel = Label(frame, image=logo, bg= MICSColor1)
    logolabel.place(x=25, y=0)
    logolabel.image = logo
    
    img1 = Image.open(img1Path)
    img1 = img1.resize((52, 52))
    logo1 = ImageTk.PhotoImage(img1)
    logo1label = Label(frame, image=logo1, bg= MICSColor1)
    logo1label.place(x=470, y=7)
    logo1label.image = logo1
    
    acc = Label(frame, text= "CHANGE PASSWORD", font= f1, fg= MICSColor1, bg= MICSColor2)
    acc.place(x= 125, y= 120)
    
    midFrame = Label(frame, text="", bg = MICSColor1)
    midFrame.place(x=35, y=180, width= 480, height= 220)
    midFrame.config(highlightthickness=1, highlightbackground=MICSColor1)
    
    #LABEL
    oldPassLabel = Label(frame, text= "ENTER OLD PASSWORD:", font= f2, fg= MICSColor2, bg= MICSColor1)
    oldPassLabel.place(x= 82, y= 220)
    newPassLabel = Label(frame, text= "ENTER NEW PASSWORD:", font= f2, fg= MICSColor2, bg= MICSColor1)
    newPassLabel.place(x= 80, y= 280)
    re_newPassLabel = Label(frame, text= "CONFIRM NEW PASSWORD:", font= f2, fg= MICSColor2, bg= MICSColor1)
    re_newPassLabel.place(x= 60, y= 340)
    
    #ENTRY VALUE
    oldPass = StringVar()
    newPass = StringVar()
    re_newPass = StringVar()
    
    #INPUT ENTRY
    oldPassEntry = Entry(frame, textvariable= oldPass, font = font4, bd= 2, show= '✱')
    oldPassEntry.place(x=290, y=217, width= 200, height= 28) 
    newPassEntry = Entry(frame, textvariable= newPass, font = font4, bd= 2, show= '✱')
    newPassEntry.place(x=290, y=277, width= 200, height= 28) 
    re_newPassEntry = Entry(frame, textvariable= re_newPass, font = font4, bd= 2, show= '✱' )
    re_newPassEntry.place(x=290, y=337, width= 200, height= 28) 
    
    def submitChange():
        global currStu_pass, current_student
        
        # Get the values entered in the entry fields
        old_password = oldPass.get()
        new_password = newPass.get()
        confirm_password = re_newPass.get()
        
        #CHANGE PASSWORD
        if old_password != decrypt(currStu_pass):
            oldPass.set('') # Clear the entry fields
            newPass.set('')
            re_newPass.set('')
            print("incorect password")
            messagebox.showerror("Incorrect Password", "The entered old password is incorrect.")
        else:
            if new_password != confirm_password:
                newPass.set('')
                re_newPass.set('')
                print("password mismatched")
                messagebox.showerror("Password Mismatch", "The entered new passwords do not match.")
            else:
                # Update the password
                messagebox.showinfo("Password Changed", "Your password has been successfully changed.")
                currStu_pass = encrypt_w_ok(new_password)
                current_student[6] = encrypt_w_ok(new_password)

                current_datetime = datetime.datetime.now()
                sys_list.add_to_stud_log([currStu_id, encrypt_w_ok("Update password"), 
                                          encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])

                mainWindow()

    #BUTTONS
    submitBtn = Button(frame, text= "CHANGE PASSWORD", font = font1, fg=MICSColor2, bg= MICSColor1, command= submitChange)
    submitBtn.place(x=240, y=420, width= 220, height=35)
    backBtn = Button(frame, text="CANCEL", font = font1, fg=MICSColor2, bg= MICSColor1, command= accountSettings)
    backBtn.place(x=90, y=420, width= 100, height=35)

#SEARCH IF THE STUDENT HAS REQUESTED A TOR
def search_request():
    for student_data in sys_list.stud_tor_req_list:
        if student_data[0] == currStu_id:
            return True
    return False   

#DELETE TOR REQUEST
def delete_tor_request():
    for student_data in SystemList.stud_tor_req_list:
        if student_data[0] == currStu_id:
            SystemList.stud_tor_req_list.remove(student_data)
            print(f"Student with number {decrypt(currStu_id)} deleted.")
            break
    else:
        print(f"Student with number {decrypt(currStu_id)} not found.")

#FOR REQUESTING TRANSCRIPT OF RECORDS
def reqTOR():
    
    topFrame = Frame(root, width=550, height=70, relief=GROOVE)
    topFrame.place(x=250, y=0)
    
    sframe = Frame(root, width= 550, height= 430, relief = GROOVE, bg = MICSColor2)
    sframe.place(x=250, y=70) 
    
    f1 = 'Arial 20 bold'
    
    lb = Label(topFrame, text= "Manila Institute of Computer Studies", font = headFont, fg= MICSColor2, bg = MICSColor1)
    lb.place(x=0, y=0, width= 550, height= 70)
    lb.config(highlightthickness=1, highlightbackground=MICSColor1)
    
    img = Image.open(imgPath)
    img = img.resize((65, 65))
    logo = ImageTk.PhotoImage(img)
    logolabel = Label(topFrame, image=logo, bg= MICSColor1)
    logolabel.place(x=25, y=0)
    logolabel.image = logo
    
    img1 = Image.open(img1Path)
    img1 = img1.resize((52, 52))
    logo1 = ImageTk.PhotoImage(img1)
    logo1label = Label(topFrame, image=logo1, bg= MICSColor1)
    logo1label.place(x=470, y=7)
    logo1label.image = logo1
    
    exists = search_request()
    
    if exists: #there is a pending request    
        tor_pending()
    else: #There is no pending request for this student
        mode = Label(sframe, text= "REQUEST FOR TOR", font= f1, fg= MICSColor1, bg= MICSColor2)
        mode.place(x= 125, y= 50)
        
        #LABELS
        stuNameLabel = Label(sframe, text="*Student Name:", font= subheadFont1, fg= MICSColor1, bg= MICSColor2)
        stuNameLabel.place(x=78, y=120, width= 120, height= 30)
        stuIDLabel = Label(sframe, text="*Student ID:", font= subheadFont1, fg= MICSColor1, bg= MICSColor2)
        stuIDLabel.place(x=92, y=165, width= 120, height= 30)
        emailLabel = Label(sframe, text="*Email Address:", font= subheadFont1, fg= MICSColor1, bg= MICSColor2)
        emailLabel.place(x=80, y=210, width= 120, height= 30)
        purposeLabel = Label(sframe, text="*Purpose:", font= subheadFont1, fg= MICSColor1, bg= MICSColor2)
        purposeLabel.place(x=100, y=255, width= 120, height= 30)
        
        #DECLARE VARIABLES
        stuNameValue = StringVar()
        stuIDValue = StringVar()
        emailValue = StringVar()
        purposeValue = StringVar()
        
        #INPUT ENTRY
        stuNameEntry = Entry(sframe, textvariable= stuNameValue, font = font2, bd= 2)
        stuNameEntry.place(x=220, y=120, width= 250, height= 30) 
        stuIDEntry = Entry(sframe, textvariable= stuIDValue, font = font2, bd= 2)
        stuIDEntry.place(x=220, y=165, width= 250, height= 30) 
        emailEntry = Entry(sframe, textvariable= emailValue, font = font2, bd= 2)
        emailEntry.place(x=220, y=210, width= 250, height= 30) 
        purposeEntry = Entry(sframe, textvariable= purposeValue, font = font2, bd= 2)
        purposeEntry.place(x=220, y=255, width= 250, height= 30) 
        
        def request():
            
            # Get the updated values from the entry widgets
            name = stuNameValue.get()
            id = stuIDValue.get()
            email = emailValue.get()
            purpose = purposeValue.get()
            
            current_date = datetime.date.today() #Get the current date
            formatted_date = current_date.strftime('%m/%d/%Y') #Format the date as a string
            
            if name == "" or id == "" or email == "" or purpose == "":
                messagebox.showwarning("Missing Information", "Please fill in all the required fields.")
                return
            else: 
                studDet = [encrypt_w_ok(id), encrypt_w_ok(name), encrypt_w_ok(email), 
                           encrypt_w_ok(purpose), encrypt_w_ok(formatted_date), encrypt_w_ok("PENDING")]
                sys_list.add_to_stud_tor_req_list(studDet)
                save_torRequest_List()
                messagebox.showinfo("Success", "TOR REQUEST SUBMITTED!")

                current_datetime = datetime.datetime.now()
                sys_list.add_to_stud_log([currStu_id, encrypt_w_ok("TOR Request"), 
                                          encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])

                accountSettings()
        
        #BUTTONS
        reqBtn = Button(sframe, text= "REQUEST", font = font1, fg=MICSColor2, bg= MICSColor1, command= request)
        reqBtn.place(x=150, y=315, width= 250, height=30)
        cancelBtn = Button(sframe, text="CANCEL", font = font1, fg=MICSColor2, bg= MICSColor3, command= accountSettings)
        cancelBtn.place(x=200, y=360, width= 150, height=30)

#IF PENDING REQUEST EXISTS
def tor_pending():
    sframe = Frame(root, width= 550, height= 430, relief = GROOVE, bg = MICSColor2)
    sframe.place(x=250, y=70) 
    
    f1 = 'Arial 20 bold'

    mode = Label(sframe, text= "REQUEST FOR TOR", font= f1, fg= MICSColor1, bg= MICSColor2)
    mode.place(x= 125, y= 50)

    for item in SystemList().return_stud_tor_req_list():
        if currStu_id == item[0]:
            statusValue = decrypt(item[5])
    
    #LABELS
    statLabel = Label(sframe, text="Status:", font= headFont, fg= "black", bg= MICSColor2)
    statLabel.place(x=60, y=140, width= 120, height= 35)
    statLabel = Label(sframe, text= statusValue, font= headFont, fg= MICSColor1, bg= "white")
    statLabel.place(x=220, y=140, width= 280, height= 35)
    
    #BUTTONS
    downloadTORBtn = Button(sframe, text= "DOWNLOAD TOR", font = headFont, fg=MICSColor2, bg= MICSColor1, command= generateTOR)
    downloadTORBtn.place(x=175, y=220, width= 200, height=80)
    
    if statusValue == "PENDING":
        downloadTORBtn.config(state=tk.DISABLED)

    backBtn = Button(sframe, text="BACK", font = font1, fg=MICSColor2, bg= MICSColor3, command= accountSettings)
    backBtn.place(x=150, y=340, width= 250, height=35)
 
#CALCULATE GPA 
def calculate_gpa(start_index, end_index):
    total_units = 0
    total_grade = 0
    allCrs = sys_list.get_all_course_list()
    
    for index, course in enumerate(allCrs[start_index:], start = start_index):
   
        #CACULATE GPA    
        x = float(decrypt(course[2])) * int(decrypt(course[1])) # grade * units
        total_grade += x
        total_units += int(decrypt(course[1]))
        
        if index == end_index:
            break
        
    # Calculate the GPA
    gpa = total_grade / total_units
    gpa = round(gpa, 2)
    return gpa 
    
#GENERATE TOR IN PDF    
def generateTOR():
    
    class CustomPDF(FPDF): # Create a custom class inheriting from FPDF
        
        def header(self):
            parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            header = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "tor_header.png")
            pdf.image(header, x=15, y=15, w=180, h=40)
        
        def get_unique_filename(self, filename):
            base, ext = os.path.splitext(filename)
            suffix = 1
            while os.path.exists(filename):
                filename = f"{base}({suffix}){ext}"
                suffix += 1
            return filename
        
        def get_text_width(self, text, font_family, font_style, font_size):
            self.set_font(font_family, font_style, font_size)
            return self.get_string_width(text) * self.k

    # Create a PDF object and add a page
    pdf = FPDF('P', 'mm', 'Letter')
    pdf = CustomPDF()
    pdf.add_page()
    pdf.set_margins(left=72, top=72, right=72)
    
    #CONTENT OF PDF HERE
    # Set font and size for text
    font_family = 'Arial'
    font_style = 'B'
    font_size = 11
    x = 10  
    y = 65  
    
    fullname = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName)
    
    pdf.set_font(font_family, font_style, font_size)
    pdf.text(x, y, "Name: " + fullname)
    pdf.text(x, y + 6, "Student No: " + decrypt(currStu_id))
    pdf.text(x, y + 12, "Course: Bachelor of Science in Computer Science")
    
    # Add table header
    header = ['COURSE CODE', 'COURSE DESCRIPTION', 'GRADE', 'CREDITS' ]
    column_widths = [35, 115, 20, 20]  # Widths for each column
    pdf.set_fill_color(200, 200, 200)  # Set fill color for header
    pdf.set_y(82)
    pdf.set_x(10)
    pdf.cell(column_widths[0], 9, header[0], 1, 0, 'C', True)  # Course Code
    pdf.cell(column_widths[1], 9, header[1], 1, 0, 'C', True)  # Course Description
    pdf.cell(column_widths[2], 9, header[2], 1, 0, 'C', True)  # Grade
    pdf.cell(column_widths[3], 9, header[3], 1, 1, 'C', True)  # Credits
    
    allCrs = sys_list.get_all_course_list()
    data = []
        
    for course in allCrs:
        grade = float(decrypt(course[2])) # Grade
        if grade == 0.0 or grade == 0.00:
            grade = "-"
        else:
            grade = "{:.2f}".format(grade)  # Format grade to 2 decimal places
    
        data.append([decrypt(course[0]), subj_def(decrypt(course[0])), grade, decrypt(course[1])])
    
    pdf.set_font(font_family, "", 10)
    for i, row in enumerate(data):
        if i == 0 and i + 1 < len(data):
            pdf.set_fill_color(234, 234, 234)
            pdf.set_x(10)  # Set the x position for the next row
            pdf.set_font(font_family, font_style, 10)
            pdf.multi_cell(column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], 7, f"1ST YEAR - 1ST SEMESTER\t\t\t\t\t\t GPA: {calculate_gpa(0, 3)}", 'LTRB', 'C', True) 
        
        pdf.set_fill_color(255, 255, 255)
        pdf.set_x(10)  # Set the initial x position for each row
        pdf.cell(column_widths[0], 7, row[0], 1, 0, 'L', True)  # Course Code
        pdf.cell(column_widths[1], 7, row[1], 1, 0, 'L', True)  # Course Description
        pdf.cell(column_widths[2], 7, str(row[2]), 1, 0, 'C', True)  # Grade
        pdf.cell(column_widths[3], 7, str(row[3]), 1, 1, 'C', True)  # Credits

        if i == 3 and i + 1 < len(data):
            pdf.set_fill_color(234, 234, 234)
            pdf.set_x(10)  # Set the x position for the next row
            pdf.multi_cell(column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], 7, f"1ST YEAR - 2ND SEMESTER\t\t\t\t\t\t GPA: {calculate_gpa(4, 8)}", 1, 'C', True) 
        if i == 8 and i + 1 < len(data):
            pdf.set_fill_color(234, 234, 234)
            pdf.set_x(10)  # Set the x position for the next row
            pdf.multi_cell(column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], 7, f"2ND YEAR - 1ST SEMESTER\t\t\t\t\t\t GPA: {calculate_gpa(9, 16)}", 1, 'C', True) 
        if i == 16 and i + 1 < len(data):
            pdf.set_fill_color(234, 234, 234)
            pdf.set_x(10)  # Set the x position for the next row
            pdf.multi_cell(column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], 7, f"2ND YEAR - 2ND SEMESTER\t\t\t\t\t\t GPA: {calculate_gpa(17, 27)}", 1, 'C', True) 
        if i == 27 and i + 1 < len(data):
            pdf.set_fill_color(234, 234, 234)
            pdf.set_x(10)  # Set the x position for the next row
            pdf.multi_cell(column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], 7, f"3RD YEAR - 1ST SEMESTER\t\t\t\t\t\t GPA: {calculate_gpa(28, 36)}", 1, 'C', True) 
        if i == 36 and i + 1 < len(data):
            pdf.set_fill_color(234, 234, 234)
            pdf.set_x(10)  # Set the x position for the next row
            pdf.multi_cell(column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], 7, f"3RD YEAR - 2ND SEMESTER\t\t\t\t\t\t GPA: {calculate_gpa(37, 45)}", 1, 'C', True) 
        if i == 45 and i + 1 < len(data):
            pdf.set_fill_color(234, 234, 234)
            pdf.set_x(10)  # Set the x position for the next row
            pdf.multi_cell(column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], 7, f"4TH YEAR - 1ST SEMESTER\t\t\t\t\t\t GPA: {calculate_gpa(46, 47)}", 1, 'C', True) 
        if i == 47 and i + 1 < len(data):
            pdf.set_fill_color(234, 234, 234)
            pdf.set_x(10)  # Set the x position for the next row
            pdf.multi_cell(column_widths[0] + column_widths[1] + column_widths[2] + column_widths[3], 7, f"4TH YEAR - 2ND SEMESTER\t\t\t\t\t\t GPA: {calculate_gpa(48, 49)}", 1, 'C', True) 
        
    parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    footer = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "signatures.png")
    pdf.image(footer, x = 26, y = pdf.get_y() + 10, w = 150, h = 30)
    
    # Save the PDF to student's desktop
    desktop_path = str(Path.home() / "Desktop")
    filename = currStu_id + "_TOR.pdf"
    file_path = os.path.join(desktop_path, filename)
    file_path = pdf.get_unique_filename(file_path)
    pdf.output(file_path)
    
    delete_tor_request()
    save_torRequest_List()

    current_datetime = datetime.datetime.now()
    sys_list.add_to_stud_log([currStu_id, encrypt_w_ok("TOR Download"), 
                              encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])

    messagebox.showinfo("Success", "TOR downloaded successfully. [" + file_path + "]")
    
#LOG OUT    
def logOut():
    global root

    current_datetime = datetime.datetime.now()
    sys_list.add_to_stud_log([currStu_id, encrypt_w_ok("Log-out"), encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])
    
    save_indiv_stud_info()
    save_all_stud_course_info()

    save_torRequest_List()
    
    save_admin_log()
    save_student_log()

    save_key()
    
    root.destroy()

#SAVE CURRENT SCHEDULE TO DESKTOP
def saveSchedule():
    currCrsList = sys_list.get_curr_course_list()
    pdf = FPDF('P', 'mm', 'Letter')

    pdf.add_page()

    pdf.set_font('helvetica', 'B', 11)

    x = 10
    y = 65

    pdf.text(x, y, 'Name: ' + decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName))
    pdf.text(x, y + 6, "Student No: " + decrypt(currStu_id))
    pdf.text(x, y + 12, "Course: Bachelor of Science in Computer Science")
    pdf.text(x, y + 24, "YEAR: " + decrypt(currStu_yr))
    pdf.text(x + 20, y + 24, "SEMESTER: " + decrypt(currStu_sem))

    pdf.set_font('helvetica', 'B', 9)
    
    headers = ['SUBJECT CODE', 'DESCRIPTION', 'UNITS', 'FACULTY', 'DAY', 'TIME']
    col_widths = [35, 65, 15, 35, 15, 35]
    pdf.set_fill_color(200, 200, 200)
    pdf.set_y(92)
    pdf.set_x(10)
    pdf.cell(col_widths[0], 10, headers[0], 1, 0, 'C', True)  # Course Code
    pdf.cell(col_widths[1], 10, headers[1], 1, 0, 'C', True)  # Course Description
    pdf.cell(col_widths[2], 10, headers[2], 1, 0, 'C', True)  # Units
    pdf.cell(col_widths[3], 10, headers[3], 1, 0, 'C', True)  # Faculty
    pdf.cell(col_widths[4], 10, headers[4], 1, 0, 'C', True)  # Day
    pdf.cell(col_widths[5], 10, headers[5], 1, 1, 'C', True)  # Time

    data = []
    for course in currCrsList:
        course_day = ""
        if decrypt(course[4]) == "MONDAY":
            course_day = "M"
        elif decrypt(course[4]) == "TUESDAY":
            course_day = "T"
        elif decrypt(course[4]) == "WEDNESDAY":
            course_day = "W"
        elif decrypt(course[4]) == "THURSDAY":
            course_day = "TH"
        elif decrypt(course[4]) == "FRIDAY":
            course_day = "F"
        elif decrypt(course[4]) == "SATURDAY":
            course_day = "SA"
        elif decrypt(course[4]) == "SUNDAY":
            course_day = "SU"
        else:
            course_day = "-"
        course_time = course[5]

        data.append([decrypt(course[0]), subj_def(decrypt(course[0])), decrypt(course[1]), 
                     decrypt(course[3]), course_day, decrypt(course[5])])

    pdf.set_fill_color(255, 255, 255)
    pdf.set_font('helvetica', '', 7)
    for i, row in enumerate(data):
        
        pdf.set_x(10)  # Set the initial x position for each row
        pdf.cell(col_widths[0], 8, row[0], 1, 0, 'C', True)  # Course Code
        pdf.cell(col_widths[1], 8, row[1], 1, 0, 'C', True)  # Course Description
        pdf.cell(col_widths[2], 8, str(row[2]), 1, 0, 'C', True)  # Course Units
        pdf.cell(col_widths[3], 8, row[3], 1, 0, 'C', True)  # Faculty
        pdf.cell(col_widths[4], 8, row[4], 1, 0, 'C', True)  # Day
        pdf.cell(col_widths[5], 8, row[5], 1, 1, 'C', True)  # Time

    header = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "cor_header.png")
    pdf.image(header, x = 15, y = 15, w = 180, h = 37)

    footer = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "signatures.png")
    pdf.image(footer, x = 26, y = 220, w = 150, h = 30)

    student_folder = os.path.expanduser("~/Desktop")  # Path to the student's desktop folder
    filename = "(" + decrypt(currStu_yr) + " - "+ decrypt(currStu_sem) +")" + decrypt(currStu_lName) + "_COR.pdf"
    file_path = os.path.join(student_folder, filename)
    pdf.output(file_path)

    current_datetime = datetime.datetime.now()
    sys_list.add_to_stud_log([currStu_id, encrypt_w_ok("Save schedule for YEAR " + decrypt(currStu_yr) + " - SEMESTER " + decrypt(currStu_sem)), 
                              encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])

    messagebox.showinfo("Schedule Saved", "Your schedule has been successfully saved.\n[" + file_path+"]")

#FOR DISPLAYING GRADES OF STUDENT PER SEMESTER
#FIRST YEAR FIRST SEM DISPLAY
def fYr_fSem():

    sframe = Frame(root, width= 550, height= 450, relief = GROOVE, bg = MICSColor2)
    sframe.place(x=250, y=50) 

    #CUSTOM FONT AND COLOR
    f1 = "Arial 11 bold"
    c1= "black"
     
    total_grade = 0
    total_units = 0
        
     
    #LABELS
    backgroundLabel = Label(sframe, text = "", bg = MICSColor3, borderwidth=1, relief="solid" )
    backgroundLabel.place(x= 15, y = 30, width = 520, height = 30)
    
    stuNameLabel = Label(sframe, text="Student's Name:", font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameLabel.place(x=25, y=30,  height = 30)
    
    stuYrLabel = Label(sframe, text="Year:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuYrLabel.place(x=26, y=65)
    stuSemLabel = Label(sframe, text="Sem:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuSemLabel.place(x=130, y=65)
    gpaLabel = Label(sframe, text="GPA:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    gpaLabel.place(x=370, y=65)   
    
    
    #FOR 1ST SEM 
    crsCodeLabel = Label(sframe, text="Course Code", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsCodeLabel.place(x=15, y=95, width = 110, height= 30)
    crsUnitLabel = Label(sframe, text="Unit", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsUnitLabel.place(x=125, y=95, width = 60, height= 30)
    crsGradeLabel = Label(sframe, text="Grade", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsGradeLabel.place(x=185, y=95, width = 65, height= 30)
    facultyLabel = Label(sframe, text="Faculty", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    facultyLabel.place(x=250, y=95, width = 195, height= 30)
    remarksLabel = Label(sframe, text="Remarks", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    remarksLabel.place(x=445, y=95, width = 90, height= 30)  
    
    allcurrCourse = sys_list.get_all_course_list()
    for index, course in enumerate(allcurrCourse):  
        yPos=index *22
        
        if float(decrypt(course[2])) == 0.00 or float(decrypt(course[2])) == 0 or float(decrypt(course[2])) == 0.0:
            remarks = "-"
        elif float(decrypt(course[2])) <= 3.00 :
            remarks = "PASSED"
        else:
            remarks = "FAILED"
        
        #CACULATE GPA    
        x = float(decrypt(course[2])) * int(decrypt(course[1]))

        # Update the total grade points and total units
        total_grade += x
        total_units += int(decrypt(course[1]))
        
        crsCodeLBL = Label(sframe, text = decrypt(course[0]), font=font2, fg= c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Code
        crsCodeLBL.place(x=15, y=125 + yPos, width=110, height=22)
        crsUnitLBL = Label(sframe, text = decrypt(course[1]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Units
        crsUnitLBL.place(x=125, y=125 + yPos, width=60, height=22)
        crsGradeLBL = Label(sframe, text = decrypt(course[2]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        crsGradeLBL.place(x=185, y=125 + yPos, width=65, height=22)
        facultyLBL = Label(sframe, text= decrypt(course[3]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        facultyLBL.place(x=250, y=125 + yPos, width=195, height=22)
        remarksLBL = Label(sframe, text= remarks, font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        remarksLBL.place(x=445, y=125 + yPos, width=90, height=22)
        
        if index == 3: #terminate at 3
            break; 

    # Calculate the GPA
    gpa = total_grade / total_units
    gpa = round(gpa, 2)
    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName)      

    #LABEL INPUT
    stuNameInput = Label(sframe, text= fullName, font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameInput.place(x=160, y=30,  height = 30) 
    
    stuYrInput = Label(sframe, text= "1", font= subheadFont, fg= c1, bg= MICSColor2)
    stuYrInput.place(x=74, y=65) 
    stuSemInput = Label(sframe, text= "1" , font= subheadFont, fg= c1, bg= MICSColor2)
    stuSemInput.place(x=180, y=65) 
    gpaInput = Label(sframe, text= gpa, font= subheadFont, fg= c1, bg= MICSColor2)
    gpaInput.place(x=420, y=65) 
    

    #BUTTONS
    if int(decrypt(currStu_yr)) == 1 and int(decrypt(currStu_sem)) ==2:
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = displayGrades)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
        
    else: 
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = fYr_sSem)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
        
    next = Image.open(nextPath)
    next = next.resize((30, 30))
    nextIcon = ImageTk.PhotoImage(next)
    nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = displayGrades)
    nextBtn.place(x= 378, y=395, width= 30, height=30)
    nextBtn.config(highlightthickness=1, highlightbackground='black')
    nextBtn.image = nextIcon      
    
    contBtn = Button(sframe, text="BACK TO MAIN MENU", font = font1, fg=MICSColor2, bg= MICSColor1, command= mainWindow)
    contBtn.place(x=190, y=395, width= 170, height=30)

#FIRST YEAR SECOND SEM DISPLAY
def fYr_sSem():
    
    sframe = Frame(root, width= 550, height= 450, relief = GROOVE, bg = MICSColor2)
    sframe.place(x=250, y=50) 

    #CUSTOM FONT AND COLOR
    f1 = "Arial 11 bold"
    c1= "black"
     
    total_grade = 0
    total_units = 0

    #LABELS
    backgroundLabel = Label(sframe, text = "", bg = MICSColor3, borderwidth=1, relief="solid" )
    backgroundLabel.place(x= 15, y = 30, width = 520, height = 30)
    
    stuNameLabel = Label(sframe, text="Student's Name:", font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameLabel.place(x=25, y=30,  height = 30)
    
    stuYrLabel = Label(sframe, text="Year:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuYrLabel.place(x=26, y=65)
    stuSemLabel = Label(sframe, text="Sem:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuSemLabel.place(x=130, y=65)
    gpaLabel = Label(sframe, text="GPA:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    gpaLabel.place(x=370, y=65) 
    
    
    crsCodeLabel = Label(sframe, text="Course Code", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsCodeLabel.place(x=15, y=95, width = 110, height= 30)
    crsUnitLabel = Label(sframe, text="Unit", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsUnitLabel.place(x=125, y=95, width = 60, height= 30)
    crsGradeLabel = Label(sframe, text="Grade", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsGradeLabel.place(x=185, y=95, width = 65, height= 30)
    facultyLabel = Label(sframe, text="Faculty", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    facultyLabel.place(x=250, y=95, width = 195, height= 30)
    remarksLabel = Label(sframe, text="Remarks", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    remarksLabel.place(x=445, y=95, width = 90, height= 30)  
    
    allcurrCourse = sys_list.get_all_course_list()
    for index, course in enumerate(allcurrCourse[4:], start = 4):
        adjusted_index = (index - 4)
        yPos= adjusted_index *22
        
        if float(decrypt(course[2])) == 0.00 or float(decrypt(course[2])) == 0 or float(decrypt(course[2])) == 0.0:
            remarks = "-"
        elif float(decrypt(course[2])) <= 3.00 :
            remarks = "PASSED"
        else:
            remarks = "FAILED"
        
        #CACULATE GPA    
        x = float(decrypt(course[2])) * int(decrypt(course[1]))

        # Update the total grade points and total units
        total_grade += x
        total_units += int(decrypt(course[1]))
        
        crsCodeLBL = Label(sframe, text = decrypt(course[0]), font=font2, fg= c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Code
        crsCodeLBL.place(x=15, y=125 + yPos, width=110, height=22)
        crsUnitLBL = Label(sframe, text = decrypt(course[1]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Units
        crsUnitLBL.place(x=125, y=125 + yPos, width=60, height=22)
        crsGradeLBL = Label(sframe, text = decrypt(course[2]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        crsGradeLBL.place(x=185, y=125 + yPos, width=65, height=22)
        facultyLBL = Label(sframe, text= decrypt(course[3]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        facultyLBL.place(x=250, y=125 + yPos, width=195, height=22)
        remarksLBL = Label(sframe, text= remarks, font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        remarksLBL.place(x=445, y=125 + yPos, width=90, height=22)
        
        if index == 8: #terminate at 8
            break; 

    # Calculate the GPA
    gpa = total_grade / total_units
    gpa = round(gpa, 2)
    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName)          

    #LABEL INPUT
    stuNameInput = Label(sframe, text= fullName, font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameInput.place(x=160, y=30,  height = 30) 
    
    stuYrInput = Label(sframe, text= "1", font= subheadFont, fg= c1, bg= MICSColor2)
    stuYrInput.place(x=74, y=65) 
    stuSemInput = Label(sframe, text= "2" , font= subheadFont, fg= c1, bg= MICSColor2)
    stuSemInput.place(x=180, y=65) 
    gpaInput = Label(sframe, text= gpa, font= subheadFont, fg= c1, bg= MICSColor2)
    gpaInput.place(x=420, y=65) 
    
    #BUTTONS
    
    if int(decrypt(currStu_yr)) == 2 and int(decrypt(currStu_sem)) == 1:
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = displayGrades)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
    else: 
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = sYr_fSem)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
         
    next = Image.open(nextPath)
    next = next.resize((30, 30))
    nextIcon = ImageTk.PhotoImage(next)
    nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = fYr_fSem)
    nextBtn.place(x= 378, y=395, width= 30, height=30)
    nextBtn.config(highlightthickness=1, highlightbackground='black')
    nextBtn.image = nextIcon
    
    contBtn = Button(sframe, text="BACK TO MAIN MENU", font = font1, fg=MICSColor2, bg= MICSColor1, command= mainWindow)
    contBtn.place(x=190, y=395, width= 170, height=30)

#SECOND YEAR FIRST SEM DISPLAY
def sYr_fSem():
    sframe = Frame(root, width= 550, height= 450, relief = GROOVE, bg = MICSColor2)
    sframe.place(x=250, y=50) 

    #CUSTOM FONT AND COLOR
    f1 = "Arial 11 bold"
    c1= "black"
    
    total_grade = 0
    total_units = 0
     
    #LABELS
    backgroundLabel = Label(sframe, text = "", bg = MICSColor3, borderwidth=1, relief="solid" )
    backgroundLabel.place(x= 15, y = 30, width = 520, height = 30)
    
    stuNameLabel = Label(sframe, text="Student's Name:", font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameLabel.place(x=25, y=30,  height = 30)
    
    stuYrLabel = Label(sframe, text="Year:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuYrLabel.place(x=26, y=65)
    stuSemLabel = Label(sframe, text="Sem:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuSemLabel.place(x=130, y=65)
    gpaLabel = Label(sframe, text="GPA:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    gpaLabel.place(x=370, y=65)  
    
    crsCodeLabel = Label(sframe, text="Course Code", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsCodeLabel.place(x=15, y=95, width = 110, height= 30)
    crsUnitLabel = Label(sframe, text="Unit", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsUnitLabel.place(x=125, y=95, width = 60, height= 30)
    crsGradeLabel = Label(sframe, text="Grade", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsGradeLabel.place(x=185, y=95, width = 65, height= 30)
    facultyLabel = Label(sframe, text="Faculty", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    facultyLabel.place(x=250, y=95, width = 195, height= 30)
    remarksLabel = Label(sframe, text="Remarks", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    remarksLabel.place(x=445, y=95, width = 90, height= 30)  
    
    allcurrCourse = sys_list.get_all_course_list()
    for index, course in enumerate(allcurrCourse[9:], start= 9):
        adjusted_index = (index - 9)
        yPos= adjusted_index *22
        
        if float(decrypt(course[2])) == 0.00 or float(decrypt(course[2])) == 0 or float(decrypt(course[2])) == 0.0:
            remarks = "-"
        elif float(decrypt(course[2])) <= 3.00 :
            remarks = "PASSED"
        else:
            remarks = "FAILED"
        
        #CACULATE GPA    
        x = float(decrypt(course[2])) * int(decrypt(course[1]))

        # Update the total grade points and total units
        total_grade += x
        total_units += int(decrypt(course[1]))
        
        crsCodeLBL = Label(sframe, text = decrypt(course[0]), font=font2, fg= c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Code
        crsCodeLBL.place(x=15, y=125 + yPos, width=110, height=22)
        crsUnitLBL = Label(sframe, text = decrypt(course[1]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Units
        crsUnitLBL.place(x=125, y=125 + yPos, width=60, height=22)
        crsGradeLBL = Label(sframe, text = decrypt(course[2]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        crsGradeLBL.place(x=185, y=125 + yPos, width=65, height=22)
        facultyLBL = Label(sframe, text= decrypt(course[3]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        facultyLBL.place(x=250, y=125 + yPos, width=195, height=22)
        remarksLBL = Label(sframe, text= remarks, font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        remarksLBL.place(x=445, y=125 + yPos, width=90, height=22)
        
        if index == 16: #terminate at 16
            break; 

    # Calculate the GPA
    gpa = total_grade / total_units
    gpa = round(gpa, 2)
    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName)          

    #LABEL INPUT
    stuNameInput = Label(sframe, text= fullName, font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameInput.place(x=160, y=30,  height = 30) 
    
    stuYrInput = Label(sframe, text= "2", font= subheadFont, fg= c1, bg= MICSColor2)
    stuYrInput.place(x=74, y=65) 
    stuSemInput = Label(sframe, text= "1" , font= subheadFont, fg= c1, bg= MICSColor2)
    stuSemInput.place(x=180, y=65) 
    gpaInput = Label(sframe, text= gpa, font= subheadFont, fg= c1, bg= MICSColor2)
    gpaInput.place(x=420, y=65) 

    #BUTTONS    
    if int(decrypt(currStu_yr)) == 2 and int(decrypt(currStu_sem)) == 2:
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = displayGrades)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
        
    else: 
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = sYr_sSem)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
          
    next = Image.open(nextPath)
    next = next.resize((30, 30))
    nextIcon = ImageTk.PhotoImage(next)
    nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = fYr_sSem)
    nextBtn.place(x= 378, y=395, width= 30, height=30)
    nextBtn.config(highlightthickness=1, highlightbackground='black')
    nextBtn.image = nextIcon       
    
    contBtn = Button(sframe, text="BACK TO MAIN MENU", font = font1, fg=MICSColor2, bg= MICSColor1, command= mainWindow)
    contBtn.place(x=190, y=395, width= 170, height=30)

#SECOND YEAR SECOND SEM DISPLAY    
def sYr_sSem():
    sframe = Frame(root, width= 550, height= 450, relief = GROOVE, bg = MICSColor2)
    sframe.place(x=250, y=50) 

    #CUSTOM FONT AND COLOR
    f1 = "Arial 11 bold"
    c1= "black"
     
    total_grade = 0
    total_units = 0

    #LABELS
    backgroundLabel = Label(sframe, text = "", bg = MICSColor3, borderwidth=1, relief="solid" )
    backgroundLabel.place(x= 15, y = 30, width = 520, height = 30)
    
    stuNameLabel = Label(sframe, text="Student's Name:", font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameLabel.place(x=25, y=30,  height = 30)
    
    stuYrLabel = Label(sframe, text="Year:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuYrLabel.place(x=26, y=65)
    stuSemLabel = Label(sframe, text="Sem:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuSemLabel.place(x=130, y=65)
    gpaLabel = Label(sframe, text="GPA:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    gpaLabel.place(x=370, y=65) 
    
    crsCodeLabel = Label(sframe, text="Course Code", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsCodeLabel.place(x=15, y=95, width = 110, height= 30)
    crsUnitLabel = Label(sframe, text="Unit", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsUnitLabel.place(x=125, y=95, width = 60, height= 30)
    crsGradeLabel = Label(sframe, text="Grade", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsGradeLabel.place(x=185, y=95, width = 65, height= 30)
    facultyLabel = Label(sframe, text="Faculty", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    facultyLabel.place(x=250, y=95, width = 195, height= 30)
    remarksLabel = Label(sframe, text="Remarks", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    remarksLabel.place(x=445, y=95, width = 90, height= 30)  
    
    allcurrCourse = sys_list.get_all_course_list()
    for index, course in enumerate(allcurrCourse[17:], start= 17):
        adjusted_index = (index - 17)
        yPos= adjusted_index *22
        
        if float(decrypt(course[2])) == 0.00 or float(decrypt(course[2])) == 0 or float(decrypt(course[2])) == 0.0:
            remarks = "-"
        elif float(decrypt(course[2])) <= 3.00 :
            remarks = "PASSED"
        else:
            remarks = "FAILED"
        
        #CACULATE GPA    
        x = float(decrypt(course[2])) * int(decrypt(course[1]))

        # Update the total grade points and total units
        total_grade += x
        total_units += int(decrypt(course[1]))
        
        crsCodeLBL = Label(sframe, text = decrypt(course[0]), font=font2, fg= c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Code
        crsCodeLBL.place(x=15, y=125 + yPos, width=110, height=22)
        crsUnitLBL = Label(sframe, text = decrypt(course[1]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Units
        crsUnitLBL.place(x=125, y=125 + yPos, width=60, height=22)
        crsGradeLBL = Label(sframe, text = decrypt(course[2]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        crsGradeLBL.place(x=185, y=125 + yPos, width=65, height=22)
        facultyLBL = Label(sframe, text= decrypt(course[3]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        facultyLBL.place(x=250, y=125 + yPos, width=195, height=22)
        remarksLBL = Label(sframe, text= remarks, font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        remarksLBL.place(x=445, y=125 + yPos, width=90, height=22)
        
        if index == 27: #terminate at 26
            break; 

    # Calculate the GPA
    gpa = total_grade / total_units
    gpa = round(gpa, 2)
    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName)         

    #LABEL INPUT
    stuNameInput = Label(sframe, text= fullName, font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameInput.place(x=160, y=30,  height = 30) 
    
    stuYrInput = Label(sframe, text= "2", font= subheadFont, fg= c1, bg= MICSColor2)
    stuYrInput.place(x=74, y=65) 
    stuSemInput = Label(sframe, text= "2" , font= subheadFont, fg= c1, bg= MICSColor2)
    stuSemInput.place(x=180, y=65) 
    gpaInput = Label(sframe, text= gpa, font= subheadFont, fg= c1, bg= MICSColor2)
    gpaInput.place(x=420, y=65) 
    
    #BUTTONS 
        
    if int(decrypt(currStu_yr)) == 3 and int(decrypt(currStu_sem)) == 1:
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = displayGrades)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
        
    else: 
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = tYr_fSem)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
          
    next = Image.open(nextPath)
    next = next.resize((30, 30))
    nextIcon = ImageTk.PhotoImage(next)
    nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = sYr_fSem)
    nextBtn.place(x= 378, y=395, width= 30, height=30)
    nextBtn.config(highlightthickness=1, highlightbackground='black')
    nextBtn.image = nextIcon       
    
    contBtn = Button(sframe, text="BACK TO MAIN MENU", font = font1, fg=MICSColor2, bg= MICSColor1, command= mainWindow)
    contBtn.place(x=190, y=395, width= 170, height=30)
    
#THIRD YEAR FIRST SEM DISPLAY    
def tYr_fSem():
    sframe = Frame(root, width= 550, height= 450, relief = GROOVE, bg = MICSColor2)
    sframe.place(x=250, y=50) 

    #CUSTOM FONT AND COLOR
    f1 = "Arial 11 bold"
    c1= "black"
     
    total_grade = 0
    total_units = 0

    #LABELS
    backgroundLabel = Label(sframe, text = "", bg = MICSColor3, borderwidth=1, relief="solid" )
    backgroundLabel.place(x= 15, y = 30, width = 520, height = 30)
    
    stuNameLabel = Label(sframe, text="Student's Name:", font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameLabel.place(x=25, y=30,  height = 30)
    
    stuYrLabel = Label(sframe, text="Year:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuYrLabel.place(x=26, y=65)
    stuSemLabel = Label(sframe, text="Sem:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuSemLabel.place(x=130, y=65)
    gpaLabel = Label(sframe, text="GPA:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    gpaLabel.place(x=370, y=65) 
    
    crsCodeLabel = Label(sframe, text="Course Code", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsCodeLabel.place(x=15, y=95, width = 110, height= 30)
    crsUnitLabel = Label(sframe, text="Unit", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsUnitLabel.place(x=125, y=95, width = 60, height= 30)
    crsGradeLabel = Label(sframe, text="Grade", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsGradeLabel.place(x=185, y=95, width = 65, height= 30)
    facultyLabel = Label(sframe, text="Faculty", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    facultyLabel.place(x=250, y=95, width = 195, height= 30)
    remarksLabel = Label(sframe, text="Remarks", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    remarksLabel.place(x=445, y=95, width = 90, height= 30)  
    
    allcurrCourse = sys_list.get_all_course_list()
    for index, course in enumerate(allcurrCourse[28:], start= 28):
        adjusted_index = (index - 28)
        yPos= adjusted_index *22  
        
        if float(decrypt(course[2])) == 0.00 or float(decrypt(course[2])) == 0 or float(decrypt(course[2])) == 0.0:
            remarks = "-"
        elif float(decrypt(course[2])) <= 3.00 :
            remarks = "PASSED"
        else:
            remarks = "FAILED"
        
        #CACULATE GPA    
        x = float(decrypt(course[2])) * int(decrypt(course[1]))

        # Update the total grade points and total units
        total_grade += x
        total_units += int(decrypt(course[1]))
        
        crsCodeLBL = Label(sframe, text = decrypt(course[0]), font=font2, fg= c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Code
        crsCodeLBL.place(x=15, y=125 + yPos, width=110, height=22)
        crsUnitLBL = Label(sframe, text = decrypt(course[1]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Units
        crsUnitLBL.place(x=125, y=125 + yPos, width=60, height=22)
        crsGradeLBL = Label(sframe, text = decrypt(course[2]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        crsGradeLBL.place(x=185, y=125 + yPos, width=65, height=22)
        facultyLBL = Label(sframe, text= decrypt(course[3]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        facultyLBL.place(x=250, y=125 + yPos, width=195, height=22)
        remarksLBL = Label(sframe, text= remarks, font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        remarksLBL.place(x=445, y=125 + yPos, width=90, height=22)
        
        if index == 36: #terminate at 36
            break; 

    # Calculate the GPA
    gpa = total_grade / total_units
    gpa = round(gpa, 2)
    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName)          

    #LABEL INPUT
    stuNameInput = Label(sframe, text= fullName, font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameInput.place(x=160, y=30,  height = 30) 
    
    stuYrInput = Label(sframe, text= "3", font= subheadFont, fg= c1, bg= MICSColor2)
    stuYrInput.place(x=74, y=65) 
    stuSemInput = Label(sframe, text= "1" , font= subheadFont, fg= c1, bg= MICSColor2)
    stuSemInput.place(x=180, y=65) 
    gpaInput = Label(sframe, text= gpa, font= subheadFont, fg= c1, bg= MICSColor2)
    gpaInput.place(x=420, y=65) 
    
    #BUTTONS 
    if int(decrypt(currStu_yr)) == 3 and int(decrypt(currStu_sem)) == 2:
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = displayGrades)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
        
    else: 
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = tYr_sSem)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
          
    next = Image.open(nextPath)
    next = next.resize((30, 30))
    nextIcon = ImageTk.PhotoImage(next)
    nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = sYr_sSem)
    nextBtn.place(x= 378, y=395, width= 30, height=30)
    nextBtn.config(highlightthickness=1, highlightbackground='black')
    nextBtn.image = nextIcon       
    
    contBtn = Button(sframe, text="BACK TO MAIN MENU", font = font1, fg=MICSColor2, bg= MICSColor1, command= mainWindow)
    contBtn.place(x=190, y=395, width= 170, height=30)
    
#THIRD YEAR SECOND SEM DISPLAY    
def tYr_sSem():
    sframe = Frame(root, width= 550, height= 450, relief = GROOVE, bg = MICSColor2)
    sframe.place(x=250, y=50) 

    #CUSTOM FONT AND COLOR
    f1 = "Arial 11 bold"
    c1= "black"
     
    total_grade = 0
    total_units = 0

    #LABELS
    backgroundLabel = Label(sframe, text = "", bg = MICSColor3, borderwidth=1, relief="solid" )
    backgroundLabel.place(x= 15, y = 30, width = 520, height = 30)
    
    stuNameLabel = Label(sframe, text="Student's Name:", font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameLabel.place(x=25, y=30,  height = 30)
    
    stuYrLabel = Label(sframe, text="Year:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuYrLabel.place(x=26, y=65)
    stuSemLabel = Label(sframe, text="Sem:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuSemLabel.place(x=130, y=65)
    gpaLabel = Label(sframe, text="GPA:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    gpaLabel.place(x=370, y=65) 
    
    crsCodeLabel = Label(sframe, text="Course Code", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsCodeLabel.place(x=15, y=95, width = 110, height= 30)
    crsUnitLabel = Label(sframe, text="Unit", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsUnitLabel.place(x=125, y=95, width = 60, height= 30)
    crsGradeLabel = Label(sframe, text="Grade", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsGradeLabel.place(x=185, y=95, width = 65, height= 30)
    facultyLabel = Label(sframe, text="Faculty", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    facultyLabel.place(x=250, y=95, width = 195, height= 30)
    remarksLabel = Label(sframe, text="Remarks", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    remarksLabel.place(x=445, y=95, width = 90, height= 30)  
    
    allcurrCourse = sys_list.get_all_course_list()
    for index, course in enumerate(allcurrCourse[37:], start= 37):
        adjusted_index = (index - 37)
        yPos= adjusted_index *22
        
        if float(decrypt(course[2])) == 0.00 or float(decrypt(course[2])) == 0 or float(decrypt(course[2])) == 0.0:
            remarks = "-"
        elif float(decrypt(course[2])) <= 3.00 :
            remarks = "PASSED"
        else:
            remarks = "FAILED"
        
        #CACULATE GPA    
        x = float(decrypt(course[2])) * int(decrypt(course[1]))

        # Update the total grade points and total units
        total_grade += x
        total_units += int(decrypt(course[1]))
        
        crsCodeLBL = Label(sframe, text = decrypt(course[0]), font=font2, fg= c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Code
        crsCodeLBL.place(x=15, y=125 + yPos, width=110, height=22)
        crsUnitLBL = Label(sframe, text = decrypt(course[1]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Units
        crsUnitLBL.place(x=125, y=125 + yPos, width=60, height=22)
        crsGradeLBL = Label(sframe, text = decrypt(course[2]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        crsGradeLBL.place(x=185, y=125 + yPos, width=65, height=22)
        facultyLBL = Label(sframe, text= decrypt(course[3]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        facultyLBL.place(x=250, y=125 + yPos, width=195, height=22)
        remarksLBL = Label(sframe, text= remarks, font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        remarksLBL.place(x=445, y=125 + yPos, width=90, height=22)
        
        if index == 45: #terminate at 45
            break; 

    # Calculate the GPA
    gpa = total_grade / total_units
    gpa = round(gpa, 2)
    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName)          

    #LABEL INPUT
    stuNameInput = Label(sframe, text= fullName, font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameInput.place(x=160, y=30,  height = 30) 
    
    stuYrInput = Label(sframe, text= "3", font= subheadFont, fg= c1, bg= MICSColor2)
    stuYrInput.place(x=74, y=65) 
    stuSemInput = Label(sframe, text= "2" , font= subheadFont, fg= c1, bg= MICSColor2)
    stuSemInput.place(x=180, y=65) 
    gpaInput = Label(sframe, text= gpa, font= subheadFont, fg= c1, bg= MICSColor2)
    gpaInput.place(x=420, y=65) 

    #BUTTONS     
    if int(decrypt(currStu_yr)) == 4 and int(decrypt(currStu_sem)) == 1:
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = displayGrades)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
        
    else: 
        prev = Image.open(prevPath)
        prev = prev.resize((30, 30))
        prevIcon = ImageTk.PhotoImage(prev)
        prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = foYr_fSem)
        prevBtn.place(x= 140, y=395, width= 30, height=30)
        prevBtn.config(highlightthickness=1, highlightbackground='black')
        prevBtn.image = prevIcon
          
    next = Image.open(nextPath)
    next = next.resize((30, 30))
    nextIcon = ImageTk.PhotoImage(next)
    nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = tYr_fSem)
    nextBtn.place(x= 378, y=395, width= 30, height=30)
    nextBtn.config(highlightthickness=1, highlightbackground='black')
    nextBtn.image = nextIcon       
    
    contBtn = Button(sframe, text="BACK TO MAIN MENU", font = font1, fg=MICSColor2, bg= MICSColor1, command= mainWindow)
    contBtn.place(x=190, y=395, width= 170, height=30)
    
#FOURTH YEAR FIRST SEM DISPLAY
def foYr_fSem():
    sframe = Frame(root, width= 550, height= 450, relief = GROOVE, bg = MICSColor2)
    sframe.place(x=250, y=50) 

    #CUSTOM FONT AND COLOR
    f1 = "Arial 11 bold"
    c1= "black"
     
    total_grade = 0
    total_units = 0

    #LABELS
    backgroundLabel = Label(sframe, text = "", bg = MICSColor3, borderwidth=1, relief="solid" )
    backgroundLabel.place(x= 15, y = 30, width = 520, height = 30)
    
    stuNameLabel = Label(sframe, text="Student's Name:", font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameLabel.place(x=25, y=30,  height = 30)
    
    stuYrLabel = Label(sframe, text="Year:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuYrLabel.place(x=26, y=65)
    stuSemLabel = Label(sframe, text="Sem:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    stuSemLabel.place(x=130, y=65)
    gpaLabel = Label(sframe, text="GPA:", font= subheadFont, fg= MICSColor1, bg= MICSColor2)
    gpaLabel.place(x=370, y=65) 
    
    crsCodeLabel = Label(sframe, text="Course Code", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsCodeLabel.place(x=15, y=95, width = 110, height= 30)
    crsUnitLabel = Label(sframe, text="Unit", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsUnitLabel.place(x=125, y=95, width = 60, height= 30)
    crsGradeLabel = Label(sframe, text="Grade", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    crsGradeLabel.place(x=185, y=95, width = 65, height= 30)
    facultyLabel = Label(sframe, text="Faculty", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    facultyLabel.place(x=250, y=95, width = 195, height= 30)
    remarksLabel = Label(sframe, text="Remarks", font= f1, fg= MICSColor2, bg= MICSColor1, borderwidth=1, relief="solid")
    remarksLabel.place(x=445, y=95, width = 90, height= 30)  
    
    allcurrCourse = sys_list.get_all_course_list()
    for index, course in enumerate(allcurrCourse[46:], start= 46):
        adjusted_index = (index - 46)
        yPos= adjusted_index *22
        
        if float(decrypt(course[2])) == 0.00 or float(decrypt(course[2])) == 0 or float(decrypt(course[2])) == 0.0:
            remarks = "-"
        elif float(decrypt(course[2])) <= 3.00 :
            remarks = "PASSED"
        else:
            remarks = "FAILED"
        
        #CACULATE GPA    
        x = float(decrypt(course[2])) * int(decrypt(course[1]))

        # Update the total grade points and total units
        total_grade += x
        total_units += int(decrypt(course[1]))
        
        crsCodeLBL = Label(sframe, text = decrypt(course[0]), font=font2, fg= c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Code
        crsCodeLBL.place(x=15, y=125 + yPos, width=110, height=22)
        crsUnitLBL = Label(sframe, text = decrypt(course[1]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid") # Course Units
        crsUnitLBL.place(x=125, y=125 + yPos, width=60, height=22)
        crsGradeLBL = Label(sframe, text = decrypt(course[2]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        crsGradeLBL.place(x=185, y=125 + yPos, width=65, height=22)
        facultyLBL = Label(sframe, text= decrypt(course[3]), font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        facultyLBL.place(x=250, y=125 + yPos, width=195, height=22)
        remarksLBL = Label(sframe, text= remarks, font=font2, fg=c1, bg=MICSColor2, borderwidth=1, relief="solid")
        remarksLBL.place(x=445, y=125 + yPos, width=90, height=22)
        
        if index == 47: #terminate at 47
            break; 

    # Calculate the GPA
    gpa = total_grade / total_units
    gpa = round(gpa, 2)
    fullName = decrypt(currStu_fName) + " " + decrypt(currStu_mName) + " " + decrypt(currStu_lName)          

    #LABEL INPUT
    stuNameInput = Label(sframe, text= fullName, font= subheadFont, fg= MICSColor2, bg= MICSColor3)
    stuNameInput.place(x=160, y=30,  height = 30) 
    
    stuYrInput = Label(sframe, text= "4", font= subheadFont, fg= c1, bg= MICSColor2)
    stuYrInput.place(x=74, y=65) 
    stuSemInput = Label(sframe, text= "1" , font= subheadFont, fg= c1, bg= MICSColor2)
    stuSemInput.place(x=180, y=65) 
    gpaInput = Label(sframe, text= gpa, font= subheadFont, fg= c1, bg= MICSColor2)
    gpaInput.place(x=420, y=65) 

    #BUTTONS 
    prev = Image.open(prevPath)
    prev = prev.resize((30, 30))
    prevIcon = ImageTk.PhotoImage(prev)
    prevBtn = Button(sframe, image=prevIcon, bg=MICSColor2, command = displayGrades)
    prevBtn.place(x= 140, y=395, width= 30, height=30)
    prevBtn.config(highlightthickness=1, highlightbackground='black')
    prevBtn.image = prevIcon
          
    next = Image.open(nextPath)
    next = next.resize((30, 30))
    nextIcon = ImageTk.PhotoImage(next)
    nextBtn = Button(sframe, image=nextIcon, bg=MICSColor2, command = tYr_sSem)
    nextBtn.place(x= 378, y=395, width= 30, height=30)
    nextBtn.config(highlightthickness=1, highlightbackground='black')
    nextBtn.image = nextIcon       
    
    contBtn = Button(sframe, text="BACK TO MAIN MENU", font = font1, fg=MICSColor2, bg= MICSColor1, command= mainWindow)
    contBtn.place(x=190, y=395, width= 170, height=30)
 