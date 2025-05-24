import matplotlib.pyplot as plt
import numpy as np

# Parámetros
prob_falsa = 0.3          # P(F)
prob_real = 0.7           # P(R)
prob_cara_dado_falsa = 0.9  # P(C|F)
prob_cara_dado_real = 0.5   # P(C|R)
caras_consecutivas = 14     # Número de caras consecutivas

# Cálculo de probabilidades condicionales
prob_c_n_dado_falsa = prob_cara_dado_falsa ** caras_consecutivas
prob_c_n_dado_real = prob_cara_dado_real ** caras_consecutivas

# Probabilidad total
prob_c_n = prob_c_n_dado_falsa * prob_falsa + prob_c_n_dado_real * prob_real

# Teorema de Bayes
prob_falsa_dado_c_n = (prob_c_n_dado_falsa * prob_falsa) / prob_c_n
prob_real_dado_c_n = (prob_c_n_dado_real * prob_real) / prob_c_n

# Mostrar resultados
print(f"P(C^{{14}}|F) = {prob_c_n_dado_falsa:.6f}")
print(f"P(C^{{14}}|R) = {prob_c_n_dado_real:.6f}")
print(f"P(C^{{14}}) = {prob_c_n:.6f}")
print(f"P(F|C^{{14}}) = {prob_falsa_dado_c_n:.6f}")
print(f"P(R|C^{{14}}) = {prob_real_dado_c_n:.6f}")

# Rango de número de caras consecutivas
valores_n = np.arange(1, 18)

prob_falsa_dado_c_n = []
prob_real_dado_c_n = []

for n in valores_n:
    # Probabilidades condicionales
    prob_c_n_dado_falsa = prob_cara_dado_falsa ** n
    prob_c_n_dado_real = prob_cara_dado_real ** n

    # Probabilidad total
    prob_c_n = prob_c_n_dado_falsa * prob_falsa + prob_c_n_dado_real * prob_real

    # Bayes
    prob_f = (prob_c_n_dado_falsa * prob_falsa) / prob_c_n
    prob_r = (prob_c_n_dado_real * prob_real) / prob_c_n

    prob_falsa_dado_c_n.append(prob_f)
    prob_real_dado_c_n.append(prob_r)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(valores_n, prob_falsa_dado_c_n, label='P(F|C^n)', color='red')
plt.plot(valores_n, prob_real_dado_c_n, label='P(R|C^n)', color='blue')
plt.axvline(x=14, linestyle='--', color='gray', label='n = 14')
plt.xlabel('Número de caras consecutivas (n)')
plt.ylabel('Probabilidad posterior')
plt.title('Probabilidad de que la moneda sea falsa o real dado n caras consecutivas')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
