import telebot
import requests
import textUtils

file = open("secret.txt", encoding='utf-8')
token = file.read()
bot = telebot.TeleBot(token)

def analyze_text(message):
    text = message.text
    bot.send_message(message.chat.id, f"Longest word: {textUtils.get_longest_word(text)}")
    bot.send_message(message.chat.id, f"Most frequent word: {textUtils.get_most_frequent_word(text)}")
    bot.send_message(message.chat.id, f"Frequency: {textUtils.word_frequency(text)}")

def calculate(message):
    try:
        bot.send_message(message.chat.id, f"Result: {eval(message.text)}")
    except Exception:
        bot.send_message(message.chat.id, "Error")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Hey! Im able to check if misis website is alive with /check command.' +
                     'Give some text statistics with /wordStats command or calculate with /calculate')

@bot.message_handler(commands=["check"])
def check_handler(message):
    response = requests.get('http://misis.ru')
    if (response.status_code == requests.codes.ok):
        bot.send_message(message.chat.id, 'Misis is alive')
    else:
        bot.send_message(message.chat.id, 'Misis is not alive...')

@bot.message_handler(commands=["wordStats"])
def word_stats_handler(message):
    bot.send_message(message.chat.id, "Enter text to analyze")
    bot.register_next_step_handler(message, analyze_text)    

@bot.message_handler(commands=["calculate"])
def calculate_handler(message):
    bot.send_message(message.chat.id, "Enter expression to analyze")
    bot.register_next_step_handler(message, calculate)  

bot.polling(none_stop = True, interval = 0)