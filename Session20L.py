import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

result = pd.read_csv('CityTemps.csv', delimiter = ',')
print(result)

print("Maximum Temparature of Ludhiana", result['Ludhiana'].max())
print("Maximum Temparature of Amritsar", result['Amritsar'].max())
print("Maximum Temparature of Chandigarh", result['Chandigarh'].max())

print("Minimum Temparature of Ludhiana", result['Ludhiana'].min())
print("Minimum Temparature of Amritsar", result['Amritsar'].min())
print("Minimum Temparature of Chandigarh", result['Chandigarh'].min())


# max_temp = {"Ldh":21.1, "Amr":22.0, "Chd":20.4}
# min_temp = {"Ldh":-8.6, "Amr":8.9, "Chd":10.3}
# for i, key in enumerate(max_temp):
#     for i, key in enumerate(max_temp):
#         # plt.bar(i, scores[key])
#         plt.bar(key, min_temp[key])
#     plt.bar(key, max_temp[key])
# plt.xlabel("Cities")
# plt.ylabel("Temp")
# plt.title("Temp_Cties")
#
# plt.show()


# data to plot
n_groups = 2
ldh = (21.1, 8.6)
amr = (22.0, 8.9)
chd = (20.4, 10.3)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.05
opacity = 0.8

rects1 = plt.bar(index, ldh, bar_width,alpha=opacity,color='b',label='Ldh')
rects2 = plt.bar(index + bar_width, amr, bar_width,alpha=opacity,color='g',label='Amr')
rects3 = plt.bar(index + bar_width, chd, bar_width,alpha=opacity,color='m',label='Chd')

plt.xlabel('Cities')
plt.ylabel('Temp')
plt.title('Scores by Temp_Cties')
plt.xticks(index + bar_width, ('Ldh', 'Amr', 'Chd'))
plt.legend()

plt.tight_layout()
plt.show()
