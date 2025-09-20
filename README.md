# 🤖 Telegram GPT-бот с памятью, голосом и кнопками

> Твой личный ИИ-ассистент в Telegram — работает 24/7, помнит контекст, принимает голосовые сообщения и управляется кнопками.

---

## ✨ Функции

- 💬 **Текстовые сообщения** — задавай любые вопросы
- 🧠 **История диалога** — бот помнит предыдущие сообщения в рамках сессии
- 🎙 **Голосовые сообщения** — говори вместо печати (распознаётся через Whisper API)
- 🔘 **Кнопки управления** — удобное меню: “Новый диалог”, “Помощь”, “О боте”
- ☁️ **Работает 24/7** — задеплоен на Render.com
- 🔐 **Безопасность** — ключи хранятся в переменных окружения, `.env` в `.gitignore`

---

## 🚀 Как запустить локально

1. Установи зависимости:
```
bash
pip install -r requirements.txt
```
2. Создай .env:
```
TELEGRAM_TOKEN=твой_токен_от_BotFather
OPENAI_API_KEY=твой_ключ_openai
```
3. Запусти бота:
```
python bot.py
```

☁️ Деплой на Render.com
Залей код на GitHub.
Создай Web Service на Render.com .
Укажи:
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: python bot.py
Добавь Environment Variables:
TELEGRAM_TOKEN
OPENAI_API_KEY
PYTHON_VERSION=3.12.3 ← обязательно!
Deploy → Profit!
📦 Требования
Python 3.12+
Библиотеки из requirements.txt
Аккаунт OpenAI с привязанной картой (для API)


