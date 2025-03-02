Для создания Telegram-бота на Python с использованием библиотеки `python-telegram-bot` версии 20.x, который будет иметь обработчики `/start` и `/help`, логировать ошибки в файл и автоматически перезапускаться при сбоях, можно использовать следующий код:

### Установка необходимых библиотек
Сначала установите библиотеку `python-telegram-bot`:

```bash
pip install python-telegram-bot
```

### Код бота

```python
import logging
import os
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='bot_errors.log'
)
logger = logging.getLogger(__name__)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я ваш бот. Используйте /help для получения списка команд.')

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Доступные команды:\n/start - Начать работу с ботом\n/help - Получить справку')

# Функция для автоматического перезапуска бота при сбоях
def restart_bot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Основная функция для запуска бота
def main():
    # Вставьте сюда ваш токен
    token = 'YOUR_TELEGRAM_BOT_TOKEN'

    # Создаем приложение и передаем ему токен
    application = Application.builder().token(token).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    try:
        application.run_polling()
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        logger.info("Перезапуск бота...")
        restart_bot()

if __name__ == '__main__':
    main()
```

### Описание кода

1. **Логирование**: Логирование ошибок настроено с использованием модуля `logging`. Все ошибки будут записываться в файл `bot_errors.log`.

2. **Обработчики команд**:
   - `/start`: Отправляет приветственное сообщение.
   - `/help`: Отправляет список доступных команд.

3. **Автоматический перезапуск**: Если бот сталкивается с ошибкой, он автоматически перезапускается с помощью функции `restart_bot()`.

4. **Запуск бота**: Бот запускается с помощью метода `run_polling()`, который позволяет боту получать обновления от Telegram.

### Запуск бота

1. Замените `'YOUR_TELEGRAM_BOT_TOKEN'` на ваш токен, полученный от BotFather.
2. Запустите скрипт:

```bash
python your_bot_script.py
```

Теперь ваш бот будет работать, логировать ошибки и автоматически перезапускаться при сбоях.