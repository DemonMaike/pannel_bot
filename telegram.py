import telebot

from main import post_text,photo_url

# включаем бота                         токен бота
bot = telebot.TeleBot('5704783208:AAHwd3eNdjXUF5aqs38beuoZ_izR9LniiuA')
media = {'text':post_text, 'url':photo_url}
chat_id = -1001395549881

def send_post():
    bot.send_photo(chat_id, media['url'], caption=media['text'])


if __name__ == '__main__':
    send_post()