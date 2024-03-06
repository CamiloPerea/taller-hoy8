import os
os.system ('cls')

kilometrosInt = 0
totalKmInt = 0
etapaInt = int(input('cuantas paradas  va realizar -> '))
for i in range(etapaInt):
    var_etapaInt =int(input(' ingrese los kmr ecorridos en el trayecto -> '))
    totalKmInt += var_etapaInt
     
print('Etapas recorridas:', etapaInt)
print(totalKmInt,'KM')  

enter= input('\n< salir del programa')