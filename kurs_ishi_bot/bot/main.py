import telebot
from telebot import types
import config
import datetime


bot = telebot.TeleBot(token = config.TOKEN,
                        parse_mode='HTML')

COUNTS = {'samsung_televizor':{'cnt' : 30, 'narxi' : 5000000, 'changes':{}}, 'samsung_telefon':{'cnt' : 40, 'narxi' : 3000000, 'changes':{}}, 'samsung_kir':{'cnt' : 21, 'narxi' : 7000000, 'changes':{}},
        'lg_televizor':{'cnt' : 30, 'narxi' : 5560000, 'changes':{}}, 'lg_telefon':{'cnt' : 4, 'narxi' : 30300000, 'changes':{}}, 'lg_kir':{'cnt' : 15, 'narxi' : 15000000, 'changes':{}},
        'shivaki_televizor':{'cnt' : 30, 'narxi' : 5000000, 'changes':{}}, 'shivaki_telefon':{'cnt' : 30, 'narxi' : 5000000, 'changes':{}}, 'shivaki_kir':{'cnt' : 30, 'narxi' : 5000000, 'changes':{}},
        'artel_televizor':{'cnt' : 34, 'narxi' : 3440000, 'changes':{}}, 'artel_telefon':{'cnt' : 10, 'narxi' : 2500000, 'changes':{}}, 'artel_kir':{'cnt' : 30, 'narxi' : 5000000, 'changes':{}}}


@bot.callback_query_handler(func = lambda call: True)
def all_callback_datas(call):
    if call.data == 'uzbek_tili':
        return bot_menu(call)
    elif call.data == 'samsung':
        return samsung(call)
    elif call.data == 'menu':
        return bot_menu(call)
    elif call.data == 'lg':
        return lg(call)
    elif call.data == 'shivaki':
        return shivaki(call)
    elif call.data == 'artel':
        return artel(call)
    elif call.data[-1] == '*':
        return page_answer(call, call.data[:-1])
    elif call.data[-1] == '+':
        good = call.data[:-1]
        COUNTS[good]['cnt'] += 1
        try:
            COUNTS[good]['changes'][f'{datetime.datetime.now().year}/{datetime.datetime.now().month}/{datetime.datetime.now().day}'] += 1
        except:
            COUNTS[good]['changes'][f'{datetime.datetime.now().year}/{datetime.datetime.now().month}/{datetime.datetime.now().day}'] = 1
        return page_answer(call, good)
    elif call.data[-1] == '-':
        good = call.data[:-1]
        if COUNTS[good]['cnt'] != 0:
            try:
                COUNTS[good]['changes'][f'{datetime.datetime.now().year}/{datetime.datetime.now().month}/{datetime.datetime.now().day}'] -= 1
            except:
                COUNTS[good]['changes'][f'{datetime.datetime.now().year}/{datetime.datetime.now().month}/{datetime.datetime.now().day}'] = 1
            COUNTS[good]['cnt'] -= 1
        return page_answer(call, good)


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
    text = """<b>Iltimos, Mahsulot brendini tanlang</b>"""
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text = 'Samsung', callback_data='samsung')
    made2 = types.InlineKeyboardButton(text = 'LG', callback_data='lg')
    made3 = types.InlineKeyboardButton(text = 'Shivaki', callback_data='shivaki')
    made4 = types.InlineKeyboardButton(text = 'Artel', callback_data='artel')
    made.add(made1, made2, made3, made4)
    bot.edit_message_text(text = text,
                            chat_id = chat_id,
                            message_id=call.message.id,
                            reply_markup=made)
                                

def samsung(call):
    chat_id = call.message.chat.id
    televizor_count = COUNTS['samsung_televizor']['cnt']
    telefon_count = COUNTS['samsung_telefon']['cnt']
    kir_count = COUNTS['samsung_kir']['cnt']
    text = f"""📂 <b>Mahsulot brendi</b>: <i>Samsung</i>\nIltimos mahsulot turini tanlang\n1.<b>Televizor</b> -- {televizor_count} dona\n2.<b>Telefon</b> -- {telefon_count} dona\n2.<b>Kir yuvish mashinasi</b> -- {kir_count} dona"""
    made = types.InlineKeyboardMarkup(row_width=2)
    made1 = types.InlineKeyboardButton(text = 'Televizor', callback_data='samsung_televizor*')
    made2 = types.InlineKeyboardButton(text = 'Telefon', callback_data='samsung_telefon*')
    made3 = types.InlineKeyboardButton(text = 'Kir yuvish mashinasi', callback_data='samsung_kir*')
    menu = types.InlineKeyboardButton(text = '⚙️ Menu', callback_data='menu')
    made.add(made1, made2)
    made.add(made3, menu, row_width=1)
    bot.edit_message_text(text=text,
                            chat_id = chat_id,
                            message_id=call.message.id,
                            reply_markup=made)


