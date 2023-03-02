import config
from datetime import date, datetime
import telebot, time, sqlite3
from telebot import types, TeleBot

exstasy = imlive = secretfriends = mydirtyhobbies = islive = camcontacts = vxmodels = xmodels = jasmin = finmoney = time_send = rsumma = shtraf = review = 0
owner = 747983713
today = date.today()
first_day_month = date.today().replace(day=1)
starting_day_of_current_year = datetime.now().date().replace(month=1, day=1)
tconv = lambda x: time.strftime("%d.%m.%Y", time.localtime(x))# Конвертация даты в читабельный вид (Переменная time_send выводит в формате 09.06.2022)
bot = telebot.TeleBot(config.token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
conn = sqlite3.connect('payouts.db', check_same_thread=False, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()


def get_models_nickname():
    button_values_list = []
    cursor.execute(f"SELECT Nickname FROM Models WHERE Date BETWEEN '{starting_day_of_current_year}' AND '{today}' ")
    for i in set(cursor.fetchall()):
        button_values_list.append(i[0])
    return button_values_list


def db_table_val(date: date, nickname: str, money: str, comment: str):
    cursor.execute('INSERT INTO Models (date, nickname, money, comment) VALUES (?, ?, ?, ?)', (date, nickname, money, comment))
    conn.commit()


@bot.message_handler(func=lambda message: message.text == 'Указать заработок за день 💸') # При отправке "Указать заработок", начинается поочередный ввод данных пользователем, в переменные указанные в шапке
def money(message):
    send_mess = "Хорошо, давай посчитаем Exstasy (Euro): "
    bot.send_message(message.chat.id, send_mess, reply_markup=reject)
    bot.register_next_step_handler(message, vol1)
reject = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = types.KeyboardButton('Отменить')
reject.add(btn1)


def vol1(message):
    global exstasy
    text = message.text
    if text == 'Отменить':
        bot.send_message(message.from_user.id, "Хорошо, посчитаем позже 😋", reply_markup=markup)
    else:
        try:
            exstasy = float(message.text)
            bot.send_message(message.chat.id, "Спасибо, теперь ImLive (Dollar): ")
            bot.register_next_step_handler(message, vol2)
        except ValueError:
            bot.send_message(message.chat.id, "Не понимаю☹\nПопробуй использовать точку, например: 7.62")
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
            bot.send_message(message.chat.id, "Не понимаю☹\nПопробуй использовать точку, например: 7.62")
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
            bot.send_message(message.chat.id, "Не понимаю☹\nПопробуй использовать точку, например: 7.62")
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
            bot.send_message(message.chat.id, "Не понимаю☹\nПопробуй использовать точку, например: 7.62")
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
            bot.send_message(message.chat.id, "Не понимаю☹\nПопробуй использовать точку, например: 7.62")
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
            bot.send_message(message.chat.id, "Не понимаю☹\nПопробуй использовать точку, например: 7.62")
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
            bot.send_message(message.chat.id, "Не понимаю☹\nПопробуй использовать точку, например: 7.62")
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
            bot.send_message(message.chat.id, "Не понимаю☹\nПопробуй использовать точку, например: 7.62")
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
            bot.send_message(message.chat.id, "Не понимаю☹\nПопробуй использовать точку, например: 7.62")
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
        db_table_val(date=m_date, nickname=m_nick, money=str(m_money), comment=comment)
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
    cursor.execute(f"SELECT Money FROM Models WHERE Nickname = '{Nik}' AND Date BETWEEN '{first_day_month}' AND '{today}' ")
    records = cursor.fetchall()
    summa = sum(sum(records, ()))
    rsumma = round(summa)
    bot.send_message(message.from_user.id, "За этот месяц ты заработала: " + str(rsumma) + "$")


@bot.message_handler(func=lambda message: message.text == 'Мои штрафы')
def modelsmoney(message):
    global shtraf
    Nik = message.from_user.username
    cursor.execute(f"SELECT Money, Comment FROM Models WHERE Nickname = '{Nik}' AND Date BETWEEN '{first_day_month}' AND '{today}' AND Money < 0")
    records = cursor.fetchall()
    if records != []:
        for row in records:
            shtrafsend = (str(row[0]) + "$ " + str(row[1]))
            bot.send_message(message.from_user.id, shtrafsend)
    else: bot.send_message(message.from_user.id, 'У тебя нет штрафов и авансовых выплат')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    username = message.from_user.username
    if message.from_user.username == 'ibexstrt':
        bot.send_message(message.chat.id, "Привет Босс", reply_markup=admin)
    else:
        send_mess = f"Привет, {username}! Я твой личный помощник! Что будем делать?)"
        bot.send_message(message.chat.id, send_mess, reply_markup=markup)


admin = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) #Админ меню выводит кому назначить штраф и выводит список моделей в отдельные кнопки по уникальному Nickname
btn1 = types.KeyboardButton('Фиксация вывода/штрафы')
admin.add(btn1)
for nick in get_models_nickname():
        admin.add(nick)

#=====================================Фиксация вывода/штрафы=====================================#
@bot.message_handler(func=lambda message: message.text == "Фиксация вывода/штрафы")
def advance_deduction_step_1(message):
    sent = bot.send_message(message.from_user.id, "Сумма в $, например -72", reply_markup=reject)
    bot.register_next_step_handler(sent, advance_deduction_step_2)


def advance_deduction_step_2(message):
    global finance
    finance = message.text
    sent_2 = bot.send_message(message.from_user.id, "Комментарий к вычету")
    bot.register_next_step_handler(sent_2, advance_deduction_step_3)


def advance_deduction_step_3(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    for nick in get_models_nickname():
        user_markup.add(nick)
    bot.send_message(message.from_user.id, 'Выберите сотрудника', reply_markup=user_markup)
    # bot.delete_message(message.message.chat.id, message_id=review.id)  # Удаляем блок чтобы информацию нельзя было задублировать
    # db_table_val(date=today, nickname=m_nick, money=finance, comment=message.text)




#=====================================Фиксация вывода/штрафы=====================================#
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

def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


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


@bot.message_handler(func=lambda message: message.text == 'О штрафах')
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


@bot.message_handler(content_types=['text'])
def get_salary(message):
    global rsumma
    if message.from_user.username == 'ibexstrt':
        if message.text in get_models_nickname():
            cursor.execute(f"SELECT Money FROM Models WHERE Nickname = '{message.text}' AND Date BETWEEN '{first_day_month}' AND '{today}' ")
            records = cursor.fetchall()
            summa = sum(sum(records, ()))
            rsumma = round(summa)
            bot.send_message(message.from_user.id, message.text + " Заработала в этом месяце: " + str(rsumma) + "$")


bot.polling(none_stop=True)
