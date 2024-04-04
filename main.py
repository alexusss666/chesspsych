from st_pages import Page, show_pages, add_page_title
import streamlit as st
import plotly.express as px
import pandas as pd

csv_path = r'data/sample_data.csv'

# app to add indentation in the sidebar
show_pages(
		[
			Page("main.py", "Home", "🏠"),
			Page("pages/late_page.py", "Reports", ":books:"),
			Page("pages/custom_page.py", "Custom Analytics", icon="📊"),
			Page("pages/model.py", "Model Regression", icon="🗒"),
			Page("pages/custom_page.py", "General Reports", icon="📈")
		]
)

# Description for the project
st.write("""
# University Attendance Tracker

This application provides analytics and predictions for university attendance data. 
You can visualize attendance trends, predict future attendance, and analyze various metrics. 
Explore different pages in the sidebar to access specific features and functionalities.
""")


# Load data
@st.cache_data
def load_data(csv_path):
	return pd.read_csv(csv_path)


# Load data
df = load_data(csv_path)


# Generate general reports
def generate_reports(df):
	st.header("General Reports")

	# Show summary statistics
	st.subheader("Summary Statistics")
	st.write(df.describe())

	# Plot distribution of attendance
	st.subheader("Attendance Distribution")
	fig = px.histogram(df, x='attendance', title='Distribution of Attendance', color='department')
	st.plotly_chart(fig)


generate_reports(df)
