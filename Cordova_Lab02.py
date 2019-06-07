import numpy as np
import sympy as sp

A = np.random.randint(10, size=(10, 10))  # matriz A de 10x10 con numeros aleatorios del 1 al 10

B = np.random.randint(10, size=(10, 10))  # matriz A de 10x10 con numeros aleatorios del 1 al 10

for a in range(len(A)):  # cambio de diagonal matriz A
    A[a][a] = 0
print("matriz A: \n " + str(A))

for b in range(len(B)):  # cambio de diagonal matriz B
    A[b][b] = 0
print("matriz B: \n " + str(B))

print("suma A+B: \n " + str(A+B))  # Suma de matrices

print("suma A-B: \n " + str(A-B))  # resta de matrices

print("Multiplicacion A*B: \n " + str(A*B))  # Multiplicacion de matrices

print("producto punto A*B \n " + str(np.dot(A, B)))  # Producto punto

x = np.arange(3)                             # producto cruz
y = x+1
print("producto cruz " + str(np.cross(x, y)))


print("A transpuesta \n " + str(A.transpose()))         #Transpuesta de Matriz A

print("B transpuesta \n " + str(B.transpose()))         #Transpuesta de Matriz B

C = np.array([[3, -6, 9, 0, -3, 18],                    #matriz con valores manuales
              [-1, 2, -3, 2, 11, 2],
              [2, -4, 6, -2, -12, 4]])

print("FERR de C= \n " + str(sp.Matrix(C).rref()))  # FERR de matriz C

