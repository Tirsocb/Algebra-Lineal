import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# funcion para agregar la matriz aumentada a una matriz cualquiera (mxm)
def Aumentar(a):
    valor = 'h' + str(sp.Matrix(a).shape)
    identidad = sp.eye(int(valor[2]))
    for x in range(0, int(valor[2])):
        identidad = identidad.col_insert(x, sp.Matrix(a).col(x))
    return identidad


#  matrices
A = np.array([[1, 1, 0],
              [1, 0, 1],
              [0, 1, 0]])
B = np.array([[2, 0, 1],
              [1, 1, -4],
              [3, 7, -3]])
C = np.array([[1, 1, 0],
              [1, 0, 1],
              [0, 1, 0],
              [0, 1, 0]])

print("MATRICES INVERSAS \n")

# Inversas con Numpy
invnumA = np.linalg.inv(A)
invnumB = np.linalg.inv(B)
# invnumc = np.linalg.inv(C)
print("inversa A con numpy: \n " + str(invnumA), "\n")
print("inversa B con numpy: \n " + str(invnumB), "\n")
# print("inversa C con numpy: \n " + str(invnumc))

#  Inversas con Sympy
invsymA = sp.Matrix(A).inv()
invsymB = sp.Matrix(B).inv()
# invsymC = sp.Matrix(C).inv()

print("inversa A con sympy: \n " + str(invsymA), "\n")
print("inversa B con sympy: \n " + str(invsymB), "\n")
# print("inversa C con sympy: \n " + str(invsymC))
print(
    "numpy utiliza floats para mostrar los valores de las matrices, ademas las imprime en varias lineas a comparacion de sympy que utiliza fracciones e imprime las matrices en una sola linea")

#  Inversas con FERR
invferA = Aumentar(A).rref()
invferB = Aumentar(B).rref()
# invferC = Aumentar(C).rref()


print("inversa A con FERR: \n " + str(invferA))
print("inversa B con FERR: \n " + str(invferB))
# print("inversa C con FERR: \n " + str(invferC))
print(" ")
print(" RANGO \n")
# Rango
Ar = np.linalg.matrix_rank(A)
Br = np.linalg.matrix_rank(B)
Cr = np.linalg.matrix_rank(C)

print("Rango Matriz A: " + str(Ar))
print("Rango Matriz B: " + str(Br))
print("Rango Matriz C: " + str(Cr))
print(
    "Las matrices A B y C tienen un rango de 3 lo cual signific aque tienen 3 lineas linealmente independientes, no se puede establecer una combinacion lineal entre ellas")
print(" ")

print("ESPACIOS NULOS Y NULIDAD \n")

NumcolsA = A.shape[1]
NumcolsB = B.shape[1]
NumcolsC = C.shape[1]

NulidadA = Ar - NumcolsA
NulidadB = Br - NumcolsB
NulidadC = Cr - NumcolsC

print("Nulidad A: " + str(NulidadA))
print("Nulidad B: " + str(NulidadB))
print("Nulidad C: " + str(NulidadC), "\n ")

# Funciones

print(" FUNCIONES LINEALES \n ")


def f(x: object) -> object:
    return 1 - x


def g(x):
    return x - 4


def h(x):
    return x + 4


def j(x):
    return 6 - x


x = range(-10, 10)

plt.plot(x, [f(i) for i in x])
plt.plot(x, [g(i) for i in x])
plt.plot(x, [h(i) for i in x])
plt.plot(x, [j(i) for i in x])

plt.axhline(0, color="black", )
plt.axvline(0, color="black")
# plt.axhline(np.arange(2.5, 5.0, 7.5, 10.0))
# Especificamos los limites de los ejes.
plt.xlim(-11, 11)
plt.ylim(-11, 11)

# cuadricula
plt.grid(None, 'major', 'both')

# Titulo
plt.title('Funciones Lab 3')

#comando para guardar la grafica en la misma carpeta del proyecto.
plt.savefig("output.png")

# Mostramos el grafico realizado.
plt.show()
