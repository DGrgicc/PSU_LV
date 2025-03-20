import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mtcars = pd.read_csv(r'Downloads\mtcars.csv')

sort_cars = mtcars.sort_values(by=['mpg'], ascending=False).head(5)
print(sort_cars['car'])

potrosnja_cilindri = mtcars[mtcars['cyl'] == 8].sort_values(by=['mpg'], ascending=True).head(3)
print(potrosnja_cilindri['car'])

cyl6 = mtcars[mtcars['cyl'] == 6]
srednjaPotrosnja = cyl6['mpg']. median()
print(srednjaPotrosnja)

cyl4 = mtcars[mtcars['cyl'] == 4]
cyl4 = mtcars[(mtcars['wt'] > 2.0) & (mtcars['wt'] < 2.2)]
srednjaPotrosnja = cyl4['mpg'].median()
print(srednjaPotrosnja)

rucni = mtcars[mtcars["am"] == 1].count()
automatik = mtcars[mtcars["am"] == 0].count()
print("Auto",rucni["am"])
print("Manual",automatik["am"])

auto_jak = mtcars[mtcars["am"] == 1]
auto_jak = auto_jak[auto_jak["hp"] > 100].count()
print("Auto + 100hp+  = ",auto_jak["hp"])

mtcars['wt_kg'] = mtcars['wt'] * 1000
print(mtcars['wt_kg'])


filtered_mtcars = mtcars[mtcars['cyl'].isin([4, 6, 8])]
mean_mpg = filtered_mtcars.groupby('cyl')['mpg'].mean()

plt.figure(figsize=(10, 6))
plt.bar(mean_mpg.index, mean_mpg.values)

plt.title('Potrošnja goriva automobila s 4, 6 i 8 cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja goriva (mpg)')

plt.show()




filtered_mtcars = mtcars[mtcars['cyl'].isin([4, 6, 8])]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
mean_mpg = filtered_mtcars.groupby('cyl')['mpg'].mean()
plt.bar(mean_mpg.index, mean_mpg.values)
plt.title('Potrošnja goriva automobila s 4, 6 i 8 cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja goriva (mpg)')

plt.subplot(1, 2, 2)
plt.boxplot([filtered_mtcars[filtered_mtcars['cyl'] == i]['wt'] for i in [4, 6, 8]], 
            labels=[4, 6, 8])
plt.title('Distribucija težine automobila s 4, 6 i 8 cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina automobila')

plt.tight_layout()
plt.show()


mtcars['am'] = mtcars['am'].map({0: 'Automatski', 1: 'Ručni'})

mean_mpg_trans = mtcars.groupby('am')['mpg'].mean()

plt.figure(figsize=(8, 6))
plt.bar(mean_mpg_trans.index, mean_mpg_trans.values, color=['blue', 'green'])
plt.title('Usporedba potrošnje goriva između automobila s ručnim i automatskim mjenjačem')
plt.xlabel('Vrsta mjenjača')
plt.ylabel('Potrošnja goriva (mpg)')

plt.show()


plt.figure(figsize=(10, 6))

plt.scatter(mtcars[mtcars['am'] == 'Ručni']['qsec'], 
            mtcars[mtcars['am'] == 'Ručni']['hp'], 
            color='blue', label='Ručni mjenjač')


plt.scatter(mtcars[mtcars['am'] == 'Automatski']['qsec'], 
            mtcars[mtcars['am'] == 'Automatski']['hp'], 
            color='green', label='Automatski mjenjač')

plt.title('Odnos ubrzanja i snage za automobila s ručnim i automatskim mjenjačem')
plt.xlabel('Ubrzanje (qsec)')
plt.ylabel('Snaga (hp)')
plt.legend()

plt.show()




