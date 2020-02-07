# -*- coding: utf-8 -*-
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"

#What is the length of the string variable verse?
print(len(verse))
#What is the index of the first occurrence of the word 'and' in verse?
longitud = len(verse)
index = verse.find("and",0,longitud)
print(index)
#What is the index of the last occurrence of the word 'you' in verse?

index = verse.rfind("you",0,longitud)
print(index)
#What is the count of occurrences of the word 'you' in the verse?
print(verse.count("you"))