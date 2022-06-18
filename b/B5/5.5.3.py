# (вес, рост) Сортировка по индексу массы тела
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]

data_sorted = sorted(data, key=lambda x: x[0] / x[1]**2)
data_min = min(data, key=lambda x: x[0] / x[1]**2)
print(data_sorted[0], data_min)
