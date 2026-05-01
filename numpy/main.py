import numpy as np
''''array=np.array([1,2,3,4])
print(array)'''



'''a=np.array([1,2,3,4])
b=np.array([1,2,3,4])
print(a+b)'''

'''a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a*4)'''

#1d example
'''a=[1,2,3,4,5,6,7,8,9,10]
arr=np.array(a)
print(arr)'''


#2d example
'''a=[[1,2,3,4,5,],[1,2,3,4,5,]]
arr=np.array(a)
print(arr.ndim)'''


#3
'''a=[[[1,2,3,4,5,]]]
arr=np.array(a)
print(arr.ndim)'''

#array indexing
'''arr=np.array([10,20,30,40,50])
print(arr[2])'''



'''arr=np.array([1,2,3,4,5,6,7,8,9,10,11])
print(arr[2])'''


'''arr=np.array(("sneha",20,30,40,50))
print(type(arr[1:3]))
print(arr.dtype)'''

'''arr=np.array([10,20,30,40,50])
print(arr)
arr[1]=60
b=arr.copy()
print(arr)
print(b)'''

'''a=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
arr=np.array(a)
x=arr.shape
print(x)'''



'''a=np.random.randint(1,10,size=(3,3))
print(a)'''





'''a=np.random.choice([40,30,50])
print(a)'''



a=list("ABCDEFGHIJKLMNOPQRSTUVWZ0123456789")
b="".join(np.random.choice(a,4))

print(b)
