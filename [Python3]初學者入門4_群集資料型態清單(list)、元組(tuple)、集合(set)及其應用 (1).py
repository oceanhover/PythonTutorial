#!/usr/bin/env python
# coding: utf-8

# 亞摩的部落格：https://oceanhover.blogspot.com/2019/11/python3-list-tuple-set.html

# In[ ]:


【範例1】利用一對中括弧來建立一個課程清單。


# In[1]:


course = ['History','Math','Physics','ComSci']
print(course)


# 【範例1-2】利用len()函式，來確認清單內的資料項目數量(或稱清單的長度)。

# In[2]:


course = ['History','Math','Physics','ComSci']
print(len(course))


# 【範例1-3】根據位置索引(location index)取出清單內的資料。

# In[3]:


course = ['History','Math','Physics','ComSci']
print(course[0])


# In[4]:


print( ['History','Math','Physics','ComSci'][0])


# 【範例1-4】從清單取出最後一個資料項。

# In[5]:


course = ['History','Math','Physics','ComSci']
print(course[3])


# In[6]:


course = ['History','Math','Physics','ComSci']
print(course[-1])


# In[9]:


course = ['History','Math','Physics','ComSci']
print(course[len(course) - 1])


# 【範例1-5】當給定的位置索引超出清單範圍時會引發IndexError。

# In[10]:


course = ['History','Math','Physics','ComSci']
print(course[4])


# 【範例1-6】從清單取出某個範圍內的資料。

# In[12]:


course = ['History','Math','Physics','ComSci']
print(course[0 : 2])


# In[13]:


course = ['History','Math','Physics','ComSci']
print(course[:2])


# 【範例1-7】從清單取出特定範圍的資料，本例為倒數2個資料項，本例為['Physics','ComSci']。

# In[18]:


course = ['History','Math','Physics','ComSci']
print(course[2:3])


# In[19]:


course = ['History','Math','Physics','ComSci']
print(course[-2:])


# 【範例2-1】新增資料項到清單，本例為新增'Art'到course裡。

# In[21]:


course = ['History','Math','Physics','ComSci']
course.append('Art')
print(course)


# 【範例2-2】在清單的特定索引位置(index)新增資料項(x)，本例為在course裡的第1項新增'Art'。

# In[22]:


course = ['History','Math','Physics','ComSci']
course.insert(0,'Art')
print(course)


# 【範例2-3-1】新增清單course_2至course清單中。(注意：coruse_2也是清單)

# In[34]:


course = ['History','Math','Physics','ComSci']
course_2 = ['Art','Education']
course_3 = 'Optics'
course.extend(course_3)
print(course)


# 【範例2-3-2】為了加深讀者對於extend方法如何將可迭代資料項新增至course中，我們將原本為清單的course_2，指定為字串'Art'。

# In[35]:


course = ['History','Math','Physics','ComSci']
course_2 = 'Art'
course.extend(course_2)
print(course)


# 【範例2-3-3】很多人把extend與append混淆，筆者在這裡示範兩者的差異。

# In[24]:


course = ['History','Math','Physics','ComSci']
course_2 = ['Art','Education']
course.append(course_2)
print(course)


# 【範例2-3-4】很多人把extend與insert混淆，筆者在這裡示範兩者的差異。

# In[32]:


course = ['History','Math','Physics','ComSci']
course_2 = ['Art','Education']
course.insert(len(course),course_2)
print(course)


# 範例3-1】移除指定名稱的資料項

# In[36]:


course = ['History','Math','Physics','ComSci']
course.remove('Math')
print(course)


# 【範例3-2】移除最後一個資料項，並回傳移除的資料項。

# In[40]:


course = ['History','Math','Physics','ComSci']
course.pop(2)
print(course)


# 【範例3-2-2】請注意pop()括弧內若不指定位置索引的話，會自動移除最後一項。如果想要把被移除的資料項記錄下來，可以指派一個新變數去記錄回傳的值。

# In[49]:


course = ['History','Math','Physics','ComSci']
popped = course.pop()
print(popped)
print(course)


# 【範例3-2-3】若pop(x)括弧內指定位置索引x，則會移除並回傳。

# In[50]:


course = ['History','Math','Physics','ComSci']
popped = course.pop(2)
print(popped)
print(course)


# 【範例4】反轉['History','Math','Physics','ComSci']

# In[51]:


course = ['History','Math','Physics','ComSci']
course.reverse()
print(course)


# 【範例5-1】根據字母排序清單的資料

# In[54]:


course = ['History','Math','Physics','ComSci']
course.sort()
print(course)


# 範例5-2】根據數值大小排序清單的資料

# In[56]:


nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)


# 【範例5-3】字母排序以Z→A，或者數值排序以遞減的方式排序

# In[58]:


course = ['History','Math','Physics','ComSci']
nums = [1, 5, 2, 4, 3]
course.sort(reverse = True)
nums.sort(reverse = True)
print(course)
print(nums)


