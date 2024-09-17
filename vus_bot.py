import logging
import sys
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(message)s',
                    stream=sys.stdout)

# Обробник команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.from_user.username
    logging.info(f"Відправляю користувача {username} на кастомну сторінку")

    # Створюємо кнопку з переходом на кастомну сторінку через Telegram WebApp
    web_app_url = f"https://vusyk-crypto.github.io/vus_bot/?username={username}"
    
    # Додаємо кнопку "Вперед"
    button = KeyboardButton(text="🚀 Вперед", web_app=WebAppInfo(url=web_app_url))
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True, one_time_keyboard=True)

    # Форматуємо ім'я користувача та VUS жирним шрифтом
    formatted_message = (
        f"Привіт, *{username}*! "
        f"Ти готовий увійти в дружню криптоспільноту *VUS*? "
        f"Тисни на ⚙️ кнопку 'Вперед!'"
    )

    # Відправляємо повідомлення з кнопкою
    await update.message.reply_text(
        formatted_message,
        reply_markup=keyboard,
        parse_mode="Markdown"  # Використовуємо Markdown для форматування
    )

# Обробник для відправки фото
async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Вказуємо абсолютний шлях до зображення
    photo_path = os.path.join(os.path.dirname(__file__), 'vus.png')
    
    try:
        await context.bot.send_photo(chat_id=update.message.chat_id, photo=InputFile(photo_path))
    except Exception as e:
        logging.error(f"Помилка при завантаженні зображення: {e}")

if __name__ == '__main__':
    token = "7230512720:AAG0mtv0oUBi9HAh-kCUex9YF-JNmkQXSxQ"  # Замініть на ваш реальний токен
    logging.info(f"Запуск бота з токеном: {token}")
    application = ApplicationBuilder().token(token).build()

    # Додаємо обробник для команди /start
    application.add_handler(CommandHandler("start", start))

    # Додаємо обробник для відправки зображення
    application.add_handler(CommandHandler("send_image", send_image))

    logging.info("Бот запущений. Очікування команд...")
    application.run_polling()
