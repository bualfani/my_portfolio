import streamlit as st
import pandas


st.title("Buloze Alfani")
content = """
Hi, I'm Buloze, welcome to my project site, on here are some of the web apps I've 
developed so far with many more to come as I continue learning to
improve on my Python skills, all these applications are projects 
I build in my journey to learning and improving on skills as a programmer, 
I had fun building these projects because a lot of them really challenged me
on my skills as a programmer. I hope you enjoy.
"""
st.info(content)

st.subheader("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col1, col2 = st.columns(2)

data_frama = pandas.read_csv('data.csv', sep=';')

with col1:
    for index, row in data_frama[:10].iterrows():
        st.header(row['title'])

with col2:
    for index, row in data_frama[10:].iterrows():
        st.header(row['title'])
