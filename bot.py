import config
import cherrypy
import telebot
from datetime import date
import telebot, time, sqlite3
from telebot import types, TeleBot


WEBHOOK_HOST = '37.46.129.233'
WEBHOOK_PORT = 8443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (config.token)


bot = telebot.TeleBot(config.token)

# Наш вебхук-сервер
class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)



#тестовый коммент1
exstasy = 0
imlive = 0
secretfriends = 0
mydirtyhobbies = 0
islive = 0
camcontacts = 0
vxmodels = 0
xmodels = 0
jasmin = 0
finmoney = 0
time_send = 0
rsumma = 0
shtraf = 0
owner = 747983713
review = 0


today = date.today()
firstday = date.today().replace(day=1)


conn = sqlite3.connect('payouts.db', check_same_thread=False, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()


def db_table_val(date: date, nickname: str, money: str, comment: str):
    cursor.execute('INSERT INTO Models (date, nickname, money, comment) VALUES (?, ?, ?, ?)', (date, nickname, money, comment))
    conn.commit()


tconv = lambda x: time.strftime("%d.%m.%Y", time.localtime(x))# Конвертация даты в читабельный вид (Переменная time_send выводит в формате 09.06.2022)


@bot.message_handler(func=lambda message: message.text == 'Указать заработок за день 💸') # При отправке "Указать заработок", начинается поочередный ввод данных пользователем, в переменные указанные в шапке
def money(message):
    send_mess = "Хорошо, давай посчитаем Exstasy (Euro): "
    bot.send_message(message.chat.id, send_mess, reply_markup=reject)
    bot.register_next_step_handler(message, vol1)


def vol1(message):
    global exstasy
    text = message.text
    if text == 'Отменить':
        bot.send_message(message.from_user.id, "Переход в главное меню...", reply_markup=markup)
    else:
        try:
            exstasy = float(message.text)
            bot.send_message(message.chat.id, "Спасибо, теперь ImLive (Dollar): ")
            bot.register_next_step_handler(message, vol2)
        except ValueError:
            bot.send_message(message.chat.id, "Похоже ты ввела ( , ) вместо ( . ) Исправь пожалуйста")
            bot.register_next_step_handler(message, vol1)


def vol2(message):
    global imlive
    text = message.text
    if text == 'Отменить':
        bot.send_message(message.from_user.id, "Переход в главное меню...", reply_markup=markup)
    else:
        try:
            imlive = float(message.text)
            bot.send_message(message.chat.id, "Спасибо, теперь MyDirtyHobbies (Euro): ")
            bot.register_next_step_handler(message, vol3)
        except ValueError:
            bot.send_message(message.chat.id, "Похоже ты ввела ( , ) вместо ( . ) Исправь пожалуйста")
            bot.register_next_step_handler(message, vol2)


def vol3(message):
    global mydirtyhobbies
    text = message.text
    if text == 'Отменить':
        bot.send_message(message.from_user.id, "Переход в главное меню...", reply_markup=markup)
    else:
        try:
            mydirtyhobbies = float(message.text)
            bot.send_message(message.chat.id, "Спасибо, теперь IsLive (Euro): ")
            bot.register_next_step_handler(message, vol4)
        except ValueError:
            bot.send_message(message.chat.id, "Похоже ты ввела ( , ) вместо ( . ) Исправь пожалуйста")
            bot.register_next_step_handler(message, vol3)


def vol4(message):
    global islive
    text = message.text
    if text == 'Отменить':
        bot.send_message(message.from_user.id, "Переход в главное меню...", reply_markup=markup)
    else:
        try:
            islive = float(message.text)
            bot.send_message(message.chat.id, "Спасибо, теперь CamContacts (Dollar): ")
            bot.register_next_step_handler(message, vol5)
        except ValueError:
            bot.send_message(message.chat.id, "Похоже ты ввела ( , ) вместо ( . ) Исправь пожалуйста")
            bot.register_next_step_handler(message, vol4)


def vol5(message):
    global camcontacts
    text = message.text
    if text == 'Отменить':
        bot.send_message(message.from_user.id, "Переход в главное меню...", reply_markup=markup)
    else:
        try:
            camcontacts = float(message.text)
            bot.send_message(message.chat.id, "Спасибо, теперь VxModels (Euro): ")
            bot.register_next_step_handler(message, vol6)
        except ValueError:
            bot.send_message(message.chat.id, "Похоже ты ввела ( , ) вместо ( . ) Исправь пожалуйста")
            bot.register_next_step_handler(message, vol5)


def vol6(message):
    global vxmodels
    text = message.text
    if text == 'Отменить':
        bot.send_message(message.from_user.id, "Переход в главное меню...", reply_markup=markup)
    else:
        try:
            vxmodels = float(message.text)
            bot.send_message(message.chat.id, "Спасибо, теперь Xmodels (Dollar): ")
            bot.register_next_step_handler(message, vol7)
        except ValueError:
            bot.send_message(message.chat.id, "Похоже ты ввела ( , ) вместо ( . ) Исправь пожалуйста")
            bot.register_next_step_handler(message, vol6)


def vol7(message):
    global xmodels
    text = message.text
    if text == 'Отменить':
        bot.send_message(message.from_user.id, "Переход в главное меню...", reply_markup=markup)
    else:
        try:
            xmodels = float(message.text)
            bot.send_message(message.chat.id, "Спасибо, теперь JasminLive (Dollar): ")
            bot.register_next_step_handler(message, vol8)
        except ValueError:
            bot.send_message(message.chat.id, "Похоже ты ввела ( , ) вместо ( . ) Исправь пожалуйста")
            bot.register_next_step_handler(message, vol7)


def vol8(message):
    global jasmin
    text = message.text
    if text == 'Отменить':
        bot.send_message(message.from_user.id, "Переход в главное меню...", reply_markup=markup)
    else:
        try:
            jasmin = float(message.text)
            bot.send_message(message.chat.id, "Спасибо, теперь SecretFriends (Credits): ")
            bot.register_next_step_handler(message, vol9)
        except ValueError:
            bot.send_message(message.chat.id, "Похоже ты ввела ( , ) вместо ( . ) Исправь пожалуйста")
            bot.register_next_step_handler(message, vol8)


def vol9(message):
    global secretfriends
    global time_send
    global review
    text = message.text
    if text == 'Отменить':
        bot.send_message(message.from_user.id, "Переход в главное меню...", reply_markup=markup)
    else:
        try:
            secretfriends = float(message.text)
            keyboard = types.InlineKeyboardMarkup()
            key_send = types.InlineKeyboardButton(text="Отправить", callback_data="send")
            keyboard.add(key_send)
            key_edit = types.InlineKeyboardButton(text="Редактировать", callback_data="edit")
            keyboard.add(key_edit)
            end_vol = "Все верно?\n" + "\nExstasy: " + str(exstasy) + (" €")  + "\nImLive: " + str(imlive) + (" €") + "\nMyDirtyHobbies: " + str(mydirtyhobbies) + (" €") + "\nIsLive: " + str(islive) + (" €") + "\nCamContacts: " + str(camcontacts) + (" $") + "\nVxModels: " + str(vxmodels) + (" €") + "\nXmodels: " + str(xmodels) + (" $") + "\nSecretFriends: " + str(secretfriends) + (" Credits") + "\nJasminLive: " + str(jasmin) + (" $")
            review = bot.send_message(message.from_user.id, text=end_vol, reply_markup=keyboard)
            time_send = tconv(message.date)
        except ValueError:
            bot.send_message(message.chat.id, "Похоже ты ввела ( , ) вместо ( . ) Исправь пожалуйста")
            bot.register_next_step_handler(message, vol8)


@bot.callback_query_handler(func=lambda call: True)# Обработчик функции callback_data после ответа (Отправить) или (Редактировать)
def callback_worker(call):
    global finmoney
    if call.data == "send":
        sendler = call.from_user.username
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Статистика успешно отправлена")
        bot.send_message(owner, "Пришла статистика от: " + str(sendler))
        secretfriendsdollar = int(secretfriends) / 2
        finmoney = float(exstasy) + float(imlive) + float(mydirtyhobbies) + float(islive) + float(secretfriendsdollar) + float(camcontacts) + float(vxmodels) + float(xmodels) + float(jasmin)
        modelsmoney = float(finmoney) / 2
        rmodelsmoney = round(modelsmoney)
        bot.send_message(call.from_user.id, "Поздравляю, за сегодня ты заработала: " + str(rmodelsmoney) + "$", reply_markup=markup)
        m_date = today
        m_nick = call.from_user.username
        m_money = rmodelsmoney
        comment = "null"
        db_table_val(date=m_date, nickname=m_nick, money=m_money, comment=comment)
        bot.delete_message(call.message.chat.id, message_id=review.id) # Удаляем блок чтобы информацию нельзя было задублировать
    elif call.data == "edit":
        bot.answer_callback_query(call.id) # Ответ клиентскому приложению что информация получена
        bot.delete_message(call.message.chat.id, message_id=review.id) # Удаляем блок чтобы информацию нельзя было задублировать
        bot.send_message(call.message.chat.id, "Хорошо, заполним данные заново")
        send_mess = "Давай посчитаем Exstasy ✏: "
        bot.send_message(call.message.chat.id, send_mess)
        bot.register_next_step_handler(call.message, vol1)


@bot.message_handler(func=lambda message: message.text == 'Моя зарплата 💰')
def modelsmoney(message):
    global rsumma
    Nik = message.from_user.username
    cursor.execute(f"SELECT Money FROM Models WHERE Nickname = '{Nik}' AND Date BETWEEN '{firstday}' AND '{today}' ")
    records = cursor.fetchall()
    summa = sum(sum(records, ()))
    rsumma = round(summa)
    bot.send_message(message.from_user.id, "За этот месяц ты заработала: " + str(rsumma) + "$")


@bot.message_handler(func=lambda message: message.text == 'Мои штрафы')
def modelsmoney(message):
    global shtraf
    Nik = message.from_user.username
    cursor.execute(f"SELECT Money, Comment FROM Models WHERE Nickname = '{Nik}' AND Date BETWEEN '{firstday}' AND '{today}' AND Money < 0")
    records = cursor.fetchall()
    for row in records:
        shtrafsend = (str(row[0]) + "$ за " + str(row[1]))
        print(shtrafsend)
        bot.send_message(message.from_user.id, shtrafsend)


admin = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)# Вывод заработной платы моделей для Администратора
btn1 = types.KeyboardButton('Ирина Худякова')
btn2 = types.KeyboardButton('Ольга Клебан')
btn3 = types.KeyboardButton('Выписать штраф')
admin.add(btn1, btn2, btn3)


