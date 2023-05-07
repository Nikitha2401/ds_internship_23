import streamlit as st
import os
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")


st.title(':red[Welcome to open pub web application]')
st.write('Basic info about  pubs')
st.write('Total No. of pubs : 50564')
st.write('Number of postial codes : 50564')
st.write('Number of cities : 50564')

st.header(":violet[About me]")
st.subheader(' :blue[Nikitha Allenkala]')
st.write('Aspiring Data Scientist')



st.subheader(":green[Connect with me on,🔗]")

col1,col2=st.columns(2, gap='small')
with col1:
    st.subheader("[LinkedIn](https://www.linkedin.com/in/nikitha-allenkala/)")
with col2:
    st.subheader("[GitHub](https://github.com/Nikitha2401)")
