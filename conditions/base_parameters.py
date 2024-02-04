# Глобальные переменные в программе
parameters: dict[str, any] = {
    "gas_name": "methane",
    "minimum_pressure": 1*10**5,
    "maximum_temperature": 200,
    "minimum_q": 0.9,
    "maximum_entropy": 6000,
    "iter_temperature": 10,
    "iter_entropy": 10,
    "p_end_coef": [1/1.6, 1/5],
}

