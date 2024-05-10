# User-Defined Imports
from students import *
from config import *
from protection import *

# Built-in Imports
import os

# Classes instantiation
system_list = SystemList()
student_position = StudentPosition.get_instance()

# Get the parent folder of the root folder
parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_stud_info(): # Load all student information and their associated individual student database

    try: 
        # Construct the file paths relative to the parent folder
        db2_file_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "1", "DB2.txt")

        with open(db2_file_path, 'r') as file:

            for student_line in file:
                student_content = student_line.strip()
                student_data = student_content.split('<--->')

                student_details = []
                student_details.append(student_data[2]) # Student number
                student_details.append(student_data[3]) # Student last name
                student_details.append(student_data[4]) # Student given name
                student_details.append(student_data[5]) # Student middle name
                student_details.append(student_data[0]) # Student year
                student_details.append(student_data[1]) # Current semester
                student_details.append(student_data[6]) # Password
                student_details.append(student_data[7]) # Student status
                student_details.append(student_data[8]) # Sex
                student_details.append(student_data[9]) # Birthdate
                student_details.append(student_data[10]) # Student phone number 
                student_details.append(student_data[11]) # Student email address
                student_details.append(student_data[12]) # Student address
                student_details.append(student_data[13]) # Student's guardian's email address
                student_details.append(student_data[14]) # Student's guardian's phone number
      

                system_list.add_to_sys_list(student_details)
    
    except FileNotFoundError:
        print(f"File not found: {db2_file_path}")
        return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
def load_all_stud_course_info():

    sys_list = system_list.return_sys_list()

    for item in sys_list:

        encrypted_stud_num = ""

        i = 1
        for char in decrypt(item[0]):
            if i < 5:
                new_char = chr(ord(char) + 3)
                encrypted_stud_num += new_char
            else:
                new_char = chr(ord(char) + 17)
                encrypted_stud_num += new_char

            i += 1
        
        try: 
            courses_file_path1 = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "2", encrypted_stud_num + ".txt")

            with open(courses_file_path1, 'r') as file1: # COMPLETE COURSE LIST

                complete_course = []

                for course_line in file1:
                    course_content = course_line.strip()
                    course_data = course_content.split('<--->')

                    course_details = []
                    course_details.append(course_data[0]) # Course Code
                    course_details.append(course_data[1]) # Course Units
                    course_details.append(course_data[2]) # Grade
                    course_details.append(course_data[3]) # Faculty Name
                    course_details.append(course_data[4]) # Day
                    course_details.append(course_data[5]) # Time

                    complete_course.append(course_details)
                
                item.append(complete_course)
    
        except FileNotFoundError:
            print(f"File not found: {courses_file_path1}")
            return None

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
        
        try: 
            courses_file_path2 = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "2", encrypted_stud_num + "1.txt")

            with open(courses_file_path2, 'r') as file2: # COMPLETE COURSE LIST

                current_course = []
                
                for course_line in file2:
                    course_content = course_line.strip()
                    course_data = course_content.split('<--->')

                    course_details = []
                    course_details.append(course_data[0]) # Course Code
                    course_details.append(course_data[1]) # Course Units
                    course_details.append(course_data[2]) # Grade
                    course_details.append(course_data[3]) # Faculty Name
                    course_details.append(course_data[4]) # Day
                    course_details.append(course_data[5]) # Time

                    current_course.append(course_details)
                
                item.append(current_course)
    
        except FileNotFoundError:
            print(f"File not found: {courses_file_path1}")
            return None

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

