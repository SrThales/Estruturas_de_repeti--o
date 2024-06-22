#O objetivo do código abaixo é exercitar as estruturas de repetição for e while ao passo que 
#consigo ler 5 notas e informar a média entre elas

#Utilizando for:

total = 0
for nota in range (1, 6):
    print('Digite a nota', nota)
    n_nota = float(input())
    total = total + n_nota
    
media = total/5

print('A média das cinco notas é:', media)

#Utilizando while:

total = 0
i = 1
while i < 6:
    print('Digite a nota', i)
    m_nota = float(input())
    total = total + m_nota
    i += 1
    
media = total/5

    