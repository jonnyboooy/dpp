
def triangle(a):

    space_count = a
    star_count = 1
    for i in range(0, a+1):
        print(' ' * space_count, '*' * star_count)
        space_count -= 1
        star_count += 2

def histDistance(hist1, hist2):

    res_hist = []

    for i in range(len(hist1)):
        res_hist.append(hist2[i] - hist1[i])

    return res_hist

def readFromFile(name_file):

    h_1 = []
    h_2 = []

    with open(name_file, encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:

        if line.find('hist1 ') != -1:
            line = line.replace('hist1 ', '')
            buff = line.split()
            for val in buff:
                h_1.append(float(val))

        if line.find('hist2 ') != -1:
            line = line.replace('hist2 ', '')
            buff = line.split()
            for val in buff:
                h_2.append(float(val))

    return h_1, h_2

def writeToFile(name_file, hist_out):

    file = open(name_file, 'w')

    for val in hist_out:
        file.write(str(val))
        file.write(" ")

    file.close()

if __name__ == "__main__":

    triangle(3)

    fileToRead = 'file_to_read.txt'
    fileToWrite = 'file_to_write.txt'

    histAXY, histBXY = readFromFile(fileToRead)

    distance = histDistance(histAXY, histBXY)

    writeToFile(fileToWrite, distance)