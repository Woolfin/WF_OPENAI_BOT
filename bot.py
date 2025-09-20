import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from openai import AsyncOpenAI
from decouple import config  # ← Безопасное чтение конфигов

# Безопасно читаем токены
TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")
OPENAI_API_KEY = config("OPENAI_API_KEY")

# Создаём клиент OpenAI
client = AsyncOpenAI(api_key=OPENAI_API_KEY)

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Команда /start


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот с GPT 🤖\nЗадай мне любой вопрос — я отвечу с помощью OpenAI!"
    )

# Обработка сообщений


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты полезный ассистент."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=512,
            temperature=0.7
        )

        ai_reply = response.choices[0].message.content.strip()
        await update.message.reply_text(ai_reply)

    except Exception as e:
        logger.error(f"Ошибка при запросе к OpenAI: {e}")
        await update.message.reply_text("Произошла ошибка. Проверь настройки API.")

# Обработка ошибок


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(msg="Exception while handling an update:",
                 exc_info=context.error)

# Запуск бота


def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)

    logger.info("Бот запущен...")
    application.run_polling()


if __name__ == '__main__':
    main()
