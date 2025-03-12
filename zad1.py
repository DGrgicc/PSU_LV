import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open(r"C:\Users\student\Desktop\lv\mtcars.csv", "rb"), 
                  usecols=(1, 2, 3, 4, 5, 6), delimiter=",", skiprows=1)


x = data[:, 0]  
y = data[:, 3]  
wt = data[:, 5]  
plt.scatter(x, y, s = wt*10)
plt.xlabel("mpg")
plt.ylabel("hp")
plt.title("mpg vs hp")
plt.show()

print(np.min(x))
print(np.max(x))
print(np.mean(x))

if np.any(data[:, 1] > 5):  
    print(np.min(x))
    print(np.max(x))
    print(np.mean(x))
