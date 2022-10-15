import config
import telebot
from telebot import types


bot = telebot.TeleBot(token = config.TOKEN,
                    parse_mode='HTML')

DATA = {'karavan_luxe-1':400000, 'karavan_luxe-2':315000, 'karavan_oddiy':250000,
        'fayz_luxe-1':400000, 'fayz_luxe-2':315000, 'fayz_oddiy':250000,
        'xorazm_luxe-1':400000, 'xorazm_luxe-2':315000, 'xorazm_oddiy':250000,
        'uzb_luxe-1':400000, 'uzb_luxe-2':315000, 'uzb_oddiy':250000,
}
USERS = {}



@bot.callback_query_handler(func = lambda call: True)
def all_call_backs(call):
    chat_id = call.message.chat.id
    if call.data == 'uzbek_tili':
        return bot_menu(call)
    elif call.data == 'menu':
        return bot_menu(call)
    elif call.data == 'karavan':
        return karavan(call)
    elif call.data == 'xorazm':
        return xorazm(call)
    elif call.data == 'fayz':
        return fayz(call)
    elif call.data == 'uzb':
        return uzb(call)
    elif call.data == 'boladi':
        return finish(call)
    elif call.data[-1] == '*':
        return page_answer(call, call.data[:-1])
    elif call.data[-1] == '+':
        try:
            callback = call.data[:-1]
            if USERS[chat_id] <= 5:
                USERS[chat_id] += 1
        except:
            return bot_menu(call)
        return page_answer(call, callback)
    elif call.data[-1] == '-':
        try:
            callback = call.data[:-1]
            if USERS[chat_id] > 1:
                USERS[chat_id] -= 1
        except:
            return bot_menu(call)
        return page_answer(call, callback)




@bot.message_handler(commands=['start'])
def start_bot(message):
    chat_id = message.chat.id
    text = f'🇺🇿 Tilni tanlang\n🇷🇺Выберите язык'
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text = '🇷🇺 Русский', callback_data='rus_tili')
    made2 = types.InlineKeyboardButton(text = "🇺🇿 O'zbek tili", callback_data='uzbek_tili')
    made.add(made1, made2)
    bot.send_message(chat_id = chat_id,
                    text = text,
                    reply_markup=made)


def bot_menu(call):
    chat_id = call.message.chat.id
    USERS[chat_id] = 1
    text = "Assalomu alaykum, Iltimos pastda keltirilgan mehmonxonalardan birini tanlang"
    made = types.InlineKeyboardMarkup(row_width=2)
    made1 = types.InlineKeyboardButton(text = 'Karavan', callback_data='karavan')
    made2 = types.InlineKeyboardButton(text = 'Fayz', callback_data='fayz')
    made3 = types.InlineKeyboardButton(text = 'Xorazm palace', callback_data='xorazm')
    made4 = types.InlineKeyboardButton(text = 'Uzbekistan', callback_data='uzb')
    made.add(made1, made2, made3, made4)
    file = open('bot/allphotos/hotel.png', 'rb')
    bot.delete_message(chat_id, call.message.id)
    bot.send_photo(chat_id,
                    photo=file,
                    caption=text,
                    reply_markup=made
                    )
    file.close()


def karavan(call):
    chat_id = call.message.chat.id
    text = f"<b>Mehmonxona:</b> Karavan"
    made = types.InlineKeyboardMarkup(row_width=2)
    made1 = types.InlineKeyboardButton(text = 'Super Luxe', callback_data='karavan_luxe-1*')
    made2 = types.InlineKeyboardButton(text = 'Luxe xona', callback_data='karavan_luxe-2*')
    made3 = types.InlineKeyboardButton(text = 'Oddiy xona', callback_data='karavan_oddiy*')
    menu = types.InlineKeyboardButton(text = '⚙️ Menu', callback_data='menu')
    made.add(made1, made2, made3)
    made.add(menu, row_width=1)
    file = open('bot/allphotos/hotel.png', 'rb')
    bot.edit_message_media(media=types.InputMedia(type = 'photo', media=file),
    chat_id =call.message.chat.id,
    message_id=call.message.id
    )
    bot.edit_message_caption(caption=text, chat_id = chat_id, message_id=call.message.id, reply_markup=made)


def fayz(call):
    chat_id = call.message.chat.id
    text = f"<b>Mehmonxona:</b> Fayz"
    made = types.InlineKeyboardMarkup(row_width=2)
    made1 = types.InlineKeyboardButton(text = 'Super Luxe', callback_data='fayz_luxe-1*')
    made2 = types.InlineKeyboardButton(text = 'Luxe xona', callback_data='fayz_luxe-2*')
    made3 = types.InlineKeyboardButton(text = 'Oddiy xona', callback_data='fayz-oddiy*')
    menu = types.InlineKeyboardButton(text = '⚙️ Menu', callback_data='menu')
    made.add(made1, made2, made3)
    made.add(menu, row_width=1)
    file = open('bot/allphotos/fayz.png', 'rb')
    bot.edit_message_media(media=types.InputMedia(type = 'photo', media=file),
    chat_id =call.message.chat.id,
    message_id=call.message.id
    )
    bot.edit_message_caption(caption=text, chat_id = chat_id, message_id=call.message.id, reply_markup=made)


