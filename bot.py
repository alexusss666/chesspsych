import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from tgbot.data.config import load_config, Config
from tgbot.handlers import routers_list
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.utils.notify_admins import on_startup_notify
from tgbot.utils.set_bot_commands import set_commands


def register_global_middlewares(dp: Dispatcher, config: Config, session_pool=None):
	"""
	Register global middlewares for the given dispatcher.
	Global middlewares here are the ones that are applied to all the handlers (you specify the type of update)

	:param dp: The dispatcher instance.
	:type dp: Dispatcher
	:param config: The configuration object from the loaded configuration.
	:param session_pool: Optional session pool object for the database using SQLAlchemy.
	:return: None
	"""
	middleware_types = [
		ConfigMiddleware(config),
	]

	for middleware_type in middleware_types:
		dp.message.outer_middleware(middleware_type)
		dp.callback_query.outer_middleware(middleware_type)


def setup_logging():
	"""
	Set up logging configuration for the application.

	This method initializes the logging configuration for the application.
	It sets the log level to INFO and configures a basic colorized log for
	output. The log format includes the filename, line number, log level,
	timestamp, logger name, and log message.

	Returns:
		None

	Example usage:
		setup_logging()
	"""
	log_level = logging.INFO
	bl.basic_colorized_config(level=log_level)

	logging.basicConfig(
			level=logging.INFO,
			format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
	)
	logger = logging.getLogger(__name__)
	logger.info("Starting bot")


def get_storage(config):
	"""
	Return storage based on the provided configuration.

	Args:
		config (Config): The configuration object.

	Returns:
		Storage: The storage object based on the configuration.

	"""
	return MemoryStorage()


async def main():
	setup_logging()

	config = load_config(".env")
	storage = get_storage(config)

	bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
	dp = Dispatcher(storage=storage)

	dp.include_routers(*routers_list)

	register_global_middlewares(dp, config)
	admins = config.tg_bot.admin_ids

	await set_commands(bot)
	await on_startup_notify(bot, admins)
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


if __name__ == "__main__":
	try:
		asyncio.run(main())
	except (KeyboardInterrupt, SystemExit):
		logging.error("The bot has been disabled!")
