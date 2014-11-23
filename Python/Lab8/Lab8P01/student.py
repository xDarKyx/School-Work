class student:
    def __init__(self,studentID,studentName):
        self.studentID = studentID
        self.studentName = studentName
        
    def getStudentID(self):
        return self.studentID
    def setStudentID(self,stID):
        self.studentID = stID
        
    def getStudentName(self):
        return self.studentName
    def setStudentName(self,stName):
        self.studentName = stName