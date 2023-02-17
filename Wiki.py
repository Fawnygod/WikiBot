import wikipedia, telebot 

bot = telebot.TeleBot('')#Insert your telegram bot api key here
wikipedia.set_lang('uk')


y = 0
def get_wiki(tex):
    try:
        x = wikipedia.page(tex)
        global y
        return x.content[:y+1000] + f'...\n\n--------------------------------------------------------------\n\nЧитати повністю! {x.url}'
    except wikipedia.exceptions.DisambiguationError:
        return 'Помилка, змініть слово або пероформулюйте!'
    except wikipedia.exceptions.PageError:
        return 'Помилка, змініть слово або пероформулюйте!'
    
            
       
            
@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, 'Відправте мені будь-яке слово і я знайду його в Wikipedia!')
    
    
@bot.message_handler(content_types=['text'])
def handle_text(mt):
    bot.send_message(mt.chat.id, get_wiki(mt.text))
    
bot.polling(none_stop=True, interval=0)