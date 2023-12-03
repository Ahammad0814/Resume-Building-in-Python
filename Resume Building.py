from colorama import Style
print()
print()
print(' '*30,f"{Style.BRIGHT}MY RESUME BUILDER{Style.RESET_ALL}")
print()
modify_list = ['Skills','Education','Experience','Projects','Certificates','Hobbies']
skills_list = []
education_data = {}
experience_data = {}
projects_list = {}
certificate_lists = {}
hobbies_list = []
modify_entry_list = []
def templet_fun():
    print(' '*15,'⓵',' '*20,'⓶')
    print()
    print()
    print(' '*14,'Name',' '*14,'• Name')
    print(' '*14,'.'*5,' '*13,'|')
    print(' '*14,'.'*5,' '*13,'|')
    print(' '*10,'-'*12,' '*10,'_'*12)
    print(' '*10,'Skills',' '*16,'• Skills')
    print(' '*16,'.'*5,' '*11,'|')
    print(' '*16,'.'*5,' '*11,'|')
    print(' '*10,'-'*12,' '*10,'_'*12)
    print(' '*10,'Education',' '*13,'• Education')
    print(' '*16,'.'*5,' '*11,'|')
    print(' '*16,'.'*5,' '*11,'|')
    print(' '*10,'-'*12,' '*10,'_'*12)
    print(' '*10,'Experience',' '*12,'• Experience')
    print(' '*16,'.'*5,' '*11,'|')
    print(' '*16,'.'*5,' '*11,'|')
    print(' '*10,'-'*12,' '*10,'_'*12)
    print()
    print()
    print()
templet_fun()
def templet2():
    print()
    print('  •',f'{Style.BRIGHT}{name}{Style.RESET_ALL}')
    print('  •',gmail)
    global linkedin
    print('  •',linkedin)
    print('  •','+91 ',contact)
    print('_'*70)
    print()
    print('  ',f"{Style.BRIGHT}SKILLS:{Style.RESET_ALL}")
    print()
    for i in skills_list:
        print('  •',i)
    print('_'*70)
    print()
    if add_experience == 'Yes':
        print('  ',f"{Style.BRIGHT}EXPERIENCE:{Style.RESET_ALL}")
        print()
        for i in experience_data:
            print('  •',f"{Style.BRIGHT}{i}{Style.RESET_ALL}")
            print('  |',experience_data[i][0])
            print('  |',experience_data[i][1])
            print('  |',experience_data[i][2])
            print()
        print('_'*70)
        print()
    print('   ',f'{Style.BRIGHT}EDUCATION:{Style.RESET_ALL}')
    print()
    for i in education_data:
        print('  •',i)
        print('  |',education_data[i][0])
        print('  |',education_data[i][1])
        print('  |','GPA',education_data[i][2])
        print()
    print('_'*70)
    print()
    if add_projects == 'Yes':
        print('   ',f"{Style.BRIGHT}PROJECTS:{Style.RESET_ALL}")
        for i in projects_list:
            print()
            print('  •',f"{Style.BRIGHT}{i}{Style.RESET_ALL}")
            project_split = projects_list[i].split(' ')
            print('  |',end='')
            print(end='  ')
            proj_cnt = 0
            p_count = 8
            for i in project_split:
                print(i,end=' ')
                proj_cnt+=1
                if proj_cnt == p_count:
                    p_count+=8
                    print()
                    print('  |  ',end='')
            print()
        print('_'*70)
        print()
    if certificate == 'Yes':
        print('   ',f"{Style.BRIGHT}CERTIFICATES:{Style.RESET_ALL}")
        print()
        for i in certificate_lists:
            print()
            print('  •',f"{Style.BRIGHT}{i}{Style.RESET_ALL}")
            certificate_split = certificate_lists[i].split(' ')
            print('  |',end='')
            print(end='  ')
            cert_cnt = 0
            c_count = 8
            for i in certificate_split:
                print(i,end=' ')
                cert_cnt+=1
                if cert_cnt == c_count:
                    c_count+=8
                    print()
                    print('  |  ',end='')
            print()
        print('_'*70)
        print()
    if hobbie == 'Yes':
        print('   ',f"{Style.BRIGHT}HOBBIES:{Style.RESET_ALL}")
        for i in hobbies_list:
            print('  •',i)
    print('_'*70)
    print()
