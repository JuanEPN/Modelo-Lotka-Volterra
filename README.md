# Parámetros del modelo
r = 0.5        # Tasa de crecimiento de presas sanas
a = 0.01       # Tasa de depredación
b = 0.005      # Eficiencia de conversión (presas → depredadores)
m = 0.2        # Mortalidad de depredadores
K = 1000       # Capacidad de carga
lambda_ = 0.01 # Tasa de infección entre presas
mu = 0.3       # Mortalidad de presas infectadas

# Condiciones iniciales
S = 500.0  # Presas sanas
I = 10.0   # Presas infectadas
D = 20.0   # Depredadores

# Parámetros de simulación
dt = 0.01
t_max = 100
steps = int(t_max / dt)

# Listas para almacenar los resultados
time = []
S_list = []
I_list = []
D_list = []

# Bucle de simulación
for step in range(steps):
    # Almacenar valores actuales
    time.append(step * dt)
    S_list.append(S)
    I_list.append(I)
    D_list.append(D)

    # Ecuaciones diferenciales (modelo extendido de Lotka-Volterra con infección)
    dS = (r * S * (1 - (S + I) / K) - a * S * D - lambda_ * S * I) * dt
    dI = (lambda_ * S * I - mu * I - a * I * D) * dt
    dD = (b * a * (S + I) * D - m * D) * dt

    # Actualizar poblaciones
    S += dS
    I += dI
    D += dD

    # Evitar valores negativos
    S = max(S, 0)
    I = max(I, 0)
    D = max(D, 0)

# Imprimir muestra de resultados cada 1 unidad de tiempo
print("Tiempo\tSanas\tInfectadas\tDepredadores")
for i in range(0, steps, int(1 / dt)):
    print(f"{time[i]:.1f}\t{S_list[i]:.1f}\t{I_list[i]:.1f}\t\t{D_list[i]:.1f}")
