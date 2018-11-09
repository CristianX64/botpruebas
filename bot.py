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
    
     # La respuesta del bot tarda 1 segundo en ejecutarse
    
    bot.send_message(cid,
                     AYUDA)  # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

# Handle '/start' and '/help'
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start1'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")



@bot.message_handler(func=lambda message: message.text == "hola")
def command_text_hola(m):

    bot.send_message('-1001160355548', "Hola a ti tambien")



def listener(
        messages):  # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.

    for m in messages:  # Por cada dato 'm' en el dato 'messages'

        cid = m.chat.id  # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios

        if cid > 0:

            mensaje = str(m.chat.first_name) + " [" + str(
                cid) + "]: " + m.text  # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.

        else:

            mensaje = str(m.from_user.first_name) + "[" + str(
                cid) + "]: " + m.text  # Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el nombre.

        f = open('log.txt', 'a')  # Abrimos nuestro fichero log en modo 'Añadir'.

        f.write(mensaje + "\n")  # Escribimos la linea de log en el fichero.

        f.close()  # Cerramos el fichero para que se guarde.

        print
        mensaje  # Imprimimos el mensaje en la terminal, que nunca viene mal :)


 # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
@bot.message_handler(func=lambda message: message.text == "hola")
def command_text_hola(m):
    time.sleep(1)

    bot.send_message(m.chat.id, "Hola a ti tambien")

if __name__ == '__main__':
    bot.set_update_listener(listener)
    command_ayuda(-1001160355548)
    #b  # Indicamos que lo siguiente va a controlar el comando '/ayuda'
    main()
    bot = telebot.TeleBot(TOKEN)
    bot.message_handler(commands=['ayuda'])
    bot.polling(none_stop=True)
