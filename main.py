from lib2to3.pgen2 import token
from os import access
import secrets
import vk_api
from * import secret


#Аунтификация
session = vk_api.VkApi(,)
try:
    session.auth()
except:
    session.check_sid
    
vk = session.get_api()

# выбор данных
posts = vk.wall.get(domain='plattenbauten', count = 2) #Так как присутствует пост в закрепе, берем последние два поста и всегда выбираем второй пост
# образец ответа {'count': 25007, 'items': [{'id': 222012, 'from_id': -66352011, 'owner_id': -66352011, 'date': 1664632919, 'marked_as_ads': 0, 'is_favorite': False, 'post_type': 'post', 'text': '', 'is_pinned': 1, 'attachments': [{'type': 'photo', 'photo': {'album_id': -7, 'date': 1664632919, 'id': 457288922, 'owner_id': -66352011, 'access_key': '28dc04ec92e0ba1075', 'post_id': 222012, 'sizes': [{'height': 75, 'url': 'https://sun9-27.userapi.com/impg/7Wk848j8noxM_6yxpWTYXUUoNzPPQeOpwMc8Yg/12MEBjEYzcU.jpg?size=72x75&quality=95&sign=3a728e0b425fb1a4980f9ac1adfe975d&c_uniq_tag=X8LRUxJz6nfrrku9Z56t-dYqAm2aEJYhUIVC3UBJKJw&type=album', 'type': 's', 'width': 72}, {'height': 130, 'url': 'https://sun9-27.userapi.com/impg/7Wk848j8noxM_6yxpWTYXUUoNzPPQeOpwMc8Yg/12MEBjEYzcU.jpg?size=125x130&quality=95&sign=8d204e34f7874e74b33c52e33540c005&c_uniq_tag=uIeDawS8cochX23KpnDetEN4_mCpL5MDaSBWBbA_b_E&type=album', 'type': 'm', 'width': 125}, {'height': 604, 'url': 'https://sun9-27.userapi.com/impg/7Wk848j8noxM_6yxpWTYXUUoNzPPQeOpwMc8Yg/12MEBjEYzcU.jpg?size=581x604&quality=95&sign=45f5a88e5365c3ea304daaa17be0d9c5&c_uniq_tag=BeimAP2YZb7JuNh0Q3zxDgYKUyk118x6pIYU-unVoj0&type=album', 'type': 'x', 'width': 581}, {'height': 773, 'url': 'https://sun9-27.userapi.com/impg/7Wk848j8noxM_6yxpWTYXUUoNzPPQeOpwMc8Yg/12MEBjEYzcU.jpg?size=744x773&quality=95&sign=7bd94a1b2c228ac75c9f59bb03b27178&c_uniq_tag=gtn8uTNJT3I9wV4Kr2P18ccOVvD_RpUG7liNs7NR58Q&type=album', 'type': 'y', 'width': 744}, {'height': 135, 'url': 'https://sun9-27.userapi.com/impg/7Wk848j8noxM_6yxpWTYXUUoNzPPQeOpwMc8Yg/12MEBjEYzcU.jpg?size=130x135&quality=95&sign=4449c4e11beb49cde7bd58a640146c61&c_uniq_tag=__6I9r9n6fOjtrD1ElaURmvf_8_oWupJ6T8yslUhIGc&type=album', 'type': 'o', 'width': 130}, {'height': 208, 'url': 'https://sun9-27.userapi.com/impg/7Wk848j8noxM_6yxpWTYXUUoNzPPQeOpwMc8Yg/12MEBjEYzcU.jpg?size=200x208&quality=95&sign=e7f39714c38427d2cf8bf3ca06a26d2f&c_uniq_tag=EmaLyrHWwNSETGv_u3eEXM9sFh83T_WtZsk_pJ5mUnI&type=album', 'type': 'p', 'width': 200}, {'height': 332, 'url': 'https://sun9-27.userapi.com/impg/7Wk848j8noxM_6yxpWTYXUUoNzPPQeOpwMc8Yg/12MEBjEYzcU.jpg?size=320x332&quality=95&sign=902e40867ca4fd3e478b153f19f72335&c_uniq_tag=K-vSAxXb1QmabZHVNdUQaO1slCjC1JQDprC31lZz974&type=album', 'type': 'q', 'width': 320}, {'height': 530, 'url': 'https://sun9-27.userapi.com/impg/7Wk848j8noxM_6yxpWTYXUUoNzPPQeOpwMc8Yg/12MEBjEYzcU.jpg?size=510x530&quality=95&sign=03dd827dab26e706c62f3d33f847e27e&c_uniq_tag=MzK4-_rspUOixrUIivxM2CwN6VP6FkiczyNg_K3xRM4&type=album', 'type': 'r', 'width': 510}], 'text': '', 'user_id': 100}}], 'post_source': {'type': 'vk'}, 'comments': {'can_post': 0, 'count': 0, 'groups_can_post': True}, 'likes': {'can_like': 1, 'count': 6612, 'user_likes': 0, 'can_publish': 1}, 'reposts': {'count': 513, 'user_reposted': 0}, 'views': {'count': 192944}, 'hash': '4kMUhiA3s8IYvJAWw16t5x4ZY2HQ'}]}
all_post = posts['items']
target_post = all_post[1]
post_text = target_post.get('text') # Текст поста
attach_post = target_post.get('attachments')
photo_post = attach_post[0].get('photo')
photo_size = photo_post.get('sizes')
photo_url = photo_size[2].get('url') # url фотки поста

# из этого файла получаем текст и урл поста
print(post_text, photo_url)
