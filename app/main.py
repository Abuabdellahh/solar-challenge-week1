import streamlit as st
import plotly.express as px
from src.data_processor import SolarDataProcessor

st.title("Solar Data Dashboard")

st.header("Benin GHI Time Series")
processor = SolarDataProcessor("../data/benin-malanville.csv")
if processor.load_data():
    fig = px.line(processor.data, x="Timestamp", y="GHI", title="GHI Time Series (Benin)")
    st.plotly_chart(fig)
else:
    st.error("Failed to load Benin data")

st.write("Planned enhancements: Cross-country comparisons, interactive filters for DNI, DHI, and weather metrics.")