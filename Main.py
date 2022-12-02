from Trapezio import Trapezio 

pecaA = Trapezio(50,30,-10)

pecaB = Trapezio(50,30,10)
pecaC = Trapezio(50,-30,-10)


pecaA.Encaixar(pecaB)
pecaA.Encaixar(pecaC)
pecaB.Encaixar(pecaC)
