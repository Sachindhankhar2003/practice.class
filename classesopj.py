#class is template  




# class Laptop:

#     def _init_ (self):
#         print("Hello world")
    
#     def config(self):
#         print("Asus","17","1TB")
# Laptop1 = Laptop()
# Laptop2 = Laptop()

# #Laptop.config(Laptop1)
# Laptop1.config()
# Laptop2.config()

# class student:
#     def _init_ (self,name,rollno):
#         self.name = name
#         self.rollno = rollno


#         def info(self):
#             print("name is : ",self.name,"roll number is : " ,self.rollno)
# student1 = student("sachin","57")
# student2 = student("gaurav","70")
# print(id(student1))
# print(id(student2))
# student1.info()
# student2.info()


#p1 p2 is object
# class person:
#     def _init_ (self):
#         self.name = "Ishan"
#         self.number = 32
#     def compare(self,other):
#         if(self.number == other.number):
#             return True
#         else:
#             return False

# p1 = person()
# p2 = person()
# p2.number = 18
# #self it directly to that object  //compare to self
# #p2.compare(p1)

# if p1.compare(p2):
#     print("same")
# else:
#     print("different")

# print(p1.number)
# print(p2.number)

#class Car:
    #value of those object very from object to object instance variable
    #static variable = shared by the equal 
    # heep memory
    #self calling method to point a perticular point
    #company  = atteribute
    # milage  = variable
    #object = box
    #wheels  = class variable
    #car = class

#     wheels = 4
#     def __init__(self):
#         self.company = "BMW"
#         self.mileage = 100
        
# car1 = Car()
# car2 = Car()

# print(car1.mileage, car1.wheels)
# print(car2.mileage,car2.wheels)

class student:
      collageName = "LPU"  # variable
      def _init_ (self, python, web, math):
          self.subject1 = python
          self.subject2 = web
          self.subject3 = math

      def avgCalculator(self):
          return (self.subject1 + self.subject2 + self.subject3)/3

        
    #  def get_subject1(self):
    #  return self.subject1
    #below the class method
@classmethod
def collageDetail(cls):
     return cls.collageName


student1 = student(4,7,9)
student2 = student(4,3,6)

print(student1.avgCalculator())
print(student.collageDetail())


#method which are sending something  = mutators change value
#written something =  acceser
#class method   = not change




    