reject = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton('Отменить')
reject.add(btn1)

# @bot.message_handler(func=lambda message: message.text == "Выписать штраф")
# def ticket(message, settings=None):
#     keyboard = types.InlineKeyboardMarkup()
#     key_mod1 = types.InlineKeyboardButton(text="Ирина Худякова", callback_data="Aarriiaannaz")
#     keyboard.add(key_mod1)
#     bot.send_message(message.from_user.id, "Выбери имя модели", reply_markup=keyboard)
#     bot.register_next_step_handler(message.from_user.id, zn1)
#
# def zn1(message):
#     bot.send_message(message.from_user.id, "Впиши сумму на которую модель будет оштрафована")
#     m_money = message.text
#
#
#     m_date = today
#     m_nick = message.from_user.id
#     bot.send_message(message.from_user.id, "Впиши сумму на которую модель будет оштрафована")
#     m_money = message.text
#     comentariy = "Прогуляла работу"
#     db_table_val(date=m_date, nickname=m_nick, money=m_money, comment=comentariy)


@bot.message_handler(func=lambda message: message.text == "Ирина Худякова")
def ikhudakova(message):
    global rsumma
    cursor.execute(f"SELECT Money FROM Models WHERE Nickname = 'Aarriiaannaz' AND Date BETWEEN '{firstday}' AND '{today}' ")
    records = cursor.fetchall()
    summa = sum(sum(records, ()))
    rsumma = round(summa)
    bot.send_message(message.from_user.id, "Ирина заработала в этом месяце: " + str(rsumma) + "$")


