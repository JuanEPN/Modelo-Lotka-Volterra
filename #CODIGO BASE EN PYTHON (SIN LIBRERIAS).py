#CODIGO BASE EN PYTHON (SIN LIBRERIAS)


# PARÁMETROS BASE 
r = 0.5    # Tasa crecimiento presas
a = 0.01   # Tasa depredación
b = 0.005  # Eficiencia conversión
m = 0.2    # Mortalidad depredadores
K = 1000   # Capacidad de carga

# CONDICIONES INICIALES
P0 = 500   # Presas iniciales
D0 = 20    # Depredadores iniciales
dt = 0.01  # Paso temporal
t_max = 100

# ARRAYS DE ALMACENAMIENTO
P = [P0]
D = [D0]
t = [0]

# SIMULACION
for _ in range(int(t_max/dt)):
    dP = (r * P[-1] * (1 - P[-1]/K) - a * P[-1] * D[-1]) * dt
    dD = (b * a * P[-1] * D[-1] - m * D[-1]) * dt
    
    P.append(P[-1] + dP)
    D.append(D[-1] + dD)
    t.append(t[-1] + dt)


# RESULTADOS (USAREMOS UN EJEMPLO CON LOS ULTIMOS 5 PUNTOS)
print("Tiempo\tPresas\tDepredadores")
for i in range (-5, 0):
    print(f"{t[i]:.1f}\t{P[i]:.1f}\t{D[i]:.1f}")
