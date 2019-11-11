#!/usr/bin/env python
# coding: utf-8

# 【範例1】定義字串變數message

# In[9]:


message = "Hello World"
print(message)


# In[13]:


print("Hello World")


# 【範例2】將字串'Booby's World'指派給message

# In[2]:


message = 'Booby's world'
print(message)


# 【範例3-1】兩種將字串'Booby's World'指派給message的語法

# In[1]:


message = 'Booby\'s world'
print(message)


# 【範例3-2】將字串"Booby's World"指派給message

# In[8]:


message = "Booby's world"
print(message)


# 【範例3-3】若字串內有包含單引號，則定義字串的時候就用成對的雙引號去包字串;
# 將'I like "apples" than "bananas".'指派給message

# In[3]:


message = 'I like "apples" than "bananas".'
print(message)


# 【範例3-4】反之，則用成對單引號去包住含雙引號的字串; 
# 將"I like "apples" than "bananas"."指派給message

# In[10]:


message = "I like "apples" than "bananas"."
print(message)


# 【範例4】若字串同時包含單引號以及雙引號，或者字串格式是多行字串，可以利用成對的3個單引號或成對的3個雙引號去包字串。

# In[4]:


message = """Bobby's world was a good
cartoon in the 1990'."""
print(message)


# 【範例5】04:30 利用len()函式來確認"字串"長度(包含幾個字元)。

# In[11]:


message = "Hello World"
print(len(message))


# In[ ]:


【範例5】在"字串"後使用方括號[]並放入數字[index]，可以取出對應位置的字元。


# In[16]:


message = "Hello World"
print(message[0])


# In[15]:


print("Hello World"[0])


# 【範例6-1】注意Python的第一個字元，其index是0；最後一個字元，其index為len() - 1。

# In[17]:


message = "Hello World"
print(message[10])


# 【範例6-2】若定義的index超出字串長度，則會引發錯誤IndexError。

# In[18]:


message = "Hello World"
print(message[11])


# 【範例7-1】從"Hello World"或message取出第1個字元(包含第1)到第5個字元(不包含第5)。

# In[19]:


message = "Hello World"
print(message[0:5])


# In[3]:


print("Hello World"[:5])


# 【範例7-2】從message取出第6個字元(包含第6)到第最後1個字元(包含最後1個)。

# In[7]:


message = "Hello World"
print(message[6:11])


# In[11]:


message = "Hello World"
print(message[6:])


# 【範例8-1】所有字元轉為小寫，從"Hello World"轉為"hello world"。

# In[13]:


message = "Hello World"
print(message.lower())


# 【範例8-2】所有字元轉為大寫，從"Hello World"轉為"HELLO WORLD"。

# In[15]:


message = "Hello World"
print(message.upper())


# 【範例8-3-1】計算特定字元出現字數，如："Hello"

# In[17]:


message = "Hello World"
print(message.count("Hello"))


# 【範例8-3-2】計算特定字元出現字數，如："l"

# In[18]:


message = "Hello World"
print(message.count("l"))


# 【範例8-4-1】找出特定字元在字串的位置索引，如："World"

# In[20]:


message = "Hello World"
print(message.find("World"))


# 【範例8-4-2】所尋找的特定字元不存在於字串的任何位置索引，如："Universe"

# In[21]:


message = "Hello World"
print(message.find("Universe"))


# 【範例8-5-1】取代字串內的特定字元，如：以"Universe"取代字串內的"World"。

# In[25]:


message = "Hello World"
print(message.replace("World","Universe"))


# 【範例8-5-2】注意message.replace("World","Universe")，回傳的是一個字串副本，結果是根據引數1、引數2的結果。原本的字串變數message所儲存的資訊仍為"Hello World"。

# In[28]:


message = "Hello World"
message.replace("World","Universe")
print(message)


# 【8-5-3】若想要儲存新的字串副本，則必須再指派一個變數。
# 語法1：指派一個新變數去儲存字串副本。

# In[29]:


message = "Hello World"
new_message = message.replace("World","Universe")
print(new_message)


# In[30]:


message = "Hello World"
message = message.replace("World","Universe")
print(new_message)


# 【8-6-1】將2組字串分別指派給2個變數，再將2組字串連接後指派給message。

# In[31]:


greeting = "Hello"
name = "Micael"
message = greeting + name
print(message)


# 【8-6-2】承上，在greeting與name之間加入字串", "(注意逗號後接1個空白字元)。

# In[32]:


greeting = "Hello"
name = "Micael"
message = greeting + ", " + name
print(message)


# 【8-6-3】承上，在最後再加入". Welcome!"。

# In[34]:


greeting = "Hello"
name = "Michael"
message = greeting + ", " + name + ". Welcome!"
print(message)


# 【8-7-1】另一種常用的方式是先建立格式化的字串後，再填入相對應的變數。

# In[41]:


greeting = "Hello"
name = "Michael"
message = "{}, {}. Welcome!".format(greeting,name)
print(message)


# 【8-7-2】如果你是使用Python3.6或Python3.6以上，另一種簡潔的寫法是使用f()的方法。

# In[39]:


greeting = "Hello"
name = "Michael"
message = f"{greeting}, {name}. Welcome!"
print(message)


# 【範例9】檢查目前的變數包含那些方法，可以利用dir()函式。

# In[42]:


greeting = "Hello"
name = "Michael"
print(dir(name))


# 【範例10-1】輸入help(變數)並無法運作，要直接輸入該類別或資料型態以本例而言是help(str)。

# In[46]:


greeting = "Hello"
name = "Michael"
print(help(name))


# In[47]:


greeting = "Hello"
name = "Michael"
print(help(str))


# 【範例10-2】查詢該類別特定的方法

# In[48]:


greeting = "Hello"
name = "Michael"
print(help(str.lower))

