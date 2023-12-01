dias = [str(x) for x in range(1, 32)]
meses = [str(x) for x in range(1, 13)]

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

def hoje_ate_proxima_semana(dia, mes, dias):
    total_dias = []
    for i in range(0,8):
        dia_dentro_do_range = int(dias[dia - 1]) + i

        if dia_dentro_do_range > dias_por_mes[mes]:
            break
        else:
            total_dias.append(str(dia_dentro_do_range))
    
    return total_dias