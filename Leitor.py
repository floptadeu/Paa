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
    distancias.append(pecas[x].Encaixar(pecas[x+1]))
  return distancias
 

# exeEncaixar(Pecas(Leitor()))
