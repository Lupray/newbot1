import telebot
import time
bot = telebot.TeleBot("814281909:AAHYOzJLPUNk8LUYRiUfsxBNNN31BTPzkVM")
@bot.message_handler(commands=['monday', 'pon', '1', 'first', 'mon'])
def command_help(message):
    bot.reply_to(message, '''_________________Понедельник_______________
     1 Подгрупа:                                   2 Подгрупа:
     1 Пара: английский язык        |1 Пара: Нету
           2 Пара: Модульная контрольная по английскому
     3 Пара: Нету                                 |3 Пара: Англ.
     4 Пара: Нету                                 |4 Пара: Нету''')
@bot.message_handler(commands=['tuesday', 'second', 'tue', '2'])
def command_help(message):
    bot.reply_to(message, '''_________________Вторник_______________
     1 Подгрупа:                                   2 Подгрупа:
     1 Пара:         Геометрія практична робота
     2 Пара:              Геометрія лекція
     3 Пара:      Вища математика практична робота
     4 Пара:             Физкультура                            ''')
@bot.message_handler(commands=['wednesday', 'third', 'wed', '3'])     
def command_help(message):
    bot.reply_to(message, '''_________________Середа_______________
     1 Подгрупа:                                   2 Подгрупа:
     1 Пара: ФПВОС                            |1 Пара: АОС лз
     2 Пара: ФПВОС                            |2 Пара: АОС лз
     3 Пара: Нету                                 |3 Пара: Нету
     4 Пара: Нету                                 |4 Пара: Нету''')
@bot.message_handler(commands=['thursday', 'forth', 'thur', '4'])     
def command_help(message):
    bot.reply_to(message, '''_________________Четверг_______________
     1 Подгрупа:                                   2 Подгрупа:
     1 Пара: НЕТУ                              |1 Пара: НЕТУ
     2 Пара: Університетські студії: вступ до спеціальності
     3 Пара:                 Вища матемтика л.
     4 Пара:                    Я студент                            ''')
@bot.message_handler(commands=['friday', 'fifht', 'fr', '5'])     
def command_help(message):
    bot.reply_to(message, '''_________________Пятниця_______________
     1 Подгрупа:                                   2 Подгрупа:
     1 Пара:  Вступ до спеціальності
     2 Пара:  Вступ до спеціальності на всі групи
     3 Пара:  Лідерствослужіння
     4 Пара: Нету                                 |4 Пара: Нету''')
@bot.message_handler(commands=['help@inb_bot', 'commands', 'hlp', ])     
def command_help(message):
    bot.reply_to(message, '''Команды:
    Понедельник: 1, mon, monday
    Вторник: 2, tue, thuesday
    Среда: 3, wednesday, wed
    Четверг: 4, thursay, thur
    Пятница: 5, friday, fr''')



bot.polling(none_stop=True)


