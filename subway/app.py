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

df2 = pd.read_csv('./subway/subway_part.csv')
st.write(df2)

fig = plt.figure(figsize=(10,4))
sns.histplot(data=df, x='호선', hue='조사일자', multiple='stack')
st.pyplot(fig)


data_market %>%
  group_by(`1`) %>%
  summarize(n())