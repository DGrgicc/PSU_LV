lista = []
while (True):
    unos = input()
    if (unos == "Done"):
        break
    try:
        lista.append(float(unos))
    except:
        print("Neispravan unos pokusaj ponovno!")    

if lista:
    print("Broj unosa je: ", len(lista))
    print("Srednja vrijednost: ",sum(lista)/len(lista))
    print("Minimalna vrijednost: ",min(lista))
    print("Maksimalna vrijednost: ",max(lista))
    lista.sort()
    print ("Sortirana lista",lista)
