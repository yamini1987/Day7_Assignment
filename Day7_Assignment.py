#!/usr/bin/env python
# coding: utf-8

# In[1]:



port1={21:"FTP",22:"SSH",23:"Telnet",80:"http"}

port2 = {value:key for key, value in port1.items()}
print(port2)
    


# In[2]:


list1=[(1,2),(3,4),(5,6),(4,5)]
list2=[] 
sum=0
for pair in list1:
    sum=pair[0]+pair[1]
    list2.append(pair[0]+pair[1])
print(list2)
   


# In[3]:


list1=[(1,2,3),[1,2],['a','hit','less']]

res = [item for t in list1 for item in t] 
  
print(res) 


# In[ ]:




