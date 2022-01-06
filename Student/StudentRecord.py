import mysql.connector
from os import name,system
import datetime
import time

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

cur = mydb.cursor()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

try:
    data = 'CREATE DATABASE school'
    cur.execute(data)
    table = 'CREATE TABLE school.student(roll_number integer(4),name varchar(20),class varchar(20),section varchar(1),date varchar(25))'
    cur.execute(table)
    primary="ALTER TABLE school.student ADD PRIMARY KEY(roll_number)"
    cur.execute(primary)
except Exception as e:
    pass

class Student:
    def __init__(self,name):
        self.name=name

    def DisplayStudent(self):
        clear(),print(f"\n\n\t\t\t{self.name}")
        s = 'SELECT * FROM school.student'
        cur.execute(s)
        result = cur.fetchall()
        roll_no,name,clas1,section,date = "  ROLL NO.".center(10),"STUDENT NAME".center(20),"CLASS".center(30),"CLASS SECTION".center(38),"DATE".center(50)
        print('\n\n\n')
        print('='*157)
        print(f"{roll_no}||{name}||{clas1}||{section}||{date}")
        print('='*157)
        for row in result:
            roll_no = f"  {row[0]}".center(10)
            name = f"{row[1]}".center(20)
            clas1 = f"{row[2]}".center(30)
            section = f"{row[3]}".center(38)
            date = f"{row[4]}".center(50)

            print(f"{roll_no}||{name}||{clas1}||{section}||{date}")
            print('-'*157)

        input(),clear()

    def AddStudent(self):
        clear(),print(f"\n\n\t\t\t{self.name}")
        roll_no = input('\n\n\t\tPlease Enter The Roll Number Of Student : ').strip()
        try:
            roll_no = int(roll_no)
            name = input('\n\n\t\tPlease Enter The Name Of Student : ').strip().title()
            clas1 = input('\n\n\t\tPlease Enter The Class Of Student: ').strip().title()
            section = input('\n\n\t\tPlease Enter the Section Of Student : ').strip().title()

        except Exception as e:
            print('\n\n\t\tOnly Numbers Are Allowed In Roll Number .')
        else:
            if len(str(roll_no)) == 4 and len(section) == 1:
                if name.isspace() or name.isdigit() or name=='' or clas1.isspace() or clas1.isdigit() or clas1=='' or section.isdigit() or section.isspace() or section == '':
                    print('\n\n\t\tOnly Alphabets Are Allowed In Name,Class and Section .')
                else:
                    cname,cclas1='',''
                    for i in name:
                        if i.isalpha() or i.isspace():
                            cname+=i
                    for i in clas1:
                        if i.isalpha() or i.isspace():
                            cclas1+=i
                    if cname==name and cclas1==clas1:
                        try:
                            s = "INSERT INTO school.student(roll_number,name,class,section,date) VALUE(%s,%s,%s,%s,%s)"
                            date = datetime.datetime.now()
                            ex = date.strftime("%x - %a - %X")
                            b1 = (roll_no,name,clas1,section,ex)
                            cur.execute(s,b1)
                        except Exception as e:
                            print('\n\n\t\tThis Roll Number Already Exists In Data Please CheckOut This !')
                        else:
                            print('\n\n\t\tData Store In DataBase Successfully ! ')
                    else:
                        print('\n\n\t\tOnly Alphabets Are Allowed In Name,Class and Section .')
            else:
                    print('\n\n\t\tFour Digits Are Required In Roll Number Only 1 Alphabet Is Required In Section Option !')
        input(),clear()         


    def SearchRoll(self):
        clear(),print(f"\n\n\t\t{self.name}")
        roll_no = input("\n\n\t\tPlease Enter The Roll Number Of Student : ").strip()
        try:
            roll_no = int(roll_no)
        except Exception as e:
            print('\n\n\t\tOnly Numbers are Allowed In Roll Number .')
        else:
            if len(str(roll_no)) == 4:
                s = f"SELECT * FROM school.student WHERE roll_number={roll_no}"
                cur.execute(s)
                res = cur.fetchall()
                if res == []:
                    print('\n\n\t\tThis Roll Number Not Exits In Data Base .')
                else:
                    print(f"\n\n\t\tStudent Name   : {res[0][1]}")
                    print(f"\n\n\t\tStudent Class  : {res[0][2]}")
                    print(f"\n\n\t\tStudent Section: {res[0][3]}")
                    print(f"\n\n\t\tStudent Date.. : {res[0][4]}")
            else:
                print("\n\n\t\tFour Digits Are Requird In Roll Number ")

        input(),clear()

    def SearchName(self):
        clear(),print(f"\n\n\t\t{self.name}")
        name = input('\n\n\t\tPlease Enter The Name Of Student : ').strip().title()
        if name.isdigit() or name.isspace() or name=='':
            print('\n\n\t\tOnly Alphabets Are Allowed In Name .')
        else:
            cname = ''
            for i in name:
                if i.isalpha() or i.isspace():
                    cname+=i
            if name == cname:
                s = f"SELECT * FROM school.student WHERE name = '{name}'"
                cur.execute(s)
                res = cur.fetchall()
                if res == []:
                    print(f'\n\n\t\tThis {name} Name Students Not In DataBase .')
                else:
                    roll_no,name,clas1,section,date = "  Roll No.".center(10),"Student Name".center(20),"Class".center(30),"Section (...)".center(38),"Date".center(50)
                    print('\n\n\n')
                    print('='*157)
                    print(f"{roll_no}||{name}||{clas1}||{section}||{date}")
                    print('='*157)
                    for row in res:
                        roll_no = f"  {row[0]}".center(10)
                        name = f"{row[1]}".center(20)
                        clas1 = f"{row[2]}".center(30)
                        section = f"{row[3]}".center(38)
                        date = f"{row[4]}".center(50)

                        print(f"{roll_no}||{name}||{clas1}||{section}||{date}")
                          
            else:
                print("\n\n\t\tOnly Alphabets Are Allowed In Name .")
        input(),clear()
   

    def DeleteStudent(self):
        clear(),print(f"\n\n\t\t{self.name}")
        roll_no = input("\n\n\t\tPlease Enter The Roll Number Of Student : ").strip()
        try:
            roll_no = int(roll_no)
        except Exception as e:
            print("\n\n\t\tOnly Numbers Are Allowed In This Programme .")
        else:
            if len(str(roll_no)) == 4 :

                s = f"SELECT * FROM school.student WHERE roll_number = {roll_no} "
                cur.execute(s)
                res = cur.fetchall()
                if res == []:
                    print("\n\n\t\tWe Have Not This Roll Number Type Data .")
                else:
                    s = f"DELETE FROM school.student WHERE roll_number = {roll_no} "
                    cur.execute(s)
                    print(f"\n\n\t\tStudent {res[0][1]} Data Is Deleted Completely In DataBase .")
            else:
                print(f"\n\n\t\tFour Digits Are Required In Roll Number .")        

        input(),clear()

    
    def constant(self,roll_no_p):
        clear(),print(f"\n\n\t\t\t{std.name}")
        print('\n\n\t\t\t\tUPDATION OF STUDENT IN THIS SECTION \n\n')
        roll_no = input('\n\n\t\tPlease Enter The Roll Number Of Student : ').strip()
        try:
            roll_no = int(roll_no)
            name = input('\n\n\t\tPlease Enter The Name Of Student : ').strip().title()
            clas1 = input('\n\n\t\tPlease Enter The Class Of Student: ').strip().title()
            section = input('\n\n\t\tPlease Enter the Section Of Student : ').strip().title()

        except Exception as e:
            print('\n\n\t\tOnly Numbers Are Allowed In Roll Number .')
        else:
            if len(str(roll_no)) == 4 and len(section) == 1:
                if name.isspace() or name.isdigit() or name=='' or clas1.isspace() or clas1.isdigit() or clas1=='' or section.isdigit() or section.isspace() or section == '':
                    print('\n\n\t\tOnly Alphabets Are Allowed In Name,Class and Section .')
                else:
                    cname,cclas1='',''
                    for i in name:
                        if i.isalpha() or i.isspace():
                            cname+=i
                    for i in clas1:
                        if i.isalpha() or i.isspace():
                            cclas1+=i
                    if cname==name and cclas1==clas1:
                        s = f"DELETE FROM school.student WHERE roll_number = {roll_no_p} "
                        cur.execute(s)
                        s = "INSERT INTO school.student(roll_number,name,class,section,date) VALUE(%s,%s,%s,%s,%s)"
                        date = datetime.datetime.now()
                        ex = date.strftime("%x - %a")
                        b1 = (roll_no,name,clas1,section,ex)
                        cur.execute(s,b1)
                    else:
                        print('\n\n\t\tOnly Alphabets Are Allowed In Name,Class and Section .')
                        
           

    def update(self):
        clear(),print(f"\n\n\t\t{self.name}")
        roll_no = input('\n\n\t\tPlease Enter The Roll Number Of Student : ').strip()
        try:
            roll_no = int(roll_no)
        except Exception as e:
            print('\n\n\t\tOnly Numbers Are Allowed In The Roll Number .')
        else:
            if len(str(roll_no)) == 4:
                search = f'SELECT * FROM school.student WHERE roll_number = {roll_no}'
                cur.execute(search)
                res = cur.fetchall()
                if res == []:
                    print('\n\n\t\tWe Have Not This Roll Number Data In DataBase .')
                else:
                   self.constant(roll_no)

            else:
                print('\n\n\t\tFour Digits Are Required In Roll Number .')
        
        input(),clear()   
           
    def EmptyAllData(self):
        clear()
        print("\n\n\t\tDATA DELETED PROCESSOR IN THIS SECTION PLEASE WAIT ..")
        time.sleep(2)
        new = ""
        for i in range(101):       
            time.sleep(0.002)
            print(f"\n\n\t\t{self.name}")
            print(f"\n\n\t\tDeleting Proceduing {i}% ")
            clear()
        print(f"\n\n\t\t{self.name}")
        choice = input('\n\n\n\n\t\t\t\tDO YOUR REALLY WANT TO DELETE ALL THE DATA IN RECORD y/n ? ')
        if choice == 'y':
            s = 'TRUNCATE TABLE school.student'
            cur.execute(s)
            print(f"\n\n\t\t{self.name}")
            print('\n\n\t\tAll The Data In Database Deleted Successfully 100% .')
        else:
            print('\n\n\t\tALL THE DATA IS SAFED IN RECORD PRESS ENTER TO GO IN MAIN MENU .')

        input(),clear()


