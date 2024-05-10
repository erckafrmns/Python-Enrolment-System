# User-Defined Imports 
from config import *
from protection import *

class SystemList:
    system_list = []
    stud_tor_req_list = []
    student_log = []
    admin_log = []

    def add_to_sys_list(self, student_list: list):
        SystemList.system_list.append(student_list)

    def add_to_cour_list(self, course_list: list):
        student_position = StudentPosition.get_instance()

        SystemList.system_list[student_position.get_stud_post()].append(course_list)

    def add_to_stud_tor_req_list(self, stuReq_list: list):
        SystemList.stud_tor_req_list.append(stuReq_list)

    def add_to_stud_log(self, stud_log: list):
        SystemList.student_log.append(stud_log)

    def add_to_admin_log(self, admin_log: list):
        SystemList.admin_log.append(admin_log)

# ################
#     def display_sys_list(self):
#         for item in SystemList.system_list:
#             print(item)

#     def display_sys_course_list(self):

#         x = SystemList.system_list[StudentPosition.get_instance().get_stud_post()]
#         print("YEAR: " + str(x[4]))
#         print("SEMESTER: " + str(x[5]))
#         print("STATUS: " + x[7])
#         print("COMPLETE COURSE LIST: ")
#         for item in x[15]:
#             print(item)
#         print("CURRENT COURSE LIST: ")
#         for item in x[16]:
#             print(item)     

#     def display_stud_log(self):

#         x = SystemList.student_log
#         for item in x:
#             print(item)

#     def display_admin_log(self):

#         x = SystemList.admin_log
#         for item in x:
#             print(item)

# ################
    def locate_student (self, stud_num: str): # FOR STUDENT
        student_position = StudentPosition.get_instance()

        for index, item in enumerate(SystemList.system_list):
            if stud_num == decrypt(item[0]): # Student ID/Number
                student_position.set_stud_pos(index)
                break
            else:
                student_position.set_stud_pos(-1)
    
    def return_sys_list(self):
        return SystemList.system_list

    def get_current_student(self):
        return SystemList.system_list[StudentPosition.get_instance().get_stud_post()]
    
    def get_curr_course_list(self):
        x = SystemList.system_list[StudentPosition.get_instance().get_stud_post()]
        inner_list = x[16]
        return inner_list
    
    def get_all_course_list(self):
        x = SystemList.system_list[StudentPosition.get_instance().get_stud_post()]
        inner_list = x[15]
        return inner_list
    
    def return_stud_tor_req_list(self):
        return SystemList.stud_tor_req_list
    
    def return_stud_log(self):
        return SystemList.student_log
    
    def return_admin_log(self):
        return SystemList.admin_log