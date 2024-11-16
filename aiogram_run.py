import asyncio
from create_bot import bot, dp, scheduler
from handlers.start import start_router, send_motivational_messages


async def main():
	dp.include_router(start_router)

	# Удаляем вебхук и очищаем все ожидающие обновления
	await bot.delete_webhook(drop_pending_updates=True)

	# Запускаем фоновую задачу для отправки сообщений
	print("Запускаем фоновую задачу...")
	asyncio.create_task(send_motivational_messages())

	# Запускаем планировщик (если он нужен)
	scheduler.start()
	print("Начинаем polling...")
	await dp.start_polling(bot)
if __name__ == "__main__":
	asyncio.run(main())
