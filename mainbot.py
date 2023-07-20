import openai
import re
import mysql.connector
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

openai.api_key = "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"
bot = Bot(token="5928007560:AAEOpXwJBRwytHsuvi2okRrykpnc1M84wqw")

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="17181920Ilya", database="TgBot")
cursor = connection.cursor(buffered=True)

class Form(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()
    question5 = State()
    question6 = State()
    name = State()
    phone = State()
    result = State()

mes1 = ""
mes2 = ""
mes3 = ""
mes4 = ""
mes5 = ""
mes6 = ""
mes7 = ""
mes8 = ""

@dp.message_handler(content_types=['text'])
async def bot_message(message: types.Message):
    if message.text == ("/start"):

        people_id = message.chat.id
        cursor.execute(f"SELECT user_id FROM middleprog WHERE user_id = {people_id};")
        data = cursor.fetchone()
        if data is None:
            user_id = [message.chat.id]
            cursor.execute("INSERT INTO middleprog (user_id) VALUES(%s);", user_id)
            connection.commit()

            cursor.execute("SELECT Начали FROM stat_middleprog;")
            statforone = cursor.fetchone()
            statone = statforone[0]
            cursor.execute(f"UPDATE stat_middleprog SET Начали = {statone + 1} WHERE Начали = {statone};")
            connection.commit()

            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_0 = types.KeyboardButton(text='Заполнить анкету (5 минут)')
            keyboard.add(button_0)
            await bot.send_message(message.chat.id, text="Доброго дня! Сейчас наша компания ТД \"МашЗавод\" ищет Junior разработчика на Python. Поэтому, предлагаем вам ответить на 6 небольших вопросов, чтобы мы могли рассмотреть вашу кандидатуру. Нажмите на кнопку ниже!", reply_markup=keyboard)

        else:
            cursor.execute(f"SELECT ОтветChatGpt FROM middleprog WHERE user_id = {people_id};")
            check = cursor.fetchone()
            if len(str(check[0])) > 1:
                await bot.send_message(message.chat.id, text="Анкету можно отправить только один раз. Она находится на проверке.")
                connection.commit()
            else:
                keyboardvar = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button_0 = types.KeyboardButton(text='Заполнить анкету (5 минут)')
                keyboardvar.add(button_0)
                await bot.send_message(message.chat.id, text="Заметили, что вы начали проходить анкету, но не сделали этого до конца. Начать заново можно по кнопке ниже:", reply_markup=keyboardvar)
                connection.commit()

    if message.text == 'Заполнить анкету (5 минут)':
        await Form.question1.set()
        keyboarddel = types.ReplyKeyboardRemove()
        await bot.send_message(message.chat.id, text="1. Какой у вас опыт программирования на Python и других языках?", reply_markup=keyboarddel)

@dp.message_handler(state=Form.question1)
async def bot_messages(message: types.Message, state: FSMContext):
    await Form.next()

    people_id = message.chat.id
    global mes1
    mes1 = f'"{str(message.text)}"'
    cursor.execute(f"UPDATE middleprog SET Вопрос1 = {mes1} WHERE user_id = {people_id};")
    connection.commit()

    await bot.send_message(message.chat.id, text="2. Как вы используете Python в своих проектах? Какими библиотеками пользовались ранее и для каких задач?")

@dp.message_handler(state=Form.question2)
async def bot_messages(message: types.Message, state: FSMContext):
    await Form.next()

    people_id = message.chat.id
    global mes2
    mes2 = f'"{str(message.text)}"'
    cursor.execute(f"UPDATE middleprog SET Вопрос2 = {mes2} WHERE user_id = {people_id};")
    connection.commit()

    await bot.send_message(message.chat.id, text="3. Как вы решаете проблемы производительности в Python? Расскажите, какие техники вы использовали для оптимизации кода и какие инструменты использовали для дебага.")

@dp.message_handler(state=Form.question3)
async def bot_messages(message: types.Message, state: FSMContext):
    await Form.next()

    people_id = message.chat.id
    global mes3
    mes3 = f'"{str(message.text)}"'
    cursor.execute(f"UPDATE middleprog SET Вопрос3 = {mes3} WHERE user_id = {people_id};")
    connection.commit()

    await bot.send_message(message.chat.id, text="4. Расскажите о вашем опыте работы с базами данных в Python. Какие СУБД использовали и какие проблемы решали?")

@dp.message_handler(state=Form.question4)
async def bot_messages(message: types.Message, state: FSMContext):
    await Form.next()

    people_id = message.chat.id
    global mes4
    mes4 = f'"{str(message.text)}"'
    cursor.execute(f"UPDATE middleprog SET Вопрос4 = {mes4} WHERE user_id = {people_id};")
    connection.commit()

    await bot.send_message(message.chat.id, text="5. Какие трудности вам пришлось преодолеть на данном этапе карьеры?")

@dp.message_handler(state=Form.question5)
async def bot_messages(message: types.Message, state: FSMContext):
    await Form.next()

    people_id = message.chat.id
    global mes5
    mes5 = f'"{str(message.text)}"'
    cursor.execute(f"UPDATE middleprog SET Вопрос5 = {mes5} WHERE user_id = {people_id};")
    connection.commit()

    await bot.send_message(message.chat.id, text="6. Обозначьте ваши сильные и слабые стороны относительно данной вакансии.")

@dp.message_handler(state=Form.question6)
async def bot_messages(message: types.Message, state: FSMContext):
    await Form.next()

    people_id = message.chat.id
    global mes6
    mes6 = f'"{str(message.text)}"'
    cursor.execute(f"UPDATE middleprog SET Вопрос6 = {mes6} WHERE user_id = {people_id};")
    connection.commit()

    await bot.send_message(message.chat.id, text="Введите Имя:")

@dp.message_handler(state=Form.name)
async def bot_messages(message: types.Message, state: FSMContext):
    await Form.next()

    people_id = message.chat.id
    name = f'"{str(message.text)}"'
    cursor.execute(f"UPDATE middleprog SET Имя = {name} WHERE user_id = {people_id};")
    connection.commit()

    await bot.send_message(message.chat.id, text="Введите свой номер телефона для обратной связи (с +7 или 8). Дается согласие на обработку персональных данных.")

@dp.message_handler(state=Form.phone)
async def bot_messages(message: types.Message, state: FSMContext):
    await Form.next()

    people_id = message.chat.id
    phonenum = f'"{str(message.text)}"'
    cursor.execute(f"UPDATE middleprog SET НомерТ = {phonenum} WHERE user_id = {people_id};")
    connection.commit()

    keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = types.KeyboardButton(text='Отправить на рассмотрение')
    button_4 = types.KeyboardButton(text='Вернуться в начало')
    keyboard3.add(button_3, button_4)
    await bot.send_message(message.chat.id, text="Если вы ответили на все вопросы, нажмите на кнопку отправки!", reply_markup=keyboard3)

@dp.message_handler(state=Form.result)
async def handler_message(message: types.Message, state: FSMContext):
    if message.text == 'Отправить на рассмотрение':
        uid = message.chat.id
        await state.finish()
        keyboarddel2 = types.ReplyKeyboardRemove()
        await bot.send_message(message.chat.id, text="Анкета отправлена! Мы рассмотрим вашу кандидатуру в течение дня. Предоставим обратную связь по указанному вами номеру телефона или WhatApp!", reply_markup=keyboarddel2)

        cursor.execute("SELECT Всего_анкет FROM stat_middleprog;")
        statfortwo = cursor.fetchone()
        stattwo = statfortwo[0]
        cursor.execute(f"UPDATE stat_middleprog SET Всего_анкет = {stattwo + 1} WHERE Всего_анкет = {stattwo};")
        connection.commit()

        async def markwrite(uid, mes1, mes2, mes3, mes4, mes5, mes6):

            messages = [
                {"role": "system",
                 "content": "Ты отдел кадров или HR. Твоя задача - нанять на работу Junior разработчика на языке программирования Python, чтобы он максимально точно соответствовал уровню Junior и выше. И уже использовал Базы Данных."},
                {"role": "user",
                 "content": "Отправлю тебе на оценку 6 вопросов с ответами от кандидата на вакансию Junior разработчика на языке Python. Твоя задача - максимально точно оценить его умения и профессионализм. И дать одну итоговую оценку уровня кандидата."},
                {"role": "assistant",
                 "content": "Хорошо, ожидаю 6 вопросов с ответами. И выставлю итоговую оценку в формате n баллов из 100 по соответствию профессионализма кандидата."},
            ]

            def update(messages, role, content):
                messages.append({"role": role, "content": content})
                return messages

            textforchat = ("Представь себя отделом кадров. Задача: найти компетентного Junior разработчика на языке программирования Python.\n"
                           "Кандидат прошёл анкетирование с помощью 6 вопросов ниже. Оцени всю анкету на профессионализм для вакансии Junior Python Разработчика в формате: n баллов из 100.\n\n"
                           "1. Какой у вас опыт программирования на Python и других языках?\n" + mes1 +
                           "\n\n2. Как вы используете Python в своих проектах? Какими библиотеками пользовались ранее и для каких задач?\n" + mes2 +
                           "\n\n3. Как вы решаете проблемы производительности в Python? Расскажите, какие техники вы использовали для оптимизации кода и какие инструменты использовали для дебага.\n" + mes3 +
                           "\n\n4. Расскажите о вашем опыте работы с базами данных в Python. Какие СУБД использовали и какие проблемы решали?\n" + mes4 +
                           "\n\n5. Какие трудности вам пришлось преодолеть на данном этапе карьеры?\n" + mes5 +
                           "\n\n6. Обозначьте ваши сильные и слабые стороны относительно данной вакансии.\n" + mes6)

            def handler_message(textforchat):

                update(messages, "user", textforchat)
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )

                textchatgpt = response['choices'][0]['message']['content']

                comment = f'"{textchatgpt}"'
                cursor.execute(f"UPDATE middleprog SET ОтветChatGpt = {comment} WHERE user_id = {uid};")
                connection.commit()

                stonum = []
                ournum = []

                estimate = re.findall(r'\d+', textchatgpt)

                for i in range(0, (len(estimate))):
                    if estimate[i] == '100':
                        stonum.append(i)
                        ournum.append(estimate[i - 1])

                resmark = int(ournum[0])
                print(resmark)
                cursor.execute(f"UPDATE middleprog SET Оценка = {resmark} WHERE user_id = {uid};")
                connection.commit()

                anketatrue = f'"Прошёл"'
                anketatrue2 = f'"Прошёл (c перепроверкой)"'
                anketafalse = f'"Не прошёл"'
                anketafalse2 = f'"Не прошёл (c перепроверкой)"'

                if (int(ournum[0]) >= 80 and len(estimate) > 2):
                    cursor.execute(f"UPDATE middleprog SET СледЭтап = {anketatrue2} WHERE user_id = {uid};")
                    connection.commit()

                    cursor.execute("SELECT На_перепроверку FROM stat_middleprog;")
                    statforfour = cursor.fetchone()
                    statfour = statforfour[0]
                    cursor.execute(f"UPDATE stat_middleprog SET На_перепроверку = {statfour + 1} WHERE На_перепроверку = {statfour};")
                    connection.commit()

                elif (int(ournum[0]) >= 80 and len(estimate) <= 2):
                    cursor.execute(f"UPDATE middleprog SET СледЭтап = {anketatrue} WHERE user_id = {uid};")
                    connection.commit()

                    cursor.execute("SELECT Прошли FROM stat_middleprog;")
                    statforthree = cursor.fetchone()
                    statthree = statforthree[0]
                    cursor.execute(f"UPDATE stat_middleprog SET Прошли = {statthree + 1} WHERE Прошли = {statthree};")
                    connection.commit()

                elif (int(ournum[0]) < 80 and len(estimate) > 2):
                    cursor.execute(f"UPDATE middleprog SET СледЭтап = {anketafalse2} WHERE user_id = {uid};")
                    connection.commit()

                    cursor.execute("SELECT На_перепроверку FROM stat_middleprog;")
                    statforfour = cursor.fetchone()
                    statfour = statforfour[0]
                    cursor.execute(f"UPDATE stat_middleprog SET На_перепроверку = {statfour + 1} WHERE На_перепроверку = {statfour};")
                    connection.commit()

                elif (int(ournum[0]) < 80 and len(estimate) <= 2):
                    cursor.execute(f"UPDATE middleprog SET СледЭтап = {anketafalse} WHERE user_id = {uid};")
                    connection.commit()

                    cursor.execute("SELECT Не_прошли FROM stat_middleprog;")
                    statforfive = cursor.fetchone()
                    statfive = statforfive[0]
                    cursor.execute(f"UPDATE stat_middleprog SET Не_прошли = {statfive + 1} WHERE Не_прошли = {statfive};")
                    connection.commit()

            handler_message(textforchat)

        await markwrite(uid, mes1, mes2, mes3, mes4, mes5, mes6)

    if message.text == 'Вернуться в начало':
        await state.finish()
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text='Заполнить анкету (5 минут)')
        keyboard.add(button_1)
        await bot.send_message(message.chat.id, text="Чтобы заново ответить на вопросы - нажмите на кнопку ниже!", reply_markup=keyboard)

executor.start_polling(dp, skip_updates=True)