"""class student:
    name="sneha"
    age=20
sd=student()
print(f"name={sd.name}age={sd.age}")


class student:
    name="xyz"
a=student()
print(a.name)

#Encopevlation
class copa:
    def show(self):
        print("hello student")
    def data(s):
        print("js iti")
    
a=copa()
a.show()  
a.data()     


class copa:
    def data(self):
     self.name="sneha"
     self.trade="copa"
    def show(self): 
       print(self.name)
a=copa()
a.data()  
a.show()  




class copa:
    def data(self,name,trade):
     self.name= name
     self.trade=trade
    def show(self): 
      print(f"name={self.name} 
trade={self.trade}")
    
a=copa()
a.data("xyz","copa")  
a.show()  






class copa:
    def __init__(self):
     self.name="sneha"
     self.trade="copa"
    def show(self): 
       print(self.name)
a=copa()
a.show()


class bank:
    def __init__(self):
       self.blance=100
       print( self.blance)
    def depogiat(self,amount): 
     self.blance+=amount
    def show_blance(self):
       print("total blance", self.blance)
a=bank()
a.depogiat(100)
a.show_blance()"""



'''class bank:
    def __init__(self):
       self.blance=100
       print( "blance",self.blance)
    def depogiat(self,amount): 
       self.amount=amount
       print("depogiat",amount)
       self.blance+=amount

    def whidtht(self,amount):
        self.amount=amount
        print("whidtht",amount)
        self.blance-=amount
    
    def show_blance(self):
       print("total blance",self.blance)


a=bank()
a.depogiat(100)

a.whidtht(10)
a.show_blance()'''

'''class student():
    def __init__(self):
        self.name="neha"
        print(self.name)
a=student()
print(a.name)'''

'''class student():
    def __init__(self):
        self._name="neha"
        print(self._name)
a=student()
print(a._name)'''


'''class student():
    def __init__(self):
        self.__name="neha"
        print(self.__name)
a=student()'''

'''class parentclass:
    def __init__(self):
        self.name="js"

class childclass(parentclass):
    def copa(self):
        print(self.name)
a=childclass()
a.copa()'''

"""class mother:
    def __init__ (self):
        print("this is mother class")
class parent:
   def __init__ (self):
        print("this is the parent class")
class son(mother,parent):
    def __init__ (self):
        mother.__init__(self)
        parent.__init__ (self)
        print("this is son class")
    
s=son()"""

'''class iti:
    def js(self):
        print(" this is js iti")
class trade(iti):
    def copa(self):
        print(" this is copa labs ")    
class python(trade):
    def python(self):
        print(" this is python")  
a=python() 

a.python()
a.copa()
a.js()'''



'''a="hello"
l=[1,2,3,4]
t=(1,2,3,4,5)
print(len(a))
print(len(l))
print(len(t))'''

class animal:
    def sound(self):
        print("animal make sound")
        

class dog(animal):
    def sound(self):
        print("dog sound")    

class cat(animal):
    def sound(self):
        print("cat sound")

a=animal() 
b=dog()   
c=cat()          
b.sound()
a.sound()
c.sound()  

