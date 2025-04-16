import streamlit as st
import pandas as pd

st.title("HII ATUL THIS IS YOUR FIRST PROJECTS")
st.title("Streamlit Text Input")

name=st.text_input("ENTER your name:")


age=st.slider("select your age:",0,100,25)

st.write(f"Your age is {age}.")

option=['Python','java','c++','Javascript']
choice=st.selectbox("choose ypur fvorite language:", option)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello,{name}")


data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
df.to_csv("sample.csv")
st.write(df)


upload_file=st.file_uploader("choose a CSV file",type='csv')

if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)