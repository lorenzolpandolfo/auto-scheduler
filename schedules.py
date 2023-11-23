import datetime

def horarios_disponiveis(agendamentos):
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

    for horario in agendamentos:
        if horario in todos_horarios:
            todos_horarios.remove(horario)
    
    # print("\nTodos horários disponíveis para marcar hoje: \n", todos_horarios)
    return todos_horarios