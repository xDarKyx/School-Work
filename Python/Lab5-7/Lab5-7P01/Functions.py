from student import *
from grades import *
from statistics import *
import operator


def AddStudent(sID,students):
    isInList=False
    for x in students:
        if x.getStudentID()==sID:
            isInList=True
            print("The ID is already in use!")
    if isInList == False:
        sNAME=str(input("StudentName:"))
        students.append(student(sID,sNAME))
        
        
def AddDiscipline(sID,Discipline,disciplines,students):
    Found=False
    for x in disciplines:
        if Discipline == x.getDiscipline() and sID == x.getGStudentID() :
            Found=True
    if(Found==True):
        print("The entry already exists!")
    else:
        Teacher=input("Teacher:")
        Grade=int(input("Grade:"))
        disciplines.append(grades(sID,Discipline,Teacher,Grade))
        

def UpdateDiscipline(sID,Discipline,disciplines):
    Found = False
    for x in disciplines:
        if (sID == (x.getGStudentID()) and (Discipline == str(x.getDiscipline()))):
            Grade=int(input("New Grade:"))
            x.setGrade(Grade)
            Found = True
    if(Found == False):
        print("Couldn't find StudentID or Discipline")
        
def RemoveDiscipline(sID,Discipline,disciplines):
    Found = False
    for x in disciplines:
        if x.getGStudentID()==sID and x.getDiscipline() == Discipline:
            disciplines.pop(x)
            Found = True
    if(Found == False):
        print("Couldn't find the discipline or user does not exist")
        
def RemoveStudent(sID,disciplines,students):
    Found1 = False
    Found2 = False
    for x in students:
        if x.getStudentID()==sID:
            students.pop(x)
            Found1 = True
    for x in disciplines:
        if x.getGStudentID()==sID:
            disciplines.pop(x)
            Found2 = True
            
    if(Found1 == False):
        print("Couldn't find StudentID in Students List")
    if(Found2 == False):
        print("Student didn't have any grades")


def FindByID(sID,students,disciplines):
    Found = False
    Name = str("NULL")
    for x in students:
        if x.getStudentID()==sID:
            Name=x.getStudentName()
            Found=True
    for x in disciplines:
        if x.getGStudentID()==sID:
            print(" ID: ",sID," Name: ",Name," Discipline: ",x.getDiscipline()," Teacher: ",x.getTeacher()," Grade: ",x.getGrade())
    if Found == False:
        print("Couldn't find StudentID:")

def FindByDiscipline(Discipline,disciplines):
    Found = False
    for x in disciplines:
        if (Discipline == str(x.getDiscipline())):
            print(" StudentID: ",x.getGStudentID()," Teacher: ",x.getTeacher()," Grade: ",x.getGrade())
            Found = True
    if Found == False:
        print("Couldn't find any entry for discipline ",Discipline)
 
def Stati1(Discipline,students,disciplines):
    sorted_alpha = sorted(students, key=lambda student: student.studentName)
    for i in sorted_alpha:
        for k in disciplines:
            if i.getStudentID() == k.getGStudentID() and k.getDiscipline() == Discipline:
                print("  ID:  ",i.getStudentID() , "  Name:  ",i.getStudentName(),"  Grade:  ",k.getGrade(),"  Discipline:  ",k.getDiscipline())

def Stati2(Discipline,students,disciplines):
    sorted_grades = sorted(disciplines, key=lambda grades: grades.grade)
    for k in sorted_grades:
        for i in students:
            if i.getStudentID() == k.getGStudentID() and k.getDiscipline() == Discipline:
                print("  ID:  ",i.getStudentID() , "  Name:  ",i.getStudentName(),"  Grade:  ",k.getGrade(),"  Discipline:  ",k.getDiscipline())

def Stati3(students,disciplines):
    FullList=[]
    avarageList=[]
    for k in disciplines:
        for i in students:
            if i.getStudentID() == k.getGStudentID():
                FullList.append(Statistics(i.getStudentID(),i.getStudentName(),k.getGrade()))
    for k in students:
        GradesSum=0
        Count=0
        avarageOfGrades=0
        for i in FullList:
            if k.getStudentID() == i.getSStudentID():
                GradesSum=GradesSum+i.getavGrade()
                Count=Count+1
        avarageOfGrades=GradesSum/Count
        avarageList.append(avarage(k.getStudentName(),avarageOfGrades))
    sortedAvarage=sorted(avarageList, key=lambda avarage: avarage.avGrade,reverse=True)
    for k in sortedAvarage:
        print("Student Name: ",k.getAName(),"  Avarage Grade: ",k.getAGrade())