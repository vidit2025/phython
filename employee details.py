<<<<<<< HEAD
#Parent class
class Person( object ):
          #__init__ is known as the constructor
          def __init__(self, name, idnumber):
                  self.name = name
                  self.idnumber = idnumber
          def display(self):
                  print(self.name)
                  print(self.idnumber)


#child class   
class Employee( Person ):
         def __init__(self, name , idnumber, salary, post):
                 self.salary = salary
                 self.post = post

                 #invoking the __init__ of the parent class
                 Person.__init__(self, name, idnumber)


#creation of an object variable or an instance 
a = Employee('vidit', 20212428, 15000, "Intern")

# calling a function of the class person using its instance
=======
#Parent class
class Person( object ):
          #__init__ is known as the constructor
          def __init__(self, name, idnumber):
                  self.name = name
                  self.idnumber = idnumber
          def display(self):
                  print(self.name)
                  print(self.idnumber)


#child class   
class Employee( Person ):
         def __init__(self, name , idnumber, salary, post):
                 self.salary = salary
                 self.post = post

                 #invoking the __init__ of the parent class
                 Person.__init__(self, name, idnumber)


#creation of an object variable or an instance 
a = Employee('vidit', 20212428, 15000, "Intern")

# calling a function of the class person using its instance
>>>>>>> e8ce271afc779164b220b9d5c8d606bdd7e82efa
a.display()                 