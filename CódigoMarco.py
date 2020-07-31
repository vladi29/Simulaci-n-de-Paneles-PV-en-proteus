from math import exp
from math import pow
from math import log

Iscn = float(input("Ingrese la corriente de cortocircuito: "))
Voc = float(input("Ingrese el voltaje de circuito abierto: "))
Impp = float(input("Ingrese la corriente de maxima potencia: "))
Vmpp = float(input("Ingrese el voltaje de maxima potencia: "))
Kv = float(input("Ingrese el coeficiente de V/T: "))*(-1)
Ki = float(input("Ingrese el coeficiente de I/T: "))
tn = float(input("Ingrese la  temperatura nominal: "))+273.15
Gn = float(input("Ingrese la irradiancia nominal: "))
G = float(input("Ingrese la irradiancia requerida: "))
t = float(input("Ingrese la  temperatura requerida: "))+273.15
Ns = float(input("Ingrese el numero de celdas conectadas en serie: "))
a = float(input("Constante del diodo: "))
q = 1.60217646*pow(10, -19)
k = 1.3806503*pow(10, -23)
vt = (Ns*k*t)/q
Dt = t - tn
iph = (Iscn + Ki*Dt)/Gn
print("El valor por el que se debe multiplicar la irradiancia es"+str(iph))
io = (Iscn + Ki*Dt)/(exp((Voc+(Kv*Dt))/(vt*a))-1)
print("La corriente de saturacion del diodo a "+str(t)+" es igual a " + str(io))
print("Luego de haber hecho la simulacion en Proteus, ingrese aqui los siguientes valores:")
Impp = float(input("Ingrese la corriente de maxima potencia antes del Buck-Boost: "))
Vmpp = float(input("Ingrese el voltaje de maxima potencia antes del Buck-Boost: "))
Vo = float(input("Ingrese el voltaje a la salida del Buck-Boost: "))
Po = float(input("Ingrese la potencia a la salida del Buck-Boost: "))
Rl= round(pow(Vo,2)/Po)
n=Po/(Impp*Vmpp)
alpha= Vo/Vmpp
D=alpha/(1+ alpha)
req=round(n*D*Rl)
print("La eficiencia es:"+str(n))
print("El Duty Cycle es :"+str(D))
print("La Resistencia de carga es:"+str(Rl)+" ohmios")
print("La resistencia equivalente es:"+str(req))