from random import randint, shuffle
import matplotlib as mpl
import timeit


Dlista = [10000, 20000, 30000, 40000, 50000]


def geraLista(tam):
    lista = []
    for i in range(tam):
        lista.append(randint(0,tam))
    shuffle(lista)

    return lista

def encontraSeparacoes (v):
    sep = []
    atual = 1
    sep.append(atual)
    while atual < len(v):
        atual = (3 * atual) + 1
        sep.append(atual)
    sep.pop()
    sep.reverse()

    return sep


def shellSort (v):
    separacoes = encontraSeparacoes(v)
    for separacao in separacoes:
        for i in range(separacao, len(v), 1):
            j = i - separacao
            if v[i] < v[i - separacao]:
                while j >= 0 and v[j] > v[i]:
                    j -= separacao
                v.insert(j + separacao, v.pop(i))


mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,ym,yp,xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Pior Tempo")
    ax.plot(x,ym, label = "Melhor Tempo")
    ax.plot(x,yp, label = "Medio Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('GraficoCasos.png')

MelhorCaso = []
PiorCaso = []
MedioCaso = []

for i in Dlista:
    medio = geraLista(i)
    melhor = sorted(medio)
    pior = sorted(melhor, reverse=True)

    MelhorCaso.append(timeit.timeit("aux={}\nshellSort(aux)".format(melhor.copy()),setup="from __main__ import shellSort",number=1))
    PiorCaso.append(timeit.timeit("aux={}\nshellSort(aux)".format(pior.copy()),setup="from __main__ import shellSort",number=1))
    MedioCaso.append(timeit.timeit("aux={}\nshellSort(aux)".format(medio.copy()),setup="from __main__ import shellSort",number=1))
    print("Ordenado um i em Dlista!")


desenhaGrafico(Dlista,MedioCaso,MelhorCaso,PiorCaso)

import itertools as it
tamlista = list(it.permutations(list(range(6))))
tempoIteracao = []
listaOrig = []
for lista in tamlista:
    tempoIteracao.append(timeit.timeit("shellSort({})".format(list(lista).copy()),setup="from __main__ import shellSort",number=1))
    listaOrig.append(list(lista))

print("O tempo minimo foi de {}".format(min(tempoIteracao)))
print("lista que teve tempo minimo foi:{}".format(listaOrig[tempoIteracao.index(min(tempoIteracao))]))
print("O tempo maximo foi de {}".format(max(tempoIteracao)))
print("lista que teve tempo maximo foi:{}".format(listaOrig[tempoIteracao.index(max(tempoIteracao))]))

