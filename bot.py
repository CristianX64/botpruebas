import telebot  # Importamos las librería

TOKEN = '786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0'  # Ponemos nuestro Token generado con el @BotFatherres

respuesta = 'https://api.telegram.org/bot786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0/getUpdates'
print(respuesta)
tb = telebot.TeleBot(TOKEN)  # Combinamos la declaración del Token con la función de la API

tb.send_message('-1001160355548', 'Hola Heisen!')  # Ejemplo tb.send_message('109556849', 'Hola mundo!')


# https://api.telegram.org/bot786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0/sendMessage?chat_id=-1001160355548&text=Soy%20el%20bot%20que%20va%20a%20dar%20Karma%20a%20los%20chicos%20buenos


def main():
    TOKEN = '786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0'  # Ponemos nuestro Token generado con el @BotFatherres

    respuesta = 'https://api.telegram.org/bot786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0/getUpdates'
    print(respuesta)
    tb = telebot.TeleBot(TOKEN)  # Combinamos la declaración del Token con la función de la API

    tb.send_message('-1001160355548', 'Hola Heisen!')  # Ejemplo tb.send_message('109556849', 'Hola mundo!')

    # https://api.telegram.org/bot786480492:AAHLglxPVMq-UUiI8z27swjr1hLZo4pHsn0/sendMessage?chat_id=-1001160355548&text=Soy%20el%20bot%20que%20va%20a%20dar%20Karma%20a%20los%20chicos%20buenos




if __name__ == '__main__':
    main()