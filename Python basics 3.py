#!/usr/bin/env python
# coding: utf-8

# In[1]:


list = [123,'abc',12.56,True]


# In[3]:


print(list)


# In[21]:


list = [123, 'abc', 12.56, True, [123,1,2,3]]
print(list [:5])


# In[22]:


len(list)


# In[23]:


list[4]


# In[24]:


#Deleting list
del list[4]


# In[25]:


list


# In[28]:


#contatination
list1 =[1,2,3,4]
list2 =[8,5,6,7]
list3 =list1+list2
print(list3)


# In[2]:


list1 =[1,2,3,4]
list2 =[8,5,6,7]
list3=list1*3
print(list3)


# In[3]:


#Replace
list1 = [123, 'abc', 12.56, True, [123,1,2,3]]
list1[4] = 'python'
print(list1)


# In[4]:


#Reverse
list1 = [123, 'abc', 12.56, True, [123,1,2,3]]
print(list1[::-1])


# In[5]:


list1 = [123, 'abc', 12.56, True, [123,1,2,3]]

for i in list1:
    print(i)


# In[10]:


list1 = [123, 'abc', 12.56, True, [123,1,2,3]]

s="python" 
list1=list(s)
print(list1)


# In[12]:


#String to a list
list1 = [1,2,3,5]
print(max(list1))


# In[13]:


list1 = [1,2,3,5,'abcd','bcde']
print(max(list1))


# In[6]:


list1 = ['java','c++','c-Sharp','programming']
max(list1)


# In[11]:


#Append
list1=['python','c++']
list1.append('java')
print(list1)


# In[12]:


#Append
list1=['python','c++']
list1.append('java','c')
print(list1)


# In[15]:


#Append
list1=['python','c++']
list1.extend(['java','c'])
print(list1)


# In[2]:


list1=['python','c++',1,2,34,4,4,4,4,4,5]
print(list1.count(4))


# In[6]:


list1=['python','c++',1,2,34,4,4,4,4,4,5]
list1.insert(5,'python')
print(list1)


# In[3]:


list1=['python','c++',1,2,34,4,4,4,4,4,5]
list1.pop(1)
print(list1)


# In[7]:


list1=['python','c++',1,2,34,4,4,4,4,4,5]
list1.remove(4)
print(list1)


# In[8]:


list1=['python','c++',1,2,34,4,4,4,4,4,5]
list1.reverse()
print(list1)


# In[14]:


#prints list in ascending order
list1= [1,2,6,3,9,4,6,22,663,63]
list1.sort()
print(list1)


# In[16]:


list1= ['science','social','mathematics']
list1.sort()
print(list1)


# In[19]:


tup = (1,2,'string',True)
print(type(tup))


# In[20]:


tup[3]=1223


# In[27]:


tup = (1,2,'string',True)
tup1=tup+(1,2,3)
print(tup1)


# In[29]:


tup = (1,2,4)
print(max(tup))


# In[31]:


list1=[1,2,3,4]
tup=tuple(list1)
print(tup)


# In[32]:


s="python"
tup=tuple(s)
print(tup)


# In[35]:


tup=(1,2,3,4,5)
list1=list(tup)
list1[1]=5
tup1=tuple(list1)
print(tup)
print(tup1)


# In[36]:


list1=[1,2,3,4,5]
tup=(1,2,3,4,5)
list1[0]
tup[0]


# In[44]:


dict1={'key':1234,12:'pair','str':(1,2,3),}
print(dict1['key'])


# In[42]:


print(dict1['str'])


# In[45]:


dict1={'key':1234,12:'pair','str':(1,2,3),}
dict1['key']=100
print(dict1['key'])


# In[47]:


dict1={'key':1234,12:'pair','str':(1,2,3),}
dict1[12]=100
print(dict1)


# In[49]:


dict1={'key':1234,12:'pair','str':(1,2,3),}
print(dict1.items())


# In[54]:


dict1={'key':1234,12:'pair','str':(1,2,3),}
print(dict1.keys())


# In[56]:


x=1
y=4
z='str'

def func1(x):
    print(x)
func1(x)
func1(y)


# In[59]:


x=1
y=4
z='str'

def func1(x,y):
    print(x,y)
func1(x,y)
func1(z,x)


# In[62]:


x=int(input("enter the number"))

def func1(number):
    z=number*number
    return z
z = func1(x)
print(z)


# In[ ]:




