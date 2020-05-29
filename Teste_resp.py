# Teste para quando alguem perguntar algo que ele n saiba:
import random


def soma(estrutura, name):
    return estrutura.replace("$", name)


def searching(limpesa):
    with open('central.txt', 'r', encoding='utf-8') as file:
        for frase_pv in file:
            frase_pv = frase_pv.replace('\n', '')
            estrutura = frase_pv.split(':')
            if len(estrutura) == 2:
                resposta_ao_telegram = estrutura[1]
                if limpesa == estrutura[1]:
                    # bot.sendMessage(chatID, resposta_ao_telegram)
                    return resposta_ao_telegram
            elif len(estrutura) >= 3:
                if estrutura[0] in globals():
                    if limpesa == estrutura[1]:
                        confirmacao = []
                        for resp_chute in estrutura[1::]:
                            confirmacao.append(resp_chute)
                        resposta_final = random.randint(2, len(confirmacao))
                        if '$' in estrutura[resposta_final]:
                            resposta_ao_telegram = globals()[estrutura[0]](estrutura[resposta_final], 'Ruan')
                            # bot.sendMessage(chatID, resposta_ao_telegram)
                            return resposta_ao_telegram
                        else:
                            # bot.sendMessage(chatID, estrutura[resposta_final])
                            return estrutura[resposta_final]
                else:
                    return "encontrado entrada no CSV nao permitida!"
        return 'Não sei responder isso ainda:'


print(searching('tudo bem'))
