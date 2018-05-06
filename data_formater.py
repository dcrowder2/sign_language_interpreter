import numpy as np
import os


def importData(path):
    filepaths = []
    words = []
    for x in os.walk(path):
        temp = []
        for i in range(len(x[2])):
            if len(x[2]) > 0 and x[2][i][:3] != "cal":
                words.append(str(x[2][i][:-6]))
                filepaths.append(x[0] + '\\' + str(x[2][i]))
    s = []
    for i in words:
        if i not in s:
            s.append(i)
    i = 0
    all_data = []
    for filepath in filepaths:
        # print("Reading file " + filepath)
        file_data = [np.array([float(s.index(words[i]))])]
        i += 1
        with open(filepath) as file:
            for line in file:
                line_data = []
                line = line.split(",")
                for number in line[:-5]:
                    line_data.append(float(number))
                file_data.append(np.array(line_data))
        all_data.append(np.array(file_data))
    return all_data, s


if __name__ == '__main__':
    write, words = importData(".\signs")
    with open("words.txt", 'w') as file:
        for word in words:
            file.write(word + ',')

