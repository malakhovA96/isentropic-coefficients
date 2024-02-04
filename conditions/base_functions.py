# Простые функции для вычислений
import numpy as np
from CoolProp.CoolProp import PropsSI as PSI
from conditions.base_parameters import parameters


def min_temperature(pressure: float) -> int:
    gas: str = parameters['gas_name']
    return int(PSI('T', 'P', pressure, 'Q', 1, gas))


def min_entropy(pressure: float, q: float) -> int:
    gas: str = parameters['gas_name']
    return int(PSI('S', 'P', pressure, 'Q', q, gas))


def start_parameters(temperature: np.array(float) | float, entropy: np.array(float) | float) -> dict[str, float]:
    s1 = entropy
    t1 = temperature
    gas: str = parameters['gas_name']
    p1 = PSI('P', 'T', t1, 'S', s1, gas)
    d1 = PSI('D', 'T', t1, 'S', s1, gas)
    return {'t1': t1,
            's1': s1,
            'p1': p1,
            'd1': d1}


def all_parameters(gas_parameters: dict[str, np.array(float) | float], p2_coef) -> dict[str, np.array(float) | float]:
    gas: str = parameters['gas_name']
    p2 = gas_parameters["p1"] * p2_coef
    s1 = gas_parameters["s1"]
    d2s = PSI('D', 'P', p2, 'S', s1, gas)
    t2s = PSI('T', 'P', p2, 'S', s1, gas)
    gas_parameters["p2"] = p2
    gas_parameters["d2s"] = d2s
    gas_parameters["t2s"] = t2s
    return gas_parameters


def expansion(gas_parameters: dict[str, np.array(float)], k_dict: dict[str, np.array(float)],
              gas: str) -> dict[str, np.array(float)]:
    p1 = gas_parameters["p1"]
    p2 = gas_parameters["p2"]
    t1 = gas_parameters["t1"]
    d1 = gas_parameters["d1"]
    d2s = gas_parameters["d2s"]
    t2s = gas_parameters["t2s"]
    eps = k_dict["e"]
    k = k_dict["k"]

    t2 = t1 * ((p2 / p1) ** ((eps-1)/eps))
    d2 = d1 * ((p2 / p1) ** (1 / k))
    s2 = PSI('S', 'T', t2, 'D', d2, gas)

    t_err = (t2s - t2) / t2s * 100
    d_err = (d2s - d2) / d2s * 100

    return {"t1": t1,
            "s1": gas_parameters["s1"],
            "t2": t2,
            "d2": d2,
            "s2": s2,
            "t_err": t_err,
            "d_err": d_err}
