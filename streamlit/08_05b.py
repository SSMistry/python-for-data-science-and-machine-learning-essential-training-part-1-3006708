import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

animals = ['pig', 'cow', 'sheep', 'horse']
height = [50, 140, 66, 189]
weight = [71, 250, 65, 154]

fig, ax = plt.subplots()

x = np.arange(len(height))
width = 0.40

ax.bar(x-0.2, height, width, color='palegreen')
ax.bar(x+0.2, weight, width, color='seagreen')

ax.legend(['Height','Weight'])
ax.set_xticks(x)
ax.set_xticklabels(animals)

st.pyplot(fig)

explode = [0.1, 0.1, 0.1, 0.25]
plot_pie, ax = plt.subplots()
ax.pie(height, explode=explode, labels=animals, autopct='%1.1f%%', shadow=True)
ax.axis('equal')
st.pyplot(plot_pie)