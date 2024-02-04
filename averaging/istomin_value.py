# Осреднение по методике Истомина
import numpy as np
from formulas.istomin import e_istomin, d_istomin
from conditions.base_functions import expansion


def istomin_value(gas_parameters: dict[str, np.array(float)], k_formula, gas: str) -> dict[str, np.array(float)]:
    k_dict = k_formula(gas_parameters["t1"], gas_parameters["s1"], gas)
    eps1 = k_dict["e"]
    delta1 = k_dict["d"]
    dict_istomin_expansion = expansion(gas_parameters, k_dict, gas)
    t2 = dict_istomin_expansion["t2"]
    s2 = dict_istomin_expansion["s2"]
    eps2 = e_istomin(t2, s2, gas)
    delta2 = d_istomin(t2, s2, gas)
    eps_avg = (eps1 + eps2) / 2
    delta_avg = (delta1 + delta2) / 2
    k_avg = (delta_avg - 1) * eps_avg / (eps_avg - 1)
    k_avg_dict = {"k": k_avg, "e": eps_avg, "d": delta_avg}
    return expansion(gas_parameters, k_avg_dict, gas)