if __name__ == "__main__":


    std = Student('GOVT. MUSLIM HIGH SCHOOL CHOWK AZAM')

    while True:
        print(f"\n\n\t\t\t\t\t{std.name}")
        print("\n\n\t\t1 . DISPLAY ALL THE STUDENTS RECORD")
        print("\n\n\t\t2 . ADD THE STUDENT RECORD IN DATABASE")
        print("\n\n\t\t3 . SEARCH THE STUDENT BY ROLL NUMBER")
        print("\n\n\t\t4 . SEARCH THE STUDENT BY NAME IN DATA")
        print("\n\n\t\t5 . DELETE THE STUDENT RECORD IN DATA")
        print("\n\n\t\t6 . UPDATE THE STUDENT RECORD IN DATA")
        print("\n\n\t\t7 . DELETE ALL THE IN DATABASE")
        print("\n\n\t\t8 . EXIT OR CLOSE THE PROGRAMME")

        choice = input('\n\n\n\n\t\tPLEASE ENTER YOUR CHOICE FOR DATA : ')
        if choice == '1':
            std.DisplayStudent()

        elif choice == '2':
            std.AddStudent()

        elif choice == '3':
            std.SearchRoll()

        elif choice == '4':
            std.SearchName()
        elif choice == '5':
            std.DeleteStudent()
        elif choice == '6':
            std.update()

        elif choice == '7':
            std.EmptyAllData()

        elif choice == '8':
            exit()

        else:
            print('\n\n\t\tInvalid Choice Please Check Out This !')
            input(),clear()
            
        mydb.commit()