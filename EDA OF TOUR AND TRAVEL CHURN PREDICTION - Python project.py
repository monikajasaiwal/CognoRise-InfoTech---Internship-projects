#!/usr/bin/env python
# coding: utf-8

# # The Analysis of Tour and Travel Compnay.
# A tour & travels company wants to predict whether a customer will churn or not. Based on a few customer characteristics 
# like their age, frequent flyer status, annual income class, services opted, account snick to social media, booked hotel or not,
# Target.
# 
# The analysis and forecasting are based on the customer churn's impact on yearly income, hotel reservations, and
# whether or not they were made in order to assist the business in developing predictive models, saving money, and
# performing fascinating EDAs.

# # Research Questions
# How Hotel Booking and Annual Income effect customer churn?
# How can we prevent customer churn?

# # Importing Libraries
# 

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # import dataset

# In[2]:


df = pd.read_csv("C:/Users/prash/Downloads/archive (3)/Customertravel.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# # Statistical Summary

# In[14]:


df.describe().T


# In[15]:


df.describe(include= object).T


# In[11]:


df.isnull().values.any()                  # make sure you use correct brakets 
value =len(df[df.duplicated()])
print(value)


# In[26]:


for col in df.describe(include = object).columns:
        print(col)
        print(df[col].unique())
        print('-'*40)


# In[27]:


df.corr()


# # Data Visualization 
# Here first creat a varible , store columns to convert them as a vaalue using pd.factorize function 

# In[38]:


feature = ['FrequentFlyer','AnnualIncomeClass','ServicesOpted','AccountSyncedToSocialMedia','BookedHotelOrNot']
for f in feature: 
        df[f] = pd.factorize(df[f])[0]
print(df.head().T)


# In[61]:


churn_prediction = df['BookedHotelOrNot'].value_counts(normalize =1 )
print(churn_prediction)


plt.figure(figsize=(7,5))
plt.bar(['Booked' , 'NotBooked'] , churn_prediction.values , color =['purple', 'pink'])
plt.title('HOW CUSTOMER AFFECTS CHURN PREDICTION')
plt.show()


# # MONTHLY INCOME VISUALISATION

# In[65]:


income = df.groupby('AnnualIncomeClass')
income = income.size()
print(income)


# In[83]:


plt.pie(income.values, labels= ['High Income', 'low Income', 'Middle Income'] , autopct = '%1.1f%%' ,radius=1, 
        textprops= {"fontsize" : 16} )
plt.title('How Income Impact Customer Churn', c='b')
plt.show()


# # Analytical Summary

# In[ ]:


customers who booked hotel are of 60%  of the total population and they must be from 43% of high income group of peope. 
whereas those who have not made hotel reservations account for 39% of the population, which is a significant number.

We found that customers with the highest yearly income have the lowest proportion of customer churn, whereas those with
the lowest (40%) and middle (42%), have the highest percentage of churn.


# # Insights

# In[ ]:


The largest customer churn has been observed when a consumer has not made a hotel reservation. 
This may be due to a number of factors, including expensive hotel rates and longer waiting lists
for reservations, both of which have a substantial impact on why people don't book hotels. 
This may help us understand how to run the campaign in order to shorten the waiting list.

The highest customer churn have also seen in the situation where customer have low and middle income.
This may give us an idea of the needs of the customers, and you can utilise the insights to work on
how to lower your pricing without affecting your revenue, which you can then offer to your customers, 
which can prevent the customer churn.

