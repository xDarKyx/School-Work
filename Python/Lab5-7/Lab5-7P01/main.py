'''Created by Sandor Feher-Simon 22.11.2014'''

from Functions import *         

students=[]
disciplines=[]
OpCode=1
while(OpCode in range(1,4)):
    print("Main Menu:")
    print("1- Manage")
    print("2- Search")
    print("3- Statistics")
    print("0- Exit")
    OpCode=int(input("Dati varianta: "))
    if(OpCode==1):
        print("Manage Menu:")
        print("1- Add new student")
        print("2- Add new discipline")
        print("3- Update a discipline")
        print("4- Remove a discipline")
        print("5- Remove a student")
        mOpCode = int(input("Chose path:"))
        if(mOpCode == 1):
            sID=int(input("StudentID:"))
            AddStudent(sID, students)
        elif(mOpCode == 2):
            sID=int(input("StudentID:"))
            Discipline=input("Discipline:")
            AddDiscipline(sID,Discipline,disciplines,students)
        elif(mOpCode == 3):
            sID=int(input("StudentID:"))
            Discipline=input("Discipline:")
            UpdateDiscipline(sID,Discipline,disciplines)
        elif(mOpCode == 4):
            sID=input("StudentID:")
            Discipline=input("Discipline:")
            RemoveDiscipline(sID,Discipline,disciplines)
        elif(mOpCode == 5):
            sID=input("StudentID:")
            RemoveStudent(sID,disciplines,students)
    
    elif(OpCode==2):
        print("Search Menu:")
        print("1- Find Student by ID")
        print("2- Find Discipline by Title")
        mOpCode = int(input("Chose path:"))
        if(mOpCode == 1):
            sID=int(input("StudentID:"))
            FindByID(sID,students,disciplines)
        elif(mOpCode == 2):
            Discipline=input("Discipline:")
            FindByDiscipline(Discipline,disciplines)
    elif(OpCode==3):
        print("Statistics Menu:")
        print("1- Sort alphabetically ")
        print("2- Sort by grades")
        print("3- Sort by avarage grades")
        mOpCode = int(input("Chose path:"))
        if(mOpCode == 1):
            Discipline = str(input("Discipline:"))
            Stati1(Discipline,students,disciplines)
        elif(mOpCode == 2):
            Discipline = str(input("Discipline:"))
            Stati2(Discipline,students,disciplines)
        elif(mOpCode == 3):
            Stati3(students,disciplines)