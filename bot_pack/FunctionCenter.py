# Funções que são chamadas no arquivo de texto junto as perguntas e respostas

mensagem = """Seja bem vindo {conta[1]} {conta[2] if len(conta) >= 3 else ''},
veja os videos e escute os audios , e principalmente coloque uma foto e nome validos
, para  a nossa e sua segurança e também não ser banido pelo robo do grupo, vc vendo
os videos saberá como aproveitar os arquivos e musicas do grupo com muito mais
facilidade, Siga as regras que são poucas, compartilhe o maximo de arquivos 
que tiver, isso ajuda a todos, obrigado.
 ———————————————————————————————————————————————————————————-
watch the videos and listen to the audios, and especially put a
valid photo and name, for ours and your safety and also not be
banned by the group robot, u watching the videos will know how to
enjoy the files and music. of the group much easier, follow the few
rules, share as many files as you have, it helps everyone, thanks."""


# Função para trocar $ pelo nome da pessoa
def soma(estrutura, name):
    return estrutura.replace("$", name)


def recebe_usuario():
    rece_list = [mensagem, '', '', '']
    print('Em desenvolvimento')
