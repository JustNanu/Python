#!/usr/bin/env python
# coding: utf-8

# In[1]:


.1 + 1


# In[3]:


3 * 4


# In[4]:


1 / 2


# In[5]:


5 ** 4


# In[6]:


(2 + 5) * (9 + 3)


# In[9]:


5 % 2

16 % 2


# In[10]:


var = 2


# In[11]:


var


# In[12]:


x = 4


# In[13]:


x = x + x


# In[14]:


x


# In[18]:


#Strings
"My Name is Abhijeet Solanki"


# In[21]:


#Format Function shayad

string = "This will take a lot of time" 

print(string)

Name = "Abhijeet Solanki"
Age = 19

print("My name is {} and I am {} years old" .format(Name, Age))


# In[22]:


print("My Name is {x} and I am {y} years old.".format(x = Name, y = Age))


# In[33]:


#Indexing in Pythom

Name_1 = "abcdefghijk"

Name_1[4:]


# In[34]:


Name_1[:5]


# In[37]:


Name_1[3:6]


# In[44]:


#Lists- Sequence of elements in a set of square brackets separated by commas

my_list = ["a","b","c","d"]

my_list.append("e")

print(my_list)


# In[42]:


my_list[1:4]


# In[49]:


nested_list = [1, 2, 3, [1, 4, 9]]


# In[52]:


nested_list[3][1]


# In[54]:


list_1 = [0, 1, 2, 3, [0, 1, 4, 9,['Name', 'Place', 'Animal', 'Thing']]]

list_1[4][4][2]


# In[55]:


#Dictionaries- Key & value pair instead of sequences, with a value corresponding to that key

dictionary = {'key1':'value', 'key2':123}

dictionary['key1']


# In[58]:


list_2 = [1, 2, 3, 4]

dict = {"key1":list_2, "key2":{"interlude" : 23545}}

dict["key1"][1]


# In[59]:


#Booleans- True and False only
True


# In[60]:


False


# In[61]:


#Tuple- Similar to list but instead of using square brackets, paranthesis are used & the key difference being that
#tuples are immutable i.e. tuples does not support item assignment

#Sets- Collection of unique elements

tuple = (1, 3 ,5, 7 ,9)

tuple[1]


# In[62]:


tuple[2] = "Name_1"


# In[63]:


seq = [1 ,2 ,3 ,4 ,5]

for num in seq:
    print(num)


# In[6]:


square = []

for num in seq:
    square.append(num**2)
    
#List Comprehension
squ = [num**2 for num in seq]

print(squ)


# In[3]:


i = 1

while i <= 5:
    print("i is: {}" .format(i))
    
    i = i + 1


# In[5]:


seq = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]

for x in seq:
    print(x)


# In[12]:


#Funtions
def funtion(num):
    print(num**3)
    
num = int(input("Enter any number:"))

funtion(num)


# In[16]:


#print vs return - print only just prints the value of anythinf but using return we can store the value in a Variable

def Square(number):
    return number**2

output = Square(4)

print(output)


# In[17]:


#Docstring- Anything included in """  """, just a really long multi-lined comment
"""
THIS IS A DOC STRING 
CAN WRITE ANYTHING IN THIS 
AND EVEN USE THE ENTER KEY

"""


# In[2]:


# Map function & lamda function

def times2(num):
    return num*2

seq = [1, 2, 3, 4, 5]

twice_num = list(map(times2, seq))

print(twice_num)


# In[4]:


seq = [1, 2, 3, 4, 5]

square = list(map(lambda num: num**2, seq))

print(square)


# In[8]:


num = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda number: number%2 == 0, num))

print(even)


# In[17]:


s = "My Name is Abhijeet Solanki"

s.split()


# In[22]:


str = "Go Sports! #Sports Spremacy"

str.split("#")[1]


# In[29]:


d = {"k1": 1, "k2" : 2}

d.keys()


# In[27]:


d.values()


# In[28]:


d.items()


# In[31]:


list = [1,2,3,4,5,6]

list.pop(1)


# In[34]:


#Tuple Unpacking

x = [(1,2), (3,4), (5,6)]

for item in x:
    print(item)
    
for (a,b) in x:
    print(a)
    print(b)


# In[ ]:




