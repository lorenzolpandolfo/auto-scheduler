import datetime

def horarios_agendados(eventos):
    todos_horarios = []

    for event in eventos:
        start = event["start"].get("dateTime", event["start"].get("date"))
        
        # Converter a string do horário para um objeto datetime
        start_datetime = datetime.datetime.fromisoformat(start)
        
        """
        # Definir o horário desejado para comparação
        horario_desejado = datetime.time(8, 00)
        """
        
        horario = start_datetime.time()
        todos_horarios.append(horario)
        
        """
        if start_datetime.time() == horario_desejado:
            print("Certo")
        else:
            print(start, event["summary"])
        """

    return todos_horarios    
