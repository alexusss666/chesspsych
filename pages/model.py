import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import streamlit as st
from pathlib import Path
import plotly.express as px
from pandas.tseries.offsets import DateOffset

csv_path = Path(__file__).parents[1] / 'data/sample_data.csv'


@st.cache_data
def load_data(path):
	return pd.read_csv(path)


df = load_data(csv_path)

# Sidebar title
st.sidebar.title('Regression Analysis')

# Sidebar description
st.sidebar.write('This app performs regression analysis on course level, department, and attendance.')

# Tabs for different prediction types
prediction_type = st.sidebar.radio("Select Prediction Type", ("Course", "Department"))
df_filtered = pd.DataFrame({})

if prediction_type == 'Course':
	st.write('Course Level Prediction')
	course_selected = st.selectbox("Select Course Level", df['course'].unique())
	df_filtered = df[df['course'] == course_selected]

elif prediction_type == 'Department':
	st.write('Department Prediction')
	department_selected = st.selectbox("Select Department", df['department'].unique())
	df_filtered = df[df['department'] == department_selected]

# Dummy encode the 'department' column and replace boolean values
df_filtered['department'] = pd.Categorical(df_filtered['department'])
df_filtered['department_code'] = df_filtered['department'].cat.codes

# Convert 'date' column to datetime
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Remove non-numeric columns before resampling
numeric_columns = df_filtered.select_dtypes(include=[np.number]).columns
numeric_columns = numeric_columns.append(pd.Index(['date']))  # Include the 'date' column
df_numeric = df_filtered[numeric_columns]

# Aggregate attendance data on a daily basis
daily_attendance = df_numeric.resample('D', on='date').mean().reset_index()

# Define features and target variable
X = daily_attendance[['course', 'department_code']]
y = daily_attendance['attendance']

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Generate predictions
X_pred = daily_attendance[['course', 'department_code']]
y_pred = model.predict(X_pred)

daily_attendance['date'] = pd.to_datetime(daily_attendance['date'])
daily_attendance['date'] = daily_attendance['date'] + DateOffset(months=1)

# Print predicted attendance in a table format
st.write("Predicted attendance:")
predicted_attendance_df = pd.DataFrame({'Date': daily_attendance['date'], 'Predicted Attendance': y_pred})
st.write(predicted_attendance_df)

# Plot line graph of daily attendance over time
fig = px.line(daily_attendance, x='date', y='attendance', title='Daily Attendance Over Time')
st.plotly_chart(fig)
