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

class ScrapBooker:
    def crop(self, array, dimensions, position):
        if type(position) is not tuple or len(position) is not 2 or array.shape[0] < (position[0] + dimensions[0]) or array.shape[1] < (position[1] + dimensions[1]):
            return "error"
        else:
            return array[position[1]: position[1] + dimensions[1], position[0]:position[0] + dimensions[0]]
    def thin(self, array, n, axis):
        i = 0
        while n * i < np.shape(array)[axis]:
            array = np.delete(array, n*i, axis)
            i += 1
        return array
    def juxtapose(self, array, n, axis):
        i = 0
        newarray = array
        while i < n - 1:
            newarray = np.concatenate((array, newarray), axis)
            i += 1
        return newarray
    def mosaic(self, array, dimensions):
        array = self.juxtapose(array, dimensions[0], 0)
        array = self.juxtapose(array, dimensions[1], 1)
        return array

imp = ImageProcessor()
arr = imp.load("42AI.png")
img = ScrapBooker()
newarr = img.crop(arr, (200,100), (210,400))
print(newarr)
imp.display(newarr)