def templet1():
    print()            
    len1 = (100-len(name))//2
    print()
    print(len1*' ',f"{Style.BRIGHT}{name}{Style.RESET_ALL}")
    len2 = (100-len(contact))//2
    print(' '*(len2-3),'+91',contact)
    len3 = (100-len(gmail))//2
    print(len3*' ',gmail)
    if link == 'Yes':
        len4 = (100-len(linkedin))//2
        print(len4*' ',linkedin)
    print('_'*100)
    print()
    print(f"{Style.BRIGHT}SKILLS:{Style.RESET_ALL}")
    for i in skills_list:
        print(' '*35,'•',i)
    print()
    print('-'*100)
    print()
    print(f"{Style.BRIGHT}EDUCATION:{Style.RESET_ALL}")
    for i in education_data:
        print(' '*35,'•',f"{Style.BRIGHT}{i}{Style.RESET_ALL}")
        print(' '*37,education_data[i][0],'| GPA',education_data[i][2])
        print(' '*37,education_data[i][1])
        print()
    if add_experience == 'Yes':
        print('-'*100)
        print()
        print(f"{Style.BRIGHT}EXPERIENCE:{Style.RESET_ALL}")
        for i in experience_data:
            print(' '*35,'•',f"{Style.BRIGHT}{i}{Style.RESET_ALL}")
            print(' '*37,experience_data[i][0])
            print(' '*37,experience_data[i][1],'|',experience_data[i][2])
            print()
        print('-'*100)
        print()
    if add_projects == 'Yes':
        print(f"{Style.BRIGHT}PROJECTS:{Style.RESET_ALL}")
        for i in projects_list:
            print()
            print(' '*35,'•',f"{Style.BRIGHT}{i}{Style.RESET_ALL}")
            project_split = projects_list[i].split(' ')
            print(' '*37,end='')
            proj_cnt = 0
            p_count = 10
            for i in project_split:
                print(i,end=' ')
                proj_cnt+=1
                if proj_cnt == p_count:
                    p_count+=10
                    print()
                    print(' '*37,end='')
        print()
        print('-'*100)
        print()
    if certificate == 'Yes':
        print(f"{Style.BRIGHT}CERTIFICATE:{Style.RESET_ALL}")
        for i in certificate_lists:
            print()
            print(' '*35,'•',f"{Style.BRIGHT}{i}{Style.RESET_ALL}")
            certificate_split = certificate_lists[i].split(' ')
            print(' '*37,end='')
            cert_cnt = 0
            c_count = 10
            for i in certificate_split:
                print(i,end=' ')
                cert_cnt+=1
                if cert_cnt == c_count:
                    c_count+=10
                    print()
                    print(' '*37,end='')
            print()
        print()
        print('-'*100)
        print()
    if hobbie == 'Yes':
        print(f"{Style.BRIGHT}HOBBIES:{Style.RESET_ALL}")
        for i in hobbies_list:
            print(' '*35,'•',i)
    print()
    print('_'*100)
while True:
    choose_templet = input(f"{Style.BRIGHT}Choose your Templet: {Style.RESET_ALL}")
    print()
    if choose_templet.isdigit():
        break
    else:
        print('Please Enter 1 or 2, to choose Templet')
        print()
print(f"{Style.BRIGHT}Personal Details{Style.RESET_ALL}")
print()
while True:
    name = input('Enter your name: ')
    if len(name) >= 3:
        break
    else:
        print('Please enter valid name.')
        print()
while True:
    gmail = input('Enter your Gmail: ')
    if len(gmail) >= 13 and gmail.endswith('@gmail.com'):
        break
    else:
        print('Please enter valid Gmail.')
        print()
