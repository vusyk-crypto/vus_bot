import logging
import sys
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(message)s',
                    stream=sys.stdout)

# Обробник команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.from_user.username
    logging.info(f"Відправляю користувача {username} на кастомну сторінку")

    # Створюємо кнопку з переходом на кастомну сторінку через Telegram WebApp
    web_app_url = f"https://vusyk-crypto.github.io/vus_bot/?username={username}"
    button = KeyboardButton(text="Вперед", web_app=WebAppInfo(url=web_app_url))
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True, one_time_keyboard=True)

    # Форматуємо ім'я користувача та VUS жирним шрифтом
    formatted_message = (
        f"Привіт, *{username}*! "
        f"Ти готовий увійти в дружню криптоспільноту *VUS*? "
        f"Тисни на кнопку '🚀 Вперед'"
    )

    # Відправляємо кнопку одразу після команди /start
    await update.message.reply_text(
        formatted_message,
        reply_markup=keyboard,
        parse_mode="Markdown"  # Використовуємо Markdown для форматування
    )

if __name__ == '__main__':
    token = "7230512720:AAG0mtv0oUBi9HAh-kCUex9YF-JNmkQXSxQ"  # Замініть на ваш реальний токен
    logging.info(f"Запуск бота з токеном: {token}")
    application = ApplicationBuilder().token(token).build()

    # Додаємо обробник для команди /start
    application.add_handler(CommandHandler("start", start))

    logging.info("Бот запущений. Очікування команд...")
    application.run_polling()
