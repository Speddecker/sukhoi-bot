# -*- coding: utf-8 -*-

import config
import random
import telebot
from datetime import datetime, date, time, timedelta

#Даты недель "над" чертой
below = {"29.01.2018-04.02.2018",
		 "12.02.2018-18.02.2018",
		 "26.02.2018-04.03.2018",
		 "12.03.2018-18.03.2018",
		 "12.03.2018-18.03.2018",
		 "09.04.2018-15.04.2018",
		 "23.04.2018-29.04.2018",
		 "07.05.2018-13.05.2018",
		 "21.05.2018-27.05.2018",
		 "04.06.2018-10.06.2018"}

#Даты недель "под" чертой
under = {"26.01.2018-28.01.2018",
		 "05.02.2018-11.02.2018",
		 "19.02.2018-25.02.2018",
		 "05.03.2018-11.03.2018",
		 "19.03.2018-25.03.2018",
		 "02.04.2018-08.04.2018",
		 "16.04.2018-22.04.2018",
		 "30.04.2018-06.05.2018",
		 "14.05.2018-20.05.2018",
		 "28.05.2018-03.06.2018"}

#Расписание звонков
bells = {1:"8.00-9.30",
		 2:"9.45-11.15",
		 3:"11.25-12.55",
		 4:"13.25-14.55",
		 5:"15.05-16.35",
		 6:"16.50-18.20",
		 7:"18.30-20.00",
		 8:"20.30-22.00"}

#Список хороших ответов для русской рулетки
good_answer = ("Выдохни, Братишка! Впрочем, сессию ты не переживешь XD",
			   "Чисто повезло!",
			   "Ладно, живи пока...",
			   "Лучше б сдох",
			   "ДЕДПУЛА ЧТОЛЕ НАСМОТРЕЛСЯ, А?!?!?",
			   "Ты точно пистолет не разрядил?!",
			   "Можешь выйти и сменить свои бронетрусы. Они чёт развонялись!",
			   "Боги тебя полюбили. Наверно, ты их любимая зверушка :|",
			   "Ну если будешь долго играть, то точно сдохнешь!")

#Список плохих ответов для русской рулетки
bad_answer = ("Братишка, прости:( Нефиг патроны сувать куда не надо!",
			  "ТУПА ЛОХ!!!",
			  "Всё-таки раскинул мозгами... по аудитории...",
			  "Земля тебе пухом, Братишка!",
			  "Ну не повезло. С кем не бывает?!",
			  "Ну зато теперь ты не будешь сессию сдавать :/",
			  "Ну в принципе, если приложить подорожник... Не, хуйня!\nХотя... А нет, прости",
			  "Ну вот! Снова могилу копать :(",
			  "ДИМОООООООООООООООООООН ТУДУ ДУ ДУ ДУ ДУ ДУ ДУУУУУУУУУУУУ\nТУ ДУ ДУ ТУ ДУ ДУ ДУУУУУУУУУУУУУ")



def what_week():
    for it in below:
        left_border = datetime.strptime(it.split('-')[0], "%d.%m.%Y")
        right_border = datetime.strptime(it.split('-')[1], "%d.%m.%Y")

        if(datetime.today() < right_border and datetime.today() > left_border):
            return "Сейчас неделя 'над' чертой"

    for it in under:
        left_border = datetime.strptime(it.split('-')[0], "%d.%m.%Y")
        right_border = datetime.strptime(it.split('-')[1], "%d.%m.%Y")

        if(datetime.today() < right_border and datetime.today() > left_border):
            return "Сейчас неделя 'под' чертой"

def how_much_time():
	now = datetime.now()
	if (now.time() < time(8,0) or now.time() > time(22,0)):
		return "Отдыхай! Пар ещё нет!"

	for lesson, lesson_range in bells.items():
		lBorder = datetime.combine(now.date(), time(int(lesson_range.split('-')[0].split('.')[0]), int(lesson_range.split('-')[0].split('.')[1])))
		rBorder = datetime.combine(now.date(), time(int(lesson_range.split('-')[1].split('.')[0]), int(lesson_range.split('-')[1].split('.')[1])))
		
		if (now.time() >= lBorder.time() and now.time() <= rBorder.time()):
			return "До конца " + str(lesson) + " пары осталось: " + str(rBorder - now)
		
		if (now.time() <= lBorder.time()):
			return "До конца перемены осталось: " + str(lBorder - now)

def russian_roulette():
	if (random.randint(1,6) == random.randint(1,6)):
		return "*Бах*\n" + bad_answer[random.randint(0,8)]
	else:
		return "*Щёлк*\n" + good_answer[random.randint(0,8)]


#main
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["week"])
def week(message):
    bot.send_message(message.chat.id, what_week())

@bot.message_handler(commands=["roulette"])
def roulette(message):
    bot.send_message(message.chat.id, russian_roulette())

@bot.message_handler(commands=["timer"])
def timer(message):
    bot.send_message(message.chat.id, how_much_time())

if __name__ == '__main__':
        bot.polling(none_stop=True)
