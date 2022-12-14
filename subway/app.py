import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.write(
   "https://www.naver.com/"
)
df = pd.read_csv('./subway/subway.csv', encoding='CP949')
st.write(df)

df = pd.read_csv('./subway/subway_part.csv', encoding='CP949')
st.write(df)

fig = plt.figure(figsize=(10,4))
sns.histplot(data=df, x='호선', hue='조사일자', multiple='stack')
st.pyplot(fig)