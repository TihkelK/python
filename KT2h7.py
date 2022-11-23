#M.Kuusemae
#KT2h7
#21.11.22
import re

failike = open("felix.txt","r")

saba = []

valikvarv = input("Värvus: ")
for line in failike:
    ni,va,sa = line.split(" ")
    if va==valikvarv:
        saba.append(int(sa))
kk = sum(saba)
uu = len(saba)
keskmine = round(kk/uu)
print(f"{valikvarv} värvi kasside keskmine saba pikkus on {keskmine}cm.")