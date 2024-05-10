# User-Defined Imports
from config import * # For miscellaneous functions and variable configuration details 
from file_handling import*  
from main_menu import* 
from enrollment import* 
from students import*
from protection import *

#Built-in Imports
from tkinter import * 
import tkinter.messagebox
from PIL import ImageTk, Image
import os 
import random 

# Get the parent folder of the root folder
parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def exam_num_check(): # Function to check if EXAMINEE_NUMBER input exists in the system records 
    
    frame = Tk() 
    frame.title('Manila Institute of Computer Studies')

    # Set size of frame
    frame.geometry("750x450") 

    # ------------------ LABEL WIDGETS ------------------ #
    rightSide = Label(frame, text = "", bg = MICSColor2)
    schoolLabel = Label(frame, text = "MANILA INSTITUTE OF\nCOMPUTER STUDIES", fg = MICSColor1, bg = MICSColor2)
    portalLabel = Label(frame, text = "EXAMINATION RESULT", fg = MICSColor2, bg = MICSColor1)
    userLabel = Label(frame, text = "Examinee Number", fg = MICSColor2, bg = MICSColor1)

    # Font configuration
    schoolLabel.config(font = ('Arial Bold', 20))
    portalLabel.config(font = ('Arial Bold', 20))
    userLabel.config(font = ('Arial Bold', 10))

    # Component placement
    rightSide.place(x = 0, y = 0, relwidth = 0.5, relheight = 1.0)
    schoolLabel.place(x = 30, y = 45)
    portalLabel.place(x = 410, y = 55)
    userLabel.place(x = 500, y = 175)

    #  ------------------ INPUT FIELD WIDGETS ------------------ #
    userExamNum = Entry(frame) 

    # Input field placement
    userExamNum.place(x = 460, y = 138, width = 200, height = 36)  
  
    #Button click handlers 
    def search_button_clicked():
        exam_num = userExamNum.get()  #Retrieve the entered examinee number

        # Call the ret_exam_num function from the file_handling.py
        exam_num_found = load_exam_num(exam_num)

        if exam_num_found: 
            frame.destroy()
            notice_of_rating_page(exam_num_found)
        else:
            tkinter.messagebox.showerror("Error",  "EXAMINEE NUMBER INVALID")

    #  ------------------ BUTTON WIDGETS ------------------ #
    searchButton = Button(frame, text="Search", bg=MICSColor3, fg="#FFFFFF", command=search_button_clicked, font = ('Arial Bold', 10))
    
     # Button placements
    searchButton.place(x = 460, y = 210, width = 200, height = 36)

    # ------------------ IMAGES ------------------ #

    # Construct the file paths relative to the parent folder
    MISC_logo_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "MICSlogo.png")

    schoolImg = Image.open(MISC_logo_path)

    resizedImg = schoolImg.resize((250, 250))
    schoolImgTk = ImageTk.PhotoImage(resizedImg)
    schoolImgLabel = Label(frame, image = schoolImgTk, bg = MICSColor2)
    schoolImgLabel.place(x = 55, y = 120)

    # Frame attributes (Tkinter)
    frame.configure(bg = MICSColor1)
    frame.resizable(False, False)
    frame.mainloop() 
     
