#M.Kuusemäe
#17.10.22
#harjutus03


#tundide ajad
a1,a2 = "8:30","14:15"
h1,m1 = a1.split(":")
minut1 = int(h1)*60+int(m1)
h2,m2 = a2.split(":")
minut2 = int(h2)*60+int(m2)
ajavahe = minut2-minut1
print(ajavahe)
vanaisa = 30/56+2
hh = ajavahe//60
mm = ajavahe%60
print(f"Ajavahe on {hh}:{mm}")



print(minut1)


#email
email = "agsgdfh@dsfkbmdpb.rer"
print("@" in email)



#vandumine
tekst = input("Ütle Kurat küll!:")
print(tekst.lower().replace("kurat","***"))
