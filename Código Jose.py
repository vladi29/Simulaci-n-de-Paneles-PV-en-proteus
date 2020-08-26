import math

#Arreglo de Paneles
Serie = 1
Paralelo = 1

#Datasheet STC
Vmpn = 17.3 * Serie                #Un panel = 20.2 V
Impn = 4.34 * Paralelo             #Un panel = 7.92 A
Vocn = 21.6 * Serie                #Un panel = 22.9 V
Iscn = 4.67 * Paralelo             #Un panel = 8.37 A
Pmn = Vmpn * Impn

# Variables de Clima
# Introduzca aca los valores del lugar geografico escogido
# Localidad escogida: Valencia (T = 298.40 y G = 416.6131)
T = 298.1500                #Temperatura del ambiente [K]
G = 1000.0000               #Irradiacion del ambiente [W/m^2]

# Constantes
Tn = 298.15                 #Temperatura nominal (25 C)
Gn = 1000                   #Radiacion nominal (1000 W/m^2)
KIsc = 0.00050              #Coeficiente de temperatura de Isc [#/C]
KVoc = -0.00310             #Coeficiente de temperatura de Voc [#/C]
KPm = -0.00420              #Coeficiente de temperatura de Pm [#/C]
k = 1.381e-23               #Constante de Boltzmann
Eg = 1.12                   #Energia de Gap (eV)
q = 1.602e-19               #Carga elemental
Csh = 34.49692      
Cs = 0.11175 

# Parametros nominales del panel
Vthn = (k*Tn)/q 
Rshon = (Csh*Vocn)/Iscn 
Rson = (Cs*Vocn)/Iscn 

log10 = math.log((Vmpn+(Impn-Iscn)*Rshon)/(Vocn-Iscn*Rshon))
An = (Vmpn+(Impn-Iscn)*Rshon)*log10 
Bn = Vmpn-Impn*Rshon 

Rsn = ((An-Bn)*Vmpn)/((An+Bn)*Impn)+((Bn*Vocn)/(Impn*(An+Bn)))
an = (((Vmpn - Impn*Rsn)*(Vmpn+(Impn-Iscn)*Rshon))/(Vmpn-Impn*Rshon))/Vthn
Rshn = ((Vmpn - Impn*Rsn)*(Vmpn-Rsn*(Iscn-Impn)-an*Vthn))/((Vmpn-Impn*Rsn)*(Iscn-Impn)-an*Vthn*Impn)
exp = math.exp(Vocn/(an*Vthn))
Ion = ((Rshn+Rsn)*Iscn-Vocn)/(Rshn*exp)
Ipvn = Iscn*((Rshn+Rsn)/(Rshn))

print("\nRs = ", Rsn)
print("\nRsh = ", Rshn)
print("\nD = ", an)
print("\nIs = ", Ion)
print("\nIpv = ", Ipvn)
print("\nlog = ", log10)