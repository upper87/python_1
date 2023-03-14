import math
seconds = int(input("Прошло секунд: "))

d = math.floor(seconds/86400)
cH = int((math.floor(seconds/3600) / 24))
h = (cH*24) -(math.floor(seconds/3600 ))
cM = int((math.floor(seconds/60) / 60))
m = (cM*60) -(math.floor(seconds/60 ))
cS = int((math.floor(seconds) / 60))
s = (cS*60) -(math.floor(seconds ))

print(d,"Дней", abs(h), "Часов", abs(m), "Минут", abs(s), "Секунд")