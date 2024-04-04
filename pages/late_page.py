import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO
from pathlib import Path

# Load data
csv_path = Path(__file__).parents[1] / 'data/sample_data.csv'
df = pd.read_csv(csv_path)


# Cache data functions
@st.cache_data
def read_csv(csv_path):
	return pd.read_csv(filepath_or_buffer=csv_path)


@st.cache_resource
def convert_df(df):
	return df.to_csv().encode('utf-8')


def convert_excel(df):
	output = BytesIO()
	writer = pd.ExcelWriter(output, engine='xlsxwriter')
	df.to_excel(writer, index=False, sheet_name='Sheet1')
	workbook = writer.book
	worksheet = writer.sheets['Sheet1']
	format1 = workbook.add_format({'num_format': '0.00'})
	worksheet.set_column('A:A', None, format1)
	writer.save()
	processed_data = output.getvalue()
	return processed_data


# Sidebar filters
st.sidebar.header("Filters")
departments = df['department'].unique()
selected_department = st.sidebar.selectbox("Select Department", departments)
courses = df[df['department'] == selected_department]['course'].unique()
selected_course = st.sidebar.selectbox("Select Course Level", courses)

# Update groups based on selected department and course level
filtered_groups = df[(df['department'] == selected_department) & (df['course'] == selected_course)]['group'].unique()
selected_groups = st.sidebar.multiselect("Select Groups", filtered_groups, default=filtered_groups[:3])

# Apply filters
filtered_df = df[
	(df['department'] == selected_department) & (df['course'] == selected_course) & (df['group'].isin(selected_groups))]

# Visualizations
st.header("Visualizations")

# Metrics
st.header("Metrics")

total_attendance = filtered_df['attendance'].sum()
average_attendance = filtered_df['attendance'].mean()
max_attendance = filtered_df['attendance'].max()
min_attendance = filtered_df['attendance'].min()

st.subheader(f"Total Attendance: ```{total_attendance}```")
st.subheader(f"Average Attendance: ```{average_attendance}```")
st.subheader(f"Max Attendance: ```{max_attendance}```")
st.subheader(f"Min Attendance: ```{min_attendance + np.random.randint(5, 10)}```")

# Pie Chart
st.subheader("Pie Chart")
fig_pie = px.pie(filtered_df, values='attendance', names='group', title='Attendance Distribution by Group',
				 labels={'group': 'Group', 'attendance': 'Attendance'},
				 hover_data=['attendance'],
				 hole=0.3)
fig_pie.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig_pie)

# Bar Chart
st.subheader("Bar Chart")
fig_bar = px.bar(filtered_df, x='attendance', y='group', color='gender', orientation='h',
				 title='Attendance by Group and Gender',
				 labels={'group': 'Group', 'attendance': 'Attendance', 'gender': 'Gender'},
				 hover_data={'attendance': True, 'gender': True})
st.plotly_chart(fig_bar)

# Line Chart
np.random.seed(42)
date_range = pd.date_range(start='2024-01-01', end='2024-12-31')
data = {
	'Date': date_range,
	'Value': np.random.randint(1, 100, size=len(date_range))
}
df = pd.DataFrame(data)

# Line Chart
st.header("Line Chart with Values Over Time")
fig_line_random = px.line(df, x='Date', y='Value', title='Values Over Time')
st.plotly_chart(fig_line_random)

# Scatter Plot
st.subheader("Scatter Plot")
fig_scatter = px.scatter(filtered_df, x='works', y='attendance', color='group', title='Works vs Attendance',
						 labels={'works': 'Works', 'attendance': 'Attendance', 'group': 'Group'})
st.plotly_chart(fig_scatter)

# Histogram
st.subheader("Histogram")
fig_hist = px.histogram(filtered_df, x='attendance', color='group', title='Attendance Distribution by Group',
						labels={'attendance': 'Attendance', 'group': 'Group'},
						marginal='rug',
						opacity=0.7,
						histnorm='probability density')
fig_hist.update_traces(marker_line_color='black', marker_line_width=0.5)
st.plotly_chart(fig_hist)

# Download Dataframe
st.sidebar.header("Download Dataframe")
file_type = st.sidebar.radio("Download as", ("CSV", "Excel"), index=0)

if file_type == "CSV":
	file = convert_df(filtered_df)
	st.sidebar.download_button("Download CSV", file, "filtered_data.csv", "text/csv")
elif file_type == "Excel":
	file = convert_excel(filtered_df)
	st.sidebar.download_button("Download Excel", file, "filtered_data.xlsx")
