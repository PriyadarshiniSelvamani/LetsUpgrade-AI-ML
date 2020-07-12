#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Question 2 
string = "Hello I am from LetsUpgrade"
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.find('e'))
print(string.count('e'))
print(string.isalpha())
print(string.isnumeric())
print(string.center(9))
print(string.endswith('e'))
print(string.encode())
print(string.index('f'))
print(string.format())
print(string.istitle())
print(string.swapcase())
print(string.partition('am'))


# In[20]:


#Question 3
string1  = input("Enter a string :")
string2 = input("Enter another string :")
if string1 == string2[::-1]:
    print("The string is Palindrome")
elif (sorted(string1)==sorted(string2)):
      print("The strings are anagrams.")
else:
    print("The string is neither anagram nor palindrome")


# In[23]:


#Question 5 
import re
string4 = "Dr. Darshan Ingle@AI-ML Trainer"
remove = "@.-"
pattern = "["+remove+"]"
string5 = re.sub(pattern,"",string4)
string6 = string5.replace(" ","")
print(string6.lower())


# In[ ]:


#Quetion 1
count = 1
num = 1
print("hi")
while count < 21:
    for i in range(2,num):
        if (num % i) == 0:
               break
        else:
            print(num)
count = count + 1


# In[ ]:





# In[ ]:




