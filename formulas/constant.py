# Вычисление коэффициента адиабаты как константы
import numpy as np


def k_const(temperature: np.array(float) | float, entropy: np.array(float) | float,
            gas: str) -> dict[str, np.array(float) | float]:
    k = np.tile([1.33], len(temperature))
    return {"k": k, "e": k, "d": k}
