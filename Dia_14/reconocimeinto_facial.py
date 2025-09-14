# requiere instalar visual studio comunity
# durante la instalación agregar Desktop Development with c++
# paquetes a instalar cmake, dlib, face-recogniton, numpy, opencv-python
# tuve que instalar cmake desde https://cmake.org/download/ y desinstalar cmake pip uninstall cmake
# para poder instalar dlib y face-recognition
import cv2
import face_recognition as fr

foto_control = fr.load_image_file('Yo_control.jpg')
#foto_control = fr.load_image_file('Yo.jpg')
foto_prueba = fr.load_image_file('Yo_prueba.jpg')

# pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control,cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba,cv2.COLOR_BGR2RGB)

# localizar caras
lugar_cara_control = fr.face_locations(foto_control)[0]
cara_codificada_control = fr.face_encodings(foto_control)[0]
lugar_cara_prueba = fr.face_locations(foto_prueba)[0]
cara_codificada_prueba = fr.face_encodings(foto_prueba)[0]

# mostrar rectangulo
cv2.rectangle(foto_control, (lugar_cara_control[3], lugar_cara_control[0]),
              (lugar_cara_control[1], lugar_cara_control[2]),(0,255,0),2)
cv2.rectangle(foto_prueba, (lugar_cara_prueba[3], lugar_cara_prueba[0]),
              (lugar_cara_prueba[1], lugar_cara_prueba[2]),(0,255,0),2)

# comparar
resultado = fr.compare_faces([cara_codificada_control],cara_codificada_prueba)
print(resultado)

# mostrar imagenes
#cv2.imshow('Control',foto_control)
#cv2.imshow('Prueba',foto_prueba)

distancia = fr.face_distance([cara_codificada_control],cara_codificada_prueba)
print(distancia)

# mantener el programa abiero
cv2.waitKey(0)