def load_admin_log():
    try:
        # Construct the file path relative to the parent folder
        db3_file_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "3", "2.txt")
        
        with open(db3_file_path, 'r') as file:
            
            for student_line in file:
                student_content = student_line.strip()
                student_data = student_content.split('<--->')
                
                student_details = []
                student_details.append(student_data[0]) # User ID
                student_details.append(student_data[1]) # Activity
                student_details.append(student_data[2]) # Date
                student_details.append(student_data[3]) # Time

                system_list.add_to_admin_log(student_details)
                
    except FileNotFoundError:
        print(f"File not found: {db3_file_path}")
        return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def load_stud_log():
    try:
        # Construct the file path relative to the parent folder
        db3_file_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "3", "1.txt")
        
        with open(db3_file_path, 'r') as file:
            
            for student_line in file:
                student_content = student_line.strip()
                student_data = student_content.split('<--->')
                
                student_details = []
                student_details.append(student_data[0]) # User ID
                student_details.append(student_data[1]) # Activity
                student_details.append(student_data[2]) # Date
                student_details.append(student_data[3]) # Time

                system_list.add_to_stud_log(student_details)
                
    except FileNotFoundError:
        print(f"File not found: {db3_file_path}")
        return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def load_exam_num(search_exam_num): # Retrieve the examinee number

    encrypted_exam_num = ""

    for char in str(search_exam_num):
        new_char = chr(ord(char) + 3)
        encrypted_exam_num += new_char

    try:
        #Define the exam number file path
        exam_num_file = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "1", "DB1.txt")

        # nitialize variables
        lines = []
        matching_line = None

        #Read the file and search for the matching examinee number
        with open(exam_num_file, 'r') as file:
            for line in file:
                values = line.split('<--->')
                if values[0] == encrypted_exam_num:
                    matching_line = line.strip()
                else:
                    lines.append(line)

        #Rewrite the file without the matching examinee number
        with open(exam_num_file, 'w') as file:
            file.writelines(lines)

        #Return the matching line (examinee number)
        return matching_line

    except FileNotFoundError:
        print(f"File not found: {exam_num_file}")
        return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def save_indiv_stud_info(): #Save individual student details
    try:
        # Construct the file path relative to the parent folder
        db2_file_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "1", "DB2.txt")

        with open(db2_file_path, 'w') as file:
            for student_data in SystemList.system_list:
                
                student_details = []
                student_details.append(encrypt(decrypt(str(student_data[4])))) # Student year
                student_details.append(encrypt(decrypt(str(student_data[5])))) # Current semester
                student_details.append(encrypt(decrypt(student_data[0]))) # Student number
                student_details.append(encrypt(decrypt(student_data[1]))) # Student last name
                student_details.append(encrypt(decrypt(student_data[2]))) # Student given name
                student_details.append(encrypt(decrypt(student_data[3]))) # Student middle name
                
                student_details.append(encrypt(decrypt(student_data[6]))) # Password
                student_details.append(encrypt(decrypt(student_data[7]))) # Student status
                student_details.append(encrypt(decrypt(student_data[8]))) # Sex
                student_details.append(encrypt(decrypt(student_data[9]))) # Birthdate
                student_details.append(encrypt(decrypt(student_data[10]))) # Student phone number 
                student_details.append(encrypt(decrypt(student_data[11]))) # Student email address
                student_details.append(encrypt(decrypt(student_data[12]))) # Student address
                student_details.append(encrypt(decrypt(student_data[13]))) # Student's guardian's email address
                student_details.append(encrypt(decrypt(student_data[14]))) # Student's guardian's phone number             
                
                # Convert student_data list to string
                student_data_str = '<--->'.join(student_details)
                file.write(student_data_str + '\n')
                
    except Exception as e:
        print(f"An error occurred while saving student information: {str(e)}")    

def save_all_stud_course_info():

    sys_list = system_list.return_sys_list()

    for item in sys_list:

        encrypted_stud_num = ""

        i = 1
        for char in decrypt(item[0]):
            if i < 5:
                new_char = chr(ord(char) + 3)
                encrypted_stud_num += new_char
            else:
                new_char = chr(ord(char) + 17)
                encrypted_stud_num += new_char

            i += 1
        
        try: 

            complete_courses_file_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "2", encrypted_stud_num + ".txt")
            current_courses_file_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "2", encrypted_stud_num + "1.txt")

            with open(complete_courses_file_path, 'w') as complete_file:
                for course_details in item[15]:
                    course_data = '<--->'.join([
                        encrypt(decrypt(course_details[0])),                            # Course Code
                        encrypt(decrypt(str(course_details[1]))),                       # Course Units
                        encrypt(decrypt(str(course_details[2]))),           # Grade with two decimal places
                        encrypt(decrypt(course_details[3])),                            # Faculty Name
                        encrypt(decrypt(course_details[4])),                            # Day
                        encrypt(decrypt(course_details[5])),                            # Time
                    
                    ])
                    complete_file.write(course_data + '\n')

            with open(current_courses_file_path, 'w') as current_file:
                for course_details in item[16]:
                    course_data = '<--->'.join([
                        encrypt(decrypt(course_details[0])),                            # Course Code
                        encrypt(decrypt(str(course_details[1]))),                       # Course Units
                        encrypt(decrypt(str(course_details[2]))),           # Grade with two decimal places
                        encrypt(decrypt(course_details[3])),                            # Faculty Name
                        encrypt(decrypt(course_details[4])),                            # Day
                        encrypt(decrypt(course_details[5])),                            # Time
                    ])
                    current_file.write(course_data + '\n')
    
        except Exception as e:
            print(f"An error occurred while saving course information: {str(e)}")

