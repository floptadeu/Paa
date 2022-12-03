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




def exeEncaixar(trapezios):
  pecas = list()
  print(trapezios)
  for x in range (len(trapezios)):
    print(x)
    pecas.append(Trapezio(float(trapezios[x][0]),float(trapezios[x][1]),float(trapezios[x][2])))
    print(pecas[x])
  for x in range (len(pecas)-1):
    pecas[x].Encaixar(pecas[x+1])


exeEncaixar(Leitor())