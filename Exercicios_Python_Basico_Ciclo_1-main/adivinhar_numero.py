from random import randint

numero = randint (1,10)

num = int (input("Digite um número: "))

while num != numero: 
    print("Número errado")
    num =int (input ("Digite de novo: "))

print ('Parabéns você acetou o número ')
