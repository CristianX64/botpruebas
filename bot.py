import telebot

TOKEN = '786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0'  # Ponemos nuestro Token generado con el @BotFatherres

respuesta = 'https://api.telegram.org/bot786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0/getUpdates'
print(respuesta)
tb = telebot.TeleBot(TOKEN)

tb.send_message('-1001160355548', 'Hola Heisen!')  # Ejemplo tb.send_message('109556849', 'Hola mundo!')


# https://api.telegram.org/bot786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0/sendMessage?chat_id=-1001160355548&text=Soy%20el%20bot%20que%20va%20a%20dar%20Karma%20a%20los%20chicos%20buenos


def main():
    TOKEN = '786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0'  # Ponemos nuestro Token generado con el @BotFatherres
    
    respuesta = 'https://api.telegram.org/bot786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0/getUpdates'
    print(respuesta)
    tb = telebot.TeleBot(TOKEN)  # Combinamos la declaración del Token con la función de la API
    
    tb.send_message('-1001160355548', 'La configuracion se ha realizado con Exito')  # Ejemplo tb.send_message('109556849', 'Hola mundo!')
    tb.send_message('-1001160355548', 'Las respuestas seran verificadas despues de terminar el juego')  # Ejemplo tb.send_message('109556849', 'Hola mundo!')
    tb.send_message('-1001160355548', '+++++++++++++++++++++++PREGUNTA 1++++++++++++++++++++++++++')
# https://api.telegram.org/bot786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0/sendMessage?chat_id=-1001160355548&text=Soy%20el%20bot%20que%20va%20a%20dar%20Karma%20a%20los%20chicos%20buenos

bot = telebot.TeleBot(TOKEN)  # Creamos el objeto de nuestro bot.

AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/ayuda - Guia para utilizar el bot. \n/info - Informacion De interes \n/hola - Saludo del Bot \n/piensa3D - Informacion sobre Piensa3D \n\n'


def command_ayuda(m):  # Definimos una función que resuleva lo que necesitemos.
    
    cid = m
    
    bot.send_chat_action(cid, 'typing')  # Enviando ...
    
    time.sleep(1)  # La respuesta del bot tarda 1 segundo en ejecutarse
    
    bot.send_message(cid,
                     AYUDA)  # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.


if __name__ == '__main__':

    command_ayuda(-1001160355548)
    bot.message_handler(commands=['ayuda'])  # Indicamos que lo siguiente va a controlar el comando '/ayuda'
    main()