def notice_of_rating_page(exam_num_found): # Once the Examinee number was FOUND it will proceed to this function.  

    notice_of_rating_frame = Tk()
    notice_of_rating_frame.title('Notice of Rating')
    notice_of_rating_frame.geometry("750x450")
 
    # ------------------ LABEL WIDGETS ------------------ #
    SchoolLabel = Label(notice_of_rating_frame, text="MANILA INSTITUTE OF COMPUTER STUDIES", fg= MICSColor2, bg = MICSColor1, font = ('Arial Bold', 12))
    TitleLabel = Label (notice_of_rating_frame, text="NOTICE OF RATING", fg= MICSColor1, bg = MICSColor2, font = ('Arial Bold', 12))  
    messageLabel = Label(notice_of_rating_frame, text="Congratulations on passing the MICS examination! Your competency rating displayed exceptional performance and highlights\nyour dedication and hard work. We believe this achievement is just the beginning of a successful journey for you.\nKeep up the excellent work!\n\n\n\n\n\n\n\n\n\n\nBest regards,\n\nAndrew Bazzi\nCS Department Head\nManila Institute of Computer Studies", fg= '#000000', bg = MICSColor2, font = ('Arial', 9),justify='left')
    SubTitleLabel = Label (notice_of_rating_frame, text="Rating Per Competency Areas", fg= MICSColor1, bg = MICSColor2, font = ('Arial Bold', 12))    
     
    #Component placement
    SchoolLabel.place(x = 0, y = 0, width=750, height=60) 
    TitleLabel.place(x = 300, y = 80)  
    messageLabel.place(x = 30, y = 110)    
    SubTitleLabel.place(x = 250, y = 170)

    # Define the table headers
    headers = ["EXAMINEE NO.", "Verbal", "Analytical", "Numerical", "General Info."]

    # Define the border style
    border = 1

    # Create a frame to hold the table
    table_frame = Frame(notice_of_rating_frame)
    table_frame.place(x=140,y=210)

    # Create and configure labels for table headers
    for i, header in enumerate(headers):
        label = Label(table_frame, text=header, font=('Arial Bold', 10,), padx=10, pady=5, bg=MICSColor1, fg="white", relief=tkinter.SOLID, borderwidth=border)
        label.grid(row=0, column=i, sticky=tkinter.NSEW)

    # Create blank labels for the table cells
    for r in range(1):
        for c in range(len(headers)):
            label = Label(table_frame, font=("Arial", 10), padx=10, pady=5, relief=tkinter.SOLID, borderwidth=border)
            label.grid(row=r+1, column=c, sticky=tkinter.NSEW)

            # Populate each cell with the corresponding data from exam_num_found
            if c < len(exam_num_found.split('<--->')):
                cell_data = exam_num_found.split('<--->')[c]  
                label.config(text = decrypt(cell_data))
            else:
                cell_data = exam_num_found.split('<--->')[c]  
                label.config(text = cell_data)


    # Configure column weights for resizing
    for c in range(len(headers)):
        table_frame.grid_columnconfigure(c, weight=1)

    # ------------------ IMAGES ------------------ #

    # Construct the file paths relative to the parent folder
    MISC_logo_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "MICSlogo.png")

    schoolImg = Image.open(MISC_logo_path)

    resizedImg = schoolImg.resize((50, 50))
    schoolImgTk = ImageTk.PhotoImage(resizedImg)
    schoolImgLabel = Label(notice_of_rating_frame, image = schoolImgTk, bg = MICSColor1)
    schoolImgLabel.place(x = 55, y = 5) 

     #Button click handlers 
    def continue_button_clicked():

        notice_of_rating_frame.destroy()
        message_page() 

    #  ------------------ BUTTON WIDGETS ------------------ #
    continueButton = Button(notice_of_rating_frame, text="Continue", bg=MICSColor3, fg="#FFFFFF", command=continue_button_clicked, font = ('Arial Bold', 10)) 
    
     # Button placements
    continueButton.place(x = 270, y = 390, width = 200, height = 36) 
 
    # Frame attributes (Tkinter)
    notice_of_rating_frame.configure(bg = MICSColor2)
    notice_of_rating_frame.resizable(False, False)
    notice_of_rating_frame.mainloop() 
 
