import numpy as np
from conditions.base_parameters import parameters
from conditions import base_functions


def temperature_range() -> np.array(int):
    t_min: int = base_functions.min_temperature(parameters["minimum_pressure"])
    t_max: int = parameters["maximum_temperature"]
    step_num: int = parameters["iter_temperature"]
    step: int = (t_max - t_min) // step_num
    return np.array(range(t_min, t_max, step))


def entropy_range() -> np.array(int):
    s_min: int = base_functions.min_entropy(parameters["minimum_pressure"], parameters["minimum_q"])
    s_max: int = parameters["maximum_entropy"]
    step_num: int = parameters["iter_entropy"]
    step: int = (s_max - s_min) // step_num
    return np.array(range(s_min, s_max, step))
