import datetime

def horarios_agendados(tk, eventos, msgbox):
    todos_horarios = []

    for event in eventos:
        start = event["start"].get("dateTime", event["start"].get("date"))
        
        # Converter a string do horário para um objeto datetime
        start_datetime = datetime.datetime.fromisoformat(start)
        
        horario = start_datetime.time()
        todos_horarios.append(horario)
        
        msgbox.insert(tk.END, "> ", start, event["summary"] + "\n")

    return todos_horarios    