def message_page():  

    message_frame = Tk()
    message_frame.title('Notice of Admission')
    message_frame.geometry("750x450")   
 
    # Create the frame to hold the message box
    messages_frame = Frame(message_frame, bd=1, relief="solid")
    messages_frame.pack(pady=10)

    # Define the table headers
    headers = ["MANILA INSTITUTE OF COMPUTER STUDIES"]

    # Define the border style
    border = 1

    # Create a frame to hold the table
    table_frame = Frame(message_frame)
    table_frame.pack(pady=20)

    # Create and configure labels for table headers
    for i, header in enumerate(headers):
        label = Label(table_frame, text=header, font=('Arial Bold', 12), bg=MICSColor1, fg=MICSColor2, padx=20, pady=10, relief="solid", borderwidth=border)
        label.grid(row=0, column=i, sticky="nsew")

    # Create blank labels for the table cells
    for r in range(1):
        for c in range(len(headers)):
            label = Label(table_frame, font=("Arial", 10), padx=20, pady=10, relief="solid", borderwidth=border, wraplength=600, justify="left")
            label.grid(row=r+1, column=c, sticky="nsew")

            # Populate the label with the message
            message = "Greetings, Students!\n\nThe Manila Institute of Computer Studies does not recognize credit units obtained from other educational institutions. Consequently, you are required to enroll at the first-year level of the program.\n\nWould you like to proceed with the admission process under these terms?"
            label.config(text=message)

    # Configure column weights for resizing
    for c in range(len(headers)):
        table_frame.grid_columnconfigure(c, weight=1) 

    #Button click handlers 
    def Yes_button_clicked():

        message_frame.destroy()
        input_stud_details_page()  

    def No_button_clicked():

        message_frame.destroy()
        exam_num_check()

    #  ------------------ BUTTON WIDGETS ------------------ #
    YesButton = Button(message_frame, text="Yes", bg=MICSColor3, fg="#FFFFFF", command=Yes_button_clicked, font = ('Arial Bold', 10)) 
    NoButton = Button(message_frame, text="No", bg=MICSColor3, fg="#FFFFFF", command=No_button_clicked, font = ('Arial Bold', 10))  
    
     # Button placements
    YesButton.place(x = 250, y = 230, width = 100, height = 36)   
    NoButton.place(x = 360, y = 230, width = 100, height = 36)      

    # Frame attributes (Tkinter)
    message_frame.configure(bg = MICSColor2)
    message_frame.resizable(False, False)
    message_frame.mainloop() 
        
