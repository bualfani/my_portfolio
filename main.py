import streamlit as st
import pandas
import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;  
    border-style: solid;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('./images/back3.png')


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
    for index, row in data_frama[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")


with col3:
    for index, row in data_frama[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")