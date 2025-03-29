import telebot

# Replace 'YOUR_API_TOKEN' with the API token you obtained from BotFather
API_TOKEN = '7706714998:AAFRI_jFMrGatp-x2CtvRlrXTgnW0E-t3ec'

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Define a handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to my bot!")

# Define a handler for the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "How can I help you?")

# Define a handler for text messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Start the bot
bot.polling()