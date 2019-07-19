import numpy as np
import math
from collections import defaultdict

# load data from a text file, with missing values handled as specified. Each line past the first skip_header lines is
# split at the delimiter character, and characters following the comments character are discarded.
# data = np.genfromtxt("CityTemps.csv", delimiter=",")
# print(data)
# print("================================")
# data = np.array(data[1:], dtype=np.float)
# print(data)
# sum_data = data.sum(axis=0)
# print(sum_data)

class TempAnalyses:
    def __init__(self, name):
        self.name = name
        # starting
        self.file = np.genfromtxt(name, delimiter=",", skip_header= 1)

    def count_year(self):
        self.years = []
        for i in range(0, len(self.file), 12):
            self.years.append(int(self.file[i][0]))

        return f"There are {len(self.years)} years i.e. {self.years}"

    def allData(self):
        return self.file

    def cold_hot(self, year, month):
        self.year = year
        self .month = month
        d = {}
        self.city_names = np.genfromtxt(self.name, delimiter=",", dtype=str)[:1][0]
        for i in range(len(self.file)):
            if self.year == self.file[i][0] and self.month == self.file[i][1]:
                for j in range(len(self.city_names[2:])):
                    d[self.city_names[2 + j]] == self.file[i, 2+j]
        print(d)
        print(d[self.city_names[2]])
        self.coldest = [self.city_names[2], d[self.city_names[2]]]
        self.hottest = [self.city_names[2], d[self.city_names[2]]]
        for city, temp in d.items():
            if self.coldest[1] > temp:
                self.coldest[1] = temp
                self.coldest[0] = city
            elif self.hottest[1] < temp:
                self.hottest[1] = temp
                self.hottest[0] = city
        self.result = [self.coldest, self.hottest]
        self.result[0].insert(0,"Coldest City")
        self.result[1].insert(0, "Hottest City")
        return self.result

    def cold_hot_year(self):
        self.array = np.genfromtxt(self.name, delimiter=",", skip_header=0, dtype=str)
        for k in range(12, len(self.array), 12):
            print("\n************************", self.array[k][0],"*******************")

            All_temp = np.array(self.array[k-11:k+1, 2:], float)
            for i in range(len(self.array[0, 2:])):
                month_list = defaultdict(list)
                for j in range(12*(k//12)-12,k):
                    month_list[float(self.array[j+1][2+i])].append(self.array[j+1][1])
                # print(month_list)
                print("\t\t\t\t",self.array[0][2+i], str(All_temp[:, i].max(axis=0))+",", " month "+" ".join(month_list[All_temp[:, i].max(axis = 0)]))

c1 = TempAnalyses("CityTemps.csv")
print(c1.count_year())
print(c1.allData())
print(c1.cold_hot_year())