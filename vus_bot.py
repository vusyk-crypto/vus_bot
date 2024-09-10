import logging
import sys
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(message)s',
                    stream=sys.stdout)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.from_user.username
    logging.info(f"Отправляю пользователя {username} на кастомную страницу")

    # Создаем кнопку с переходом на кастомную страницу через Telegram WebApp
    button = InlineKeyboardButton(text="Вперед", 
                                  web_app=WebAppInfo(url="https://vusyk-crypto.github.io/vus_bot/"))
    keyboard = InlineKeyboardMarkup([[button]])

    # Отправляем кнопку сразу после команды /start
    await update.message.reply_text(f"Привіт, {username}! Ти готовий увійти в дружню криптоспільноту VUS? Тисни на кнопку -Вперед-", reply_markup=keyboard)

if __name__ == '__main__':
    token = "7230512720:AAG0mtv0oUBi9HAh-kCUex9YF-JNmkQXSxQ"  # Твой рабочий токен
    logging.info(f"Запуск бота с токеном: {token}")
    application = ApplicationBuilder().token(token).build()

    # Добавляем обработчик для команды /start
    application.add_handler(CommandHandler("start", start))

    logging.info("Бот запущен. Ожидание команд...")
    application.run_polling()
