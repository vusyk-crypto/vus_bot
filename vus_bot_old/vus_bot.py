import logging
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    stream=sys.stdout)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = f"Привіт! Це нова відповідь. Поточний час: {current_time}"
    logging.info(f"Відправляю відповідь: {response}")
    await update.message.reply_text(response)

# Обработчик команды /main
async def main(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = "Це відповідь на команду /main."
    logging.info(f"Відправляю відповідь: {response}")
    await update.message.reply_text(response)

if __name__ == '__main__':
    token = "7230512720:AAG0mtv0oUBi9HAh-kCUex9YF-JNmkQXSxQ"
    logging.info(f"Запуск бота з токеном: {token}")
    application = ApplicationBuilder().token(token).build()

    # Добавляем обработчики для команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("main", main))

    logging.info("Бот запущений. Очікування команд...")
    application.run_polling()