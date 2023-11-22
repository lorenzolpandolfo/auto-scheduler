import datetime

def horarios_disponiveis(agendamentos):
    todos_horarios = [
        datetime.time(8,30).strftime("%H:%M"),
        datetime.time(9,0).strftime("%H:%M"),
        datetime.time(9,30).strftime("%H:%M"),
        datetime.time(10,0).strftime("%H:%M"),
        datetime.time(10,30).strftime("%H:%M"),
        datetime.time(11,0).strftime("%H:%M"),
        datetime.time(11,30).strftime("%H:%M"),

        datetime.time(14,30).strftime("%H:%M"),
        datetime.time(15,0).strftime("%H:%M"),
        datetime.time(15,30).strftime("%H:%M"),
        datetime.time(16,0).strftime("%H:%M"),
        datetime.time(16,30).strftime("%H:%M"),
        datetime.time(17,00).strftime("%H:%M"),
        datetime.time(17,30).strftime("%H:%M"),
        datetime.time(18,0).strftime("%H:%M"),
        datetime.time(18,30).strftime("%H:%M"),
        datetime.time(19,0).strftime("%H:%M")
    ]

    for horario in agendamentos:
        if horario in todos_horarios:
            todos_horarios.remove(horario)
    
    return todos_horarios