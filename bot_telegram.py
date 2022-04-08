#Importando API do Telegram
#pip install pytelegrambotapi
import telebot

#Chave da API do bot
chave_API = 'Sua chave API'
#Ativando bot
bot = telebot.TeleBot(chave_API)

#Responde uma mensagem específica que comece com "/" (commands=mensagem_que_tem_que_ser_dita_sem_a_/)
#sempre tem que vim antes do "responder"
@bot.message_handler(commands='ola')
def ola(mensagem):
    #Envia mensagem específica para alguém (ID_que_recebe, mensagem
    bot.send_message(mensagem.chat.id, 'Olá, '+mensagem.from_user.first_name)

#fazer a função "responder" funcionar
def verificar(mensagem): return True
#Reagir a qualquer mensagem
@bot.message_handler(func=verificar)
def responder(mensagem):
    #Responder marcando mensagem (mensagem_a_ser_respondida, mensagem_que_quer_mandar)
    bot.reply_to(mensagem, '''Olá, mundo!
/ola''')
    #colocar "/" torna a palavra clicável para responder, assim criando opções

    #Para poder ver os parâmetros da mensagem
    print(mensagem)

#Para manter o bot ligado
bot.polling()
