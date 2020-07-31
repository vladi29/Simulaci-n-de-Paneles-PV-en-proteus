import math, sys

Isc = 4.67   #Corriente de corto circuito a STC 
Voc = 21.6   #Voltaje de circuito abierto a STC
Imp = 4.34   #Corriente a máxima transferencia de potencia en STC
Vmp = 17.3   #Voltaje a máxima transfenecia de potencia en STC
Gstv = 1000  #Irradiancia STC en W/m^2
Tstc = 25    #Temperatura STC en °C
T = 25       #Temperatura nominl en °C
Kv = 0       #Coeficiente de Voltaje según la temperatura
Ki = 0       #Coeficiente de Corriente según la temperatura

#En este modelo se toma la corriente de corto circuito como la corriente fotovoltáica generada por un panel
#es decir Isc = Ipv, es por esto que se establece la siguiente relación para Ipv según G y T

G = float(input("Nueva Irradiancia (W/m^2): "))
Ipv = (Isc + Ki*(T-Tstc))*G/Gstv
print("La corriente fotovoltáica será: ", Ipv)

