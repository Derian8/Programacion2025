#Autor: Derian Acuña Rojas
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# numero total de minutos
mins = mins + dura
#encontrar el numero de horas
hour = hour + mins // 60
# poner que los minutos lleguen hasta el 60 rango (0..59)
mins = mins % 60
# corrige las horas para que estén en un rango de (0..23)
hour = hour % 24 
print(hour, ":", mins, sep='')

