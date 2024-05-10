# User-Defined Imports
from config import * # For miscellaneous functions and variable configuration details
from file_handling import *
from protection import *
from students import *

# Built-In Imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import datetime
import os
from fpdf import FPDF
from pathlib import Path
from tkinter import messagebox


imgPath = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "MICSlogo.png")
img1Path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "CHED_LOGO.png")

sys_list = SystemList()

def entry_admin():
 
    frame = Tk()
    frame.geometry("300x130")

    # ENTRY FIELD WIDGET
    entryfield = Entry(frame, show = '*')
    entryfield.place(x = 50, y = 30, width = 200, height = 30)

    # BUTTON WIDGET
    enterButton = Button(frame, text = "ENTER", bg = MICSColor3, fg = "#FFFFFF")
    enterButton.config(font = ('Arial Bold', 10))

    def enterButton_clicked(event):
        entry = entryfield.get()
        if entry == acp:

            current_datetime = datetime.datetime.now()
            sys_list.add_to_admin_log([encrypt_w_ok("ADMIN"), encrypt_w_ok("Log-in"), 
                                       encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])

            frame.destroy()    
            admin_menu()
        else:
            frame.destroy()

    enterButton.bind("<Button-1>", enterButton_clicked)
    enterButton.place(x = 100, y = 75, width = 100, height = 25)

    # Frame attributes (Tkinter)
    frame.configure(bg = MICSColor1)
    frame.resizable(False, False)
    frame.mainloop()

def admin_menu():
    
    frame = Tk()
    frame.title("ADMIN - Main Menu")
    frame.geometry("400x300")

    img = Image.open(imgPath)
    img = img.resize((80, 80))
    logo = ImageTk.PhotoImage(img)
    logolabel = Label(frame, image = logo, bg = MICSColor2)
    logolabel.place(x = 160, y = 15)
    logolabel.image = logo

    # BUTTONS WIDGET
    schedButton = Button(frame, text = "Schedule Student", bg = MICSColor3, fg = "#FFFFFF")
    schedButton.config(font = ('Arial Bold', 10))

    def sched_stud(event):
        frame.destroy()
        set_schedule_menu()

    schedButton.bind("<Button-1>", sched_stud)

    schedButton.place(x = 100, y = 110, width = 200, height = 30)

    TORButton = Button(frame, text = "TOR Requests", bg = MICSColor3, fg = "#FFFFFF")
    TORButton.config(font = ('Arial Bold', 10))

    def tor_reqs(event):
        frame.destroy()
        tor_req()

    TORButton.bind("<Button-1>", tor_reqs)
    TORButton.place(x = 100, y = 150, width = 200, height = 30)

    logButton = Button(frame, text = "Activity History", bg = MICSColor3, fg = "#FFFFFF")
    logButton.config(font = ('Arial Bold', 10))

    def log_history(event):
        frame.destroy()
        activity_history()

    logButton.bind("<Button-1>", log_history)

    logButton.place(x = 100, y = 190, width = 200, height = 30)

    logOutButton = Button(frame, text = "LOG OUT", bg = MICSColor3, fg = "#FFFFFF")
    logOutButton.config(font = ('Arial Bold', 10))
 
    def return_to_Menu(event):     
        current_datetime = datetime.datetime.now()
        sys_list.add_to_admin_log([encrypt_w_ok("ADMIN"), encrypt_w_ok("Log-out"), 
                                   encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])

        save_indiv_stud_info()
        save_all_stud_course_info()

        save_torRequest_List()

        save_admin_log()
        save_student_log()

        save_key()

        frame.destroy()

    logOutButton.bind("<Button-1>", return_to_Menu)
    logOutButton.place(x = 150, y = 230, width = 100, height = 30)

    # Frame attributes (Tkinter)
    frame.configure(bg = MICSColor2)
    frame.resizable(False, False)
    frame.mainloop()

