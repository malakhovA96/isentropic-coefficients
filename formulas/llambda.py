# Вычисление коэффициента лямбда и дальнейший расчет конечных параметров
# from formulas.istomin import k_istomin, e_istomin
# import numpy as np
# from CoolProp.CoolProp import PropsSI as PSI
#
# m = 0
# l = 0.2
# n = -0.8
#
#
# def k_lambda(temperature: np.array | float, entropy: np.array | float, gas: str) -> np.array | float:
#     k = k_istomin(temperature, entropy, gas)
#     e = e_istomin(temperature, entropy, gas)
#     return 1 / ((l / k) - (n / e))
#
#
# def t_lambda(start_p: np.array | float,
#              end_p: np.array | float,
#              start_s: np.array | float,
#              gas: str) -> np.array | float:
#     start_t = PSI('T', 'P', start_p, 'S', start_s, gas)
#     start_z = PSI('Z', 'P', start_p, 'S', start_s, gas)
#     end_z = PSI('Z', 'P', end_p, 'S', start_s, gas)
#     k = k_lambda(start_t, start_s, gas)
#     return 1 / ((end_z ** l) * (((((start_z ** l) * start_t) ** k) / (start_p ** (k - 1)) * (end_p ** (k-1))) ** k))