def page_answer(call, callback, count = COUNTS):
    type_good, brend_good = callback.split('_')[0], callback.split('_')[1]
    chat_id = call.message.chat.id
    text1 = type_good
    txt = ''
    dct = COUNTS[callback]['changes']
    for keys, values in dct.items():
        if values > 0:
            values = '+' + str(values)
        txt += f'{keys} ~~ {values}\n'
    if type_good == 'kir':
        text1 = 'Kir yuvish mashinasi'
    t = 'narxi'
    text = f"<b>Mahsulot :</b> {str(brend_good[0]).upper()+brend_good[1:]} {str(text1[0]).upper()+text1[1:]}\n<b>O'zgarishlar:</b>\n\n{txt}\n    <b>Narxi:</b>{count[callback][t]}"
    number = count[callback]['cnt']
    made = types.InlineKeyboardMarkup(row_width=1)
    made1 = types.InlineKeyboardButton(text = "➕ Mahsulot qo'shish ➕", callback_data=callback+'+')
    made2 = types.InlineKeyboardButton(text = f'{number}', callback_data='nothing')
    made3 = types.InlineKeyboardButton(text = "➖ Mahsulot chiqarish ➖", callback_data=callback+'-')
    menu = types.InlineKeyboardButton(text = '⚙️ Menu', callback_data='menu')
    made.add(made1, made2, made3, menu)
    bot.edit_message_text(text = text,
                        chat_id = chat_id,
                        message_id=call.message.id,
                        reply_markup=made)


def lg(call):
    chat_id = call.message.chat.id
    televizor_count = COUNTS['lg_televizor']['cnt']
    telefon_count = COUNTS['lg_telefon']['cnt']
    kir_count = COUNTS['lg_kir']['cnt']
    text = f"""📂 <b>Mahsulot brendi</b>: <i>LG</i>\nIltimos mahsulot turini tanlang\n1.<b>Televizor</b> -- {televizor_count} dona\n2.<b>Telefon</b> -- {telefon_count} dona\n2.<b>Kir yuvish mashinasi</b> -- {kir_count} dona"""
    made = types.InlineKeyboardMarkup(row_width=2)
    made1 = types.InlineKeyboardButton(text = 'Televizor', callback_data='lg_televizor*')
    made2 = types.InlineKeyboardButton(text = 'Telefon', callback_data='lg_telefon*')
    made3 = types.InlineKeyboardButton(text = 'Kir yuvish mashinasi', callback_data='lg_kir*')
    menu = types.InlineKeyboardButton(text = '⚙️ Menu', callback_data='menu')
    made.add(made1, made2)
    made.add(made3, menu, row_width=1)
    bot.edit_message_text(text=text,
                            chat_id = chat_id,
                            message_id=call.message.id,
                            reply_markup=made)

def shivaki(call):
    chat_id = call.message.chat.id
    televizor_count = COUNTS['shivaki_televizor']['cnt']
    telefon_count = COUNTS['shivaki_telefon']['cnt']
    kir_count = COUNTS['shivaki_kir']['cnt']
    text = f"""📂 <b>Mahsulot brendi</b>: <i>Shivaki</i>\nIltimos mahsulot turini tanlang\n1.<b>Televizor</b> -- {televizor_count} dona\n2.<b>Telefon</b> -- {telefon_count} dona\n2.<b>Kir yuvish mashinasi</b> -- {kir_count} dona"""
    made = types.InlineKeyboardMarkup(row_width=2)
    made1 = types.InlineKeyboardButton(text = 'Televizor', callback_data='shivaki_televizor*')
    made2 = types.InlineKeyboardButton(text = 'Telefon', callback_data='shivaki_telefon*')
    made3 = types.InlineKeyboardButton(text = 'Kir yuvish mashinasi', callback_data='shivaki_kir*')
    menu = types.InlineKeyboardButton(text = '⚙️ Menu', callback_data='menu')
    made.add(made1, made2)
    made.add(made3, menu, row_width=1)
    bot.edit_message_text(text=text,
                            chat_id = chat_id,
                            message_id=call.message.id,
                            reply_markup=made)


def artel(call):
    chat_id = call.message.chat.id
    televizor_count = COUNTS['artel_televizor']['cnt']
    telefon_count = COUNTS['artel_telefon']['cnt']
    kir_count = COUNTS['artel_kir']['cnt']
    text = f"""📂 <b>Mahsulot brendi</b>: <i>Artel</i>\nIltimos mahsulot turini tanlang\n1.<b>Televizor</b> -- {televizor_count} dona\n2.<b>Telefon</b> -- {telefon_count} dona\n2.<b>Kir yuvish mashinasi</b> -- {kir_count} dona"""
    made = types.InlineKeyboardMarkup(row_width=2)
    made1 = types.InlineKeyboardButton(text = 'Televizor', callback_data='artel_televizor*')
    made2 = types.InlineKeyboardButton(text = 'Telefon', callback_data='artel_telefon*')
    made3 = types.InlineKeyboardButton(text = 'Kir yuvish mashinasi', callback_data='artel_kir*')
    menu = types.InlineKeyboardButton(text = '⚙️ Menu', callback_data='menu')
    made.add(made1, made2)
    made.add(made3, menu, row_width=1)
    bot.edit_message_text(text=text,
                            chat_id = chat_id,
                            message_id=call.message.id,
                            reply_markup=made)


if __name__ == '__main__':
    bot.polling(non_stop=True)
    bot.infinity_polling()

