from config import *
from students import *

def select_new_subs():

    stud_list = SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()]

    comp_course = stud_list[15] # Complete courses list
    curr_course = stud_list[16] # Current courses list

    new_courses = []

    for item in curr_course:
        if float(decrypt(item[2])) > 3.00:
            stud_list[7] = encrypt_w_ok("IRREGULAR")
            break

    for item in curr_course:

        # 1st Year - 1st Semester
        if item[0] == encrypt_w_ok("CC131L"):

            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CC132"):
                    break
            
            if float(decrypt(item[2])) <= 3.00 and float(decrypt(item2[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CC141L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CC142"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)
                comp_course.append(crs2)

                new_courses.append(crs1)
                new_courses.append(crs2)
            else:
                crs1 = [encrypt_w_ok("CC131L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CC132"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CC131L") or x[0] == encrypt_w_ok("CC132"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CC131L/CC132 grade in the complete course list
                        x[3] = ""    # Update CC131L/CC132 faculty in the complete course list
                        x[4] = ""    # Update CC131L/CC132 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("MATHA05S"):

            if float(decrypt(item[2])) <= 3.00:
                crs1 = [encrypt_w_ok("MATHA35"), encrypt_w_ok(str(5)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)

                new_courses.append(crs1)
            else:
                crs1 = [encrypt_w_ok("MATHA05S"), encrypt_w_ok(str(5)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("MATHA05S"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update MATHA05S grade in the complete course list
                        x[3] = ""    # Update MATHA05S faculty in the complete course list
                        x[4] = ""    # Update MATHA05S schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CC113"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CC113"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CC113"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update MATHA05S grade in the complete course list
                        x[3] = ""    # Update MATHA05S faculty in the complete course list
                        x[4] = ""    # Update MATHA05S schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        # 1st Year - 2nd Semester
        elif item[0] == encrypt_w_ok("CC141L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CC142"):
                    break
            
            if float(decrypt(item[2])) <= 3.00 and float(decrypt(item2[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CC211L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CC212"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs3 = [encrypt_w_ok("CS213"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)
                comp_course.append(crs2)
                comp_course.append(crs3)

                new_courses.append(crs1)
                new_courses.append(crs2)
                new_courses.append(crs3)
            else:
                crs1 = [encrypt_w_ok("CC141L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs1 = [encrypt_w_ok("CC142"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CC141L") or x[0] == encrypt_w_ok("CC142"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CC141L/CC142 grade in the complete course list
                        x[3] = ""    # Update CC141L/CC142 faculty in the complete course list
                        x[4] = ""    # Update CC141L/CC142 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CC103"):
            if float(decrypt(item[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CS233"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)

                new_courses.append(crs1)
            else:
                crs1 = [encrypt_w_ok("CC103"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CC103"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CC103 grade in the complete course list
                        x[3] = ""    # Update CC103 faculty in the complete course list
                        x[4] = ""    # Update CC103 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CS123"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS123"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS123"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update MATHA05S grade in the complete course list
                        x[3] = ""    # Update MATHA05S faculty in the complete course list
                        x[4] = ""    # Update MATHA05S schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("MATHA35"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("MATHA35"), encrypt_w_ok(str(5)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("MATHA35"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update MATHA35 grade in the complete course list
                        x[3] = ""    # Update MATHA35 faculty in the complete course list
                        x[4] = ""    # Update MATHA35 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        # 2nd Year - 1st Semester
        elif item[0] == encrypt_w_ok("CC211L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CC212"):
                    break

            for item3 in comp_course:
                if item3[0] == encrypt_w_ok("CS271L"):
                    break

            for item4 in comp_course:
                if item4[0] == encrypt_w_ok("CS272"):
                    break
            
            if float(decrypt(item[2])) <= 3.00 and float(decrypt(item2[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CC201L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CC202"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs3 = [encrypt_w_ok("CS243"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)
                comp_course.append(crs2)
                comp_course.append(crs3)

                new_courses.append(crs1)
                new_courses.append(crs2)
                new_courses.append(crs3)

                if float(decrypt(item3[2])) <= 3.00 and float(decrypt(item4[2])) <= 3.00:
                    crs3 = [encrypt_w_ok("CS201L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                    crs4 = [encrypt_w_ok("CS202"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                    # Add new subjects to complete course list
                    comp_course.append(crs3)
                    comp_course.append(crs4)

                    new_courses.append(crs3)
                    new_courses.append(crs4)

            else:
                crs1 = [encrypt_w_ok("CC211L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CC212"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CC211L") or x[0] == encrypt_w_ok("CC212"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CC211L/CC212 grade in the complete course list
                        x[3] = ""    # Update CC211L/CC212 faculty in the complete course list
                        x[4] = ""    # Update CC211L/CC212 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CS251L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CS252"):
                    break

            for item3 in comp_course:
                if item3[0] == encrypt_w_ok("CS213"):
                    break
            
            if float(decrypt(item[2])) <= 3.00 and float(decrypt(item2[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CS221L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS222"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)
                comp_course.append(crs2)

                new_courses.append(crs1)
                new_courses.append(crs2)

                if float(decrypt(item3[2])) <= 3.00:
                    crs3 = [encrypt("CC223"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                    # Add new subjects to complete course list
                    comp_course.append(crs3)

                    new_courses.append(crs3)

            else:
                crs1 = [encrypt("CS251L"), encrypt(str(1)), encrypt(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS252"), encrypt(str(2)), encrypt(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS251L") or x[0] == encrypt_w_ok("CS252"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS251L/CS252 grade in the complete course list
                        x[3] = ""    # Update CS251L/CS252 faculty in the complete course list
                        x[4] = ""    # Update CS251L/CS252 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CS271L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CS272"):
                    break
            
            if float(decrypt(item[2])) <= 3.00 and float(decrypt(item2[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CS261L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS262"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)
                comp_course.append(crs2)

                new_courses.append(crs1)
                new_courses.append(crs2)

            else:
                crs1 = [encrypt_w_ok("CS271L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS272"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS271L") or x[0] == encrypt_w_ok("CS272"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS271L/CS272 grade in the complete course list
                        x[3] = ""    # Update CS271L/CS272 faculty in the complete course list
                        x[4] = ""    # Update CS271L/CS272 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CS213"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS213"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS213"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS213 grade in the complete course list
                        x[3] = ""    # Update CS213 faculty in the complete course list
                        x[4] = ""    # Update CS213 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CS233"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS233"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS233"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS233 grade in the complete course list
                        x[3] = ""    # Update CS233 faculty in the complete course list
                        x[4] = ""    # Update CS233 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        # 2nd Year - 2nd Semester
        elif item[0] == encrypt_w_ok("CC201L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CC202"):
                    break

            for item3 in comp_course:
                if item3[0] == encrypt_w_ok("CS251L"):
                    break

            for item4 in comp_course:
                if item4[0] == encrypt_w_ok("CS252"):
                    break
            
            for item5 in comp_course:
                if item5[0] == encrypt_w_ok("MATHSTAT03"):
                    break
            
            if float(decrypt(item[2])) <= 3.00 and float(decrypt(item2[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CC312L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CC311L"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)
                comp_course.append(crs2)

                new_courses.append(crs1)
                new_courses.append(crs2)

                if float(decrypt(item3[2])) <= 3.00 and float(decrypt(item4[2])) <= 3.00:
                    crs3 = [encrypt_w_ok("CS351L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                    crs4 = [encrypt_w_ok("CS352"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                    # Add new subjects to complete course list
                    comp_course.append(crs3)
                    comp_course.append(crs4)

                    new_courses.append(crs3)
                    new_courses.append(crs4)

                if float(decrypt(item5[2])) <= 3.00:
                    crs5 = [encrypt_w_ok("CS333"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                    # Add new subjects to complete course list
                    comp_course.append(crs5)

                    new_courses.append(crs5)

            else:
                crs1 = [encrypt_w_ok("CC201L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CC202"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CC201L") or x[0] == encrypt_w_ok("CC202"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CC201L/CC202 grade in the complete course list
                        x[3] = ""    # Update CC201L/CC202 faculty in the complete course list
                        x[4] = ""    # Update CC201L/CC202 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CS201L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CS202"):
                    break

            for item3 in comp_course:
                if item3[0] == encrypt_w_ok("CC223"):
                    break
            
            if float(decrypt(item[2])) <= 3.00 and float(decrypt(item2[2])) <= 3.00 and float(decrypt(item3[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CS373"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)

                new_courses.append(crs1)

            else:
                crs1 = [encrypt_w_ok("CC201L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CC202"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CC201L") or x[0] == encrypt_w_ok("CC202"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CC201L/CC202 grade in the complete course list
                        x[3] = ""    # Update CC201L/CC202 faculty in the complete course list
                        x[4] = ""    # Update CC201L/CC202 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CS261L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CS262"):
                    break
            
            if float(decrypt(item[2])) <= 3.00 and float(decrypt(item2[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CS313"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)

                new_courses.append(crs1)

            else:
                crs1 = [encrypt_w_ok("CS261L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS262"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS261L") or x[0] == encrypt_w_ok("CS262"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS261L/CS262 grade in the complete course list
                        x[3] = ""    # Update CS261L/CS262 faculty in the complete course list
                        x[4] = ""    # Update CS261L/CS262 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CS221L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CS222"):
                    break
            
            if float(decrypt(item[2])) > 3.00 and float(decrypt(item2[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS221L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS222"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS221L") or x[0] == encrypt_w_ok("CS222"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS221L/CS222 grade in the complete course list
                        x[3] = ""    # Update CS221L/CS222 faculty in the complete course list
                        x[4] = ""    # Update CS221L/CS222 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CS243"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS243"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS243"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS243 grade in the complete course list
                        x[3] = ""    # Update CS243 faculty in the complete course list
                        x[4] = ""    # Update CS243 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CC223"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CC223"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CC223"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CC223 grade in the complete course list
                        x[3] = ""    # Update CC223 faculty in the complete course list
                        x[4] = ""    # Update CC223 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("MATHSTAT03"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("MATHSTAT03"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("MATHSTAT03"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update MATHSTAT03 grade in the complete course list
                        x[3] = ""    # Update MATHSTAT03 faculty in the complete course list
                        x[4] = ""    # Update MATHSTAT03 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        # 3rd Year - 1st Semester
        elif item[0] == encrypt_w_ok("CS351L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CS352"):
                    break
            
            if float(decrypt(item[2])) <= 3.00 and float(decrypt(item2[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CS361L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS362"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)
                comp_course.append(crs2)

                new_courses.append(crs1)
                new_courses.append(crs2)

            else:
                crs1 = [encrypt_w_ok("CS351L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS352"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS351L") or x[0] == encrypt_w_ok("CS352"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS351L/CS352 grade in the complete course list
                        x[3] = ""    # Update CS351L/CS352 faculty in the complete course list
                        x[4] = ""    # Update CS351L/CS352 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CS333"):
            if float(decrypt(item[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CS321L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS322"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs3 = [encrypt_w_ok("CS343"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)
                comp_course.append(crs2)
                comp_course.append(crs3)

                new_courses.append(crs1)
                new_courses.append(crs2)
                new_courses.append(crs3)
            else:
                crs1 = [encrypt_w_ok("CS333"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS333"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS333 grade in the complete course list
                        x[3] = ""    # Update CS333 faculty in the complete course list
                        x[4] = ""    # Update CS333 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CC311L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CC312"):
                    break
            
            if float(decrypt(item[2])) > 3.00 and float(decrypt(item2[2])) > 3.00:
                crs1 = [encrypt_w_ok("CC311L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CC312"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CC311L") or x[0] == encrypt_w_ok("CC312"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CC311L/CC312 grade in the complete course list
                        x[3] = ""    # Update CC311L/CC312 faculty in the complete course list
                        x[4] = ""    # Update CC311L/CC312 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CSE1"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CSE1"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CSE1"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CSE1 grade in the complete course list
                        x[3] = ""    # Update CSE1 faculty in the complete course list
                        x[4] = ""    # Update CS2E1 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CSE2"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CSE2"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CSE2"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CSE1 grade in the complete course list
                        x[3] = ""    # Update CSE1 faculty in the complete course list
                        x[4] = ""    # Update CS2E1 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CS373"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS373"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS373"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS373 grade in the complete course list
                        x[3] = ""    # Update CS373 faculty in the complete course list
                        x[4] = ""    # Update CS373 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CS313"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS313"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS313"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS313 grade in the complete course list
                        x[3] = ""    # Update CS313 faculty in the complete course list
                        x[4] = ""    # Update CS313 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        # 3rd Year - 2nd Semester
        elif item[0] == encrypt_w_ok("CS321L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CS322"):
                    break
            
            if float(decrypt(item[2])) > 3.00 and float(decrypt(item2[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS321L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS322"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS321L") or x[0] == encrypt_w_ok("CS322"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS321L/CS322 grade in the complete course list
                        x[3] = ""    # Update CS321L/CS322 faculty in the complete course list
                        x[4] = ""    # Update CS321L/CS322 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CS361L"):
            for item2 in comp_course:
                if item2[0] == encrypt_w_ok("CS362"):
                    break
            
            if float(decrypt(item[2])) > 3.00 and float(decrypt(item2[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS361L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
                crs2 = [encrypt_w_ok("CS362"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS361L") or x[0] == encrypt_w_ok("CS362"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS361L/CS362 grade in the complete course list
                        x[3] = ""    # Update CS361L/CS362 faculty in the complete course list
                        x[4] = ""    # Update CS361L/CS362 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
                new_courses.append(crs2)
        elif item[0] == encrypt_w_ok("CC303"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CC303"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CC303"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CC303 grade in the complete course list
                        x[3] = ""    # Update CC303 faculty in the complete course list
                        x[4] = ""    # Update CC303 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CS303"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS303"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS303"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS303 grade in the complete course list
                        x[3] = ""    # Update CS303 faculty in the complete course list
                        x[4] = ""    # Update CS303 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CS343"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS343"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS343"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS343 grade in the complete course list
                        x[3] = ""    # Update CS343 faculty in the complete course list
                        x[4] = ""    # Update CS343 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CSE3"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CSE3"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CSE3"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CSE3 grade in the complete course list
                        x[3] = ""    # Update CSE3 faculty in the complete course list
                        x[4] = ""    # Update CSE3 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CSE4"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CSE4"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CSE4"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CSE4 grade in the complete course list
                        x[3] = ""    # Update CSE4 faculty in the complete course list
                        x[4] = ""    # Update CSE4 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        # 4th Year - 1st Semester
        elif item[0] == encrypt_w_ok("CS413"):
            if float(decrypt(item[2])) <= 3.00:
                crs1 = [encrypt_w_ok("CS423"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                # Add new subjects to complete course list
                comp_course.append(crs1)

                new_courses.append(crs1)
            else:
                crs1 = [encrypt_w_ok("CS413"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS413"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS413 grade in the complete course list
                        x[3] = ""    # Update CS413 faculty in the complete course list
                        x[4] = ""    # Update CS413 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CS433"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS433"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS433"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS433 grade in the complete course list
                        x[3] = ""    # Update CS433 faculty in the complete course list
                        x[4] = ""    # Update CS433 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        # 4th Year - 2nd Semester
        elif item[0] == encrypt_w_ok("CS403"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS403"), encrypt_w_ok(str(6)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS403"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS403 grade in the complete course list
                        x[3] = ""    # Update CS403 faculty in the complete course list
                        x[4] = ""    # Update CS403 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        elif item[0] == encrypt_w_ok("CS423"):
            if float(decrypt(item[2])) > 3.00:
                crs1 = [encrypt_w_ok("CS423"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

                for x in SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][15]:
                    if x[0] == encrypt_w_ok("CS423"):
                        x[2] = encrypt_w_ok(str(0.00))  # Update CS423 grade in the complete course list
                        x[3] = ""    # Update CS423 faculty in the complete course list
                        x[4] = ""    # Update CS423 schedule in the complete course list
                        x[5] = ""

                new_courses.append(crs1)
        
    # SUBJECTS WITH NO PREREQUISITES
    if int(decrypt(stud_list[4])) == 1 and stud_list[5] == 1:
        crs1 = [encrypt_w_ok("CC103"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]
        crs2 = [encrypt_w_ok("CS123"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

        comp_course.append(crs1)
        comp_course.append(crs2)

        new_courses.append(crs1)
        new_courses.append(crs2)
    elif int(decrypt(stud_list[4])) == 1 and int(decrypt(stud_list[5])) == 2:
        crs1 = [encrypt_w_ok("CS251L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
        crs2 = [encrypt_w_ok("CS252"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]
        crs3 = [encrypt_w_ok("CS271L"), encrypt_w_ok(str(1)), encrypt_w_ok(str(0.00)), "", "", ""]
        crs4 = [encrypt_w_ok("CS272"), encrypt_w_ok(str(2)), encrypt_w_ok(str(0.00)), "", "", ""]

        comp_course.append(crs1)
        comp_course.append(crs2)
        comp_course.append(crs3)
        comp_course.append(crs4)

        new_courses.append(crs1)
        new_courses.append(crs2)
        new_courses.append(crs3)
        new_courses.append(crs4)
    elif int(decrypt(stud_list[4])) == 2 and int(decrypt(stud_list[5])) == 1:
        crs1 = [encrypt_w_ok("MATHSTAT03"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

        comp_course.append(crs1)

        new_courses.append(crs1)
    elif int(decrypt(stud_list[4])) == 2 and int(decrypt(stud_list[5])) == 2:
        crs1 = [encrypt_w_ok("CSE1"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]
        crs2 = [encrypt_w_ok("CSE2"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

        comp_course.append(crs1)
        comp_course.append(crs2)

        new_courses.append(crs1)
        new_courses.append(crs2)
    elif int(decrypt(stud_list[4])) == 3 and int(decrypt(stud_list[5])) == 1:
        for item in comp_course:
            if item[0] == encrypt_w_ok("CS233"):
                break

        if float(decrypt(item[2])) <= 3.00:
            crs1 = [encrypt_w_ok("CS303"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

            # Add new subjects to complete course list
            comp_course.append(crs1)

            new_courses.append(crs1)

        crs2 = [encrypt_w_ok("CC303"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]
        crs3 = [encrypt_w_ok("CSE3"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]
        crs4 = [encrypt_w_ok("CSE4"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

        comp_course.append(crs2)
        comp_course.append(crs3)
        comp_course.append(crs4)

        new_courses.append(crs2)
        new_courses.append(crs3)
        new_courses.append(crs4)
    elif int(decrypt(stud_list[4])) == 3 and int(decrypt(stud_list[5])) == 2:
        crs1 = [encrypt_w_ok("CS413"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]
        crs2 = [encrypt_w_ok("CS433"), encrypt_w_ok(str(3)), encrypt_w_ok(str(0.00)), "", "", ""]

        comp_course.append(crs1)
        comp_course.append(crs2)

        new_courses.append(crs1)
        new_courses.append(crs2)
    elif int(decrypt(stud_list[4])) == 4 and int(decrypt(stud_list[5])) == 1:
        crs1 = [encrypt_w_ok("CS403"), encrypt_w_ok(str(6)), encrypt_w_ok(str(0.00)), "", "", ""]

        comp_course.append(crs1)

        new_courses.append(crs1)

    # UPDATE YEAR AND SEMESTER
    if int(decrypt(stud_list[5])) == 1:
        stud_list[5] = encrypt_w_ok(str(2))
    else:
        if int(decrypt(stud_list[4])) < 4:
            stud_list[4] = encrypt_w_ok(str(int(decrypt(stud_list[4])) + 1))
            stud_list[5] = encrypt_w_ok(str(1))
    
    SystemList().return_sys_list()[StudentPosition.get_instance().get_stud_post()][16] = new_courses # Set as the current course list
