# Осреднение приравниванием к начальному значению
import numpy as np
from conditions.base_functions import expansion


def avg_start_value(gas_parameters: dict[str, np.array(float)], k_formula, gas: str) -> dict[str, np.array(float)]:
    t1 = gas_parameters["t1"]
    s1 = gas_parameters["s1"]
    k_avg = k_formula(t1, s1, gas)
    return expansion(gas_parameters, k_avg, gas)
