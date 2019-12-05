#!/usr/bin/env python
# coding: utf-8

# 亞摩的部落格：https://oceanhover.blogspot.com/2019/12/python35-dictionarieskeyvalue.html
# 
# 字典(dictionaries)允許我們操作成對的鍵(key)與值(value)，鍵值對(key value pairs)是組成字典的元素，Hash maps或關聯式陣列(associative array)也是由成對的鍵與值所組成。鍵與值的關係可以用實體字典作比喻，每一個鍵都是唯一的，就像字典裡的每個定義，而定義的內容就像是儲存的資料。(個人偏好用房子來作比喻：鍵就像是房子的位址，而值就像是住在房子裡的人、物)

# 【範例1-1】以建立1個student字典為例。 

# In[2]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
print(student)


# 【範例1-2】取出student字典裡某一個鍵的值，本例以取出'name'為例。

# In[3]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
print(student['name'])


# 注意字典裡鍵與值可以為任意的資料型態如：字串、整數、元組、清單、字典、集合…等。
# 
# 【範例2-1】原本儲存在student裡的一個鍵'name'為字串，將其改為整數型態的1。

# In[5]:


student = {1:'John', 'age':25, 'courses':['Math', 'ComSci']}
print(student[1])


# 【範例2-2】若想取出的鍵不存在於字典中，將會引發KeyError。

# In[6]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
print(student['phone'])


# 【範例2-3】第二種情況，當取出的鍵不存在於字典中，回傳none而不是KeyError。

# In[7]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
print(student.get('phone'))


# 【範例2-4】第三種情況，當你希望取出的鍵不存在於字典中時，既非引發KeyError也非None而是回傳一個指定的預設值。

# In[8]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
print(student.get('phone', 'Not found'))


# 【範例3-1】於既有的字典裡新增鍵值對。本例是在student字典裡新增{phone:555-5555}。

# In[9]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
student['phone'] = '555-5555'
print(student.get('phone', 'Not found'))


# 【範例3-2】更新字典裡的鍵值對。本例是將student字典裡的{'name': 'John'}更新為{'name': 'Jane'}。

# In[13]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
student['name'] = 'Jane'
print(student.get('name'))


# 在【範例3-1】與【範例3-2】示範了如何新增以及更新字典裡的鍵值對，但利用dict[key] = value的語法，其限制是只能修改一組鍵值對。
# 
# 【範例3-3】如果使用者想一次修改多組鍵值對，可以利用update方法。本例是用一行程式碼完成【範例3-1】以及【範例3-2】的工作。

# In[15]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
student.update({'name': 'Jane', 'age': 26,'phone': '555-5555'})
print(student)


# 範例3-4-1】移除字典裡的鍵值對。本例是利用del陳述來移除{'age':25}。

# In[1]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
del student['age']
print(student)


# 【範例3-4-2】移除字典裡的鍵值對。本例是利用pop()方法來移除{'age':25}並將回傳的值25指派給變數age。

# In[2]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
age = student.pop('age')
print(student)
print(age)


# 【範例3-4-3】檢查字典長度(鍵的數量)

# In[12]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
print(len(student))


# 【範例3-4-4】取出字典裡的鍵

# In[11]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
print(student.keys())


# 範例3-4-5】取出字典裡的值

# In[15]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
print(student.values())


# 【範例3-4-6】取出字典裡的鍵值對

# In[16]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
print(student.items())


# 【範例3-4-7】利用for loop迴圈語法去取出字典的資訊。本例逐一取出字典的鍵。
# for key in student:  的這段陳述有個小細節，若不指定student.keys()或students.values()，而是僅以stduent代表，預設會印出鍵值。也就是說for key in student:  與 for key in student.keys():  都是逐一取出鍵值。

# In[17]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
for key in student:
    print(key)


# In[18]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
for key in student.keys():
    print(key)


# 【範例3-4-8】利用for loop迴圈語法去取出字典的資訊。本例逐一取出字典的值。

# In[20]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
for value in student.values():
    print(value)


# 【範例3-4-9】利用for loop迴圈語法去取出字典的資訊。本例逐一取出字典的鍵值對。

# In[22]:


student = {'name':'John', 'age':25, 'courses':['Math', 'ComSci']}
for key,value in student.items():
    print(key, value)

