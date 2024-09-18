# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

numero = int(input("fatorial de : "))
resultado = 1 

for i in range(1, numero + 1):
    resultado*=i
print("fatorial de:  ", numero, "é", resultado)