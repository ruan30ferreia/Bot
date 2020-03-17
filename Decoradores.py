def validate_type(type, *args):
    return all(isinstance(val, int) for val in args)


def media_acumulada():
    valores = []
    def calcula_media(valor):
        valores.append(valor)
        return sum(valores)/len(valores)
    return calcula_media


def soma(x, y):
    if all(isinstance(val, int) for val in [x, y]):
        return x + y


def sub(x, y):
    if all(isinstance(val, int) for val in [x, y]):
        return x - y


def vailidate_int(func):

    # func é uma variavel livre

    def validate(x, y):
        print(x, y)
        return func(x, y)

    return validate


# soma(1, 1)
# soma_validacao = vailidate_int(soma)
# soma_validacao(1, 1)


def decorador(func):

    def interna(*args, **kwargs):
        print('Antes de executar a função')
        return func(*args, **kwargs)
        print('depois')

    return interna


def ola():
    print('dentro da função')
