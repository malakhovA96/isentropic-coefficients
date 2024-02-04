# Вычисление коэффициента адиабаты по формуле Истомина
import numpy as np
from CoolProp.CoolProp import PropsSI as PSI


def k_istomin(temperature: np.array(float) | float, entropy: np.array(float) | float, gas: str) -> dict[str, np.array]:
    diff = PSI('d(P)/d(D)|S', 'T', temperature, 'S', entropy, gas)
    d = PSI('D', 'T', temperature, 'S', entropy, gas)
    p = PSI('P', 'T', temperature, 'S', entropy, gas)
    eps = e_istomin(temperature, entropy, gas)
    delta = d_istomin(temperature, entropy, gas)
    return {"k": d / p * diff,
            "e": eps,
            "d": delta}


def e_istomin(temperature: np.array(float) | float,
              entropy: np.array(float) | float, gas: str) -> np.array(float) | float:
    p = PSI('P', 'T', temperature, 'S', entropy, gas)
    t = temperature
    alpha_e = p/t * PSI('d(T)/d(P)|S', 'T', temperature, 'S', entropy, gas)
    epsilon = 1 / (1 - alpha_e)
    return epsilon


def d_istomin(temperature: np.array(float) | float,
              entropy: np.array(float) | float, gas: str) -> np.array(float) | float:
    d = PSI('D', 'T', temperature, 'S', entropy, gas)
    t = temperature
    detta = d/t * PSI('d(T)/d(D)|S', 'T', temperature, 'S', entropy, gas) + 1
    return detta
