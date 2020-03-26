import numpy
from PIL import Image


def median_filter(data, filter_size):
    temp = []
    index = filter_size // 2
    data_final = []
    data_final = numpy.zeros((len(data),len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[0])):
            for z in range(filter_size):
                if i + z - index < 0 or i + z - index > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - index < 0 or j + index > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - index][j + k - index])
            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final

def main():
    img = Image.open("testimg.bmp").convert("L")
    arr = numpy.array(img)
    fs = 10
    result = median_filter(arr, fs) 
    img = Image.fromarray(result)
    img.show()
    img = img.convert("L")
    img.save("result.png")

main()
