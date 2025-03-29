import os
import telebot
import logging

# Replace 'YOUR_API_TOKEN' with the API token you obtained from BotFather
API_TOKEN = os.getenv('7706714998:AAFRI_jFMrGatp-x2CtvRlrXTgnW0E-t3ec')

if not API_TOKEN:
    raise ValueError("No API token provided. Set the TELEGRAM_API_TOKEN environment variable.")

# Initialize the bot
bot = telebot.TeleBot('7706714998:AAFRI_jFMrGatp-x2CtvRlrXTgnW0E-t3ec')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define a handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    logging.info(f"Received /start command from {message.chat.id}")
    bot.reply_to(message, "Welcome to my bot!")

# Define a handler for the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    logging.info(f"Received /help command from {message.chat.id}")
    bot.reply_to(message, "How can I help you?")

# Define a handler for text messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    logging.info(f"Echoing message from {message.chat.id}: {message.text}")
    bot.reply_to(message, message.text)

# Start the bot
if __name__ == "__main__":
    try:
        logging.info("Starting bot polling...")
        bot.polling()
    except Exception as e:
        logging.error(f"Error occurred: {e}")