# 【範例5-4】示範如何利用sorted()函式取得排序後的清單副本，而不會取代原本的清單。若想儲存排序後並回傳的清單副本，必須指派一個變數給它。

# In[60]:


course = ['History','Math','Physics','ComSci']
sorted_course = sorted(course)
print(course)
print(sorted_course)


# 【範例6-1】利用min()函式回傳最小值。

# In[61]:


nums = [1, 5, 2, 4, 3]
print(min(nums))


# 【範例6-2】利用max()函式回傳最大值。

# In[63]:


nums = [1, 5, 2, 4, 3]
print(max(nums))


# 【範例6-3】利用sum()函式回傳總和。

# In[64]:


nums = [1, 5, 2, 4, 3]
print(sum(nums))


# 【範例7-1】利用index()方法取得清單特定資料項(x)的位置索引。

# In[66]:


course = ['History','Math','Physics','ComSci']
print(course.index('ComSci'))


# 【範例7-2】若資料項(x)不在清單內，則index(x)會引法IndexError。本例為取得'Art'的位置索引。

# In[68]:


course = ['History','Math','Physics','ComSci']
print(course.index('Art'))


# 【範例7-3】利用in運算符來檢查資料項(x)是否存在於清單中。若存在則回傳True，若不存在則回傳False。

# In[72]:


course = ['History','Math','Physics','ComSci']
print('Art' in course)
print('Math' in course)


# 【範例8】利用迴圈把清單裡的每個資料項印出來。

# In[73]:


course = ['History','Math','Physics','ComSci']
for item in course:
    print(item)


# 【範例9-1】利用for迴圈以及enumerate()函式把清單的每個索引位置以及對應的資料項印出來。enumerate()函式會回傳兩個值，第1個是位置索引，第2個是該位置索引所對應的資料項。

# In[74]:


course = ['History','Math','Physics','ComSci']
for index, item in enumerate(course):
    print(index, item)


# 【範例9-2】Python的位置索引預設值是從0開始，如果想要從1開始，可以在enumerate()函式中，多指定1個引數：start = 1。

# In[75]:


course = ['History','Math','Physics','ComSci']
for index, item in enumerate(course, start = 1 ):
    print(index, item)


# 【範例10-1】示範把清單內的所有資料項轉成一個字串，並以特定的分隔符號隔開。將['History','Math','Physics','ComSci']清單轉成一個字串，各資料項以"- "連接。

# In[77]:


course = ['History','Math','Physics','ComSci']
course_str = " - ".join(course)
print(course_str)


# 【範例10-2】將History - Math - Physics - ComSci字串分拆後再存成清單。

# In[82]:


course_str = "History - Math - Physics - ComSci"
new_list = course_str.split(" - ")
print(new_list)


# In[84]:


course_str = " - History - Math - Physics - ComSci"
new_list = course_str.split(" - ")
print(new_list)


# 【範例11-1】示範清單(list)可修改的特性。

# In[85]:


list_1 = ['History','Math','Physics','ComSci']
list_2 = list_1
list_1[0] = 'Art'
print(list_1)
print(list_2)


# 【範例11-2】示範元組(tuple)不可修改的特性。(immutable)

# In[88]:


tuple_1 = ('History','Math','Physics','ComSci')
tuple_2 = tuple_1
tuple_1[0] = 'Art'
print(tuple_1)
print(tuple_2)


# 【範例12-1】示範如何建立一個集合，以及觀察集合無序的特性。

# In[89]:


cs_course = {'History','Math','Physics','ComSci'}
print(cs_course)


# 【範例12-2】示範集合裡資料項的唯一特性。本範例在集合最後一項再新增一個'Math'。

# In[91]:


cs_course = {'History','Math','Physics','ComSci','Math'}
print(cs_course)


# 【範例12-3】如何檢查兩個集合之間的交集資料。

# In[90]:


cs_course = {'History','Math','Physics','ComSci'}
art_course = {'History','Math','Art','Design'}
print(cs_course.intersection(art_course))


# 【範例12-4】如何檢查兩個集合之間的差集資料(difference)。

# In[92]:


cs_course = {'History','Math','Physics','ComSci'}
art_course = {'History','Math','Art','Design'}
print(cs_course.difference(art_course))


# 【範例12-5】如何檢查兩個集合之間的聯集資料(union)。

# In[93]:


cs_course = {'History','Math','Physics','ComSci'}
art_course = {'History','Math','Art','Design'}
print(cs_course.union(art_course))


# 【範例13-1】建立空清單、空元組與空集合的方法。

# 【範例13-1】建立空清單、空元組與空集合的方法。

# In[94]:


#建立空清單
empty_list = []
empty_list = list()

#建立空元組
empty_tuple = ()
empty_tuple = tuple()

#建立空集合
empty_set = {} #本語法不是建立空集合，而是建立空字典(dict)，這裡要特別小心。
empty_set = set()


# In[ ]:




