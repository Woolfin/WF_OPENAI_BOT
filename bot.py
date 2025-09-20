import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Токены
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Создаём асинхронный клиент OpenAI
client = AsyncOpenAI(api_key=OPENAI_API_KEY)

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот с ИИ. Напиши мне что-нибудь — я отвечу с помощью искусственного интеллекта 🤖"
    )

# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        # Запрос к OpenAI через новый API (v1+)
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты полезный ассистент."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=1000,
            temperature=0.7
        )

        ai_reply = response.choices[0].message.content.strip()

        # Отправляем ответ пользователю
        await update.message.reply_text(ai_reply)

    except Exception as e:
        logger.error(f"Ошибка при запросе к OpenAI: {e}")
        await update.message.reply_text("Произошла ошибка при обращении к ИИ. Попробуй позже.")

# Обработка ошибок
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

# Основная функция запуска бота
def main():
    # Создаём приложение
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Добавляем обработчик ошибок
    application.add_error_handler(error_handler)

    # Запускаем бота
    logger.info("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()