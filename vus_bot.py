import logging
import sys
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(message)s',
                    stream=sys.stdout)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Відправляю кнопку для переходу на кастомну сторінку")
    
    # Создаем кнопку с переходом на кастомную страницу через Telegram WebApp
    button = InlineKeyboardButton("Перейти на кастомну сторінку", 
                                  web_app=WebAppInfo(url="https://vusyk-crypto.github.io/vus_bot/"))
    keyboard = InlineKeyboardMarkup([[button]])

    # Ответ с кнопкой
    await update.message.reply_text("Натисни кнопку для переходу на кастомну сторінку:", reply_markup=keyboard)

if __name__ == '__main__':
    token = "7230512720:AAG0mtv0oUBi9HAh-kCUex9YF-JNmkQXSxQ"
    logging.info(f"Запуск бота з токеном: {token}")
    application = ApplicationBuilder().token(token).build()

    # Добавляем обработчик для команды /start
    application.add_handler(CommandHandler("start", start))

    logging.info("Бот запущений. Очікування команд...")
    application.run_polling()


