import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Chart Elements")

chartData = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

scatterData = pd.DataFrame({
    "x": np.random.randn(100),
    "y": np.random.randn(100)
})

mapData = pd.DataFrame({
    "lat": np.random.randn(100),
    "lon": np.random.randn(100)
})

st.subheader("Area Chart")
st.area_chart(chartData)

st.subheader("Bar Chart")
st.bar_chart(chartData)

st.subheader("Line Chart")
st.line_chart(chartData)

st.subheader("Scatter Plot")
st.scatter_chart(scatterData)

st.subheader("Map")
st.map(mapData)

st.subheader("Matplotlib Chart")
fig, ax = plt.subplots()
ax.plot(chartData['a'], label='A')
ax.plot(chartData['b'], label='B')
ax.plot(chartData['c'], label='C')
ax.set_title('Matplotlib Line Chart')
ax.legend()
st.pyplot(fig)