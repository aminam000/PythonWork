# Amina Muumin, muumi002, 08 HW7
#==========================================
# Name: studentGrades
# Purpose: creates a student object
# Precondition: It needs to have a studentid, a last name, a first name and a grade
# Input Parameter(s): a studentid, a last name, a first name and a grade
# Return Value(s): a student object with the updated values
#============================================
class StudentGrades:

    def __init__(self, studentID, lastName, firstName, grades):
        
        self.studentID = studentID
        self.lastName = lastName
        self.firstName = firstName
        self.grades = [[],[],[]]
 
    def setStudentID(self, studentID):
        self.studentID = studentID
    def setLastName(self, lastName):
        self.lastName = lastName
    def setFirstName(self, firstName):
        self.firstName = firstName
        
    def getStudentID(self):
        return int(self.studentID)
    def getLastName(self):
        return str(self.lastName)
    def getFirstName(self):
        return str(self.firstName)
    def getGrades(self):
        return self.grades

    def addGrade(self,score_type, score):
         if score_type == 'Q':
             self.grades[0].append(score)
         elif score_type == 'H':
             self.grades[1].append(score)
         elif score_type == 'L':
             self.grades[2].append(score)
    
             
    def averageGrades(self):
        ave_Q = sum(self.grades[0])/len(self.grades[0])
        ave_H = sum(self.grades[1])/len(self.grades[1])
        ave_L = sum(self.grades[2])/len(self.grades[2])
        new_averagegrade = [ave_Q, ave_H, ave_L]
        return new_averagegrade
    
    def __str__(self):
        return 'StudentID: ' + str(self.studentID) +'\nGrades: ' + str(self.grades) + '\nAverages: ' + str(self.averageGrades()) 
    
def main():    
    
    # Testing the constructor and getters and averagegrade:
    s1 = StudentGrades(104123, "Smith", "John", [[], [], []])
    s2 = StudentGrades(239108, "Ali", "James", [[], [], []])
    s3 = StudentGrades(544958, "Reddy", "Nicole", [[], [], []])
    
    s1.addGrade("Q", 100)
    s1.addGrade("Q", 12)
    s1.addGrade("H", 0)
    s1.addGrade("L", 50)
    
    s2.addGrade("Q", 80)
    s2.addGrade("Q", 42)
    s2.addGrade("H", 68)
    s2.addGrade("L", 70)
    
    s3.addGrade("Q", 55)
    s3.addGrade("Q", 25)
    s3.addGrade("H", 0)
    s3.addGrade("L", 0)
    s3.addGrade("L", 2)


    students = [s1, s2, s3]
    for x in students:
        print(x)

    
    

main()
              
#==========================================
# Name: CourseGrades
# Purpose: Creates an average grade for the course for students
# Precondition: StudentGrades needs to exist
# Input Parameter(s): course, section, semester, year, and list of StudentGrades objects
# Return Value(s): an average of all the students grades who are in the course
#============================================
class CourseGrades:

    def __init__(self, course, section, semester, year, grades):
        
        self.course = course
        self.section = section
        self.semester = semester
        self.year = year
        self.grades = [[],[],[]]
 
    def getGrades(self):
        return self.grades
    
    def printStudents(self):
        grades = self.getGrades()
        for x in grades:
            print(x)
            
    def addGrades(self, score):
        self.grades.append(score)

            
def main():    
   c1 = CourseGrades("Calculus", "Mathematics", "1", 2019, [[],[],[]])
   c1.addGrades([[1],[1],[1]])



   
   print(c1.grades)
   
main()
    

