from scipy import signal
import matplotlib.pyplot as plt
import scipy

tentrada = []
for i in range(0,300):
    time = 0.1 * i
    tentrada.append(time)


umbral = 0.67
a2 = 0.67
a1 = 210
a0 = 12
sys_car = signal.lti(1,[a2,a1,a0])
t , y = signal.step2(sys_car)

#print(t)
p_entrada = 0.1 * t
y2 = p_entrada * y
plt.plot(t,y2)


def presiondeentrada(p_entrada):
    if p_entrada >= umbral:
        salida = p_entrada - umbral
    else: 
        salida = 0
        
    return salida


for entrada in tentrada:
    print(presiondeentrada(entrada))

print("=============================")

for entrada2 in p_entrada:
    print(presiondeentrada(entrada2))