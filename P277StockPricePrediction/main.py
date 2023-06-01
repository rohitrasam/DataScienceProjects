# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 00:07:08 2023

@author: admin
"""

import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns
from pickle import load
from gzip import open
from time import sleep


apple_stk=pd.read_csv("AAPL.csv")

st.sidebar.header('Input no. of days')

Days = st.sidebar.number_input("Number of days for forecasting",min_value=1,max_value=1000,step=1)

st.subheader('No. of Days')
st.write(Days)

with open('Final_Model_Sarima.pkl', 'rb') as f:
    model = load(f)
    
 
result = model.forecast(Days)


st.write("Forecasted Results")



load_result = lambda: pd.DataFrame(result.values, columns=['Price']) 
    
df=load_result()
df.index = range(1, Days+1)
st.write(df)

sns.set(rc={'figure.figsize':(15, 10), 'figure.titlesize': 18,'figure.dpi': 150, 'font.size': 16, 'xtick.labelsize': 13, 'ytick.labelsize': 13})

if Days > 1:
    chart = plt.figure()
    sns.lineplot(df['Price'], color='green', label='Forcasted Values')
    plt.title('Apple Stock Forecasting Result', size=18)
    plt.xlabel('No. Of Days', size=17)
    plt.ylabel('Forecasted Price', size=17)
    plt.legend()

    st.pyplot(chart) 


chart1 = plt.figure()
sns.lineplot(result, color='green', label='Forecasted Price')
plt.title('Apple Stock Forecasting Result', size=18)
plt.xlabel('No. Of Days', size=17)
plt.ylabel('Price', size=17)
sns.lineplot(apple_stk['Adj Close'], color='red', label='Past Prices')
plt.legend()
st.pyplot(chart1)
