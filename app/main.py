import streamlit as st
import plotly.express as px
from src.data_processor import SolarDataProcessor
from src.cross_country import CrossCountryAnalyzer

st.title("Solar Data Dashboard")

st.header("Benin GHI Time Series")
processor = SolarDataProcessor("../data/benin-malanville.csv")
if processor.load_data():
    fig = px.line(processor.data, x="Timestamp", y="GHI", title="GHI Time Series (Benin)")
    st.plotly_chart(fig)
else:
    st.error("Failed to load Benin data")

st.header("Cross-Country GHI Comparison")
analyzer = CrossCountryAnalyzer({
    "Benin": "../data/benin_clean.csv",
    "Sierra Leone": "../data/sierra_leone_clean.csv",
    "Togo": "../data/togo_clean.csv"
})
if analyzer.load_data():
    combined = pd.DataFrame()
    for country, df in analyzer.datasets.items():
        temp = df[["GHI"]].copy()
        temp["Country"] = country
        combined = pd.concat([combined, temp], axis=0)
    fig = px.box(combined, x="Country", y="GHI", title="GHI Distribution by Country")
    st.plotly_chart(fig)
else:
    st.error("Failed to load cross-country data")

st.write("Planned enhancements: Interactive filters for DNI, DHI, and weather metrics; statistical comparisons.")