import numpy as np
import matplotlib.pyplot as plt

img = plt.imread(r"C:\Users\student\Desktop\lv\tiger.png")
img = img[:,:,0].copy()
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(np.rot90(img), cmap="gray")
plt.imshow(np.fliplr(img), cmap="gray")

def reduce_resolution(image_array, factor=10):
    reduced_img = image_array[::factor, ::factor]
    return reduced_img

plt.imshow(reduce_resolution, cmap="gray")
plt.show()
