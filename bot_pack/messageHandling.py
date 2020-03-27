abecedario = {'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'Á': 'a', 'À': 'a', 'Â': 'a', 'Ã': 'a', 'é': 'e', 'è': 'e',
              'ê': 'e', 'È': 'e', 'É': 'e', 'Ê': 'e', 'í': 'i', 'ì': 'i', 'î': 'i', 'Ì': 'i', 'Í': 'i', 'Î': 'i',
              'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'Ò': 'o', 'Ó': 'o', 'Ô': 'o', 'Õ': 'o', 'ú': 'u',
              'ù': 'u', 'û': 'u', 'Ù': 'u', 'Ú': 'u', 'Û': 'u', 'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e',
              'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
              'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y',
              'Z': 'z'}
lista_acentos = ['`', '´', '~', '^', '?', '!']


# Essa função troca algumas abreviações que tiverem na frase se tiverem e tira letras maiusuclas e acentos.
def ABC(frase):
    letras_frase = list(frase)
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
    reformado_1 = ''.join(letras_frase)
    palavra_frase = reformado_1.split()
    for pala in palavra_frase:
        if pala == 'vc':
            seque = palavra_frase.index('vc')
            palavra_frase.pop(seque)
            palavra_frase.insert(seque, 'voce')
    for pala1 in palavra_frase:
        if pala1 == 'beleza':
            seque1 = palavra_frase.index('beleza')
            palavra_frase.pop(seque1)
            palavra_frase.insert(seque1, 'blz')
    for pala2 in palavra_frase:
        if pala2 == 'hj':
            seque2 = palavra_frase.index('hj')
            palavra_frase.pop(seque2)
            palavra_frase.insert(seque2, 'hoje')
    reformado = ' '.join(palavra_frase)
    reformado = reformado.replace('por que', 'porque')
    return reformado
