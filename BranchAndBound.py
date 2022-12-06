from itertools import permutations
from Trapezio import Trapezio
from Leitor import Leitor,Pecas,exeEncaixar,exeDesperdicio,exeDesperdicioMultiplasPecas
from Interface import Interface
import time
from Permutacao import Permutacao,exePermutacao


global melhor
global arranjo

melhor = float('inf')


def BranchAndBound(remaining, candidate=[]):
    global melhor
    global arranjo

    if len(remaining) == 0:
        if exeDesperdicioMultiplasPecas(candidate)[0] < melhor:
            melhor = exeDesperdicioMultiplasPecas(candidate)[0]
            arranjo = candidate
        # print(candidate)
 
    for i in range(len(remaining)):
 
        newCandidate = candidate + [remaining[i]]
        newRemaining = remaining[0:i] + remaining[i+1:]

        if exeDesperdicioMultiplasPecas(newCandidate)[0] <= melhor:
            BranchAndBound(newRemaining, newCandidate)
    return arranjo



pecas= Pecas(Leitor())
Interface(BranchAndBound(pecas))
print(melhor)
print(arranjo)
# print(permutacao(arr))
