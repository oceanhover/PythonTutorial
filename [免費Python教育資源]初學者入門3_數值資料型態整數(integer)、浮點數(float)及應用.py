#!/usr/bin/env python
# coding: utf-8

# 【範例1】指派一個整數3至變數num，並利用type()函式確認num的資料型態。

# In[1]:


num = 3
print(type(num))


# 【範例2】指派一個浮點數3.14至變數num，並利用type()函式確認num的資料型態。

# In[8]:


num = 3.14
print(type(num))


# 【範例3】操作算術運算符：
# addition : + 
# subtration : -
# multiplication : *
# division: /
# floor division: //
# exponents: **
# modulus : %

# In[9]:


print(3 + 2)


# In[10]:


print(3 - 1)


# In[11]:


print(3 * 2)


# In[12]:


print(3 / 2)


# In[34]:


print(1// 2)


# In[14]:


print(3 ** 2)


# In[23]:


print(3 % 2)


# 【範例4】先乘除後加減的操作。

# In[115]:


print(3 * 2+ 1)


# In[117]:


print(3 * (2+ 1))


# 【範例5-1】利用算術運算符來操作數字變數常用的語法。

# In[38]:


num = 1
num = num + 1
print(num)


# In[41]:


num = 1
num += 1
print(num)


# 【範例5-2】兩種常見的語法：將數值變數 * 10

# In[118]:


num = 1
num = num * 10
print(num)


# In[42]:


num = 1
num *= 10
print(num)


# 【範例6】示範其他處理數值的內建函式。

# In[43]:


print(abs(-3))


# In[69]:


print(round(3.75))


# In[70]:


print(round(3.75,1))


# 【範例7】示範比較運算符的操作。
# 等於(Equal)： ==
# 不等於(Not Equal)： !=
# 大於(Greater than)： >
# 小於(Less than)： <
# 大於等於(Greater or Equal)： >=
# 小於等於(Less or Equal)： <=

# In[92]:


num_1 = 3
num_2 = 2
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)


# 【範例8-1】在處值數值運算時，末確認變數的資料型態就進行算數操作。

# In[113]:


num_1 = '200'
num_2 = '100'
print(num_1 + num_2)


# 【範例8-2】在處值數值運算時，先將變數的資料型態轉為整數後再進行算數操作。

# In[114]:


num_1 = '200'
num_2 = '100'
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)


# In[ ]:




