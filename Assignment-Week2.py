#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Question 1
def Addition(a, b):
    return(a + b)

x = input('Enter a number' )
y = input('Enter a number' )
z = Addition(x, y)
print('The addition of numbers ', z)


# In[3]:


# Question 2-A
a = 7
str1 = 'Hello'
b = a + str1


# In[4]:


# Question 2-B
a = 7
str1 = 'Hello'
b = str1 + a


# In[5]:


# Question 3
str1 = 'Data Science'
if ('s' in str1):
    print('s is found')
else:
    print('s is not found')


# In[11]:


# Question 4
def Find(list1):
    if (list1[0] == list1[5]):
        return(True)
    else:
        return(False)

Numbers = [1, 2, 3, 4, 5, 1]
print(Find(Numbers))


# In[12]:


# Question 5 
l1 = [10, 20, 33, 46, 55]
for i in l1:
    if (i%5 == 0):
        print(i)


# In[13]:


# Question 6
def calculation():
    a = input('Enter a number ')
    b = input('Enter a number ')
    c = a + b
    d = a - b
    return(c, d)

print(calculation())


# In[14]:


# Question 7
def function(a=7, b):
    print(a, b)


# In[16]:


# Question 8
# A function or a program calling itself is called Recursion
def add(a):
    if (a == 0):
        return(a)
    else:
        return(a + add(a - 1))

print(add(10))


# In[24]:


# Question 9
square = lambda x: x * x 
list1 = [12, 11, 53, 22, 21, 77, 87, 88, 98]

fil = list(filter(lambda y : y%2 == 1, list1))

for i in fil:
    print(' The square of the odd numbers is ', i * i)


# In[31]:


# Q|uestion 10
list1 = ['A', 'B', 'C', 'D', 'E']
list2 = [1, 2, 3, 4, 5]

list3 = list(map(lambda x : x.lower(), list1))
print('Lower case of the letters ', list3)

list4 = list(map(lambda y : y * y * y, list2))
print('Cube of the numbers ', list4)


# In[ ]:





# In[ ]:





# In[ ]:




