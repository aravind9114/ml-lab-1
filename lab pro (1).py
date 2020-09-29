#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import csv


# In[3]:


attributes=[['sunny','rainy'],
            ['warm','cold'],
            ['normal','high'],
            ['strong','weak'],
            ['warm','cool'],
            ['same','change']]


# In[4]:


print(attributes)


# In[5]:


num_attributes=len(attributes)
print(num_attributes)


# In[6]:


print("/nthe most general hypothesis :['?','?','?','?','?','?']/n")


# In[7]:


print("/nthe most general hypothesis :['?','?','?','?','?','?']/n")
print("/nthe most specific hypothesis :['0','0','0','0','0','0']/n")


# In[8]:


print("\nthe most general hypothesis :['?','?','?','?','?','?']\n")
print("\nthe most specific hypothesis :['0','0','0','0','0','0']\n")


# In[23]:


a=[]
print("\n the given training data set\n")
with open('data.csv','r') as csvFile:
 reader=csv.reader(csvFile)
for row in reader:
    a.append(row)
    print(row)
        


# In[24]:


print("\ninitial value of hypothesis:")
h=['0']*num_attributes
print(h)


# In[27]:


for i in range(0,len(a)):
    if a[i][num_attributes]=='yes':
     for j in range(num_attributes):
        ifh[j]=='0' or h[j]==a[i][j]
        h[j]=a[i][j]
        else
            h[j]='?'
print("\nfor training examples:{0} the hypothesis\n".format(i+1),h)
            


# In[ ]:




