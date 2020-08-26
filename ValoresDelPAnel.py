#Vladimir Alfaro - Caracas, Venezuela
#Código para el cálculo de los parámetros de un panel, a partir de su DataSheet
#Panel usado por defecto: Isofotón I-75S-12
import math, cmath, sys

#----------Características del arreglo---------------
Serie = 1                           #Número de paneles en serie
Paralelo = 1                        #Número de paneles en paralelo
#Arreglo total de 40 (Seire*paralelo) paneles

#----------Valores del Panel----------
Isc = 4.67                          #Corriente de corto circuito a STC 
Voc = 21.6                          #Voltaje de circuito abierto a STC
Imp = 4.34                          #Corriente a máxima transferencia de potencia en STC
Vmp = 17.3                          #Voltaje a máxima transfenecia de potencia en STC
Pmp = Vmp * Imp                     #Potencia máxima para un panel

Isc1 = Isc * Paralelo               #Corriente de corto circuito en el arreglo       
Voc1 = Voc * Serie                  #Voltaje de circuito abierto en el arreglo
Imp1 = Imp * Paralelo               #Corriente a máximo punto de potencia en el arreglo
Vmp1 = Vmp * Serie                  #Voltaje a máximo punto de potencia en el arreglo
Pmp1 = Pmp*Serie*Paralelo           #Potencia máxima para el arreglo

#----------Datos Ambientales----------
Gstv = 1000                         #Irradiancia STC en W/m^2
Tstc = 298.15                       #Temperatura STC en °K
k = 1.381e-23                       #Constante de Boltzmann
Eg = 1.12                           #Banda Gap (eV)
q = 1.602e-19                       #Carga del electrón
Csh = 34.49692                      #Capacitancia 1
Cs = 0.11175                         #Capacitancia 2
Kv = 0                              #Coeficiente de Voltaje según la temperatura
Ki = 0                              #Coeficiente de Corriente según la temperatura

#-----------Datos ambientales en los que se hace el estudio----------
T = 298.15                          #Temperatura promedio de la zona de estudio en °K
G = 477.46                          #Irradiancia promedio de la zona de estudio en W/m^2

#Seguirermo con el algoritmo para el cálculo de los parámetros del panel como se vio en
#el paper Cubas, Victoria, Pindado "On the analytical approach for modeling photovoltaic systems behavior". 2014

Vth = (k*Tstc)/q
Rsho = (Csh*Voc1)/Isc1
Rso = (Cs*Voc1)/Isc1

log10 = math.log10((Vmp1 + (Imp1-Isc1)*Rsho)/(Voc1-Isc1*Rsho))
A = (Vmp1 + (Imp1 - Isc1)*Rsho)*log10
B = Vmp1-Imp1*Rsho

Rs = ((A-B)*Vmp1)/((A+B)*Imp1) + (B*Voc1)/(Imp1*(A+B))                                                      #Resistencia en Serie
D = ((Vmp1-Imp1*Rs)*(Vmp1+(Imp1-Isc1)*Rsho))/((Vmp1-Imp1*Rsho)*Vth)                                         #Factor de idealidad del diodo 
Rsh = (Vmp1 - Imp1*Rs)*(Vmp1 - Rs*(Isc1 - Imp1) - D*Vth)/((Vmp1 - Imp1*Rs)*(Isc1-Imp1) - D*Vth*Imp1)        #Resistencia en paralelo
exp = math.exp(Voc1/(D*Vth))
Io = ((Rsh + Rs)*Isc1 - Voc1)/(Rsh*exp)                                                                     #Corriente de salida
Ipv = Isc1*((Rsh + Rs)/Rsh)                                                                                #Corriente fotovoltáica

print("Rs = ", Rs)
print("\nRsh = ", Rsh)
print("\nFactor de calidad del diodo D = ", D)
print("\nCorriente fotovoltaica Ipv = ", Ipv)
