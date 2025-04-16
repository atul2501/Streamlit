import streamlit as st
import pandas as pd
import numpy as np

## Title of the applicaton 
st.title("Hello Streamlit")


## Display a simple Text
st.write('This is a imple text')

##create a simple Datafrome


df=pd.DataFrame({

    'first column': [1,2,3,4],
    'second colum':[10,20,30,40]
})

## Display the dataframe
st.write("here is the dataframe")
st.write(df)

##create a line chart 
chart_data=pd.DataFrame(

    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)