import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

col_names = ['column1','column2','column3']

data = pd.DataFrame(np.random.randint(30, size=(30,3)), columns=col_names)

#create line chart
'Line graph:'
st.line_chart(data)

#create bar chart
'Bar graph:'
st.bar_chart(data)

animals = ['Dog', 'Cat', 'Fish', 'Lizard']
heights = [45, 27, 5, 13]

#create pie chart in matplotlib
'Pie chart:'
fig, ax = plt.subplots()
ax.pie(heights, labels=animals, colors=plt.cm.Paired.colors)
st.pyplot(fig)