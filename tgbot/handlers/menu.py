import logging
import pandas as pd
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline import groups_keyboards, categories_keyboard, course_keyboard

menu_router = Router()

data = pd.read_csv(
		filepath_or_buffer=r'C:\Users\AMinturganov\DataspellProjects\univer-tracker\data\sample_data.csv')


# Define a function to get analysis for a specific department
def get_department_analysis(department):
	# Read the CSV file into a pandas DataFrame
	df = data

	# Filter data for the specified department
	department_data = df[df['department'] == department]

	# Calculate some analytics
	total_students = len(department_data)
	average_attendance = department_data['attendance'].mean()
	max_attendance = department_data['attendance'].max()

	# Generate the analysis message
	analysis_message = f"Analysis for {department.capitalize()} department:\n"
	analysis_message += f"Total students: {total_students}\n"
	analysis_message += f"Average attendance: {average_attendance}\n"
	analysis_message += f"Maximum attendance: {max_attendance}\n"

	return analysis_message, department_data


@menu_router.message(F.text.contains('Departments'))
async def select_category(message: Message):
	logging.info(message)
	logging.info(f"{message.from_user.username=}")
	logging.info(f"{message.from_user.full_name=}")

	await message.answer(f"Choose the Department", reply_markup=categories_keyboard())


@menu_router.message(F.text.contains('Analytics'))
async def show_courses(message: Message):
	logging.info(message)
	logging.info(f"{message.from_user.username=}")
	logging.info(f"{message.from_user.full_name=}")
	await message.answer("Analytics For Which Group", reply_markup=groups_keyboards())


@menu_router.callback_query(F.data == "tourism")
async def department_analysis(call: CallbackQuery):
	callback_data = call.data
	logging.info(f"{callback_data=}")
	logging.info(f"{call.from_user.username=}")
	analysis, _ = get_department_analysis('tourism')
	await call.answer(analysis, cache_time=60, show_alert=True)


@menu_router.callback_query(F.data == "corporate governance")
async def department_analysis(call: CallbackQuery):
	callback_data = call.data
	logging.info(f"{callback_data=}")
	logging.info(f"{call.from_user.username=}")
	analysis, _ = get_department_analysis('corporate governance')
	await call.answer(analysis, cache_time=60, show_alert=True)


@menu_router.callback_query(F.data == "economics")
async def department_analysis(call: CallbackQuery):
	callback_data = call.data
	logging.info(f"{callback_data=}")
	logging.info(f"{call.from_user.username=}")
	analysis, _ = get_department_analysis('economics')
	await call.answer(analysis, cache_time=60, show_alert=True)


@menu_router.callback_query(F.data == "accounting")
async def department_analysis(call: CallbackQuery):
	callback_data = call.data
	logging.info(f"{callback_data=}")
	logging.info(f"{call.from_user.username=}")
	analysis, _ = get_department_analysis('accounting')
	await call.answer(analysis, cache_time=60, show_alert=True)


@menu_router.callback_query(F.data == "cancel")
async def cancel_buying(call: CallbackQuery):
	await call.message.edit_reply_markup(reply_markup=categories_keyboard())
	await call.answer()


@menu_router.callback_query(F.data == "cg_group")
async def sending_course(call: CallbackQuery):
	await call.message.edit_reply_markup(f"Choose The Group", reply_markup=course_keyboard('cg_group'))

	await call.answer(cache_time=60)


@menu_router.callback_query(F.data == "AT-81")
async def department_analysis(call: CallbackQuery):
	callback_data = call.data
	print(callback_data)
	logging.info(f"{callback_data=}")
	logging.info(f"{call.from_user.username=}")
	department = "corporate governance"  # You need to determine the department based on the group, e.g., from your data
	_, analysis = get_department_analysis(department)

	# Filter analysis based on group
	group_analysis = analysis[analysis['group'] == callback_data]

	# Generate response message
	response_message = f"Analysis for group {callback_data} in {department}:\n"
	response_message += f"Student Course: {group_analysis['course'].iloc[0]}\n"
	response_message += f"Average attendance: {group_analysis['attendance'].mean()}\n"

	await call.message.answer(response_message, cache_time=60)


@menu_router.callback_query(F.data == "BR-25")
async def department_analysis(call: CallbackQuery):
	callback_data = call.data
	print(callback_data)
	logging.info(f"{callback_data=}")
	logging.info(f"{call.from_user.username=}")
	department = "corporate governance"  # You need to determine the department based on the group, e.g., from your data
	_, analysis = get_department_analysis(department)

	# Filter analysis based on group
	group_analysis = analysis[analysis['group'] == callback_data]

	# Generate response message
	response_message = f"Analysis for group {callback_data} in {department}:\n"
	response_message += f"Student Course: {group_analysis['course'].iloc[0]}\n"
	response_message += f"Average attendance: {group_analysis['attendance'].mean()}\n"

	await call.message.answer(response_message, cache_time=60)


@menu_router.callback_query(F.data == "BR-77")
async def department_analysis(call: CallbackQuery):
	callback_data = call.data
	print(callback_data)
	logging.info(f"{callback_data=}")
	logging.info(f"{call.from_user.username=}")
	department = "corporate governance"  # You need to determine the department based on the group, e.g., from your data
	_, analysis = get_department_analysis(department)

	# Filter analysis based on group
	group_analysis = analysis[analysis['group'] == callback_data]

	# Generate response message
	response_message = f"Analysis for group {callback_data} in {department}:\n"
	response_message += f"Student Course: {group_analysis['course'].iloc[0]}\n"
	response_message += f"Average attendance: {group_analysis['attendance'].mean()}\n"

	await call.message.answer(response_message, cache_time=60)


@menu_router.callback_query(F.data == "KB-81")
async def department_analysis(call: CallbackQuery):
	callback_data = call.data
	print(callback_data)
	logging.info(f"{callback_data=}")
	logging.info(f"{call.from_user.username=}")
	department = "corporate governance"  # You need to determine the department based on the group, e.g., from your data
	_, analysis = get_department_analysis(department)

	# Filter analysis based on group
	group_analysis = analysis[analysis['group'] == callback_data]

	# Generate response message
	response_message = f"Analysis for group {callback_data} in {department}:\n"
	response_message += f"Student Course: {group_analysis['course'].iloc[0]}\n"
	response_message += f"Average attendance: {group_analysis['attendance'].mean()}\n"

	await call.message.answer(response_message, cache_time=60)


@menu_router.callback_query(F.data == "RI-91")
async def department_analysis(call: CallbackQuery):
	callback_data = call.data
	print(callback_data)
	logging.info(f"{callback_data=}")
	logging.info(f"{call.from_user.username=}")
	department = "corporate governance"  # You need to determine the department based on the group, e.g., from your data
	_, analysis = get_department_analysis(department)

	# Filter analysis based on group
	group_analysis = analysis[analysis['group'] == callback_data]

	# Generate response message
	response_message = f"Analysis for group {callback_data} in {department}:\n"
	response_message += f"Student Course: {group_analysis['course'].iloc[0]}\n"
	response_message += f"Average attendance: {group_analysis['attendance'].mean()}\n"

	await call.message.answer(response_message, cache_time=60)
