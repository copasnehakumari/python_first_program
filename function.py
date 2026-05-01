"""def name():
 for i in range(1,11):
  print(i,"_","sneha")
name()


def number():
 for i in range(1,11):
  print(i)
number()

def number(a,b):
 print(a+b)
number(10,20)
number(10,10)
number(20,20)


def num(a,b,c):
 print(a+b+c)
num(10,20,30)"""

"""def sum():
 num1=int(input("enter first  number"))
 num2=int(input("enter secand  number"))
 opertor=input("enter your opertor")
 while opertor  in["+","-","*","/"]:
  
  if opertor=="+":
    print(num1+num2)
  elif opertor=="-":
    print(num1-num2)
  elif opertor=="*":
    print(num1*num2)
  elif opertor=="/":
    print(num1/num2)
  else:
    print("invalid opertor") 
 opertor=input("enter your opertor")
sum()"""


'''def student(*name):
  for i in name:
   print(i)
student("js","iti","copa") '''







#return  function
'''def sum(a,b):
  return a+b
print(sum(10,20))'''




def sum(a,b):
  add=a+b
  sub=a-b
  return add,sub
add, sub=sum(10,20)
print(add,sub)