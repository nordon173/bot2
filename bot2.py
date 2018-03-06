import telebot
import os
import random


token="554192076:AAG_LTd1yE2rrDle0Z_JRvHAKLVZPvoVKGs"
bot=telebot.TeleBot(token)

#bot.send_message(258340140,"testik")

#upd=bot.get_updates()

#last_upd=upd[-1]
#message_from_user=last_upd.message

#print(message_from_user)
@bot.message_handler(commands = ['zagadki'])
def knopk(message):
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row('Загадка 1','Загадка 2','Загадка 3')
    bot.send_message(message.from_user.id,'Добро пожаловать',reply_markup=markup)
@bot.message_handler(commands=['dopzadacha'])
def dop(message):
    directory = "C:\\Users\\User\\Pictures\\Вова\\Снимок.PNG"
    img1 = open(directory, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img1)
    img1.close()

@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.from_user.id,'Для ввывода кнопок с загадками нажми ->\n /zagadki \n Для рестарта бота нажми -> /start \n чтобы вызвать кнопки еще можно нажать на значек в поле ввода сообщения\n если ошибешься с ответом появится рандомное фото')

@bot.message_handler(commands=['start'])
def hendle_text(message):
      bot.send_message(message.from_user.id, 'Привет, я кусок бездушного когда(КБК). Рад буду помагать тебе с получением твоего настоящего подарка.Для этого тебе придется отгадать 3 загадки,ответом на которые будут куски ссылки на подарок.Но для начала включи эту песню и поехали... ')
      audio = open('C:/Users/User/PycharmProjects/imge/61078708_160562257.mp3', 'rb')
      bot.send_chat_action(message.from_user.id, 'upload_audio')
      bot.send_audio(message.from_user.id, audio)
      audio.close()
      bot.send_message(message.from_user.id,' Нажми сюда -> /zagadki и выбери загадку \nЕсли нужна помощь нажми сюда -> /help')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Загадка 1':
        bot.send_message(message.from_user.id, 'Для начала я задам тебе простейший вопрос, чтобы проверить роботостопособность кода и твоих навыков набирать сообщения.\n Итак, какая станция является особенной с самого начала наших отношений? \nПример ответа такой: Новослободская')


    elif message.text == 'Театральная':
            bot.send_message(message.from_user.id, 'https://yadi    \n копируй, вставляй в блокнот и переходи к -> /zagadki ')
            directory = "C:\\Users\\User\\Pictures\\Вова"
            all_files_of_directory = os.listdir(directory)
            random_file = random.choice(all_files_of_directory)
            img = open(directory + '/' + random_file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()


    elif message.text == 'Загадка 2':
        bot.send_message(message.from_user.id, 'На столе лежат две монеты, в сумме 3 рубля, одна из них не 1 рубль. Что это за монеты? \nПример ответа : 2 рубля и 3 рубля или 3 рубля и 2 рубля ты можешь решить эту задачу если не знаешь ответ -> /dopzadacha')
    elif message.text == '2' :
            bot.send_message(message.from_user.id, '.sk/i/JCQjtfS     \n копируй, вставляй в блокнот и переходи к -> /zagadki')
            directory = "C:\\Users\\User\\Pictures\\Вова"
            all_files_of_directory = os.listdir(directory)
            random_file = random.choice(all_files_of_directory)
            img = open(directory + '/' + random_file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()

    elif message.text == '1 рубль и 2 рубля' :
            bot.send_message(message.from_user.id, '.sk/i/JCQjtfS      \n копируй, вставляй в блокнот и переходи к -> /zagadki')
            directory = "C:\\Users\\User\\Pictures\\Вова"
            all_files_of_directory = os.listdir(directory)
            random_file = random.choice(all_files_of_directory)
            img = open(directory + '/' + random_file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()
    elif message.text == '2 рубля и 1 рубль' :
            bot.send_message(message.from_user.id, '.sk/i/JCQjtfS      \n копируй, вставляй в блокнот и переходи к -> /zagadki')
            directory = "C:\\Users\\User\\Pictures\\Вова"
            all_files_of_directory = os.listdir(directory)
            random_file = random.choice(all_files_of_directory)
            img = open(directory + '/' + random_file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()
    elif message.text == 'Загадка 3':
            bot.send_message(message.from_user.id, 'Где была сделана эта фотография?')
            directory = "C:\\Users\\User\\Pictures\\Вова\\gmICSecUWAM (1).jpg"
            img1 = open(directory, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img1)
            img1.close()

    elif message.text == 'Холи':
        bot.send_message(message.from_user.id, '93T5zgQ     \n копируй, вставляй и смотри на подарок! С 8 Марта, солнце ))))')
        directory = "C:\\Users\\User\\Pictures\\Вова"
        all_files_of_directory = os.listdir(directory)
        random_file = random.choice(all_files_of_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()


        #directory = "C:\\Users\\User\\Pictures\\Вова"
        #all_files_of_directory=os.listdir(directory)
        #random_file=random.choice(all_files_of_directory)
        #img=open(directory + '/' + random_file,'rb')
        #bot.send_chat_action(message.from_user.id,'upload_photo')
        #bot.send_photo(message.from_user.id,img)
        #img.close()

    elif message.text == 'Аудио':
        audio=open('C:/Users/User/PycharmProjects/imge/61078708_160562257.mp3', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
    elif message.text == 'кто ты':
        bot.send_message(message.from_user.id, "Я бот")


    else:

         bot.send_message(message.from_user.id,'Ты ответила не правильно')
         directory = "C:\\Users\\User\\Pictures\\Вова"
         all_files_of_directory=os.listdir(directory)
         random_file=random.choice(all_files_of_directory)
         img=open(directory + '/' + random_file,'rb')
         bot.send_chat_action(message.from_user.id,'upload_photo')
         bot.send_photo(message.from_user.id,img)
         img.close()
bot.polling(none_stop=True)