while True:
    link = input('Do you want to add linkedin / Github (yes/no): ').capitalize()
    if link == 'Yes':
        linkedin = input('Enter linkedin / Github profile: ')
        break
    elif link == 'No':
        break
    else:
        print('Please enter Yes or No')
        print()
num_list = ['6','7','8','9']
while True:
    contact = input('Enter you contact number +91:')
    if contact[0] in num_list and len(contact) == 10:
        break
    else:
        print('Enter Valid Contact number')
print()
def skills_details():
    print(f"{Style.BRIGHT}Skills:{Style.RESET_ALL}")
    print()
    while True:
        skills = input('How many skills would you like to add: ')
        print()
        if skills.isdigit():
            skill_cnt = 1
            for i in range(0,int(skills)):
                add_skills = input(f'Enter your {skill_cnt} skill: ')
                skills_list.append(add_skills)
                skill_cnt+=1
            break
        else:
            print('Enter a digits that how many skills like to add.')
            print()
        print()
    print()
skills_details()
def education_details():
    print(f"{Style.BRIGHT}Education Details:{Style.RESET_ALL}")
    print()
    while True:
        education = input('How many education entries would you like to add: ')
        print()
        if education.isdigit():
            break
        else:
            print('Enter a digit that how many education entries would like to add.')
            print()
    education_cnt = 1
    for i in range(int(education)):
        add_education = input(f'Enter your {education_cnt} (University / College) Name & Place: ')
        course = input('Enter your Degreee: ')
        while True:
            pass_year = input('Enter year of passed out: ')
            if 1947 < float(pass_year):
                break
            else:
                print('Entered year is invaled.\nPlease enter a valid year.')
                print()
        while True:
            gpa = input('Enter your GPA: ')
            if not gpa.isalpha():
                break
            else:
                print('Please enter a valid GPA.')
                print()
        education_cnt+=1
        print()
        education_data[add_education]=[course,pass_year,gpa]
education_details()
def experience_details():
    print()
    print(f"{Style.BRIGHT}Experience:{Style.RESET_ALL}")
    print()
    while True:
        global add_experience
        add_experience = input('Would like to add Work Experience ?(yes/no): ').capitalize()
        if add_experience == 'Yes':
            while True:
                exp = input('Enter how many experiences would like to add: ')
                print()
                if exp.isdigit():
                    break
                else:
                    print('Please enter digit that how many experiences would like to add')
                    print()
            exp_cnt = 1
            for i in range(int(exp)):
                print('Experience',exp_cnt)
                role = input('You worked as a: ')
                comp_name = input('Enter Company name: ')
                start_year = input('Enter starting month and year: ')
                while True:
                    work_here = input('Do you still work here ?(yes/no): ').capitalize()
                    if work_here == 'Yes':
                        end_year = 'Present'
                        break
                    elif work_here == 'No':
                        end_year = input('Enter ending year: ')
                        break
                    else:
                        print('Please enter Yes or No')
                        print()
                experience_data[comp_name]=[role,start_year,end_year]
                print()
                exp_cnt+=1
            break
        elif add_experience == 'No':
            break
        else:
            print('Enter Yes or No, to add work experience.')
            print()
experience_details()
def projects_details():
    print()
    print(f"{Style.BRIGHT}PROJECTS:{Style.RESET_ALL}")
    print()
    while True:
        global add_projects
        add_projects = input('Would like to add projects ?(Yes/No): ').capitalize()
        if add_projects == 'Yes':
            while True:
                repeat_project = input('How many projects would you like to add: ')
                if repeat_project.isdigit():
                    break
                else:
                    print('Enter a digit. How many project would like to add.')
            print()
            project_cnt = 1
            for i in range(int(repeat_project)):
                project_title = input(f'Enter your Project Title {project_cnt}: ')
                project_details = input('Enter about your project details: ')
                projects_list[project_title]=project_details
                print()
                project_cnt+=1
            break
        elif add_projects == 'No':
            break
        else:
            print('Enter Yes or No to add projects.')
