from datetime import datetime
from pytz import timezone


def hour():
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    hora_sao_paulo = data_e_hora_sao_paulo.strftime('%H:%M')
    return hora_sao_paulo


def dat():
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    dia_sao_paulo = data_e_hora_sao_paulo.strftime('%d')
    return dia_sao_paulo