@bot.message_handler(func=lambda message: message.text == "Ольга Клебан")
def kleban(message):
    global rsumma
    cursor.execute(f"SELECT Money FROM Models WHERE Nickname = 'OlgaKleban' AND Date BETWEEN '{firstday}' AND '{today}' ")
    records = cursor.fetchall()
    summa = sum(sum(records, ()))
    rsumma = round(summa)
    bot.send_message(message.from_user.id, "Оля заработала в этом месяце: " + str(rsumma) + "$")


@bot.message_handler(func=lambda message: message.text == "Ирина Худякова")
def shtraf(message):
    global shtraf
    cursor.execute(f"SELECT Money FROM Models WHERE Nickname = 'Aarriiaannaz' AND Date BETWEEN '{firstday}' AND '{today}' ")
    records = cursor.fetchall()
    summa = sum(sum(records, ()))
    rsumma = round(summa)
    bot.send_message(message.from_user.id, "Ирина заработала в этом месяце: " + str(rsumma) + "$")


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton('Указать заработок за день 💸')
btn2 = types.KeyboardButton('Узнать о бонусах 🍀')
btn3 = types.KeyboardButton('FAQ ❓')
btn4 = types.KeyboardButton('Моя зарплата 💰')
markup.add(btn1, btn2, btn3, btn4)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton('Можно ли курить перед камерой?')
btn2 = types.KeyboardButton('Я плохо знаю английский, что делать?')
btn3 = types.KeyboardButton('Хочу уйти на удаленную работу')
btn4 = types.KeyboardButton('О штрафах')
btn5 = types.KeyboardButton('Мои штрафы')
btn6 = types.KeyboardButton('Назад')
markup3.add(btn1, btn2, btn3, btn4, btn5, btn6)


