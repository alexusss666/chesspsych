from itertools import chain

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).parents[1] / "data/sample_data.csv"
data = pd.read_csv(
		filepath_or_buffer=r'C:\Users\AMinturganov\DataspellProjects\univer-tracker\data\sample_data.csv')


# Function to paginate a list of items
def paginate_keyboard(items, page_size=5):
	pages = [items[i:i + page_size] for i in range(0, len(items), page_size)]
	return pages


def categories_keyboard():
	keyboard = InlineKeyboardBuilder()
	buttons = data
	keyboard.row(*[InlineKeyboardButton(text=i, callback_data=i) for i in chain(buttons['department'].unique())],
				 width=1)
	return keyboard.as_markup()


def groups_keyboards():
	keyboard = InlineKeyboardBuilder()
	buttons = [
		["Corporate Governance", "cg_group"],
		["Economics", "eco_group"],
		["Accounting", "acc_group"],
		["Tourism", "t_group"],
		["🔙 Ortga", "cancel"],
	]
	keyboard.row(*[InlineKeyboardButton(text=i[0], callback_data=i[1]) for i in chain(buttons)], width=1)
	return keyboard.as_markup()


def course_keyboard(department, page=1):
	departs = {
		'cg_group': "corporate governance",
		"eco_group": "economics",
		"acc_group": "accounting",
		"t_group": "tourism"
	}
	df = data[data['department'] == departs[department]]['group'].unique().tolist()

	# Paginate the list of groups
	pages = paginate_keyboard(df)

	# Select the current page
	current_page = page - 1
	current_page = min(current_page, len(pages) - 1)  # Ensure page is within bounds

	# Get the groups for the current page
	groups_on_page = pages[current_page]

	# Create keyboard markup
	# keyboard = InlineKeyboardMarkup(row_width=1)
	# for group in groups_on_page:
	# 	keyboard.add(InlineKeyboardButton(text=group, callback_data=group))
	# 	keyboard.row(*[InlineKeyboardButton(text=i, callback_data=i) for i in chain(groups_on_page)], width=1)

	keyboard = InlineKeyboardBuilder()
	keyboard.row(*[InlineKeyboardButton(text=i, callback_data=i) for i in chain(groups_on_page)], width=1)
	return keyboard.as_markup()