def set_schedule_menu():

    frame = Tk()
    frame.title("ADMIN - Schedule Student")
    frame.geometry("725x500")

    # MAIN FRAME HEADERS
    header = Label(frame, text = "STUDENT SCHEDULING", bg = MICSColor1, fg = MICSColor2)
    header.config(font = ('Arial Bold', 15))
    header.place(x = 150, y = 20, width = 425, height = 35)

    img = Image.open(imgPath)
    img = img.resize((75, 75))
    logo = ImageTk.PhotoImage(img)
    logolabel = Label(frame, image = logo, bg = MICSColor1)
    logolabel.place(x = 0, y = 0)
    logolabel.image = logo
    
    img1 = Image.open(img1Path)
    img1 = img1.resize((50, 50))
    logo1 = ImageTk.PhotoImage(img1)
    logo1label = Label(frame, image = logo1, bg = MICSColor1)
    logo1label.place(x = 650, y = 10)
    logo1label.image = logo1

    schedLabel = Label(frame, text = "SCHEDULE STATUS", relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")
    IDLabel = Label(frame, text = "STUDENT", relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")
    statusLabel = Label(frame, text = "SCHOLASTIC STATUS", relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")

    schedLabel.config(font = ('Arial Bold', 10))
    IDLabel.config(font = ('Arial Bold', 10))
    statusLabel.config(font = ('Arial Bold', 8))
    
    schedLabel.place(x = 50, y = 75, width = 150, height = 25)
    IDLabel.place(x = 200, y = 75, width = 320, height = 25)
    statusLabel.place(x = 520, y = 75, width = 151, height = 25)

    # TABLE CONFIGURATION
    tree_frame = Frame(frame, width = 600, height = 200, bg = MICSColor2)
    tree_frame.place(x = 50, y = 100)

    scrollbar = Scrollbar(tree_frame)
    scrollbar.pack(side = RIGHT, fill = Y)

    canvas = Canvas(tree_frame, width = 600, height = 325, yscrollcommand = scrollbar.set)
    canvas.pack(side = RIGHT, fill = BOTH)
    scrollbar.config(command = canvas.yview)

    sample = Frame(canvas, bg = MICSColor1)
    canvas.create_window((0, 0), window = sample, anchor = NW)

    # Add data
    sys_list = SystemList().return_sys_list()
    x_list = SystemList()

    def create_status_clicked_handler(student):
        def status_clicked(event):
            global confirmButton
            frame.destroy()

            def handle_row_click(event):
                
                confirmButton.place_forget()
                selected_item = table.focus()

                if selected_item:
                    x = table.item(selected_item, 'values')
                    first_column_entry = x[0]
                    
                    facultyLabel = Label(new_frame, text = "SELECT FACULTY:", bg = MICSColor1, fg = "white")
                    dayLabel = Label(new_frame, text = "      SELECT DAY:", bg = MICSColor1, fg = "white")
                    timeLabel = Label(new_frame, text = "     SELECT TIME:", bg = MICSColor1, fg = "white")    

                    facultyLabel.config(font = ('Arial Bold', 10))
                    dayLabel.config(font = ('Arial Bold', 10))
                    timeLabel.config(font = ('Arial Bold', 10))

                    facultyLabel.place(x = 50, y = 275, width = 150, height = 30)
                    dayLabel.place(x = 50, y = 315, width = 150, height = 30)
                    timeLabel.place(x = 50, y = 355, width = 150, height = 30)

                    select_faculty = ttk.Combobox(new_frame, values = faculty_assign(first_column_entry))
                    select_faculty.current(0)

                    select_days = ttk.Combobox(new_frame, values = days)
                    select_days.current(0)

                    select_time = ttk.Entry(new_frame)

                    select_faculty.place(x = 200, y = 275, width = 200, height = 30)
                    select_days.place(x = 200, y = 315, width = 200, height = 30)
                    select_time.place(x = 200, y = 355, width = 200, height = 30)

                    applyButton = Button(new_frame, text = "APPLY", bg = MICSColor3, fg = "white", 
                                      command = lambda: update_values(selected_item, select_faculty.get(), select_days.get(), select_time.get()))
                    applyButton.config(font = ('Arial Bold', 10))                  
                    applyButton.place(x = 450, y = 310, width = 200, height = 40)

                    def update_values(selected_item, faculty_value, day_value, time_value):
                        values = table.item(selected_item, 'values')
                        updated_values = (values[0], values[1], faculty_value, day_value, time_value)
                        table.item(selected_item, values = updated_values)

                        # Remove the labels, combo boxes, and button
                        facultyLabel.place_forget()
                        dayLabel.place_forget()
                        timeLabel.place_forget()
                        select_faculty.place_forget()
                        select_days.place_forget()
                        select_time.place_forget()
                        applyButton.place_forget()

                        # Make confirmButton reappear
                        confirmButton.place(x = 400, y = 310, width = 200, height = 40)

                        new_frame.update()  # REFRESH

            new_frame = Tk()
            new_frame.geometry("1000x400")
            
            table_frame = Frame(new_frame)
            table_frame.place(x = 25, y = 25, height = 200, width = 950)

            scroll_y = Scrollbar(table_frame)
            scroll_y.pack(side = RIGHT, fill = Y)

            table = ttk.Treeview(table_frame, height = 10, yscrollcommand = scroll_y.set)
            table.pack(side = RIGHT, fill = BOTH)
            scroll_y.config(command = table.yview)  

            table["columns"] = ("col1", "col2", "col3", "col4", "col5")

            table.column("#0", width = 0, stretch = NO)
            table.column("col1", width = 110)
            table.column("col2", width = 400)
            table.column("col3", width = 200)
            table.column("col4", width = 110)
            table.column("col5", width = 130)

            table.tag_configure("heading", background = MICSColor3, foreground = "white")
            table.tag_configure("heading", font = ("Arial", 10, "bold"))              

            table.heading("#0", text = "")
            table.heading("col1", text = "SUBJECT CODE", anchor = "center")
            table.heading("col2", text = "DESCRIPTION", anchor = "center")
            table.heading("col3", text = "FACULTY", anchor = "center")
            table.heading("col4", text = "DAY", anchor = "center")
            table.heading("col5", text = "TIME", anchor = "center")

            table.tag_bind("heading", "<<TreeviewSelect>>", lambda event: "break")

            days = ["MONDAY", "TUESDAY", "WEDNESDAY", 
                         "THURSDAY", "FRIDAY", "SATURDAY"]

            i = 1
            for x in student[16]:

                table.insert(parent = "", index = "end", iid = i, text = "1",
                            values = (decrypt(x[0]), subj_def(decrypt(x[0])), decrypt(x[3]),  decrypt(x[4]), decrypt(x[5])))

                i += 1

            table.bind('<ButtonRelease-1>', handle_row_click)

            confirmButton = Button(new_frame, text = "CONFIRM", bg = MICSColor3, fg = "white")
            confirmButton.config(font = ('Arial Bold', 10))

            def check_schedule(event):
                storage = []
                dup_check = 1
                stud_post = -1

                for index, item in enumerate(SystemList().return_sys_list()):
                    if student[0] in item:
                        stud_post = index

                row_vals = table.get_children()
                unique_entry = set()

                for row_val in row_vals:
                    values = table.item(row_val, 'values')
                    entry = values[0] + values[2] + values[3] + values[4]

                    if entry in unique_entry:
                        dup_check = -1
                        unique_entry.clear()
                        storage.clear()
                        break
                    else:
                        list = [values[0], values[2], values[3], values[4]]
                        storage.append(list)
                        unique_entry.add(entry)

                if dup_check == 1:
                    for item in storage:
                        for item2 in SystemList().return_sys_list()[stud_post][15]:
                            if item[0] == decrypt(item2[0]):
                                item2[3] = encrypt_w_ok(item[1])
                                item2[4] = encrypt_w_ok(item[2])
                                item2[5] = encrypt_w_ok(item[3])
                        for item3 in SystemList().return_sys_list()[stud_post][16]:
                            if item[0] == decrypt(item3[0]):
                                item3[3] = encrypt_w_ok(item[1])
                                item3[4] = encrypt_w_ok(item[2])
                                item3[5] = encrypt_w_ok(item[3])

                    

                    current_datetime = datetime.datetime.now()
                    x_list.add_to_admin_log(["ADMIN", "Assign schedule for student " + SystemList().return_sys_list()[stud_post][0], 
                                               current_datetime.strftime("%I:%M:%S %p"), current_datetime.strftime("%Y/%m/%d")])
                
                    new_frame.destroy()
                    admin_menu()

            confirmButton.bind("<Button-1>", check_schedule)
            confirmButton.place(x = 400, y = 310, width = 200, height = 40)

            # Frame attributes (Tkinter)
            new_frame.configure(bg = MICSColor1)
            new_frame.resizable(False, False)
            new_frame.mainloop()
            
        return status_clicked

    for item in sys_list:
        inner = Frame(sample)

        if any(item2[3] == '' or item2[4] == '' or item2[5] == '' for item2 in item[16]):
            status = Button (inner, text = "INCOMPLETE", height = 1, width = 17, bg = "red")
            status.bind("<Button-1>", create_status_clicked_handler(item))
        else:
            status = Button (inner, text = "COMPLETE", height = 1, width = 17, bg = "green", state = "disabled", disabledforeground = "white")

        ID = "[" + decrypt(item[0]) + "] " + decrypt(item[1]) + ", " + decrypt(item[2]) + " " + decrypt(item[3])
        IDlabel = Label(inner, text = ID, height = 1, width = 45, pady = 5, anchor = "w", 
                        highlightbackground = "black", highlightthickness = 1)
        statusLabel = Label(inner, text = decrypt(item[7]), height = 1, width = 20, pady = 5,
                        highlightbackground="black", highlightthickness = 1)

        status.config(font = ('Arial Bold', 10))
        IDlabel.config(font = ('Arial Bold', 8))
        statusLabel.config(font = ('Arial Bold', 8))

        status.pack(side = "left")
        IDlabel.pack(side = "left")
        statusLabel.pack(side = "left")
        inner.pack()

    backButton = Button(frame, text = "BACK", bg = MICSColor3, fg = "#FFFFFF")
    backButton.config(font = ('Arial Bold', 10))

    def return_to_menu(event):
        frame.destroy()
        admin_menu()

    backButton.bind("<Button-1>", return_to_menu)
    backButton.place(x = 285, y = 450, width = 155, height = 30)

    # Frame attributes (Tkinter)
    frame.configure(bg = MICSColor1)
    frame.resizable(False, False)
    frame.mainloop()

def tor_req():

    frame = Tk()
    frame.title("ADMIN - TOR Requests")
    frame.geometry("900x500")

    # MAIN FRAME HEADERS
    header = Label(frame, text = "REQUESTS FOR TRANSCRIPT OF RECORDS", bg = MICSColor1, fg = MICSColor2)
    header.config(font = ('Arial Bold', 15))
    header.place(x = 165, y = 30, width = 600, height = 35)

    img = Image.open(imgPath)
    img = img.resize((75, 75))
    logo = ImageTk.PhotoImage(img)
    logolabel = Label(frame, image = logo, bg = MICSColor1)
    logolabel.place(x = 0, y = 0)
    logolabel.image = logo
    
    img1 = Image.open(img1Path)
    img1 = img1.resize((50, 50))
    logo1 = ImageTk.PhotoImage(img1)
    logo1label = Label(frame, image = logo1, bg = MICSColor1)
    logo1label.place(x = 835, y = 10)
    logo1label.image = logo1

    # Table Headers
    studIDLabel = Label(frame, text = "STUDENT ID", relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")
    nameLabel = Label(frame, text = "STUDENT NAME", relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")
    purposeLabel = Label(frame, text = "PURPOSE OF REQUEST", relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")
    blankLabel = Label(frame, relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")

    studIDLabel.config(font = ('Arial Bold', 10))
    nameLabel.config(font = ('Arial Bold', 10))
    purposeLabel.config(font = ('Arial Bold', 10))
    
    studIDLabel.place(x = 50, y = 100, width = 125, height = 25)
    nameLabel.place(x = 175, y = 100, width = 250, height = 25)
    purposeLabel.place(x = 425, y = 100, width = 200, height = 25)
    blankLabel.place(x = 625, y = 100, width = 225, height = 25)

    # TABLE CONFIGURATION
    tree_frame = Frame(frame, width = 780, height = 200, bg = MICSColor2)
    tree_frame.place(x = 50, y = 125)

    scrollbar = Scrollbar(tree_frame)
    scrollbar.pack(side = RIGHT, fill = Y)

    canvas = Canvas(tree_frame, width = 780, height = 300, yscrollcommand = scrollbar.set)
    canvas.pack(side = RIGHT, fill = BOTH)
    scrollbar.config(command = canvas.yview)

    sample = Frame(canvas, bg = MICSColor1)
    canvas.create_window((0, 0), window = sample, anchor = NW)

    # Add data
    sys_list = SystemList().return_stud_tor_req_list()
    x_list = SystemList()

    def approve_button_clicked(item, appBtn, decBtn, inner):
        item[5] = encrypt_w_ok("APPROVED")
        
        appBtn.destroy()
        decBtn.forget()

        current_datetime = datetime.datetime.now()
        x_list.add_to_admin_log([encrypt_w_ok("ADMIN"), encrypt_w_ok("Approve TOR request of student " + decrypt(item[0])), 
                                    encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])

        approved = Label (inner, text = "APPROVED", height = 1, pady = 5, width = 28, bg = MICSColor3, fg = "#FFFFFF", relief = 'raised')
        approved.config(font = ('Arial Bold', 9))
        approved.pack(side = "left")  

    def decline_button_clicked(item, appBtn, decBtn, inner):
        item[5] = encrypt_w_ok("DECLINED")
        appBtn.destroy()
        decBtn.destroy()

        current_datetime = datetime.datetime.now()
        x_list.add_to_admin_log([encrypt_w_ok("ADMIN"), encrypt_w_ok("Decline TOR request of student " + decrypt(item[0])), 
                                    encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])

        declined = Label (inner, text = "DECLINED", height = 1, pady = 5, width = 28, bg = MICSColor3, fg = "#FFFFFF", relief = 'raised')
        declined.config(font = ('Arial Bold', 9))
        declined.pack(side = "left")

    for item in sys_list:
        inner = Frame(sample)

        IDlabel = Label(inner, text = decrypt(item[0]), height = 1, width = 17, pady = 5, 
                            highlightbackground = "black", highlightthickness = 1)
        nameLabel = Label(inner, text = decrypt(item[1]), height = 1, width = 34, pady = 5,
                            highlightbackground="black", highlightthickness = 1)
        purpLabel = Label(inner, text = decrypt(item[3]), height = 1, width = 28, pady = 5,
                            highlightbackground="black", highlightthickness = 1)
        
        IDlabel.config(font = ('Arial Bold', 9))
        nameLabel.config(font = ('Arial Bold', 9))
        purpLabel.config(font = ('Arial Bold', 9))

        IDlabel.pack(side = "left")
        nameLabel.pack(side = "left")
        purpLabel.pack(side = "left")

        if item[5] == encrypt_w_ok("PENDING"):
            appBtn = Button(inner, text="APPROVE", height=1, pady=5, width=14, bg="green",)
            decBtn = Button(inner, text="DECLINE", height=1, pady=5, width=13, bg="red",)
            
            appBtn.config(command=lambda appBtn = appBtn, decBtn = decBtn, item=item, inner = inner: approve_button_clicked(item, appBtn, decBtn, inner))
            decBtn.config(command=lambda appBtn = appBtn, decBtn = decBtn, item=item, inner = inner: decline_button_clicked(item, appBtn, decBtn, inner))
        
            appBtn.config(font = ('Arial Bold', 9))
            decBtn.config(font = ('Arial Bold', 9))
            
            appBtn.pack(side = "left")
            decBtn.pack(side = "left")       
        elif item[5] == encrypt_w_ok("APPROVED"):
            approved = Label (inner, text = "APPROVED", height = 1, pady = 5, width = 28, bg = MICSColor3, fg = "#FFFFFF", relief = 'raised')
            approved.config(font = ('Arial Bold', 9))
            approved.pack(side = "left")      
        else:
            declined = Label (inner, text = "DECLINED", height = 1, pady = 5, width = 28, bg = MICSColor3, fg = "#FFFFFF", relief = 'raised')
            declined.config(font = ('Arial Bold', 9))
            declined.pack(side = "left")

        inner.pack()

    backButton = Button(frame, text = "BACK", bg = MICSColor3, fg = "#FFFFFF")
    backButton.config(font = ('Arial Bold', 10))

    def return_to_menu(event):
        frame.destroy()
        admin_menu()

    backButton.bind("<Button-1>", return_to_menu)
    backButton.place(x = 370, y = 450, width = 160, height = 30)

    # Frame attributes (Tkinter)
    frame.configure(bg = MICSColor1)
    frame.resizable(False, False)
    frame.mainloop()

def activity_history():

    frame = Tk()
    frame.title("ADMIN - TOR Requests")
    frame.geometry("875x550")

    # MAIN FRAME HEADERS
    header = Label(frame, text = "SYSTEM LOG HISTORY", bg = MICSColor1, fg = MICSColor2)
    header.config(font = ('Arial Bold', 15))
    header.place(x = 135, y = 30, width = 605, height = 35)

    img = Image.open(imgPath)
    img = img.resize((75, 75))
    logo = ImageTk.PhotoImage(img)
    logolabel = Label(frame, image = logo, bg = MICSColor1)
    logolabel.place(x = 0, y = 0)
    logolabel.image = logo
    
    img1 = Image.open(img1Path)
    img1 = img1.resize((50, 50))
    logo1 = ImageTk.PhotoImage(img1)
    logo1label = Label(frame, image = logo1, bg = MICSColor1)
    logo1label.place(x = 810, y = 10)
    logo1label.image = logo1

    # Navigation Bars
    adminBtn = Button(frame, text = "ADMIN LOG", bg = MICSColor3, fg = "#FFFFFF")
    studentBtn = Button(frame, text = "STUDENT LOG", bg = MICSColor3, fg = "#FFFFFF")

    show_student_log(frame)

    adminBtn.config(font = ('Arial Bold', 12))
    studentBtn.config(font = ('Arial Bold', 12))

    def admin(event):
        current_datetime = datetime.datetime.now()
        sys_list.add_to_admin_log([encrypt_w_ok("ADMIN"), encrypt_w_ok("View admin log"), 
                                   encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])
        show_admin_log(frame)

    def student(event):
        current_datetime = datetime.datetime.now()
        sys_list.add_to_admin_log([encrypt_w_ok("ADMIN"), encrypt_w_ok("View student log"), 
                                   encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])
        show_student_log(frame)

    adminBtn.bind("<Button-1>", admin)
    studentBtn.bind("<Button-1>", student)

    adminBtn.place(x = 100, y = 100, width = 200, height = 35)
    studentBtn.place(x = 575, y = 100, width = 200, height = 35)

    # Table Headers
    userLabel = Label(frame, text = "USER", relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")
    actLabel = Label(frame, text = "ACTIVITY", relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")
    dateLabel = Label(frame, text = "TIME", relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")
    timeLabel = Label(frame, text = "DATE", relief = RAISED, bg = MICSColor3, fg = "#FFFFFF")

    userLabel.config(font = ('Arial Bold', 10))
    actLabel.config(font = ('Arial Bold', 10))
    dateLabel.config(font = ('Arial Bold', 10))
    timeLabel.config(font = ('Arial Bold', 10))
    
    userLabel.place(x = 50, y = 150, width = 125, height = 25)
    actLabel.place(x = 175, y = 150, width = 250, height = 25)
    dateLabel.place(x = 425, y = 150, width = 200, height = 25)
    timeLabel.place(x = 625, y = 150, width = 200, height = 25)

    # FOOTERS
    backButton = Button(frame, text = "BACK", bg = MICSColor3, fg = "#FFFFFF")
    backButton.config(font = ('Arial Bold', 10))

    def return_to_menu(event):
        frame.destroy()
        admin_menu()

    backButton.bind("<Button-1>", return_to_menu)
    backButton.place(x = 50, y = 500, width = 155, height = 30)

    # Frame attributes (Tkinter)
    frame.configure(bg = MICSColor1)
    frame.resizable(False, False)
    frame.mainloop()

def show_admin_log(frame):

    # TABLE CONFIGURATION
    tree_frame = Frame(frame, width = 755, height = 200, bg = MICSColor2)
    tree_frame.place(x = 50, y = 175)

    scrollbar = Scrollbar(tree_frame)
    scrollbar.pack(side = RIGHT, fill = Y)

    canvas = Canvas(tree_frame, width = 755, height = 300, yscrollcommand = scrollbar.set)
    canvas.pack(side = RIGHT, fill = BOTH)
    scrollbar.config(command = canvas.yview)

    sample = Frame(canvas, bg = MICSColor1)
    canvas.create_window((0, 0), window = sample, anchor = NW)
    
    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))


    # Add data
    sys_list = SystemList().return_admin_log()  

    for item in sys_list:
        inner = Frame(sample)

        userlabel = Label(inner, text = decrypt(item[0]), height = 1, width = 17, pady = 5, 
                            highlightbackground = "black", highlightthickness = 1)
        actLabel = Label(inner, text = decrypt(item[1]), height = 1, width = 34, pady = 5,
                            highlightbackground="black", highlightthickness = 1)
        dateLabel = Label(inner, text = decrypt(item[2]), height = 1, width = 28, pady = 5,
                            highlightbackground="black", highlightthickness = 1)
        timeLabel = Label(inner, text = decrypt(item[3]), height = 1, width = 28, pady = 5,
                            highlightbackground="black", highlightthickness = 1)
        
        userlabel.config(font = ('Arial Bold', 9))
        actLabel.config(font = ('Arial Bold', 9))
        dateLabel.config(font = ('Arial Bold', 9))
        timeLabel.config(font = ('Arial Bold', 9))

        userlabel.pack(side = "left")
        actLabel.pack(side = "left")
        dateLabel.pack(side = "left")
        timeLabel.pack(side = "left")

        inner.pack()

    canvas.update_idletasks()  # Update canvas size and scrollbar
    canvas.configure(scrollregion=canvas.bbox("all"))  # Set scrollable region

    downButton = Button(frame, text = "DOWNLOAD", bg = MICSColor3, fg = "#FFFFFF")
    downButton.config(font = ('Arial Bold', 10))

    def download_admin_log(event):
        generate_admin_log_file()

    downButton.bind("<Button-1>", download_admin_log)
    downButton.place(x = 670, y = 500, width = 155, height = 30)

def show_student_log(frame):

    # TABLE CONFIGURATION
    tree_frame = Frame(frame, width = 755, height = 200, bg = MICSColor2)
    tree_frame.place(x = 50, y = 175)

    scrollbar = Scrollbar(tree_frame)
    scrollbar.pack(side = RIGHT, fill = Y)

    canvas = Canvas(tree_frame, width = 755, height = 300, yscrollcommand = scrollbar.set)
    canvas.pack(side = RIGHT, fill = BOTH)
    scrollbar.config(command = canvas.yview)

    sample = Frame(canvas, bg = MICSColor1)
    canvas.create_window((0, 0), window = sample, anchor = NW)
    
    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))


    # Add data
    sys_list = SystemList().return_stud_log()  

    for item in sys_list:
        inner = Frame(sample)

        userlabel = Label(inner, text = decrypt(item[0]), height = 1, width = 17, pady = 5, 
                            highlightbackground = "black", highlightthickness = 1)
        actLabel = Label(inner, text = decrypt(item[1]), height = 1, width = 34, pady = 5,
                            highlightbackground="black", highlightthickness = 1)
        dateLabel = Label(inner, text = decrypt(item[2]), height = 1, width = 28, pady = 5,
                            highlightbackground="black", highlightthickness = 1)
        timeLabel = Label(inner, text = decrypt(item[3]), height = 1, width = 28, pady = 5,
                            highlightbackground="black", highlightthickness = 1)
        
        userlabel.config(font = ('Arial Bold', 9))
        actLabel.config(font = ('Arial Bold', 9))
        dateLabel.config(font = ('Arial Bold', 9))
        timeLabel.config(font = ('Arial Bold', 9))

        userlabel.pack(side = "left")
        actLabel.pack(side = "left")
        dateLabel.pack(side = "left")
        timeLabel.pack(side = "left")

        inner.pack()

    canvas.update_idletasks()  # Update canvas size and scrollbar
    canvas.configure(scrollregion=canvas.bbox("all"))  # Set scrollable region

    downButton = Button(frame, text = "DOWNLOAD", bg = MICSColor3, fg = "#FFFFFF")
    downButton.config(font = ('Arial Bold', 10))

    def download_stud_log(event):
        generate_admin_stud_file()

    downButton.bind("<Button-1>", download_stud_log)
    downButton.place(x = 670, y = 500, width = 155, height = 30)

def generate_admin_log_file():
    
    def get_unique_filename(filename):
            base, ext = os.path.splitext(filename)
            suffix = 1
            while os.path.exists(filename):
                filename = f"{base}({suffix}){ext}"
                suffix += 1
            return filename
        
    
    pdf = FPDF('P', 'mm', 'Letter')
    pdf.add_page()
    pdf.set_margins(left=72, top=72, right=72)
    
    # Set font and size for text
    font_family = 'Arial'
    font_style = 'B'
    font_size = 11
    x = 10  
    y = 65  
    
    #GET CURRENT DATE AND TIME
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.strftime("%m-%d-%Y")
    current_time = current_datetime.strftime("%H:%M:%S")
    
    parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    header = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "adminLog_header.png")
    pdf.image(header, x=15, y=15, w=180, h=40)
    
    pdf.set_y(50)
    pdf.set_font(font_family, font_style, font_size)
    pdf.text(x, y, "Date and Time Printed: " + current_date + " | " + current_time)
    
    # Add table header
    header = ['USER', 'ACTIVITY', 'TIME', 'DATE' ]
    column_widths = [35, 85, 35,35]  # Widths for each column
    pdf.set_fill_color(200, 200, 200)  # Set fill color for header
    pdf.set_y(75)
    pdf.set_x(10)
    pdf.cell(column_widths[0], 9, header[0], 1, 0, 'C', True)  # USER
    pdf.cell(column_widths[1], 9, header[1], 1, 0, 'C', True)  # ACTIVITY
    pdf.cell(column_widths[2], 9, header[2], 1, 0, 'C', True)  # TIME
    pdf.cell(column_widths[3], 9, header[3], 1, 1, 'C', True)  # DATE
    
    
    sys_list = SystemList().return_admin_log()  
    x_list = SystemList()

    for row in sys_list:
        
        if pdf.get_y() > 255:  # Check if the y position exceeds the maximum page height
            pdf.add_page()  # Add a new page
            pdf.set_y(20)  # Set the y position back to default
        
        pdf.set_fill_color(255, 255, 255)
        pdf.set_x(10)  # Set the initial x position for each row
        pdf.cell(column_widths[0], 7, decrypt(row[0]), 1, 0, 'L', True)  # USER
        pdf.cell(column_widths[1], 7, decrypt(row[1]), 1, 0, 'L', True)  # ACTIVITY
        pdf.cell(column_widths[2], 7, decrypt(row[2]), 1, 0, 'C', True)  # TIME
        pdf.cell(column_widths[3], 7, decrypt(row[3]), 1, 1, 'C', True)  # DATE
    
    # Save the PDF to user's desktop
    desktop_path = str(Path.home() / "Desktop")
    filename = "ADMIN_LOG.pdf"
    file_path = os.path.join(desktop_path, filename)
    file_path = get_unique_filename(file_path)
    pdf.output(file_path)

    current_datetime = datetime.datetime.now()
    x_list.add_to_admin_log([encrypt_w_ok("ADMIN"), encrypt_w_ok("Download ADMIN log"), 
                             encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])
    
    messagebox.showinfo("SUCESS", "ADMIN LOG has been successfully downloaded.\n[" + file_path+"]")

def generate_admin_stud_file():
    
    def get_unique_filename(filename):
            base, ext = os.path.splitext(filename)
            suffix = 1
            while os.path.exists(filename):
                filename = f"{base}({suffix}){ext}"
                suffix += 1
            return filename
        
    
    pdf = FPDF('P', 'mm', 'Letter')
    pdf.add_page()
    pdf.set_margins(left=72, top=72, right=72)
    
    # Set font and size for text
    font_family = 'Arial'
    font_style = 'B'
    font_size = 11
    x = 10  
    y = 65  
    
    #GET CURRENT DATE AND TIME
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.strftime("%m-%d-%Y")
    current_time = current_datetime.strftime("%H:%M:%S")
    
    parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    header = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "IMAGES", "stuLog_header.png")
    pdf.image(header, x=15, y=15, w=180, h=40)
    
    pdf.set_y(50)
    pdf.set_font(font_family, font_style, font_size)
    pdf.text(x, y, "Date and Time Printed: " + current_date + " | " + current_time)
    
    # Add table header
    header = ['USER', 'ACTIVITY', 'TIME', 'DATE' ]
    column_widths = [35, 85, 35,35]  # Widths for each column
    pdf.set_fill_color(200, 200, 200)  # Set fill color for header
    pdf.set_y(75)
    pdf.set_x(10)
    pdf.cell(column_widths[0], 9, header[0], 1, 0, 'C', True)  # USER
    pdf.cell(column_widths[1], 9, header[1], 1, 0, 'C', True)  # ACTIVITY
    pdf.cell(column_widths[2], 9, header[2], 1, 0, 'C', True)  # TIME
    pdf.cell(column_widths[3], 9, header[3], 1, 1, 'C', True)  # DATE
    
    
    sys_list = SystemList().return_stud_log()  
    x_list = SystemList()

    for row in sys_list:
        
        if pdf.get_y() > 255:  # Check if the y position exceeds the maximum page height
            pdf.add_page()  # Add a new page
            pdf.set_y(20)  # Set the y position back to default
        
        pdf.set_fill_color(255, 255, 255)
        pdf.set_x(10)  # Set the initial x position for each row
        pdf.cell(column_widths[0], 7, decrypt(row[0]), 1, 0, 'L', True)  # USER
        pdf.cell(column_widths[1], 7, decrypt(row[1]), 1, 0, 'L', True)  # ACTIVITY
        pdf.cell(column_widths[2], 7, decrypt(row[2]), 1, 0, 'C', True)  # TIME
        pdf.cell(column_widths[3], 7, decrypt(row[3]), 1, 1, 'C', True)  # DATE
    
    # Save the PDF to user's desktop
    desktop_path = str(Path.home() / "Desktop")
    filename = "STUDENT_LOG.pdf"
    file_path = os.path.join(desktop_path, filename)
    file_path = get_unique_filename(file_path)
    pdf.output(file_path)

    current_datetime = datetime.datetime.now()
    x_list.add_to_admin_log([encrypt_w_ok("ADMIN"), encrypt_w_ok("Download STUDENT log"), 
                             encrypt_w_ok(current_datetime.strftime("%I:%M:%S %p")), encrypt_w_ok(current_datetime.strftime("%Y/%m/%d"))])
    
    messagebox.showinfo("SUCESS", "STUDENT LOG has been successfully downloaded.\n[" + file_path+"]")

def faculty_assign(course_code):

    if course_code == "CC113":
        return ["VALERIE K. WILLIAMS", "ANTHONY J. MORROW"]
    elif course_code == "CC131L" or course_code == "CC132":
        return ["HAROLD O. POWELL", "MARY ANNE F. LEE"]
    elif course_code == "MATHA05S":
        return ["DOROTHY K. ROSE", "ALBERT G. JONES"]
    elif course_code == "CC141L" or course_code == "CC142":
        return ["HAROLD O. POWELL", "MARY ANNE F. LEE"]
    elif course_code == "CC103":
        return ["DOROTHY K. ROSE", "CHRISTOPHER L. PARKER"]
    elif course_code == "CS123":
        return ["ALBERT G. JONES", "CHRISTOPHER L. PARKER"]
    elif course_code == "MATHA35":
        return ["DOROTHY K. ROSE", "ALBERT G. JONES"]
    elif course_code == "CC211L" or course_code == "CC212":
        return ["MARY ANNE F. LEE", "CHRISTOPHER L. PARKER"]
    elif course_code == "CS213":
        return ["VALERIE K. WILLIAMS", "ANTHONY J. MORROW"]
    elif course_code == "CS233":
        return ["DOROTHY K. ROSE", "CHRISTOPHER L. PARKER"]
    elif course_code == "CS251L" or course_code == "CS252":
        return ["HAROLD O. POWELL", "LESLIE O. PRICE"]
    elif course_code == "CS271L" or course_code == "CS272":
        return ["DANIEL M. MASLOW", "DARLENE Q. BROWN"]
    elif course_code == "CC201L" or course_code == "CC202":
        return ["JAMES H. JOHNSON", "KATRINA F. CRAIG"]
    elif course_code == "CC223":
        return ["DOROTHY K. ROSE", "CHRISTOPHER L. PARKER"]
    elif course_code == "CS201L" or course_code == "CS202":
        return ["VALERIE K. WILLIAMS", "DARLENE Q. BROWN"]
    elif course_code == "CS221L" or course_code == "CS222":
        return ["HAROLD O. POWELL", "JAMES H. JOHNSON"]
    elif course_code == "CS243":
        return ["ALBERT G. JONES", "CHRISTOPHER L. PARKER"]
    elif course_code == "CS261L" or course_code == "CS262":
        return ["ANTHONY J. MORROW", "DANIEL M. MASLOW"]
    elif course_code == "MATHSTAT03":
        return ["DOROTHY K. ROSE", "JOHN U. MOORE"]
    elif course_code == "CSE1":
        return ["HAROLD O. POWELL", "JAMES H. JOHNSON"]
    elif course_code == "CSE2":
        return ["VALERIE K. WILLIAMS", "MARY ANNE F. LEE"]
    elif course_code == "CSE3":
        return ["ANTHONY J. MORROW", "HAROLD O. POWELL"]
    elif course_code == "CSE4":
        return ["MARY ANNE F. LEE", "JOHN U. MOORE"]
    elif course_code == "CS413":
        return ["ALBERT G. JONES", "CHRISTOPHER L. PARKER", "LESLIE O. PRICE", "DARLENE Q. BROW", "KATRINA F. CRAIG"]
    elif course_code == "CS423":
        return ["ALBERT G. JONES", "CHRISTOPHER L. PARKER", "LESLIE O. PRICE", "DARLENE Q. BROW", "KATRINA F. CRAIG"]
    elif course_code == "CS373":
        return ["ALBERT G. JONES", "LESLIE O. PRICE"]
    elif course_code == "CS351L" or course_code == "CS352":
        return ["KATRINA F. CRAIG", "OWEN Y. TRUMAN"]
    elif course_code == "CS333":
        return ["CHRISTOPHER L. PARKER", "JOHN U. MOORE"]
    elif course_code == "CS313":
        return ["DANIEL M. MASLOW", "JUSTIN O. JACKSON"]
    elif course_code == "CC311L" or course_code == "CC312":
        return ["ANTHONY J. MORROW", "DARLENE Q. BROWN"]
    elif course_code == "CC303":
        return ["VALERIE K. WILLIAMS", "HAROLD O. POWELL"]
    elif course_code == "CS303":
        return ["JAMES H. JOHNSON", "JUSTIN O. JACKSON"]
    elif course_code == "CS313":
        return ["DANIEL M. MASLOW", "JUSTIN O. JACKSON"]
    elif course_code == "CS321L" or course_code == "CS322":
        return ["DOROTHY K. ROSE", "JUSTIN O. JACKSON"]
    elif course_code == "CS343":
        return ["ALBERT G. JONES", "CHRISTOPHER L. PARKER"]
    elif course_code == "CS361L" or course_code == "CS362":
        return ["KATRINA F. CRAIG", "OWEN Y. TRUMAN"]
    elif course_code == "CS433":
        return ["VALERIE K. WILLIAMS", "ANTHONY J. MORROW"]
    elif course_code == "CS403":
        return ["DOROTHY K. ROSE", "OWEN Y. TRUMAN"]
