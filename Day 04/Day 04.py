#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Question 1 
print("Floor division operator and modulo operator cannot be performed on complex numbers")
a = 2+9j
b = 7+8j
print("Addition of two complex number is : ",a+b)
print("Subtraction of two complex number is : ",a-b)
print("Multiplication of two complex number is : ",a*b)
print("Division of two complex number is : ",a/b)
#print("Floor division of two complex number is : ",a//b)
#print("Modulo of two complex number is : ",a%b)


# #Question 2
# 
# *range()* **is a built-in function in python. It is used to generate a sequence of numbers within a given range. Depending
# on the parameters passed user can decide where the series of number can begin as well as end.**
# 
# 
# 

# In[8]:


#example simple range function :range(stop)
for i in range(10):
    print(i,end=" ")


# In[9]:


#example for range function with 2 parameters : range(start,stop)
for i in range(10,20):
    print(i,end=" ")


# In[11]:


#example fr range function with 3 parameters : range(start,stop,step)
for i in range (1,15,2):
    print(i,end=" ")


# In[15]:


#Question 3
a = 100
b = 50
subt = a-b
print(subt)
if subt > 25:
    print("Result of subtraction is greater than 25 so multiplication is",a*b)
else:
    print("Result of subtraction is less than 25 so division is",a/b)


# In[16]:


#Question 4 
lis = [10,56,89,42,90,46,92,12,57,49]
for i in lis:
    if i%2==0:
        print("Result : ",i*i-2)


# In[23]:


#Question 5
lis1 = [6,49,8,12,14,20,4,17,20,28]
for i in lis1:
    j = i/2
    if j>7:
      print(i)


# In[ ]:





# In[ ]:




