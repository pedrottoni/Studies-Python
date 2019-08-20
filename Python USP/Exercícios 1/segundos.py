segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
emDias = segundos // 86400
emHoras = segundos // 3600
emSegundos = segundos % 3600
emMinutos = emSegundos // 60
emSegundosTotal = emSegundos % 60
emHorasTotal = emHoras % 24

print (emDias,"dias,",emHorasTotal,"horas,",emMinutos,"minutos e",emSegundosTotal,"segundos.")