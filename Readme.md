**Zadatak 1**
Ovaj kod implementira linearnu regresiju koristeći nadgledano učenje. Prvo se definira funkcija non_func(x) koja generira stvarne vrijednosti y prema danoj matematičkoj funkciji koja uključuje trigonometrijske funkcije. Zatim, funkcija add_noise(y) dodaje šum na te stvarne vrijednosti kako bi simulirala mjerenja u stvarnom svijetu. Nakon toga se inicijalizira linearni regresijski model, trenira se na skupu podataka za obuku (xtrain, ytrain), a model predviđa vrijednosti za testni skup podataka (xtest). Izračunava se srednja kvadratna pogreška (MSE) za evaluaciju točnosti modela. Na kraju, vizualiziraju se stvarne i predviđene vrijednosti kako bi se procijenila učinkovitost modela. Scikit-learn se koristi za inicijalizaciju modela, treniranje, predviđanje i evaluaciju.

**Zadatak 2**
Ovaj kod implementira polinomijalnu regresiju. Funkcija non_func(x) generira stvarne vrijednosti y prema trigonometrijskoj funkciji, dok add_noise(y) dodaje šum. Zatim se koriste PolynomialFeatures za kreiranje polinomijalnih značajki, a model se trenira s linearnom regresijom na proširenim podacima. Predviđanja se izvode na testnom skupu, a model se evaluira pomoću srednje kvadratne pogreške (MSE). Vizualiziraju se stvarne vrijednosti, predviđanja i podaci za obuku. Scikit-learn se koristi za transformaciju podataka, treniranje, predviđanje i evaluaciju modela.

**Zadatak 4**
    U databeseu je dostupno 4843 mjerenja.
      Tipovi pojedinih stupaca u dataframe-u su:
        name: string (ime automobila)
        year: integer (godina proizvodnje automobila)
        selling_price: float (logaritam cijene u indijskim rupijama)
        km_driven: integer (prijeđeni broj kilometara)
        fuel: string (tip motora: Diesel, Petrol, CNG, LPG)
        seller_type: string (prodavač: individual/dealer)
        transmission: string (tip mjenjača: automatic/manual)
        owner: integer (broj prethodnih vlasnika)
        mileage: float (potrošnja automobila)
        engine: integer (zapremnina motora u cm3)
        max_power: float (maksimalna snaga motora u bhp)
        seats: integer (broj sjedala)
  
    
**Zadatak 5**
Utjecaji su:
    1. Dodavanje relevantnih značajki
    2. Dodavanje nepotrebnih značajki
    3. Uklanjanje relevantnih značajki
    4. Smanjenje broja značajki
