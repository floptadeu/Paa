class Trapezio(object):
    x1 = float()
    x2 = float()
    x3 = float()
    superiorEsquerdo = []
    superiorDireito = []
    inferiorEsquerdo = []
    inferiorDireito = []
    altura = 100

    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

        # coordenadas
        self.superiorEsquerdo = [0,100]
        self.superiorDireito = [x1,100]
        if(x3< 0 and  x2<=0  ):
            self.inferiorEsquerdo = [x3 +    x2,0]
        else:
            self.inferiorEsquerdo = [x3,0]

        if(x3> 0 and x2>0  ):
            self.inferiorDireito = [x2 + x3,0]
        else:
            self.inferiorDireito = [x2,0]


    def TamanhoDaBase(self):
        return self.inferiorDireito[0] - self.inferiorEsquerdo[0]
    
    def AreaTrapezio(self):
        return ((self.x1+self.TamanhoDaBase())*self.altura)/2
    def ToquePecaBPorCima(self,pecaB):
        return 
    
    def ExtremaDireita(self):
        return max(self.inferiorDireito[0],self.superiorDireito[0])

    def ExtremaEsquerda(self):
        return min(self.inferiorEsquerdo[0],self.superiorEsquerdo[0])

    def PontaEmCimaNaDireta(self):
        return self.superiorDireito[0]>=self.inferiorDireito[0]
    
    def PontaEmCimaNaEsquerda(self):
        #Como e para valores negativos o lado esquerdo inferior sera ponta se for menor que 0
        return self.superiorEsquerdo[0]<=self.inferiorEsquerdo[0]
    # def distanciaNoEixoX(self):
    # def DistanciaNaDireita(self):
        
    # def DistanciaNaEsquerda(self):
    #     return
    
    
    def OndeToca(self,pecaB):
        if(self.PontaEmCimaNaEsquerda() and pecaB.PontaEmCimaNaDireta()):
            #Cima
            return True
        elif(self.PontaEmCimaNaEsquerda()):
            # nesse caso a distancia do lado inferior direito ja e o tamanho da ponta de cima a esquerda
            if(self.inferiorEsquerdo[0] >= pecaB.inferiorDireito[0]-pecaB.superiorDireito[0]):
                return True
            else:
                #Baixo
                return False
           
        elif(pecaB.PontaEmCimaNaDireta()):
            if(pecaB.superiorDireito[0]-pecaB.inferiorDireito[0]>=-(self.inferiorEsquerdo[0])):
                return True
            else:
                return False
        else:
            return False
    def Encaixar(pecaA,pecaB):
        baseRetangulo = float()
        distanciaDeVertices = float()

        if(pecaA.OndeToca(pecaB)):
            #Tocam em Cima

            baseRetangulo = pecaB.superiorDireito[0]+pecaA.ExtremaDireita()-(pecaB.ExtremaEsquerda())
            print("Base do Retangulo = "+ str(baseRetangulo))
            distanciaDeVertices = pecaB.superiorDireito[0]
            print("Distancia dos vertices de A e B ="+ str(distanciaDeVertices))
        else:
            #Tocam em baixo
            baseRetangulo = pecaB.inferiorDireito[0]+pecaA.ExtremaDireita()-(pecaB.ExtremaEsquerda())
            print("Base do Retangulo = "+ str(baseRetangulo))
            distanciaDeVertices = pecaB.inferiorDireito[0] - pecaA.ExtremaEsquerda() 
            print("Dinstancia dos vertices de A e B = "+ str(distanciaDeVertices))
        
        areaRetangulo = baseRetangulo*100
        print("Area Retangulo = "+ str(areaRetangulo))

        areaTrapezioA = pecaA.AreaTrapezio()
        print("Area Trapezio A = "+ str(areaTrapezioA))
        areaTrapezioB = pecaB.AreaTrapezio()
        print("Area Trapezio B = "+ str(areaTrapezioB))

        areaTotal = areaTrapezioA + areaTrapezioB
        print("Area dos dois trapezios "+ str(areaTotal))
        desperdicio = areaRetangulo - areaTotal 
        print("Desperdicio = "+ str(desperdicio))

        print("Porcentagem do desperdicio = "+ str(desperdicio/areaRetangulo*100)+"%")

     


    
        
        

# def CoordenadasDoPano(trapezio):
#     # coordenadas
#     superiorEsquerdo = [0,100]
#     superiorDireito = [trapezio.x1,100]
#     if(trapezio.x3< 0 and trapezio.x2<=0  ):
#         inferiorEsquerdo = [trapezio.x3+trapezio.x2,0]
#     else:
#         inferiorEsquerdo = [trapezio.x3,0]

#     if(trapezio.x3> 0 and trapezio.x2>0  ):
#          inferiorDireito = [trapezio.x2 + trapezio.x3,0]
#     else:
#         inferiorDireito = [trapezio.x2,0]


#     coordenadas = [superiorEsquerdo,superiorDireito,inferiorEsquerdo,inferiorDireito]

#     return coordenadas

# def AreaTrapezio(coordenadas):
#     b1 = coordenadas[1][0]
#     print(b1)
#     b2 = coordenadas[3][0]-coordenadas[2][0]
#     print(b2)
#     return ((b1+b2)*100)/2

# trapezio1 = Trapezio(50,30,-10)
# t1=CoordenadasDoPano(trapezio1)
# print(t1)
# print(AreaTrapezio(t1))
# trapezio2 = Trapezio(50,30,10)
# t2=CoordenadasDoPano(trapezio2)
# print(t2)
# print(AreaTrapezio(t2))
# trapezio3 = Trapezio(50,-30,-10)
# t3=CoordenadasDoPano(trapezio3)
# print(t3)
# print(AreaTrapezio(t3))

# def encaixe(tA,tB):
    
   
#     if (tA.x1 == tA.x2):
#        pontoA = 0
#        #tanto faz bro
#     elif (tA.x1 > tA.x2) : 
#         pontoA = tA.x1
#         #ponto em cima mais a frente
#     else:
#         pontoA = tA.x2
#         #ponto em baixo mais atras
#     if (tB.x3 == 0) :
#         pontoB = 0
#         #tanto faz bro
#     elif(tB.x3 < 0 ):
#         pontoB = tB.x3
#         #ponto em baixo mais a frente
#     else:
#         pontoB = 0
#         #ponto em cima mais atras


# def TipoTrapezio(t):
  
#     # montagem
#     # 1º passo lado a esquerda de A
#     if(t.x3<= 0 and t.x2>0  ):
#         ladoSuperior = x3
#         ladoInferior = -x3 
#     else:
#         ladoSuperior = -x3
#         ladoInferior = x3

#     # 2º passo lado a direita de B
    
#     if(x1-x2>=0):
#         ladoSuperior =  (x1-x2)
#         ladoInferior =  -(x1-x2)
#     else:
#         ladoSuperior =  -(x1-x2)
#         ladoInferior =  (x1-x2)
    










