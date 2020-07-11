abecedario = {'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'Á': 'a', 'À': 'a', 'Â': 'a', 'Ã': 'a', 'é': 'e', 'è': 'e',
              'ê': 'e', 'È': 'e', 'É': 'e', 'Ê': 'e', 'í': 'i', 'ì': 'i', 'î': 'i', 'Ì': 'i', 'Í': 'i', 'Î': 'i',
              'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'Ò': 'o', 'Ó': 'o', 'Ô': 'o', 'Õ': 'o', 'ú': 'u',
              'ù': 'u', 'û': 'u', 'Ù': 'u', 'Ú': 'u', 'Û': 'u', 'ç': 'c', 'Ç': 'c'}
lista_acentos = ['`', '´', '~', '^', '?', '!']
palavras_abreviadas = {'vc': 'voce', 'vm': 'vamo', 'blz': 'beleza', 'vms': 'vamos', 'hj': 'hoje', 'por que': 'porque'}
t = ['vc', 'vm', 'blz', 'vms', 'hj']


def ABC(frase):
    letras_frase = list(frase.lower())
    for i in abecedario:
        while i in letras_frase:
            if i in letras_frase:
                num = letras_frase.index(i)
                letras_frase.pop(num)
                letras_frase.insert(num, abecedario[i])
    for acen in lista_acentos:
        while acen in letras_frase:
            if acen in letras_frase:
                num_1 = letras_frase.index(acen)
                letras_frase.pop(num_1)
    reformado = ''.join(letras_frase)
    for palavra in t:
        reformado = reformado.replace(palavra, palavras_abreviadas[palavra])
    return reformado
