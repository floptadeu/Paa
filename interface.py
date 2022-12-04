import numpy as np 
import cv2
from Trapezio import Trapezio
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from Leitor import Leitor,Pecas,exeEncaixar

pts = list()


pecas = Pecas(Leitor())

print(pecas)

pecaA = Trapezio(50,30,-10)

pecaB = Trapezio(50,30,10)

distanciasDeVertices = exeEncaixar(pecas)

distanciasDeVertices.insert(0,0)
print(distanciasDeVertices)

ix = 800
iy = 100
image = np.zeros((iy, ix, 3), np.uint8)

isClosed = True
color = (255, 0, 0)
thickness = 2

pontoReferencia = float(ix/2)
for w in range (len(pecas)):
   #ponto de referencia e o ponto superior esquerdo da peca
   
    pontoReferencia = pontoReferencia - distanciasDeVertices[w]
    print(pontoReferencia)
    #Na biblioteca do opencv, o eixo y cresce para baixo
    
    pts.append(np.array([[pecas[w].inferiorEsquerdo[0]+pontoReferencia, 100], [pontoReferencia, 0],
            [pecas[w].superiorDireito[0]+pontoReferencia,0], [pecas[w].inferiorDireito[0]+pontoReferencia, 100]],
            np.int32))
    # pts.append(np.array([[pontoReferencia+ix/2, pecas[w].superiorEsquerdo[1]], [pecas[w].superiorDireito[0]+ix/2+pontoReferencia, pecas[w].superiorDireito[1]],
    #         [pecas[w].inferiorDireito[0]+ix/2+pontoReferencia, pecas[w].inferiorDireito[1]], [pecas[w].inferiorEsquerdo[0]+ix/2+pontoReferencia, pecas[w].inferiorEsquerdo[1]]],
    #         np.int32))

    print(pontoReferencia)
    print(pts[w])
 
    cv2.polylines(image, [pts[w]],
                     isClosed, color, thickness)

#cv2.polylines(image, [pts[0].reshape((-1, 1, 2))],
#                      isClosed, color, thickness)

cv2.imshow('Black Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()