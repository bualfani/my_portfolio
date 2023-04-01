import streamlit as st
import pandas
import base64

st.set_page_config(layout='wide')

st.title("Buloze Alfani")
content = """
Hi, I'm Buloze, welcome to my project site, on here are some of the web apps I've 
developed so far with many more to come as I continue learning to
improve on my Python skills, all these applications are projects 
I build in my journey to learning and improving on my skills as a programmer, 
I had fun building these projects because a lot of them really challenged me
on my skills as a programmer. I hope you enjoy.
"""
st.info(content)

st.subheader("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col1, col2, col3 = st.columns([1.5, 0.5, 1.5])

data_frama = pandas.read_csv('data.csv', sep=';')


with col1:
    for index, row in data_frama[:8].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")


with col3:
    for index, row in data_frama[8:17].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")