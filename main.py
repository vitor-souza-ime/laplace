import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Definindo símbolos
s, t = sp.symbols('s t')
Y = sp.Function('Y')(s)
X = 1 / s  # Transformada de Laplace de degrau unitário (u(t))

# Parâmetros do circuito
R = 1  # Ohm
C = 1  # Farad
RC = R * C

# Equação no domínio de Laplace: RC * s * Y(s) + Y(s) = X(s)
Y_s = sp.solve(RC * s * Y + Y - X, Y)[0]
print("Y(s) =", Y_s)

# Transformada inversa para obter y(t)
y_t = sp.inverse_laplace_transform(Y_s, s, t)
print("y(t) =", y_t)

# Plotando a resposta ao degrau (usando Scipy para simular)
# Função de transferência H(s) = 1 / (RC*s + 1) com RC = 1
system = lti([1], [RC, 1])
t_vals, y_vals = step(system)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(t_vals, y_vals, label="Resposta ao degrau", color="blue")
plt.title("Resposta ao Degrau de um Sistema RC (1ª Ordem)")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída y(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
