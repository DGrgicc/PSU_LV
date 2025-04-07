import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

imageNew = mpimg.imread(r'C:\Users\student\Downloads\example_grayscale.png')

print("Dimenzije slike:", imageNew.shape)

if len(imageNew.shape) == 3:
    image_reshaped = imageNew.reshape((-1, 3))
else:
    image_reshaped = imageNew.reshape((-1, 1)) 

plt.imshow(imageNew)
plt.title('Originalna slika')
plt.axis('off')
plt.show()

def quantize_image(image, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(image)
    
    centroids = kmeans.cluster_centers_
    
    labels = kmeans.predict(image)
    
    quantized_image = centroids[labels].reshape(image.shape)
    
    return quantized_image

n_clusters = 10
quantized_image = quantize_image(image_reshaped, n_clusters)

plt.imshow(quantized_image)
plt.title(f'Kvantizirana slika ({n_clusters} klastera)')
plt.axis('off')
plt.show()

def calculate_compression(image, quantized_image):
    original_size = image.size * image.itemsize 
    quantized_size = quantized_image.size * quantized_image.itemsize  
    
    compression_ratio = original_size / quantized_size
    return compression_ratio

compression_ratio = calculate_compression(image_reshaped, quantized_image)
print(f'Kompresija s {n_clusters} klastera: {compression_ratio:.2f}x')

