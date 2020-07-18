#!/usr/bin/env python
# coding: utf-8

# # Question 1
# 

# In[1]:


import re
email = input("Enter your official email address")
print(re.findall(r'\w+[.]', email)[0][:-1])


# # Question 2
# 

# In[23]:


tup = ("Hi","I","am","new","to","AI","ML","course")
print(sorted(tup, key = lambda x: x[0]))


# # Question 3

# In[3]:


fruits = {"apple","banana","grapes","watermelon"}
print(fruits)
print("pineapple" in fruits)
fruits.add("pineapple")
print(fruits)
fruits.update(["cherry","mango"])
print(fruits)

print(len(fruits))

fruits.remove("apple")
print(fruits)

fruits.discard("banana")
print(fruits)

fruits.pop()

print(fruits)
vegetables = {"onion","potato","carrot"}
set1 = fruits.union(vegetables)
print(set1)


# # Question 4 

# In[4]:


def find_missing(lst): 
    return [x for x in range(lst[0], lst[-1]+1)  
                               if x not in lst] 
lst = [11,12,13,15,20]
print(find_missing(lst))


# # Question 5 

# In[5]:


lst = [11,12,11,34,56,78,34,32,43,56,87,78,12]
mylist = list(dict.fromkeys(lst))
print(mylist)


# In[ ]:





# In[ ]:




