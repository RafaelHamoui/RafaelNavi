#Exercício 1:

total=0
for i in range(1,5000000):
    if i%2 == 0 and i%37==0 and i%49==0:
        total+=1
print("Total de números que satisfazem as condições simultaneamente: {}".format(total))

#Exercício 2:

import numpy as np
import math
lista=[]
for i in range(10):
    lista.append(0)
    if i%2==0:
        lista[i]=(3^i)+7*(math.factorial(i))
    else:
        lista[i]=(2^i)+4*math.log(i)

x=np.array(lista)
print(x)
maior_valor_pos=np.argmax(x)
valor_medio=x.mean().round(2)
print("Posição do maior elemento contido no vetor: {}".format(maior_valor_pos))
print("Valor médio dos elementos contidos no vetor: {}".format(valor_medio))

#Exercício 3:

dic={}
for i in range(5):
    nome=str(input("Insira o nome do aluno: "))
    nota=float(input("Insira a nota do aluno: "))
    dic[nome]=nota
max_nota=0
melhor_aluno="?"
for i in dic.items():
    if i[1]>max_nota:
        max_nota=i[1]
        melhor_aluno=i[0]

print("A melhor nota foi {0}, e foi tirada pelo {1}".format(max_nota,melhor_aluno))