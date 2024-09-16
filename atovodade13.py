# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.

num = int(input("digite o número"))

if num >0:
    print ("é um número positivo")
elif num ==0:
    print ("número neutro (0)")
elif num <0:
    print ("é um número negativo")   