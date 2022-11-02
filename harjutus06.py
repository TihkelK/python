#M.Kuusemäe
#27.10.22
#tekstifailiga mässamine

failike=open("s6pru_l6ustaraamatus.txt","r")

reformikad = 0
kesikud = 0
erakonnad = []

for i in failike.readlines():
    ee,pe,er,kyl = i.split(" ")
    if er=="RE":
        reformikad+=1
    elif er=="KE":
        kesikud+=1
    if er not in erakonnad:
        erakonnad.append(er)
    with open('kirjutamine.txt','a') as fail_kirjutamiseks:
         fail_kirjutamiseks.write(ee + " " +pe +"\n")

print(erakonnad)




print(f"Refomikad kokku {reformikad}")
print(f"Kesikud kokku {kesikud}")
print(f"Erakondi kokku {len(erakonnad)}")
failike.close()


#faili kirjutamine