projects_details()
def certificate_fun():
    print()
    print(f"{Style.BRIGHT}CERTIFICATES:{Style.RESET_ALL}")
    print()
    while True:
        global certificate
        certificate = input('Would you like to add Certificates ?(Yes/No): ').capitalize()
        if certificate == 'Yes':
            print()
            while True:
                repeat = input('How many certificates would like to add: ')
                if repeat.isdigit():
                    break                
                else:
                    print('Enter a digit to how many certificates to add.')
            print()
            certificate_cnt = 1
            for i in range(int(repeat)):
                certificate_title = input(f'Enter your certificate title {certificate_cnt}: ')
                certificate_details = input('Enter about your certificate details: ')
                certificate_lists[certificate_title]=certificate_details
                certificate_cnt+=1
                print()         
            break
        elif certificate == 'No':
            break
        else:
            print('Enter Yes or No to add certification.')
            print()
certificate_fun()
def hobbies_details():
    print()
    print(f"{Style.BRIGHT}HOBBIES:{Style.RESET_ALL}")
    print()
    while True:
        global hobbie
        hobbie = input('Would like to add Hobbies ?(yes/no): ').capitalize()
        print()
        if hobbie == 'Yes':
            while True:
                hobbies = input('How many hobbies would you like to add: ')
                print()
                hobbies_cnt = 1
                if hobbies.isdigit():
                    for i in range(0,int(hobbies)):
                        add_hobbies = input(f'Enter your hobbie {hobbies_cnt}: ')
                        hobbies_list.append(add_hobbies)
                        hobbies_cnt+=1
                    break
                else:
                    print('Enter a digits that how many skills like to add.')
                    print()
            break        
        elif hobbie == 'No':
            break
        else:
            print('Enter Yes or No, for hobbies.')
hobbies_details()
if choose_templet == '1':
    templet1()
if choose_templet == '2':
    templet2()
print()
print(' '*5,f"{Style.BRIGHT}MODIFY RESUME{Style.RESET_ALL}")
print()
while True:
    modify_data = input('Do you want to modify the resume ?(yes/no): ').capitalize()
    if modify_data == 'Yes':
        cnt = 1
        for i in  modify_list:
            print(f'  -> {cnt}',i)
            cnt+=1
        print()
        what_to_modify = input('How many entries want to Modify or Add ?: ')
        print()
        if what_to_modify.isdigit() and int(what_to_modify) <= len(modify_list):
            cnt = 1
            for i in  modify_list:
                print(f'  -> {cnt}',i)
                cnt+=1
            print()
            modify_cnt = int(what_to_modify)
            cnt=1
            while modify_cnt>0:
                modify_entries = input(f'Enter {cnt} entry from above options: ')
                if modify_entries in modify_list:
                    modify_entry_list.append(modify_entries)        
                else:
                    print(f'No data found on {modify_entries}')
                    modify_cnt += 1
                    print()
                cnt+=1
                modify_cnt -= 1
            print()
        else:
            print()
            print('Invalid Input. Input must be and between 1 - 6.')
            print()
        for entry in modify_entry_list:
            if entry == 'Skills':
                skills_list.clear()
                skills_details()
            if entry == 'Education':
                education_data.clear()
                education_details()
            if entry == 'Experience':
                experience_data.clear()
                experience_details()
            if entry == 'Certificate':
                certificate_lists.clear()
                certificate_fun()
            if entry == 'Projects':
                projects_list.clear()
                projects_details()
            if entry == 'Hobbies':
                hobbies_list.clear()
                hobbies_details()
    elif modify_data == 'No':
        break
    else:
        print('Enter Yes or No, to modify.')
print()
def change_templet():
    while True:
        change_temp = input('Do you want to change Templet ?(yes/no): ').capitalize()
        if change_temp == 'Yes' or 'No':
            break
        else:
            print('Please enter Yes or No, to change Templet.')
        if change_temp == 'Yes':
            templet_fun()
            print()
            temp = input('Choose Templet 1 or 2: ')
            if temp == '1':
                global templet1
                templet1()
            else:
                global templet2
                templet2()
change_templet()