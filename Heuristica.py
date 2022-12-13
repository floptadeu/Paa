from Leitor import Leitor,Pecas,exeEncaixar,exeDesperdicio,exeDesperdicioMultiplasPecas
from Interface import Interface
import time
from Permutacao import Permutacao,exePermutacao



def Heuristica(pecas):
    
    heuristicaList = list()
    

    
    
    def PegaX3Negativo(pecas,heuristicaList):
        if(len(pecas) == 1):
            heuristicaList.append(pecas[0])
            return heuristicaList
        else:
            x = 0
            novasPecas = list()
            while x < len(pecas):
                if pecas[x].x3 <= 0:
                    heuristicaList.append(pecas[x])
                    novasPecas = pecas[:x] + pecas[x+1:]
                    return X1MaiorX2(novasPecas,heuristicaList)
                x += 1
        
    def X1MaiorX2(pecas,heuristicaList):
        if(len(pecas) == 1):
            heuristicaList.append(pecas[0])
            return heuristicaList
        else:
            x = 0
            while x < len(pecas):
                if pecas[x].x1 >= pecas[x].x2:
                    heuristicaList.append(pecas[x])
                    novasPecas = pecas[:x] + pecas[x+1:]
                    return PegaX3Negativo(novasPecas,heuristicaList)
                x += 1
    

    def split_list(a_list):
        half = len(a_list)//2
        return a_list[:half]

    print(PegaX3Negativo(pecas,heuristicaList))
    Interface(pecas)
    Interface(split_list(PegaX3Negativo(pecas,heuristicaList)))
    return heuristicaList

        
vetor1 = Heuristica(Pecas(Leitor()))

desperdicio1 = exeDesperdicioMultiplasPecas(vetor1)[0]
print(desperdicio1)

vetor2 = Permutacao(Pecas(Leitor()))[0]
desperdicio2 = exeDesperdicioMultiplasPecas(vetor2)[0]
print(desperdicio2)

print("porcentagemd e acerto : ",desperdicio2/desperdicio1*100,"%")





