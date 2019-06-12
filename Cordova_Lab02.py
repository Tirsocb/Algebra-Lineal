import numpy as np
import sympy as sp

A = np.random.randint(10, size=(10, 10))  # matriz A de 10x10 con numeros aleatorios del 1 al 10

B = np.random.randint(10, size=(10, 10))  # matriz A de 10x10 con numeros aleatorios del 1 al 10

for a in range(len(A)):  # cambio de diagonal matriz A, metodo sin numpy
    A[a][a] = 0
print("matriz A: \n " + str(A))

for b in range(len(B)):  # cambio de diagonal matriz B, metodo sin numpy
    A[b][b] = 0
print("matriz B: \n " + str(B))

print("numpy cambio diagonal A: " + str(np.fill_diagonal(A,5)))  # cambio de diagonal matriz A con numpy
print("numpy cambio diagonal A: " + str(np.fill_diagonal(B, 5)))  # cambio de diagonal matriz B con numpy

print("suma A+B: \n " + str(A+B))  # Suma de matrices

print("suma A-B: \n " + str(A-B))  # resta de matrices

print("Multiplicacion A*B: \n " + str(A*B))  # Multiplicacion de matrices

print("A transpuesta \n " + str(A.transpose()))         #Transpuesta de Matriz A

print("B transpuesta \n " + str(B.transpose()))         #Transpuesta de Matriz B

#  vectores
c = np.random.randint(10, 100, 3)
d = np.random.randint(10, 100, 3)

print("producto punto entre dos vectores c y d: " + str(np.dot(c, d)))  # producto punto
print("Producto cruz entre c y d: " + str(np.cross(c, d)))  # producto punto

C = np.array([[3, -6, 9, 0, -3, 18],
              [-1, 2, -3, 2, 11, 2],
              [2, -4, 6, -2, -12, 4]])

print("FERR de C= \n " + str(sp.Matrix(C).rref()))  # FERR de matriz C

