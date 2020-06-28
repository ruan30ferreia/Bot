# Funções do arquivo Bot_4.4
from time import sleep


def receiving_new_users(msg, bot):
    chatID = msg['chat']['id']
    if 'last_name' in msg:
        bot.sendMessage(chatID, f"Seja bem vindo {msg['new_chat_member']['first_name']} "
                                f"{msg['new_chat_member']['last_name']} "
                                f"veja os videos e escute os audios , e "
                                "principalmente coloque uma foto e nome validos , para  a nossa e sua "
                                "segurança e também não ser banido pelo robo do grupo, vc vendo os videos "
                                "saberá como aproveitar os arquivos e musicas do grupo com muito mais "
                                "facilidade, Siga as regras que são poucas, compartilhe o maximo de arquivos "
                                "que tiver, isso ajuda a todos, obrigado."
                                " ———————————————————————————————————————————————————————————-   "
                                "watch the videos and listen to the audios, and especially put a "
                                "valid photo and name, for ours and your safety and also not be "
                                "banned by the group robot, u watching the videos will know how to "
                                "enjoy the files and music. of the group much easier, follow the few "
                                "rules, share as many files as you have, it helps everyone, thanks.")
    else:
        bot.sendMessage(chatID, f"Seja bem vindo {msg['new_chat_member']['first_name']} "
                                f"veja os videos e escute os audios , e "
                                "principalmente coloque uma foto e nome validos , para  a nossa e sua "
                                "segurança e também não ser banido pelo robo do grupo, vc vendo os videos "
                                "saberá como aproveitar os arquivos e musicas do grupo com muito mais "
                                "facilidade, Siga as regras que são poucas, compartilhe o maximo de arquivos "
                                "que tiver, isso ajuda a todos, obrigado."
                                " ———————————————————————————————————————————————————————————-   "
                                "watch the videos and listen to the audios, and especially put a "
                                "valid photo and name, for ours and your safety and also not be "
                                "banned by the group robot, u watching the videos will know how to "
                                "enjoy the files and music. of the group much easier, follow the few "
                                "rules, share as many files as you have, it helps everyone, thanks.")
    bot.sendVoice(chatID, 'AwACAgEAAxkBAANVXiuxhUE0WgJDyqj4AAG4eM8254ZiAAI0AAPnWOhEAQg3hqI1xhQYBA')
    bot.sendVoice(chatID, 'AwACAgEAAxkBAANlXiu4q4yzXzfJe6tBjArmNKjYaUYAAlwAA-dY4ETHWLuPWrOryBgE')
    bot.sendVoice(chatID, 'AwACAgEAAxkBAANmXiu4zd9JaawsvLFD4wnEQI9xuBwAAl8AA-dY4EQwetjYNiG1eRgE')
    bot.sendMessage(chatID, 'https://www.youtube.com/watch?v=gjroA6z6T7U&t=211s')
    bot.sendMessage(chatID, 'https://www.youtube.com/watch?v=RZAYppEvkqM&t=80s')
    bot.sendMessage(chatID, "https://www.youtube.com/watch?v=UuyJGyOaot4")


if __name__ == '__main__':
    print('O arquivo CentralLibrary esta sendo executado, por favor não execute este arquivo diretamente pois ele'
          'fornece modulos para o arquivo central!')
    sleep(10)
