import streamlit as st
import requests
import pandas as pd

st.title('FastAPI & Streamlit app')

name = st.text_input('Item name')
description = st.text_area('Item description')

def load_data():
    response = requests.get('http://localhost:8000/items/')
    if response.status_code == 200:
        # 'id'列を最初に配置
        df = pd.DataFrame(response.json())
        if all(col in df.columns for col in ['id', 'name', 'description']):
            df = df[['id', 'name', 'description']]

        return df
    else:
        st.error('Failed to retrieve items.')
        return pd.DataFrame()

data = load_data()

if st.button('Create'):
    response = requests.post('http://localhost:8000/items/', json={'name': name, 'description': description})
    if response.status_code == 200:
        st.success('Item added successfully!')
        data = load_data()
    else:
        st.error('Failed to add item.')

# DataFrameの表示（
st.dataframe(data, hide_index=True)
