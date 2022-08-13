# https://www.hackerrank.com/challenges/30-inheritance/submissions/code/231145985
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
    
    
class Student(Person):
   def __init__(self, firstName, lastName, idNumber, scores):
      super().__init__(firstName, lastName, idNumber)
      self.scores = score

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores   
    
    def calculate(self):
        char, sumof = "X", 0
        
        for i in scores:
            sumof += i
        
        sumof /= len(scores)      
        
        if sumof >= 90 and sumof <= 100:
            return "O"
        elif sumof >= 80 and sumof < 90:
            return "E"
        elif sumof >= 70 and sumof < 80:
            return "A"
        elif sumof >= 55 and sumof < 70:
            return "P"
        elif sumof >= 40 and sumof < 55:
            return "D"
        else:
            return "T"
          
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
