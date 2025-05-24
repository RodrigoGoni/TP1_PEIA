import sympy as sp

# Definir las variables simbolicas
x, y, K = sp.symbols('x y K')

# Definir la funcion a integrar
f = K * y

# Definir los limites de integracion
inner_integral = sp.integrate(f, (y, 9 * x**2, 9 * x))
outer_integral = sp.integrate(inner_integral, (x, 0, 1))

# Igualamos la integral a 1 para encontrar el valor de K
equation = sp.Eq(outer_integral, 1)

# Resolver la ecuacion para K
solution = sp.solve(equation, K)

# Mostrar resultados
print("Valor de K que hace que la integral sea 1:")
print(solution[0])

# Definir las variables
x, y = sp.symbols('x y')

# Definir la funcion a integrar
f = (27/5) * y

# Limite inferior: sqrt(y/9) = sqrt(y)/3
lower_limit = sp.sqrt(y/9)
upper_limit = y/9

# Calcular la integral con respecto a x
f_Y = sp.integrate(f, (x, lower_limit, upper_limit))

# Mostrar resultado
print("f_Y(y) =", f_Y)
