import pandas as pd
import time
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

rows = np.random.randn(1,1)

'Growing Line Chart:'
chart = st.line_chart(rows)

#real-time update of a chart with new random data points
for i in range(1,100):
  new_rows = rows[0] + np.random.randn(1,1)
  chart.add_rows(new_rows)
  rows = new_rows
  time.sleep(0.05)

values = np.random.rand(10)
'Matplotlibs Line Chart:'
fig, ax = plt.subplots()
ax.plot(values)
st.pyplot(fig)
