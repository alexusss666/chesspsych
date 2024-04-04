import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
from pathlib import Path

csv_path = Path(__file__).parents[1] / 'data/sample_data.csv'

st.set_page_config(page_title="Students Tracker",
				   page_icon="⏰",
				   layout="wide",
				   initial_sidebar_state="expanded",
				   menu_items={
					   'Get Help': "mailto:alixan.me@yandex.com",
					   'Report a bug': "mailto:alixan.me@yandex.com",
					   'About': "A Student tracker app made with Streamlit."
				   })

# Establish communication between pygwalker and streamlit
init_streamlit_comm()

# Add a title
st.title("Use Pygwalker In Streamlit")


@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
	df_pyg = pd.read_csv(filepath_or_buffer=csv_path, parse_dates=['date'])
	return StreamlitRenderer(df_pyg, spec="./gw_config.json", debug=False)


renderer = get_pyg_renderer()

# Render your data exploration interface. Developers can use it to build charts by drag and drop.
renderer.render_explore()
