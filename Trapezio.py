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
            if(self.inferiorEsquerdo[0] >= abs(pecaB.inferiorDireito[0]-pecaB.superiorDireito[0])):
                return True
            else:
                #Baixo
                return False
        elif(pecaB.PontaEmCimaNaDireta()):
            if(abs(pecaB.superiorDireito[0]-pecaB.inferiorDireito[0])>=abs(self.inferiorEsquerdo[0])):
                return True
            else:
                return False
        else:
            return False
    def Encaixar(pecaA,pecaB):
        baseRetangulo = float()
        distanciaDeVertices = float()
        # print("AQUIIIIIIIIIIIIIIIIIII")
        # print(pecaA.OndeToca(pecaB))
        if(pecaA.OndeToca(pecaB)):
            #Tocam em Cima

            baseRetangulo = pecaB.superiorDireito[0]+pecaA.ExtremaDireita()+abs(pecaB.ExtremaEsquerda())
            print("Base do Retangulo = "+ str(baseRetangulo))
            distanciaDeVertices = pecaB.superiorDireito[0]
            print("Distancia dos vertices de A e B ="+ str(distanciaDeVertices))
        else:
            #Tocam em baixo

            baseRetangulo = pecaB.inferiorDireito[0]+pecaA.ExtremaDireita()+abs(pecaB.ExtremaEsquerda())
            print("Base do Retangulo = "+ str(baseRetangulo))

       
            distanciaDeVertices = pecaB.inferiorDireito[0] +( pecaA.superiorEsquerdo[0]-pecaA.inferiorEsquerdo[0])
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

        return distanciaDeVertices









