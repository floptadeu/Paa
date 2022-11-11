class Trapezio:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

def CoordenadasDoPano(trapezio):
    # coordenadas
    superiorEsquerdo = [0,100]
    superiorDireito = [trapezio.x1,100]
    if(trapezio.x3< 0 and trapezio.x2<=0  ):
        inferiorEsquerdo = [trapezio.x3+trapezio.x2,0]
    else:
        inferiorEsquerdo = [trapezio.x3,0]

    if(trapezio.x3> 0 and trapezio.x2>0  ):
         inferiorDireito = [trapezio.x2 + trapezio.x3,0]
    else:
        inferiorDireito = [trapezio.x2,0]


    coordenadas = [superiorEsquerdo,superiorDireito,inferiorEsquerdo,inferiorDireito]

    return coordenadas

def AreaTrapezio(coordenadas):
    b1 = coordenadas[1][0]
    print(b1)
    b2 = coordenadas[3][0]-coordenadas[2][0]
    print(b2)
    return ((b1+b2)*100)/2

trapezio1 = Trapezio(50,30,-10)
t1=CoordenadasDoPano(trapezio1)
print(t1)
print(AreaTrapezio(t1))
trapezio2 = Trapezio(50,30,10)
t2=CoordenadasDoPano(trapezio2)
print(t2)
print(AreaTrapezio(t2))
trapezio3 = Trapezio(50,-30,-10)
t3=CoordenadasDoPano(trapezio3)
print(t3)
print(AreaTrapezio(t3))


# def encaixe(t1,t2,c1,c2):



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
    










