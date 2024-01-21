from os import name
from funcs import new_quiz, generate_options_keyboard, get_question, update_quiz_index, get_quiz_index, create_table, new_user
import asyncio
import logging
from aiogram import Dispatcher, Bot, types
from aiogram.filters.command import Command
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from quiz_data import quiz_data
import aiosqlite

logging.basicConfig(level=logging.INFO)

API_TOKEN = '#################################'

bot= Bot(API_TOKEN)

dp=Dispatcher()




@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Создаем сборщика клавиатур типа Reply
    builder = ReplyKeyboardBuilder()
    # Добавляем в сборщик одну кнопку
    builder.add(types.KeyboardButton(text="Начать игру"))
    builder.add(types.KeyboardButton(text="Статистика"))
    # Прикрепляем кнопки к сообщению
    await message.answer("Добро пожаловать в квиз!", reply_markup=builder.as_markup(resize_keyboard=True))
    await create_table()
    



@dp.message(F.text=="Начать игру")
@dp.message(Command("quiz"))
async def cmd_quiz(message: types.Message):
    user_id=message.from_user.id
    # Отправляем новое сообщение без кнопок
    await message.answer(f"Давайте начнем квиз!")
    # Запускаем новый квиз
    await new_quiz(message)
    await new_user(message)
    async with aiosqlite.connect('quiz_bot.db') as db:
        # Обновление данных в таблице quiz_results
        await db.execute('''
            UPDATE quiz_results
            SET right_answ_total = 0
            WHERE user_id = ?
        ''', (user_id,))
        await db.commit()
    



@dp.callback_query()
async def answer(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id, 
        message_id=callback.message.message_id, 
        reply_markup=None
    )
    user_id=callback.from_user.id
    
    current_question_index=await get_quiz_index(callback.from_user.id)

    correct_option=quiz_data[current_question_index]['correct_option']

    if callback.data=="right_answer":
        async with aiosqlite.connect('quiz_bot.db') as db:
        # Обновление данных в таблице quiz_results
            await db.execute('''
                UPDATE quiz_results
                SET right_answ_total = right_answ_total + 1 
                WHERE user_id = ?
            ''', (user_id,))
            await db.commit()

        await callback.message.answer(quiz_data[current_question_index]['options'][correct_option])
        await callback.message.answer("Верно!")
    else:
        await callback.message.answer(callback.data)
        await callback.message.answer(f"Неправильно. Правильный ответ: {quiz_data[current_question_index]['options'][correct_option]}")

    current_question_index+=1
    await update_quiz_index(callback.from_user.id, current_question_index)

    # Проверяем достигнут ли конец квиза
    if current_question_index < len(quiz_data):
        # Следующий вопрос
        await get_question(callback.message, callback.from_user.id)
    else:
        # Уведомление об окончании квиза
        await callback.message.answer("Это был последний вопрос. Квиз завершен!")  



# Обработчик команды /stats
@dp.message(Command('stats'))
@dp.message(F.text=='Статистика')
async def stats_command(message: types.Message):
    user_id = message.from_user.id
    async with aiosqlite.connect('quiz_bot.db') as db:
        # Получение статистики из таблицы quiz_results
        stats = await db.execute('''
            SELECT username, right_answ_total
            FROM quiz_results
            WHERE user_id = ?
        ''', (user_id,))
        stats = await stats.fetchone()

        if stats:
            stats_message = f"Статистика для {stats[0]}:\n"
            stats_message += f"Правильных ответов: {stats[1]}"
            await message.answer(stats_message)
        else:
            await message.answer("Ошибка при получении статистики.")



async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())
    