def save_torRequest_List(): #Save all students who requested TOR
    try:
        # Construct the file path relative to the parent folder
        db3_file_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "1", "DB3.txt")

        with open(db3_file_path, 'w') as file:
            for student_data in SystemList().return_stud_tor_req_list():
                
                student_details = []
                student_details.append(encrypt(decrypt(student_data[0]))) # Student number
                student_details.append(encrypt(decrypt(student_data[1])))  # Student name
                student_details.append(encrypt(decrypt(student_data[2])))  # Student email address
                student_details.append(encrypt(decrypt(student_data[3])))  # purpose of requesting
                student_details.append(encrypt(decrypt(student_data[4])))  # date requested
                student_details.append(encrypt(decrypt(student_data[5])))  # Status
                
                # Convert student_data list to string
                student_data_str = '<--->'.join(student_details)
                file.write(student_data_str + '\n')
                
    except Exception as e:
        print(f"An error occurred while saving student information: {str(e)}")

def save_student_log():
    try:
        # Construct the file path relative to the parent folder
        db3_file_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "3", "1.txt")

        with open(db3_file_path, 'w') as file:
            for student_data in SystemList().return_stud_log():
                
                student_details = []
                student_details.append(encrypt(decrypt(student_data[0])))  # User ID
                student_details.append(encrypt(decrypt(student_data[1])))  # Activity
                student_details.append(encrypt(decrypt(student_data[2])))  # Date
                student_details.append(encrypt(decrypt(student_data[3])))  # Time
                
                # Convert student_data list to string
                student_data_str = '<--->'.join(student_details)
                file.write(student_data_str + '\n')
                
    except Exception as e:
        print(f"An error occurred while saving student information: {str(e)}")

def save_admin_log():
    try:
        # Construct the file path relative to the parent folder
        db3_file_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "3", "2.txt")

        with open(db3_file_path, 'w') as file:
            for admin_data in SystemList().return_admin_log():
                
                admin_details = []
                admin_details.append(encrypt(decrypt(admin_data[0])))  # User ID
                admin_details.append(encrypt(decrypt(admin_data[1])))  # Activity
                admin_details.append(encrypt(decrypt(admin_data[2])))  # Date
                admin_details.append(encrypt(decrypt(admin_data[3])))  # Time
                
                # Convert student_data list to string
                student_data_str = '<--->'.join(admin_details)
                file.write(student_data_str + '\n')
                
    except Exception as e:
        print(f"An error occurred while saving student information: {str(e)}")

def save_key():
    bin_fp = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "3", "3.bin")

    with open(bin_fp, 'wb') as file:
        data = str(nsm)
        encoded_data = data.encode()
        file.write(encoded_data)
        
def retrieve_torRequest_List():
    try:
        # Construct the file path relative to the parent folder
        db3_file_path = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "1", "DB3.txt")
        
        with open(db3_file_path, 'r') as file:
            
            for student_line in file:
                student_content = student_line.strip()
                student_data = student_content.split('<--->')
                
                student_details = []
                student_details.append(student_data[0]) # Student number
                student_details.append(student_data[1]) # Student name
                student_details.append(student_data[2]) # Student email 
                student_details.append(student_data[3]) # Purpose of transaction
                student_details.append(student_data[4]) # Date requested
                student_details.append(student_data[5]) # Status
                            
                system_list.add_to_stud_tor_req_list(student_details)
                
    except FileNotFoundError:
        print(f"File not found: {db3_file_path}")
        return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None