import random

mi = ['ola', 'teste', 'como vai']
chute = random.choices(mi)
embaralhar = random.shuffle(mi)
# with open('centralMessages.txt', 'r', encoding='utf-8') as file:
#     for frase_pv in file:
#         camp1, camp2 = frase_pv.split(':')
#         camp2_list = camp2.split()
#         #print(camp2_list)
#         if '$' in camp2:
#             camp2 = camp2.replace('$', 'nome')
#         print(camp2)


#def soma(frase, nome):
#    print(frase)


#with open('centralMessages.txt', 'r', encoding='utf-8') as file:
#    for frase_pv in file:
#        funcao_da_pergunta, pergunta, resposta = frase_pv.split
#        # funcao_da_pergunta = funcao_da_pergunta
#        resposta_ao_telegram = locals[funcao_da_pergunta](funcao_da_pergunta, 'ruan')
#        print(resposta_ao_telegram)


# def soma(frase, nome):
#     return frase.replace("$", nome)
#
#
# with open('centralMessages.txt', 'r', encoding='utf-8') as file:
#     for frase_pv in file:
#         estrutura = frase_pv.split(':')
#         resposta_ao_telegram = locals()[estrutura[0]](estrutura[1], 'ruan')
#         print(resposta_ao_telegram)


def soma_num(fra):
    return fra.replace("$", "ruan")


def soma_erro(estrutura):
    confir = []
    for res_chute in estrutura[2::]:
        confir.append(res_chute)
    if len(confir) == 1:
        if "$" in confir:
            return confir[0].replace("$", "ruan")
        else:
            return confir
    else:
        resp_final = random.randint(0, len(confir))
    if "$" in confir[resp_final]:
        modificando = confir[resp_final]
        return modificando.replace("$", "Ruan")
    else:
        return confir[resp_final]


def soma(frase):
    return


with open('central.txt', 'r', encoding='utf-8') as file:
    for frase_pv in file:
        frase_pv = frase_pv.replace('\n', '')
        estrutura = frase_pv.split(':')
        if len(estrutura) == 2:
            resposta_ao_telegram = estrutura[1]
            print(resposta_ao_telegram)
        # elif len(estrutura) >= 3:
        #     if estrutura[0] in locals():
        #         resposta_ao_telegram = locals()[estrutura[0]](estrutura)
        #         print(resposta_ao_telegram)
        #     else:
        #         print("funcao especificada no CSV nao existe no codigo python!!!")
        elif len(estrutura) >= 3:
            if estrutura[0] in locals():
                confirmacao = []
                for resp_chute in estrutura[1::]:
                    confirmacao.append(resp_chute)
                resposta_final = random.randint(2, len(confirmacao))
                if '$' in estrutura[resposta_final]:
                    resposta_ao_telegram = locals()[estrutura[0]](estrutura[resposta_final])
                    print(resposta_ao_telegram)
                else:
                    print(estrutura[resposta_final])
            else:
                print("funcao especificada no CSV nao existe no codigo python!!!")
        else:
            print("encontrado entrada no CSV nao permitida!")
