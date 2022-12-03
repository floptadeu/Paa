import numpy as np 
import cv2
from Trapezio import Trapezio
import matplotlib.pyplot as plt
import matplotlib.patches as patches

pecaA = Trapezio(50,30,-10)

pecaB = Trapezio(50,30,10)
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

y = np.array([pecaA.inferiorEsquerdo[0],pecaA.superiorEsquerdo[0],pecaA.superiorDireito[0],pecaA.inferiorDireito[0]])
x = np.array([pecaA.inferiorEsquerdo[1],pecaA.superiorEsquerdo[1],pecaA.superiorDireito[1],pecaA.inferiorDireito[1]])
plt.figure(x, y)
plt.show()



# img = np.zeros((4000, 4000, 3), dtype = "uint8") 
# pts = pts.reshape((-1,1,2))

# cv2.polylines(img,[pts],True,(255,0,0),8)

# cv2.imshow('dark', img) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows() 



# # Drawing Shapes

# def ImageProcessing():
#     image = np.zeros((512, 512, 3), np.uint8)

#     cv2.line(image, (20, 200), (200, 20), (0, 0, 255), 5)
#     cv2.rectangle(image, (200, 60), (20, 200), (255, 0, 0), 3)
#     cv2.circle(image, (80, 80), 50, (0, 255, 0), 4)

#     mytext = "Hello World"

#     cv2.putText(image, mytext, (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

#     cv2.imshow('Black Image', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# ImageProcessing()