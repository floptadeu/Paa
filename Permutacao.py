from itertools import permutations
from Trapezio import Trapezio
from Leitor import Leitor,Pecas,exeEncaixar,exeDesperdicio,exeDesperdicioMultiplasPecas
from Interface import Interface
import time

def permutacao(pecas):
    tempoInicial = time.time()
   
    desperdicioIndv = list()
    desperdicioPerm = list()
    
    guia = [1,2,3]
    permGuia = permutations(guia)
    permPecas = permutations(pecas)
    salvaPerm = 0
    menorDesperdicio = 0
#for x in permGuia:
#print(x)

#desperdicio de cada peca individualmente
#for x in permPecas:
    
#desperdicioIndv.append((exeEncaixar(x)))
# print(desperdicioIndv)
# print(permGuia)

#desperdicio total por permutacao
    y = 0
    for x in permPecas:
        desperdicioPerm.append((exeDesperdicioMultiplasPecas(x)))
        if(desperdicioPerm[y]== min(desperdicioPerm)):
            # print("Menor desperdicio ate agora ")
            menorDesperdicio = desperdicioPerm[y]
            # print( menorDesperdicio)
            # print("Permutacao: ")
            salvaPerm = x
        # print(y)
        y = y + 1

    
    print(menorDesperdicio)
    tempoFinal = time.time()
    tempoDeExecucao = tempoFinal - tempoInicial
    print("Tempo de execucao: " + str(tempoDeExecucao) + " segundos")
    return salvaPerm,menorDesperdicio,tempoDeExecucao

pecas = Pecas(Leitor())
permutacao(pecas)
Interface(permutacao(pecas)[0])