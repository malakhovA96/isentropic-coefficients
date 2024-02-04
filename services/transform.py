# Модуль преобразований
import numpy as np
from conditions import base_functions


# функция для формирования словаря с параметрами точек графика
def parameters_array(temperature: np.array(int), entropy: np.array(int)) -> np.array(float):
    temperature_array = np.repeat(temperature, len(entropy))
    entropy_array = np.tile(entropy, len(temperature))
    result_array = base_functions.start_parameters(temperature_array, entropy_array)
    return result_array
