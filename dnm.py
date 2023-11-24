dias = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
meses = ["1","2","3","4","5","6","7","8","9","10","11","12"]

dias_por_mes = {
    "1":     31,
    "2":     28,
    "3":     31,
    "4":     30,
    "5":     31,
    "6":     30,
    "7":     31,
    "8":     31,
    "9":     30,
    "10":    31,
    "11":    30,
    "12":    31
}

def hoje_ate_proxima_semana(dia, mes):
    global dias
    total_dias = []
    for i in range(0,8):
        dia_dentro_do_range = int(dias[dia - 1]) + i

        if dia_dentro_do_range > dias_por_mes[mes]:
            break
        else:
            total_dias.append(str(dia_dentro_do_range))
        
    print(total_dias)
    return total_dias