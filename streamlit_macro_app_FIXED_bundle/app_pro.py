import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Macro Mining System")

st.write("If you see this, deployment is working.")

df = pd.DataFrame({
    "Asset": ["GLD","GDX","GDXJ"],
    "Weight": [0.1,0.08,0.08]
})

st.dataframe(df)

fig = px.bar(df, x="Asset", y="Weight", title="Sample Weights")
st.plotly_chart(fig)
