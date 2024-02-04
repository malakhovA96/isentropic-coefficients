# Вычисление коэффициента адиабаты по формуле Шехтмана
import numpy as np
from CoolProp.CoolProp import PropsSI as PSI


def k_shekhtman(temperature: np.array(float), entropy: np.array(float) | float,
                gas: str) -> dict[str, np.array(float) | float]:
    d_step = 0.0001
    z = PSI('Z', 'T', temperature, 'S', entropy, gas)
    d = PSI('D', 'T', temperature, 'S', entropy, gas)
    p = PSI('P', 'T', temperature, 'S', entropy, gas)
    diff = _diff_p_zd_s(p, d, gas, d_step)
    k = z * d / p * diff
    return {"k": k, "e": k, "d": k}


def _diff_p_zd_s(p: np.array(float) | float, d: np.array(float) | float,
                 gas: str, d_step: float) -> np.array(float) | float:
    # частная производная dP/d(density*z) |S
    d1 = d
    p1 = p
    s1 = PSI('S', 'P', p1, 'D', d1, gas)
    z1 = PSI('Z', 'P', p1, 'D', d1, gas)
    d2 = d1+d_step
    p2 = PSI('P', 'S', s1, 'D', d2, gas)
    z2 = PSI('Z', 'S', s1, 'D', d2, gas)
    return (p1-p2)/(d1*z1 - d2*z2)
