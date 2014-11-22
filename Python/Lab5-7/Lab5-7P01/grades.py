class grades:
    def __init__(self,studentID,discipline,teacher,grade):
        self.studentID = studentID
        self.discipline = discipline
        self.teacher = teacher
        self.grade = grade

    def getGStudentID(self):
        return self.studentID
    def setGStudentID(self, stID):
        self.studentID = stID
        
    def getDiscipline(self):
        return self.discipline
    def setDiscipline(self, discip):
        self.discipline = discip
    
    def getTeacher(self):
        return self.teacher
    def setTeacher(self, tchr):
        self.teacher = tchr
        
    def getGrade(self):
        return self.grade
    def setGrade(self, grd):
        self.grade = grd