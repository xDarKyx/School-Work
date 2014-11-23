from test.regrtest import count
class Statistics:
    def __init__(self,studentID,studentName,avGrade):
        self.studentID = studentID
        self.studentName = studentName
        self.avGrade = avGrade
        self.cout = count
        
    def getSStudentID(self):
        return self.studentID
    def setSStudentID(self,stid):
        self.studentID = stid
    
    def getSSName(self):
        return self.studentName
    def setSSName(self,stname):
        self.studentName = stname
        
    def getavGrade(self):
        return self.avGrade
    def setavGrade(self,sgrd):
        self.Grade = sgrd
        
class avarage:
    def __init__(self,studentName,avGrade):
        self.studentName=studentName
        self.avGrade=avGrade
    
    def getAName(self):
        return self.studentName
    def setAName(self,stname):
        self.studentName = stname
    
    def getAGrade(self):
        return self.avGrade
    def setAGrade(self,grd):
        self.avGrade = grd