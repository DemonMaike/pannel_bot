# Документация https://vk-api.readthedocs.io/en/latest/
from lib2to3.pgen2 import token
from os import access
import secrets
import vk_api
from secret import PHONE,PASS,VK_TOKEN


#Аунтификация
session = vk_api.VkApi(login=PHONE, password=PASS, token=VK_TOKEN)
session.auth(reauth=True, token_only=True)
vk = session.get_api()

# выбор данных
posts = vk.wall.get(domain='plattenbauten', count = 2) #Так как присутствует пост в закрепе, берем последние два поста и всегда выбираем второй пост
# образец ответа {'count': 25007, 'items': [{'id': 222012, 'from_id':.....
all_post = posts['items']
target_post = all_post[1]
post_text = target_post.get('text') # Текст поста
attach_post = target_post.get('attachments')
photo_post = attach_post[0].get('photo')
photo_size = photo_post.get('sizes')
photo_url = photo_size[2].get('url') # url фотки поста

# из этого файла получаем текст и урл поста
print(post_text, photo_url)
