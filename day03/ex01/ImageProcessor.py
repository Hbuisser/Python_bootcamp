import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class ImageProcessor:
    def load(self, path):
        img = mpimg.imread(path)
        size = np.shape(img)
        print("The dimensions of the image are {0}x{1}".format(size[0], size[1]))
        return img
    def display(self, array):
        plt.imshow(array)
        plt.show()

