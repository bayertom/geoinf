import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread(r'E:/Tomas/Graf/diff_metric.jpg')
plt.plot([0, 1000], [0, 1000], 'r')
plt.imshow(image)
plt.show()