#kuupäev
kuud = ("jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember")
def kuu_nimi():
    kuud.split(", ")
    kuu_nimi.append(kuu_nimi)

kuupaev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
def kuupaev_sonena():
    kuupaev.split(".")
    kuupaev_sonena.append(kuupaev_sonena)

#Mündid

#Tervitused mõtisklustega

#peo eelarve
kutsutud = int(input("Mitu kutsutud: "))
tuleb = int(input("Mitu tuleb: "))
eelarve = 55

print(kutsutud*eelarve)

#Õunamahla tegemine
ounad = int(input("Õunte kogus (kg): "))
mahlapakke = round(ounad * 0.4 / 3,)
print(mahlapakke)

#bänner
kordus = int(input("Mitu korda kuvada: "))
banner = input("Sisestage reklaamilause: ")
for i in range(kordus):
    print(banner.upper())

#Tahvli juurde
from datetime import *
print(datetime.now().day-1)



fail = open("edm.txt",encoding="utf-8")
laulud = []

#Jukebox

#sissetulekud

#jänesevanemate mure ver.3

#ülikooli vastuvõetud

#ounad
import random
mitu = int(input("Mitu pöialpoissi tahab õunu?: "))

ounad = 0
for i in range(mitu):
    suv=random.randint(1,2)
    ounad+=suv
    print(suv)
print(f"Alles jäi {12-ounad} õuna")

#male

#täringud

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