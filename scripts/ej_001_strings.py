# -*- coding: utf-8 -*-
verse = "White river You stole my eyes Never gave them back You tried to kiss me  And sent a shiver Round my neck White river Wet golden shrine You sold my mind and Tried to kill me Sent a shiver down my spine "
longitud = len(verse)
print(longitud)
index = verse.find("stole",0,longitud)
print(index)
index = verse.rfind("river",0,longitud)
print(index)
veces = verse.count("river")
print(veces)
anhos = 10;
print("Tengo {} años".format(anhos))