@bot.message_handler(commands=['start', 'help'])
def start(message, settings=None):
    username = message.from_user.username
    if message.from_user.username == 'ibexstrt':
        bot.send_message(message.chat.id, "Привет Босс", reply_markup=admin)
    else:
        send_mess = f"Привет, {username}! Я твой личный помощник! Что будем делать?)"
        bot.send_message(message.chat.id, send_mess, reply_markup=markup)
        keyboard = types.InlineKeyboardMarkup()


@bot.message_handler(func=lambda message: message.text == 'FAQ ❓')
def foo(message):
    send_mess = "Что тебя интересует?"
    bot.send_message(message.chat.id, send_mess, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Можно ли курить перед камерой?')
def foo2(message):
    final_message = "К сожалению не все сайты одобряют курение моделей перед камерой, а так как наша работа заключена на нескольких сайтах одновременно, то курить перед камерой становится строго запрещено!"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Я плохо знаю английский, что делать?')
def foo3(message):
    final_message = "Не переживай если тебе приходится много отвлекаться на переводчик, в скором времени у нас в штате будет преподаватель Английского языка, он будет заниматься и обучать нас основам, чтоб бы тебе было комфортно отвечать на банальные вопросы и общаться с несколькими мемберами сразу!"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Хочу уйти на удаленную работу')
def foo4(message):
    final_message = "Мы с радостью поддерживаем моделей, которые хотят уйти на удаленную работу и не тратить время на поездки в студию. Но чтобы уйти работать удаленно, тебе необходимо выполнить несколько обязательных пунктов: \n 1. Опыт работы на студии Muskad от 1 года и более \n 2. Дома есть оборудованное место (Хотя бы хороший свет и яркая привлекательная комната, ноутбук и камеру мы можем дать в аренду)"
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Штрафы')
def foo5(message):
    final_message = "Прогул рабочего дня наказывается штрафом, как бы сурово это не было, выгоду теряете не только вы. Штраф расчитывается индивидуально и составляет от 3 000р до 6 000р в сутки. Прогул по уважительной причине (есть справка), штрафом не облагается."
    bot.send_message(message.chat.id, final_message, reply_markup=markup3)


@bot.message_handler(func=lambda message: message.text == 'Назад')
def foo6(message):
    final_message = "Главное меню"
    bot.send_message(message.chat.id, final_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Узнать о бонусах 🍀")
def foo7(message):
    final_message = "У нас действует предложение, если твоя подруга хочет вступить к нам в команду, то мы с радостью рассмотрим ее кандидатуру, а тебе будет положен бонус 5 000₽. Но есть одно условие, твоя подруга должна пройти испытательный срок равный 1 месяцу. "
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


# Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)
bot.remove_webhook()


# Ставим заново вебхук
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Указываем настройки сервера CherryPy
cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

 # Собственно, запуск!
cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})
