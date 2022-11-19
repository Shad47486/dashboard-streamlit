import pandas as pd 
import numpy as np
import streamlit as st
import plotly

st.title('Speech Language Pathology Burn Out?')

dspl = pd.read_csv('Data\SPLv2.csv')

st.dataframe(dspl)

drained = dspl[['Q11','Q4']]
st.subheader('Setting vs bring emotionally drained')
st.bar_chart(drained, x='Q4', y='Q11', use_container_width=True)
st.text ('This displays the number of people who are emotionally drained based on setting')
st.text ('Below this dispays the number of males and females that took the survey')

gender = dspl[['Q3']]
st.bar_chart(gender)