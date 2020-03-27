from amanobot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def botao1(tt=None):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Google', callback_data=f'go {tt}'),
         InlineKeyboardButton(text='Wikipédia', callback_data=f'wiki {tt}')],
    ])
    return keyboard


def botao2():
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Link do grupo', callback_data='L'),
         InlineKeyboardButton(text='Help', callback_data='SOS')],
        [InlineKeyboardButton(text='Sites + usados', callback_data='url')],
        [InlineKeyboardButton(text='Conteúdo', callback_data='co')],
    ])
    return menu


def botao3():
    redi = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Menu', callback_data='M')],
    ])
    return redi


def botao4():
    conte = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Cursos', callback_data='curs'),
         InlineKeyboardButton(text='HQs', callback_data='li')],
        [InlineKeyboardButton(text='Musicas', callback_data='mu')],
        [InlineKeyboardButton(text='Radios', callback_data='ha')],
    ])
    return conte
