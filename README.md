### Streamlit App

#### Student Tracker

The Student Tracker is a web application built using Streamlit, a Python library for creating interactive web apps for data analysis and visualization.

#### How to Run

1. Install the necessary dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Access the app in your web browser at `http://localhost:8501`.

#### Features

- **Visualization Type**: Choose between different types of visualizations such as pie chart, bar chart, and line chart.
- **Focus Column**: Select the column to emphasize in the visualization.
- **Dataframe Editing**: Edit the data directly within the app using the built-in data editor.
- **Download Dataframe**: Export the edited data as a CSV or Excel file.
- **Pagination**: Navigate through multiple pages of data using pagination.
- **Dynamic Filtering**: Filter data based on department, course level, and groups.

#### Benefits

- Provides an intuitive interface for exploring and analyzing Student data.
- Allows for easy data manipulation and visualization without writing code.
- Enables users to export the edited data for further analysis in external tools.
- Supports dynamic filtering and pagination for handling large datasets efficiently.

### Telegram Bot

#### University Tracker Bot

The University Tracker Bot is a Telegram bot built using the aiogram library in Python. It provides analysis and insights into university attendance data.

#### How to Use

1. Start the bot by searching for "University Tracker Bot" on Telegram or clicking on the provided link.

2. Use the following commands to interact with the bot:
    - `/start`: Start the bot and view available commands.
    - `/departments`: View the list of departments.
    - `/courses <department>`: View available courses for a specific department.
    - `/groups <department> <course>`: View available groups for a specific department and course.
    - `/analytics <group>`: View analytics and insights for a specific group.

#### Features

- **Department Selection**: Choose a department to view available courses and groups.
- **Course Selection**: Select a course to view available groups within the chosen department.
- **Group Analytics**: Get detailed analytics and insights for a specific group, including attendance statistics and performance metrics.

#### Benefits

- Provides a convenient way for stakeholders to access and analyze university attendance data directly from Telegram.
- Offers a user-friendly interface with intuitive commands for navigation.
- Delivers actionable insights and analytics for informed decision-making.
- Enhances communication and collaboration among stakeholders by centralizing data access within the Telegram platform.