#M.Kuusemae
#KT2h7
#21.11.22

failike = open("felix.txt","r")

kassid = failike.readlines()
for kass in kassid:
    ni,va,sa = kass.split()

valikvarv = input("Värvus: ")
if valikvarv==va:
    print(f"Saba keskmine pikkus on {sa}")
