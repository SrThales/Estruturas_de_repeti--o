#O código a seguir tem o objetivo de exercitar estruturas de repetição, tanto for como while,
#através da criação da tabuada de 3


#Utilizando for:
i = 3

print('A tabuada do número 3 é:')

for j in range (1, 11):
    print(i, 'x', j, '=', i*j)
    

#Utilizando while:

k = 1

while k < 11:
    print(i, 'x', k, '=', i*k)
    k += 1
