import datetime

def horarios_disponiveis(agendamentos, dia):
    todos_horarios = [
        datetime.time(8,30),
        datetime.time(9,00),
        datetime.time(9,30),
        datetime.time(10,00),
        datetime.time(10,30),
        datetime.time(11,00),
        datetime.time(11,30),

        datetime.time(14,30),
        datetime.time(15,00),
        datetime.time(15,30),
        datetime.time(16,00),
        datetime.time(16,30),
        datetime.time(17,00),
        datetime.time(17,30),
        datetime.time(18,00),
        datetime.time(18,30),
        datetime.time(19,00)
    ]

    sabado_horarios = [
        datetime.time(8,30),
        datetime.time(9,00),
        datetime.time(9,30),
        datetime.time(10,00),
        datetime.time(10,30),
        datetime.time(11,00),
        datetime.time(11,30)
    ]

    
    if dia == 'sábado':
        for horario in agendamentos:
            if horario in sabado_horarios:
                sabado_horarios.remove(horario)

        return sabado_horarios    
    
    else:
        for horario in agendamentos:
            if horario in todos_horarios:
                todos_horarios.remove(horario)

        return todos_horarios