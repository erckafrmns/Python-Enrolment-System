# User-Defined Imports
from admin import *
from config import * # For miscellaneous functions and variable configuration details
from enrollment import *
from file_handling import *
from students import *
from main_menu import * # For main menu functions
from registration import * # For registration functions

# Built-In Imports
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
import os

frame = Tk()
sys_list = SystemList()
student_position = StudentPosition.get_instance()

def Menu(): # Function that displays the ENTRY_MENU

    # Set size of frame
    frame.geometry("750x450")

    load_stud_info()
    load_all_stud_course_info()

    retrieve_torRequest_List()

    load_admin_log()
    load_stud_log()

    # ------------------ LABEL WIDGETS ------------------ #
    rightSide = Label(frame, text = "", bg = MICSColor2)
    schoolLabel = Label(frame, text = "MANILA INSTITUTE OF\nCOMPUTER STUDIES", fg = MICSColor1, bg = MICSColor2)
    portalLabel = Label(frame, text = "STUDENT PORTAL", fg = MICSColor2, bg = MICSColor1)
    userLabel = Label(frame, text = "Username", fg = MICSColor2, bg = MICSColor1)
    passLabel = Label(frame, text = "Password", fg = MICSColor2, bg = MICSColor1)

    # Font configuration
    schoolLabel.config(font = ('Arial Bold', 20))
    portalLabel.config(font = ('Arial Bold', 20))
    userLabel.config(font = ('Arial Bold', 10))
    passLabel.config(font = ('Arial Bold', 10))

    # Component placement
    rightSide.place(x = 0, y = 0, relwidth = 0.5, relheight = 1.0)
    schoolLabel.place(x = 30, y = 45)
    portalLabel.place(x = 435, y = 50)
    userLabel.place(x = 525, y = 165)
    passLabel.place(x = 525, y = 237)

    #  ------------------ INPUT FIELD WIDGETS ------------------ #
    userEntry = Entry(frame)
    passEntry = Entry(frame, show = '*')

    # Input field placement
    userEntry.place(x = 460, y = 128, width = 200, height = 36)
    passEntry.place(x = 460, y = 200, width = 200, height = 36)

    #  ------------------ BUTTON WIDGETS ------------------ #
    submitButton = Button(frame, text = "Log-in", bg = MICSColor3, fg = "#FFFFFF")
    regButton = Label(frame, text = "I AM A NEW STUDENT", fg = "#FFFFFF", bg = MICSColor1)

    # Configurations
    submitButton.config(font = ('Arial Bold', 10))
    regButton.config(font = ('Arial Bold', 10), relief = "flat", cursor = "hand2", highlightthickness = 0)

    # Button click handlers
    def submitButton_clicked(event):

        system_list = sys_list.return_sys_list()
        actual_list = []

        username = userEntry.get()  # Retrieve the entered username
        password = passEntry.get()  # Retrieve the entered password

        if username == '' and password == '':

            messagebox.showwarning("ERROR", "ENTRIES ARE EMPTY")

        else:
            if username == axu: # FOR ADMIN
                if password == axp:
                    frame.destroy()
                    entry_admin()
            else:
                sys_list.locate_student(username) # Locate the student's current position in the list based on the user's input

                if student_position.get_stud_post() == -1: # Student not found

                    messagebox.showwarning("ERROR", "STUDENT NOT FOUND")

                else: # Student found
                    actual_list = system_list[student_position.get_stud_post()]

                    if password == decrypt(actual_list[6]): # Password matched with the user's input
                        frame.destroy()
                        main__menu()
                    else: # Password incorrect

                        messagebox.showwarning("ERROR", "PASSWORD INCORRECT")

    def regButton_clicked(event):
        frame.destroy()
        exam_num_check()

    # Bind click handlers to buttons
    submitButton.bind("<Button-1>", submitButton_clicked)
    regButton.bind("<Button-1>", regButton_clicked)

    # Button placements
    submitButton.place(x = 460, y = 275, width = 200, height = 36)
    regButton.place(x = 460, y = 320, width = 200, height = 36)

    # ------------------ IMAGES ------------------ #
    # Get the parent folder of the root folder
    parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
