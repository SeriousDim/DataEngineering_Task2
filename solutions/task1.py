import numpy as np
import json
from sklearn.preprocessing import Normalizer


def count_diagonal_sum(arr, side=False):
    copied_array = arr
    if side:
        copied_array = np.fliplr(copied_array)
    return np.trace(copied_array)


def count_diagonal_mean(arr, side=False):
    copied_array = arr
    if side:
        copied_array = np.fliplr(copied_array)
    return np.diagonal(copied_array).mean()


def output_json(values):
    with open('../outputs/task1.json', 'w') as output_file:
        json.dump(values, output_file, indent=4)


numpy_array = np.load('../first_task.npy')

array_sum = numpy_array.sum()
print('Сумма: ', array_sum)

array_mean = numpy_array.mean()
print('Среднее: ', array_mean)

diag_sum = count_diagonal_sum(numpy_array)
print('Сумма главной диагонали:', diag_sum)
diag_mean = count_diagonal_mean(numpy_array)
print('Среднее главной диагонали:', diag_mean)

side_diag_sum = count_diagonal_sum(numpy_array, side=True)
print('Сумма побочной диагонали:', side_diag_sum)
side_diag_mean = count_diagonal_mean(numpy_array, side=True)
print('Среднее побочной диагонали:', side_diag_mean)

array_max = numpy_array.max()
array_min = numpy_array.min()
print('Макс: ', array_max)
print('Мин: ', array_min)

output_json({
    "sum": int(array_sum),
    "avr": array_mean,
    "sumMD": int(diag_sum),
    "avrMD": diag_mean,
    "sumSD": int(side_diag_sum),
    "avrSD": side_diag_mean,
    "max": int(array_max),
    "min": int(array_min)
})

transformer = Normalizer().fit(numpy_array)
normalized_array = transformer.transform(numpy_array)
print(normalized_array)

np.save('../outputs/task1.npy', normalized_array)

print(np.load('../outputs/task1.npy'))
