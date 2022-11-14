import telebot
from secret import TG_TOKEN, ID_GROUP

from main import post_text,photo_url

# включаем бота                         токен бота
bot = telebot.TeleBot(TG_TOKEN)
media = {'text':post_text, 'url':photo_url}
chat_id = ID_GROUP
def send_post():
    bot.send_photo(chat_id, media['url'], caption=media['text'])


if __name__ == '__main__': 
    send_post()