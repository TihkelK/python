#M.Kuusemäe
#25.10.22
#harjutus05



#Vanused
vanused = ["9","15","18","21"]



#Duplikaadid
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
puh_opilased = []
for opilane in opilased:
    if opilane not in puh_opilased:
        puh_opilased.append(opilane)

print(puh_opilased)

print()


#Õpilased
jrk = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]

#kuva nimed
for opilane in opilased:
    print(f"{jrk}. {opilane}")
    jrk+=1

#kasutaja valib mitmendat muuta INT
niminr = int(input("Mitmendat nime muuta?: "))

#kasutaja valib uue nime STRING
kasutajavalik = input("Uus nimi: ")
del opilased[niminr-1]

#uus nimi lisatakse nimekirja
opilased.insert(niminr-1,kasutajavalik)

#näita uut nimekirja
print(opilased)




"""
#Nimede lisamine loendisse
print("----------")
nimed = []
for i in range(5):
    nimi = input("Lisa nimi: ")
    nimed.append(nimi)

print(f"Viimane nimi: {nimed[-1]}")
nimed.sort()
print(nimed)
"""
