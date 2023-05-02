import time

import telebot
from telebot import types
import random
import os


# bot initialization with user telegram token
bot = telebot.TeleBot(token='Your_token')

# add some buttons
keyboard_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn = types.KeyboardButton('Хочу котика!')

# show this buttons
keyboard_markup.add(btn)

# list of names for photos
names = ['Вайт', 'Сноу', 'Хмарка', 'Сніжок', 'Пушинка', 'Бланш', 'Білик', 'Кефірчик', 'Асія', 'Агата', 'Зефірка', 'Адам',
         'Айзек', 'Алан', 'Айс', 'Альфред', 'Аміго', 'Амур', 'Степан', 'Аполон', 'Арчі', 'Арнольд', 'Ахіл', 'Артур',
         'Аскольд', 'Кафка', 'Барні', 'Бартон', 'Барон', 'Бенедикт', 'Бернард', 'Блейк', 'Бонд', 'Боря', 'Ватсон',
         'Версаль', 'Васька', 'Габл', 'Гамлет', 'Гарольд', 'Гектор', 'Герцог', 'Гоша', 'Граф', 'Грегор', 'Густаф',
         'Грім', 'Давид', 'Джин', 'Дакстер', 'Донателло', 'Франко', 'Дарлінг', 'Декстре', 'Пейсик', 'Джек',
         'Діма', 'Дональд', 'Девід', 'Дункан', 'Жак', 'Женя', 'Жора', 'Макс', 'Зорро', 'Ікар', 'Ірон', 'Іствуд', 'Кай',
         'Карлос', 'Каспер', 'Квентін', 'Клайд', 'Клео', 'Конфуцій', 'Крістіант', 'Кузьма', 'Кузя', 'Лакі', 'Ламберт',
         'Лео', 'Леонардо', 'Леопольд', 'Локкі', 'Людвіг', 'Лютер', 'Майк', 'Макс', 'Мамай', 'Маріо', 'Марсель', 'Марк',
         'Мартін', 'Матіас', 'Маузер', 'Мерлін', 'Мебіус', 'Мойсей', 'Монті', 'Морфей', 'Моцарт', 'Найт', 'Наполеон',
         'Натан', 'Нельсон', 'Немо', 'Нео', 'Нестор', 'Норман', 'Ньютон', 'Обелікс', 'Обормот', 'Онікс', 'Орест',
         'Оскар', 'Остап', 'Отелло', 'Акорд', 'Алтай', 'Алмаз', 'Альянс', 'Амазон', 'Амстердам', 'Ампер', 'Апач',
         'Атом', 'Ахтунг', 'Бабай', 'Базальт', 'Байт', 'Банзай', 'Бейсік', 'Бісквіт', 'Бінг', 'Бластер', 'Бруклін',
         'Вегас', 'Вольт', 'Вулкан', 'Гайд', 'Гендальф', 'Дарт Вейдер', 'Десерт', 'Джаз', 'Джедай', 'Діамант',
         'Диктатор', 'Джокер', 'Доманітор', 'Дюшес', 'Живчик', 'Зеніт', 'Зефір', 'Зеро', 'Зодіак', 'Хвостик', 'Імбир',
         'Імпульс', 'Ірис', 'Йода', 'Йогурт', 'Кагор', 'Кварц', 'Квест', 'Кексик', 'Кілер', 'Князь', 'Ковбой', 'Кокос',
         'Конкорд', 'Консул', 'Лаваш', 'Лайм', 'Лапа', 'Лотос', 'Магнат', 'Мажор', 'Майор', 'Мандарин', 'Марс',
         'Мармелад', 'Мілан', 'Міксер', 'Міраж', 'Мурзик', 'Мурчик', 'Мяус', 'Нептун', 'Няха', 'Окей', 'Оріон',
         'Осіріс', 'Охламон', 'Паладін', 'Персик', 'Піксель', 'Плінтус', 'Протон', 'Пузо', 'Пухлик', 'Радар',
         'Рефлекс', 'Рубін', 'Рижик', 'Салют', 'Сатурн', 'Саурон', 'Сенатор', 'Сідней', 'Скаут', 'Сніжок', 'Тайфун',
         'Туман', 'Тюльпан', 'Фаворит', 'Флаєр', 'Федерал', 'Фенікс', 'Фокус', 'Форвард', 'Хаос', 'Хвостик', 'Цезар',
         'Цитрус', 'Челенджер', 'Чикаго', 'Чудік', 'Шалфей', 'Шаман', 'Шатун', 'Шнурок', 'Шредер', 'Шторм',
         'Шухер', 'Юпітер']

# name counter for image naming
id = 0


def start(message):
    bot.send_message(message.from_user.id, text="❤", reply_markup=keyboard_markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # help for all hidden command
    if message.text == "/help":
        bot.send_message(message.from_user.id, "/load_cute - для загрузки коциків (бажано фото соло котиків))")
    elif message.text == "Хочу котика!":
        # create list names of images
        directory = './images'
        files = os.listdir(directory)
        #  if in folder is no photos return:
        if not len(files):
            bot.send_message(message.from_user.id, "У ящичку з котиками закінчились котики =(,"
                                                   " звернись до Маска - нехай ворушить задом)")

        else:
            # take one random image name
            random_image = random.choice(files)

            img = open(f'./images/{random_image}', 'rb')
            bot.send_photo(message.chat.id, img)
            img.close()
            ran_name = random.choice(names)
            bot.send_message(message.from_user.id, f"Котик {ran_name} special for Валя)")
            # delete image
            os.remove(f'./images/{random_image}')

    elif message.text == "/load_cute":
        @bot.message_handler(content_types=['photo'])
        def download_image(message):
            global id
            # get original size photo
            fileID = message.photo[-1].file_id
            # generate id
            file_info = bot.get_file(fileID)
            # download photo
            downloaded_file = bot.download_file(file_info.file_path)
            # save photo
            directory2 = './images'
            files2 = os.listdir(directory2)
            for elem in files2:
                x = f"image{id}.jpg"
                if elem == x:
                    id += 1
            with open(f"image{id}.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, f"Коцика успішно інтегровано в систему: image{id}.jpg")
            # replace photo to needed dir
            os.replace(src=f"image{id}.jpg", dst=f'./images/image{id}.jpg')
            id += 1

    else:
        bot.send_message(message.from_user.id, "Привіт, Сонце) Якщо тобі сумно і хочеш няшного котика,"
                                               " а я про це і не підозрюю, нажми на кнопочку нижче)",
                         reply_markup=keyboard_markup)


# eternal cycle with update of incoming messages
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        time.sleep(15)

# another variant of polling
# bot.polling(none_stop=True, timeout=123)