def xorazm(call):
    chat_id = call.message.chat.id
    text = f"<b>Mehmonxona:</b> Kharezm Palace"
    made = types.InlineKeyboardMarkup(row_width=2)
    made1 = types.InlineKeyboardButton(text = 'Super Luxe', callback_data='xorazm_luxe-1*')
    made2 = types.InlineKeyboardButton(text = 'Luxe xona', callback_data='xorazm_luxe-2*')
    made3 = types.InlineKeyboardButton(text = 'Oddiy xona', callback_data='xorazm_oddiy*')
    menu = types.InlineKeyboardButton(text = '⚙️ Menu', callback_data='menu')
    made.add(made1, made2, made3)
    made.add(menu, row_width=1)
    file = open('bot/allphotos/palace.png', 'rb')
    bot.edit_message_media(media=types.InputMedia(type = 'photo', media=file),
    chat_id =call.message.chat.id,
    message_id=call.message.id
    )
    bot.edit_message_caption(caption=text, chat_id = chat_id, message_id=call.message.id, reply_markup=made)



def uzb(call):
    chat_id = call.message.chat.id
    text = f"<b>Mehmonxona:</b> Uzbekistan hotel"
    made = types.InlineKeyboardMarkup(row_width=2)
    made1 = types.InlineKeyboardButton(text = 'Super Luxe', callback_data='uzb_luxe-1*')
    made2 = types.InlineKeyboardButton(text = 'Luxe xona', callback_data='uzb_luxe-2*')
    made3 = types.InlineKeyboardButton(text = 'Oddiy xona', callback_data='uzb_oddiy*')
    menu = types.InlineKeyboardButton(text = '⚙️ Menu', callback_data='menu')
    made.add(made1, made2, made3)
    made.add(menu, row_width=1)
    file = open('bot/allphotos/uzb.png', 'rb')
    bot.edit_message_media(media=types.InputMedia(type = 'photo', media=file),
    chat_id =call.message.chat.id,
    message_id=call.message.id
    )
    bot.edit_message_caption(caption=text, chat_id = chat_id, message_id=call.message.id, reply_markup=made)


def page_answer(call, callback):
    chat_id = call.message.chat.id
    data = callback.split('_')
    if data[0] == 'karavan':
        title = 'Karavan'
    elif data[0] == 'fayz':
        title = 'Fayz mehmonxonasi'
    elif data[0] == 'uzb':
        title = 'Ubekistan mehmonxonasi'
    elif data[0] == 'xorazm':
        title = 'Xorazm palace'
    if data[1] == 'luxe-1':
        tip = 'Super luxe xona'
    elif data[1] == 'luxe-2':
        tip = 'Luxe xona'
    elif data[1] == 'oddiy':
        tip = 'Oddiy xona'
    narx = DATA[callback]
    try:
        text = f"<b>Mehmonxona:</b> {title}\n<b>    Xona:</b> {tip}\n   <b>Narxi</b>: {narx} x {USERS[chat_id]} = {narx*USERS[chat_id]} so'm"
    except:
        return bot_menu(call)
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text = '➕', callback_data=callback + '+')
    made2 = types.InlineKeyboardButton(text = f'{USERS[chat_id]} kishi', callback_data='nothing')
    made3 = types.InlineKeyboardButton(text = '➖', callback_data=callback + '-')
    made4 = types.InlineKeyboardButton(text = '✅ Buyurtma berish', callback_data='boladi')
    menu = types.InlineKeyboardButton(text = '⚙️ Menu', callback_data='menu')
    made.add(made3, made2, made1)
    made.add(made4, menu, row_width=1)
    bot.edit_message_caption(caption = text,
                            chat_id = chat_id,
                            message_id=call.message.id,
                            reply_markup=made)


def finish(call):
    chat_id = call.message.chat.id
    text = "Iltimos, siz bilan bog'lanish uchun o'z telefon raqamingizni qoldiring."
    made = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    made1 = types.KeyboardButton(text = '📲 Telefon raqamni qoldirish', request_contact=True)
    made.add(made1)
    bot.delete_message(chat_id=chat_id,
                        message_id = call.message.id)
    bot.send_message(chat_id=chat_id,
                    text = text,
                    reply_markup= made)


@bot.message_handler(content_types='contact')
def qabul(message):
    chat_id = message.chat.id
    text = f"Sizni so'rovingiz qabul qilindi"
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text = 'Menu', callback_data='menu')
    made.add(made1)
    bot.send_message(chat_id=chat_id,
                    text = text,
                    reply_markup=made)

if __name__ == '__main__':
    bot.polling(non_stop=True)
    bot.infinity_polling()


