import numpy as np


arr = np.load('../second_task.npy')
threshold = 500 + 51

print(arr)

x = []
y = []
z = []

shape = arr.shape
print(shape)

for i in range(shape[0]):
    for j in range(shape[1]):
        if arr[i][j] > threshold:
            x.append(i)
            y.append(j)
            z.append(arr[i][j])

np.savez('../outputs/task2/x.npz', x)
np.savez('../outputs/task2/y.npz', y)
np.savez('../outputs/task2/z.npz', z)

np.savez_compressed('../outputs/task2/x_compressed.npz', x)
np.savez_compressed('../outputs/task2/y_compressed.npz', y)
np.savez_compressed('../outputs/task2/z_compressed.npz', z)

"""
Полученные размеры файлов:
x.nps - 1,24Кб
y.nps - 1,24Кб
z.nps - 768 байт
x_compressed.nps - 221 байт
y_compressed.nps - 427 байт
z_compressed.nps - 453 байт
"""
