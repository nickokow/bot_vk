import pogoda_v1
from pogoda_v1 import *
import oborona
from oborona import *
import matclock
from matclock import *
import random
from random import *
import auth
from auth import *
import vk_api
import vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
vk_session = vk_api.VkApi(token = secret)
longpoll = VkBotLongPoll(vk_session, 174963147)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        if 'Команды ' in str(event) or 'команды' in str(event) or 'Бот' in str(event):
            random_id = round(random() * 10 ** 9)
            chat_id = int(event.chat_id)

            vk.messages.send(
                    random_id=random_id,
                    chat_id=chat_id,
                    message='Кожанный мешок называй меня Тоб, можешь дать мне команды: \nТоб время \nТоб погода \nТоб песню \nТоб музыку ',
                    )

        if 'привет бот' in str(event) or 'Привет бот' in str(event):
            random_id = round(random() * 10 ** 9)
            chat_id = int(event.chat_id)

            vk.messages.send(
                    random_id=random_id,
                    chat_id=chat_id,
                    message='Здравствуй кожанный мешок',
                    )

        if 'Тоб время' in str(event) or 'тоб время' in str(event):
            random_id = round(random() * 10 ** 9)
            chat_id = int(event.chat_id)
            cltext = mclock()

            vk.messages.send(
                        random_id=random_id,
                        chat_id=chat_id,
                        message=cltext,
                        )

        if 'Тоб погода' in str(event) or 'тоб погода' in str(event):
            random_id = round(random() * 10 ** 9)
            chat_id = int(event.chat_id)

            vk.messages.send(
                random_id=random_id,
                chat_id=chat_id,
                #if 'пасмурно' in str(json_result()) or '','',#
                message='Уважаемый кожанный мешок, погода збс! ' + str(json_result()),
                )
                        if 'Тоб песню' in str(event) or 'тоб песню' in str(event):
            random_id = round(random() * 10 ** 9)
            chat_id = int(event.chat_id)

                vk.messages.send(
                    random_id=random_id,
                    chat_id=chat_id,
                    message='Ооо, Моя оборона!!! ' + oborona_gen(),
                    )

        if 'Тоб музыку' in str(event) or 'тоб музыку' in str(event):
            random_id = round(random() * 10 ** 9)
            chat_id = int(event.chat_id)

            vk.messages.send(
                    random_id=random_id,
                    chat_id=chat_id,
                    message='Уважаемый кожанный мешок, эта функция еще не готова.',
                    )
