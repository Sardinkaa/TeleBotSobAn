# Телеграм-бот v.002 - бот создаёт меню, присылает собачку, и анекдот

import telebot  # pyTelegramBotAPI	4.3.1
from telebot import types
import requests  # Требуется для "Прислать собаку"
import bs4  # требуется для get_anekdot()

bot = telebot.TeleBot('5140769396:AAFyJmEyB62p8Loitm_TvI2CYMNz5YTixB8')


# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке Пайтон".format(
                         message.from_user), reply_markup=markup)


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == "Вернуться в главное меню":  # ..........
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения")
        btn2 = types.KeyboardButton("WEB-камера")
        btn3 = types.KeyboardButton("Управление")
        btn3 = types.KeyboardButton("Домашка")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)
    elif ms_text == "Домашка":  # .............................................................................
        bot.send_message(chat_id, text=get_dz())
    elif ms_text == "Развлечения":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку")
        btn2 = types.KeyboardButton("Прислать анекдот")
        btn3 = types.KeyboardButton("Прислать слово")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)

    elif ms_text == "/dog" or ms_text == "Прислать собаку":  # .........................................................
        contents = requests.get('https://random.dog/woof.json').json()
        urlDOG = contents['url']
        bot.send_photo(chat_id, photo=urlDOG, caption="Вот тебе собачка!")

    elif ms_text == "Прислать слово":  # .............................................................................
        bot.send_message(chat_id, text=get_word())

    elif ms_text == "Прислать анекдот":  # .............................................................................
        bot.send_message(chat_id, text=get_anekdot())

    elif ms_text == "WEB-камера":
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Управление":  # ...................................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Помощь" or ms_text == "/help":  # .................................................................
        bot.send_message(chat_id, "Автор: Селиверстова Серафима")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/user59387")
        key1.add(btn1)
        img = open('Швец Андрей.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)

    else:  # ...........................................................................................................
        bot.send_message(chat_id, text="Я тебя слышу!!! Твое сообщение: " + ms_text)


# -----------------------------------------------------------------------
def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]


# -----------------------------------------------------------------------
def get_word():
    array_words = []
    req_anek = requests.get('http://sanstv.ru/randomWord/')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.words')
    for result in result_find:
        array_words.append(result.getText().strip())
    return array_words[0]


# -----------------------------------------------------------
# def get_dz():
# n1
# n = "Сима"
# bot.send_message(chat_id, text=n)
# n2
# age = 18
# n = "Сима"
# bot.send_message(chat_id, text="Я", n, "и мне", age, "лет")
# n3
# name = "Сима"
# n = name+name+name+name+name
# bot.send_message(chat_id, text=n)
# n4
# bot.send_message(chat_id, text="Как тебя зовут?")
# n = input()
# bot.send_message(chat_id, text="Сколько тебе лет?")
# age = input()
# print("Привет,", n + "!", "Ну ты и старпер!")
# n5
# print("Сколько тебе лет?")
# age = int(input())
# if age <= 5:
#     print("Да ты еще даже читать не умеешь!")
# if (age >=6) and (age <= 17):
#     print("Сначала школу окончи")
# if (age >= 18) and (age <= 55):
#     print("Работа - шутка для тебя?")
# if age >= 56:
#     print("Ого! Какой же ты старый!")
# n6
# print("Как тебя зовут?")
# n = input()
# k = " "
# m = " "
# for i in range(1,len(n)-1):
#     k = k + n[i]
# print(k)
# p = n[::-1]
# print(p)
# l = n[len(n)-3] + n[len(n)-2] + n[len(n)-1]
# print(l)
# m = n[0] + n[1] + n[2] + n[3] + n[4]
# print(m)
# n7
# n = input()
# age = int(input())
# l = len(n)
# a = age // 10
# b = age % 10
# print(l,a+b,a*b)
# n8
# n = input()
# lowerstring = n.lower()
# print(lowerstring)
# upperstring = n.upper()
# print(upperstring)
# capitalize = n.capitalize()
# print(capitalize)
# c = capitalize.swapcase()
# print(c)
# n9
# print("веди имя")
# n = input()
# print("введи возраст")
# age = input()
# k = " "
# for i in range((len(n)-1)):
#     if n[i] == k
#         print("ты читать не умеешь?")
#     if (a < 0) or (a > 150)
#         print("не ври")
# n10
# print("Реши задачку: 7 * 5 + 9")
# k = input()
# if k != 44:
#     print("лошара")
# else:
#     print("красава")


# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)  # Запускаем бота

print()
