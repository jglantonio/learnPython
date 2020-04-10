# -*- coding: utf-8 -*-
# if

cartera = 0
banco = 100
if cartera < 5 :
    cartera+=10
    banco-=10

print(banco,cartera)

# if else

if banco & 2 == 0 :
    print("Es par : "+str(banco))
else :
    print("Es impar : "+str(banco))

# if else

tiempo = "Verano"

if tiempo == "primavera" :
    print("Es primavera")
elif tiempo == "otoño" :
    print("Es primavera")
elif tiempo == "Verano" :
    print("Es verano")
elif tiempo == "Invierno" :
    print("Es invierno")
