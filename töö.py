#murelikud lapsevanemad
mehis = int(input("pls ring arv: "))
ring = 0
porgand = 0
while ring<mehis:
    ring +=1
    if ring%2==0:
        porgand+=ring
print(f"porgand: {porgand}")



#äratus
aratus = int(input("Mitu korda äratada: "))
for i in range(aratus):
    print("Tõuse ja sära!")

#bussid
import math

inimeste_arv = int(input("inimeste arv: "))
kohtade_arv = int(input("kohtade arv: "))
bussid = math.ceil(inimeste_arv/kohtade_arv)
print(f"Busse vaja: {bussid}")
inimesed = inimeste_arv%kohtade_arv
if inimesed==0:
    print(f"viimases bussis: {kohtade_arv}")
else:
    print(f"viimases bussis: {inimesed}")


#pilved




#aasta liblikas
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta)+lause_keskosa+liblikas

print(lause)
#tervitus
print("Tere, maailm!")