# Arquivo para colocar as funções que mexeram com os arquivos .txt


def abre_id(arq):
    with open(arq, 'r') as lei:
        z = []
        # print(file.readlines())
        lei.seek(0)
        for le in lei.readlines():
            z.append(le)
        # lista_formated = list(map(lambda l: l.replace('\n', ''), a))
        lista_formated_1 = list(map(lambda l: l.rstrip(), z))
        return lista_formated_1