def input_stud_details_page(): 

    stud_details_frame = Tk()
    stud_details_frame.title('Enrollment Form')
    stud_details_frame.geometry("800x500")

    # Function to generate the student number
    def accNumGen():
        example = 'MICS232023'
        check = -1

        while check == -1:
            random.seed()
            currentY = 2023  # Assuming the current year is 2023
            sy = currentY % 100

            lastFour = [random.randint(0, 9) for _ in range(4)]
            lastStr = ''.join(str(num) for num in lastFour)
            studNum = f"MICS{sy}{lastStr}"

            if example == studNum:
                check = -1
                break
            check = 1

        return studNum

    # Function to generate the student password
    def passGen():
        fName = givenNameTextField.get()
        lName = nameTextField.get().replace(" ", "")

        fParts = fName.split(" ")
        fInitials = []

        for part in fParts:
            if part:
                fInitials.append(part[0])

        fName = "".join(fInitials)
        fName = fName.lower()
        lName = lName.lower()

        studPass = fName + lName

        return studPass 

    # Button click handler
    def submit_button_clicked(): 

        if not nameTextField.get() or not givenNameTextField.get():
            tkinter.messagebox.showerror("Error", "Please complete the form.")
        else:
  
            save_new_student()
            stud_details_frame.destroy()   
            main__menu()   
        

     # ------------------ LABEL WIDGETS ------------------ #
    SchoolLabel = Label(stud_details_frame, text="MANILA INSTITUTE OF COMPUTER STUDIES", fg="white", bg=MICSColor1, font=('Arial Bold', 12))
    TitleLabel = Label(stud_details_frame, text="ENROLLMENT FORM", fg=MICSColor1, bg="white", font=('Arial Bold', 12))

    # Component placement
    SchoolLabel.place(x=0, y=0, width=800, height=60)
    TitleLabel.place(x=0, y=60, width=800, height=40) 

    #For Student's name
    studsNameTitle = Label(stud_details_frame, text="Student's Name", font=("Arial", 8), bg=MICSColor2)
    studsNameTitle.place(x=100, y=105, width=150, height=35)

    nameLabel = Label(stud_details_frame, text="Last Name", font=("Arial", 7), bg=MICSColor2)
    nameLabel.place(x=90, y=145, width=150, height=35)

    nameTextField = Entry(stud_details_frame, width=32, bg="white")
    nameTextField.place(x=130, y=130, width=160, height=25)

    givenNameLabel = Label(stud_details_frame, text="Given Name", font=("Arial", 7), bg=MICSColor2)
    givenNameLabel.place(x=290, y=145, width=150, height=35)

    givenNameTextField = Entry(stud_details_frame, width=32, bg="white")
    givenNameTextField.place(x=325, y=130, width=160, height=25)

    middleNameLabel = Label(stud_details_frame, text="Middle Name", font=("Arial", 7), bg=MICSColor2)
    middleNameLabel.place(x=485, y=145, width=150, height=35)

    middleNameTextField = Entry(stud_details_frame, width=32, bg="white")
    middleNameTextField.place(x=515, y=130, width=160, height=25)

    #For Student's sex
    sexLabel = Label(stud_details_frame, text="Sex", font=("Arial", 8), bg=MICSColor2)
    sexLabel.place(x=80, y=170, width=150, height=35)

    maleRadioButton = Radiobutton(stud_details_frame, text="Male", background=MICSColor2)
    femaleRadioButton = Radiobutton(stud_details_frame, text="Female", background=MICSColor2)
    maleRadioButton.place(x=130, y=195, width=70, height=35)
    femaleRadioButton.place(x=210, y=195, width=80, height=35)

    sexButtonGroup = StringVar()
    sexButtonGroup.set(None)
    maleRadioButton.config(variable=sexButtonGroup, value="Male")
    femaleRadioButton.config(variable=sexButtonGroup, value="Female")

    #For Student's birthday
    birthdateLabel = Label(stud_details_frame, text="Date of Birth", font=("Arial", 8), bg=MICSColor2)
    birthdateLabel.place(x=290, y=170, width=150, height=35)

    bdayLabel = Label(stud_details_frame, text="[MM-DD-YYYY]", font=("Arial", 7), bg=MICSColor2)
    bdayLabel.place(x=295, y=210, width=150, height=35)

    birthdateTextField = Entry(stud_details_frame, width=32, bg="white")
    birthdateTextField.place(x=325, y=195, width=160, height=25)

    #For Student's phone number
    phoneNumLabel = Label(stud_details_frame, text="Phone No.", font=("Arial", 8), bg=MICSColor2)
    phoneNumLabel.place(x=475, y=240, width=150, height=35)

    phoneNumTextField = Entry(stud_details_frame, width=12, bg="white")
    phoneNumTextField.place(x=515, y=265, width=160, height=25)

    #For Student's email
    emailAddLabel = Label(stud_details_frame, text="Email", font=("Arial", 8), bg=MICSColor2)
    emailAddLabel.place(x=75, y=240, width=150, height=35)

    emailFormatLabel = Label(stud_details_frame, text="example@example.com", font=("Arial", 7), bg=MICSColor2)
    emailFormatLabel.place(x=115, y=280, width=150, height=35)

    emailAddTextField = Entry(stud_details_frame, width=32, bg="white")
    emailAddTextField.place(x=130, y=265, width=345, height=25)

    #For Student's address
    addrssLabel = Label(stud_details_frame, text="Student's Address", font=("Arial", 8), bg=MICSColor2)
    addrssLabel.place(x=110, y=310, width=150, height=35)

    addrssFormatLabel = Label(stud_details_frame, text="Street Address", font=("Arial", 7), bg=MICSColor2)
    addrssFormatLabel.place(x=95, y=350, width=150, height=35)

    addrssTextField = Entry(stud_details_frame, width=50, bg="white")
    addrssTextField.place(x=130, y=335, width=535, height=25)

    #For Guardian's email
    gemailAddLabel = Label(stud_details_frame, text="Guardian's Email", font=("Arial", 8), bg=MICSColor2)
    gemailAddLabel.place(x=105, y=370, width=150, height=35)

    gemailFormatLabel = Label(stud_details_frame, text="example@example.com", font=("Arial", 7), bg=MICSColor2)
    gemailFormatLabel.place(x=115, y=410, width=150, height=35)

    gemailAddTextField = Entry(stud_details_frame, width=50, bg="white")
    gemailAddTextField.place(x=130, y=395, width=345, height=25)

    #For Guardian's phone number
    gPhoneNumLabel = Label(stud_details_frame, text="Guardian's Phone No.", font=("Arial", 8), bg=MICSColor2)
    gPhoneNumLabel.place(x=505, y=370, width=150, height=35)

    gPhoneNumTextField = Entry(stud_details_frame, width=12, bg="white")
    gPhoneNumTextField.place(x=515, y=395, width=160, height=25)

     # ------------------ IMAGES ------------------ #
    MICS_logo_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "MICSlogo.png")
    schoolImg = Image.open(MICS_logo_path)
    resizedImg = schoolImg.resize((50, 50))
    schoolImgTk = ImageTk.PhotoImage(resizedImg)
    schoolImgLabel = Label(stud_details_frame, image=schoolImgTk, bg=MICSColor1)
    schoolImgLabel.place(x=55, y=5)

    submitButton = Button(stud_details_frame, text="Submit", bg=MICSColor3, fg="#FFFFFF", font=('Arial Bold', 10), command=submit_button_clicked)
     
     # Button placements
    submitButton.place(x = 325, y = 440, width = 150, height = 36)     

    
    def save_new_student():
        student_list = SystemList()  # Create an instance of SystemList 
    
        courses = [encrypt_w_ok("CC131L"), encrypt_w_ok("CC132"), encrypt_w_ok("CC113"), encrypt_w_ok("MATHA05S")]
        units = [encrypt_w_ok(str(1)), encrypt_w_ok(str(2)), encrypt_w_ok(str(3)), encrypt_w_ok(str(5))]

        stud_year = 1
        stud_sem = 1
        l_name = nameTextField.get().upper()
        f_name = givenNameTextField.get().upper()
        m_name = middleNameTextField.get().upper()
        sex = 'M' if sexButtonGroup.get() == "Male" else 'F'
        birthdate = birthdateTextField.get()
        phone_number = phoneNumTextField.get()
        email = emailAddTextField.get()
        address = addrssTextField.get()
        guardian_email = gemailAddTextField.get()
        guardian_phone_number = gPhoneNumTextField.get()

        stud_num = accNumGen()  # Generate student number
        stud_pass = passGen()  # Generate student password
        tkinter.messagebox.showinfo("Generated Information", f"Student Number: {stud_num}\nStudent Password: {stud_pass}") 

        student = [ encrypt_w_ok(stud_num), encrypt_w_ok(l_name), encrypt_w_ok(f_name), encrypt_w_ok(m_name), encrypt_w_ok(str(stud_year)), 
                   encrypt_w_ok(str(stud_sem)), encrypt_w_ok(stud_pass), encrypt_w_ok("REGULAR"), encrypt_w_ok(sex), encrypt_w_ok(birthdate), 
                   encrypt_w_ok(phone_number), encrypt_w_ok(email), encrypt_w_ok(address), encrypt_w_ok(guardian_email), encrypt_w_ok(guardian_phone_number)]

        student_list.add_to_sys_list(student)
        student_list.locate_student(stud_num)
        course_list = []
        
        for i in range(len(courses)):
            course_details = []
            course_details.append(courses[i]) # Course Code
            course_details.append(units[i]) # Course Units
            course_details.append(encrypt_w_ok(str(0.00))) # Grade
            course_details.append("") # Faculty Name
            course_details.append("") # Day
            course_details.append("") # Time
            
            course_list.append(course_details)
            i += 1 
        
        student_list.add_to_cour_list(course_list) #ALL COURSES
        student_list.add_to_cour_list(course_list) # CURRENT COURSES
 

    # Frame attributes (Tkinter)
    stud_details_frame.configure(bg=MICSColor2)
    stud_details_frame.resizable(False, False)
    stud_details_frame.mainloop() 