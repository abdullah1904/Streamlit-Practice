import streamlit as st
import pandas as pd

st.title("Data Elements")

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Occupation': ['Engineer', 'Doctor', 'Artist']
})

st.subheader("DataFrame Example")
st.dataframe(df)

st.subheader("Editable DataFrame")
edited_df = st.data_editor(df)

st.subheader("Static Table")
st.table(edited_df)

st.subheader("Metrics")
st.metric(label="Total Users", value=df.shape[0])
st.metric(label="Average Age", value=df['Age'].mean())

st.subheader("JSON and Dictionary")
st.json(df.to_dict())
st.write("Dictionary:", df.to_dict())