'''University Management System'''

class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
class student(person):
    def __init__(self,name,age,gender,student_id, major,year):
        self.student_id=student_id
        self.major=major
        self.year=year
        super().__init__(name,age,gender)
    def get_study_level(self):
        if self.year==1 or self.year==2 or self.year==3 or self.year==4:
            print("Undergraduate") 
        else:
            print( "Postgraduate")
class faculty(person):
    def __init__(self,name,age,gender,faculty_id, department, title):
        super().__init__(name,age,gender)
        self.faculty_id=faculty_id
        self.department=department
        self.title=title
        
    def get_title(self):

        print(f"name={self.name} ,age={self.age} , gender={self.gender}, faculty_id={self.faculty_id}, department={self.department} title={self.title}")
        #return self.title
s1=student("Niloy",20,"Male",1003,"ITM",2)
s1.display_info()
s1.get_study_level()
f1=faculty("Raisul",30,"male",20,"ITM","lecturer")
f1.get_title()
