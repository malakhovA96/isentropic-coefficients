# Осреднение приравниванием к среднему значению
import numpy as np
from conditions.base_functions import expansion


def avg_middle_value(gas_parameters: dict[str, np.array(float)], k_formula, gas: str) -> dict[str, np.array(float)]:
    t1 = gas_parameters["t1"]
    s1 = gas_parameters["s1"]
    k1 = k_formula(t1, s1, gas)
    end_parameters = expansion(gas_parameters, k1, gas)
    t2 = end_parameters["t2"]
    s2 = end_parameters["s2"]
    k2 = k_formula(t2, s2, gas)
    k_avg = {"k": (k1["k"] + k2["k"]) / 2,
             "e": (k1["e"] + k2["e"]) / 2,
             "d": (k1["d"] + k2["d"]) / 2}
    return expansion(gas_parameters, k_avg, gas)
