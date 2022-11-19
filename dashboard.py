#importing  needed moduules
import pandas as pd 
import numpy as np
import streamlit as st

st.title('Speech Language Pathology Burn Out?')

Datacol = 'Q3/Q_40_3'
Datais = 'Data\SPLv2.csv'

def load_data(nrows):
    data = pd.read_csv(Datais, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(30)
data_load_state.text('Loading data...done!')

st.bar_chart(hist_values)