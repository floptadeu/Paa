from Trapezio import Trapezio 

def Leitor():
  # print(f.readline())
  # print(f.readline())
  # print(f.read())
  f = open("trapezios.txt", "r")
  #numero de trapezios no arquivo
  trapezios = list()
  ntrapezios = int(f.readline())
  for x in range (ntrapezios):
   
    linha = f.readline()
  
    trapezios.append(linha.split())
  

  f.close()

  # print(trapezios[1][0])

  return trapezios



def Pecas(trapezios):
  pecas = list()
  for x in range (len(trapezios)):
    # print(x)
    pecas.append(Trapezio(float(trapezios[x][0]),float(trapezios[x][1]),float(trapezios[x][2])))
    # print(pecas[x])

  return pecas


# print(Pecas(Leitor())[0].superiorEsquerdo)
# print(Pecas(Leitor())[0].superiorDireito)
# print(Pecas(Leitor())[0].inferiorEsquerdo)
# print(Pecas(Leitor())[0].inferiorDireito)
# print(Pecas(Leitor())[1].superiorEsquerdo)
# print(Pecas(Leitor())[1].superiorDireito)
# print(Pecas(Leitor())[1].inferiorEsquerdo)
# print(Pecas(Leitor())[1].inferiorDireito)
# print(Pecas(Leitor())[2].superiorEsquerdo)
# print(Pecas(Leitor())[2].superiorDireito)
# print(Pecas(Leitor())[2].inferiorEsquerdo)
# print(Pecas(Leitor())[2].inferiorDireito)

def exeEncaixar(pecas):
  distancias = list()
  for x in range (len(pecas)-1):
    # print(x)
    distancias.append(pecas[x].Encaixar(pecas[x+1])[0])
  return distancias

def exeDesperdicio(pecas):
  desperdicio = list()
  for x in range (len(pecas)-1):
    # print(x)
    desperdicio.append(pecas[x].Encaixar(pecas[x+1])[1])
  return desperdicio
exeDesperdicio(Pecas(Leitor()))
# def Desperdicio(pecas):
#   ladoRetangulo = list()
#   areaTrapeziolist = list()
#   areaRetangulo = float()

#   for x in range (len(pecas)):
#      areaTrapeziolist.append(pecas[x].AreaTrapezio())
  
#   for x in range (len(pecas)-1):
#     ladoRetangulo.append(pecas[x].Encaixar(pecas[x+1])[2])
  
#   areaDosTrapezios = sum(areaTrapeziolist)
#   areaRetangulo = (sum(ladoRetangulo))*100
#   print("Lista dos lados do retangulo: " + str(ladoRetangulo))
#   print("Lista de areas dos trapezios: " + str(areaTrapeziolist))
#   print("Area dos trapezios: " + str(areaDosTrapezios))
#   print("Area Retangulo = "+ str(areaRetangulo))

#   desperdicio = areaRetangulo - areaDosTrapezios 
#   print("Desperdicio = "+ str(desperdicio))
#   print("Porcentagem do desperdicio = "+ str(desperdicio/areaRetangulo*100)+"%")

  
#   return desperdicio
# print(Desperdicio(Pecas(Leitor())))

# exeEncaixar(Pecas(Leitor()))

def exeDesperdicioMultiplasPecas(pecas):
  partesDosTrapezios = list()
  areaDosTrapezios = list()
  for x in range (len(pecas)):
    areaDosTrapezios.append(pecas[x].AreaTrapezio())
    # print("Area do trapezio "+str(x+1)+" = "+str(pecas[x].AreaTrapezio()))
  for x in range (len(pecas)-1):
    if(x==0):
      partesDosTrapezios.append(pecas[x].Encaixar(pecas[x+1])[3])
      partesDosTrapezios.append(pecas[x].Encaixar(pecas[x+1])[4])
    else:
      partesDosTrapezios.append(pecas[x].Encaixar(pecas[x+1])[4])
  ladoDoRetangulo=sum(partesDosTrapezios)
  areaDoRetangulo = ladoDoRetangulo*100
  
  # print("Lista de partes dos trapezios: " + str(partesDosTrapezios))
  # print("Area do retangulo = "+ str(areaDoRetangulo))
  # print("Area dos trapezios = "+ str(sum(areaDosTrapezios)))
  despercio = areaDoRetangulo - sum(areaDosTrapezios)
  # print("Desperdicio = "+ str(despercio))
  return despercio,areaDoRetangulo

exeDesperdicioMultiplasPecas(Pecas(Leitor()))
