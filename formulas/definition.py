# Вычисление коэффициента адиабаты по определению
import numpy as np
from CoolProp.CoolProp import PropsSI as PSI


def k_cpcv(temperature: np.array(float) | float, entropy: np.array(float) | float,
           gas: str) -> dict[str, np.array(float) | float]:
    cp = PSI('CPMASS', 'T', temperature, 'S', entropy, gas)
    cv = PSI('CVMASS', 'T', temperature, 'S', entropy, gas)
    k = cp / cv
    return {"k": k, "e": k, "d": k}
