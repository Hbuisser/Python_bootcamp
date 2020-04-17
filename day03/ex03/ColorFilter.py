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

class ColorFilter:
    def invert(self, array):
        return float(1) - array
    def to_blue(self, array):
        array[:,:,0] = 0
        array[:,:,1] = 0
        return array
    def to_green(self, array):
        array[:,:,2] = 0
        array[:,:,0] = 0
        return array
    def to_red(self, array):
        array[:,:,2] = 0
        array[:,:,1] = 0
        return array
    def celluloid(self, array, threshold=10):
        # array *= threshold
        # array //= 1
        # array /= threshold
        # return array
        def celluloid(self, array, threshold=10):
        steps = np.linspace(0, 1, threshold)
        for i in range(len(array)) :
            for j in range(len(array[0])) :
                for k in range(len(array[0][0])) :
                    tmp = 0
                    for step in steps:
                        if array[i][j][k] > step:
                            tmp = step
                    array[i][j][k] = tmp
        return array

imp = ImageProcessor()
arr = imp.load("42AI.png")
img = ColorFilter()
newarr = img.celluloid(arr)
print(newarr)
imp.display(newarr)
