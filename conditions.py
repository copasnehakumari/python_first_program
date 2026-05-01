#example of if conditions


'''num=5
if num>0:
    print("number is postive")

    num=-5
if num<0:
    print("number is negative")'''

#example of if and else conditions

'''  password=1234
username="sneha"
if password==1234 and username=="sneha":
    print("login is successfull")
else : 
     print(" username and password not match")'''  

#example of even and odd number
"""
num=10
if num%2==0:
    print("even number") 
else:
    print("odd number")
 

#example of if and else condition
    marks=30
if marks>33:
    print("pass")
else:
    print ("fail")"""
#example of if elif else condition

'''   marks=100
if marks>80:
    print("grate(A)")
elif marks>60:
    print("grate (B)")  
elif marks>50:
    print("grate (C)") 
elif marks>34:
    print("grate (C)") 
     
else:
    print ("fail") '''  


name = "sneha"
city = "varansi"
trade = "copa"

'''if name == "sneha":
    print("name is match")
    
    if city == "varansi":
        print("city is match")
        
        if trade == "copa":
            print("trade is match")
        else:
            print(" not match")'''

"""atte=70
practical=33
fees="no"  
            
if atte>=70:
 if practical>=33:
  if fees=="yes":
   print("downlode")
  else:
         print("you are not eligibale")  
 else:
         print("you are not eligibale")     
else:
 print("you are not eligibale")""" 

"""month=2
match month:
    case 1:
        print("January")
    case 2:
        print("February")        
    case 3:
        print("January") 
    case 4:
        print("April") 
    case 5:
        print("May") 
    case 6:
        print("June") 
    case 7:
        print("July") 
    case 8:
        print("August") 
    case 9:
        print("septemeber") 
    case 10:
        print("Octber") 
    case 11:
        print("Nomvember") 
    case 12:
        print("december") 
    case _:
        print("Invalid Number") """


username="student"
password="123"

match username:
    case "admin":
        if password == "123" :
          print("admin login ")
        else:
          print("admin username nad password not match")

    case "subadmin":
            if password == "1234" :
             print("subadmin login ")
            else:
                print("subadmin username nad password nat match")
    case "student":
           if password == "12" :
              print("user login ")
           else:  
                print("student username nad password nao match")
    case _:
        print("nvalid input")
  
          
     
 