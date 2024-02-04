import numpy as np
import math
import matplotlib.pyplot as plt
import CoolProp
from CoolProp.CoolProp import PropsSI as PSI
from CoolProp.Plots import PropertyPlot
import matplotlib as mpl
from matplotlib import cm, ticker
import numpy as np
from conditions import ranges, base_parameters, formulas_dict, base_functions
from services import transform
import logging
from drawing.drawing import drawing
import matplotlib.pyplot as plt


logger = logging.getLogger(__name__)

def drawCoolPropPlots(diagramType, gas_name):
    if diagramType == 'PH':
        plot = PropertyPlot(gas_name, 'PH', unit_system='EUR', tp_limits='ACHP')
        plot.calc_isolines(CoolProp.iQ, num=2)
        plot.calc_isolines(CoolProp.iT, num=25)
        plot.calc_isolines(CoolProp.iSmass, num=15)
        plot.draw()  # обязательно, не удалять
    elif diagramType == 'TS':
        plot = PropertyPlot(gas_name, 'TS', unit_system='KSI', tp_limits='DEF')
        plot.calc_isolines(CoolProp.iQ, num=2)
        plot.calc_isolines(CoolProp.iP, num=25)
        plot.draw()  # обязательно, не удалять
    else:
        raise Exception(f'incorrect type of diagram; {diagramType} was given, but should be PH or TS')
    return plot.axis

def drawing( z, x, y, title):

    map = cm.PuBu
    map = mpl.colormaps['Set1']
    cs = plt.contourf(x, y, z, 30, locator=ticker.LogLocator(), cmap=map)
    plt.colorbar(cs)
    plt.title(title)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting program')
    # задаем диапазоны температур и энтропий на графике
    temperature_range = ranges.temperature_range()
    entropy_range = ranges.entropy_range()
    ls = len(entropy_range)
    lt = len(temperature_range)
    # преобразование диапазонов в массив с определением дополнительных параметров
    start_parameters = transform.parameters_array(temperature_range, entropy_range)
    t1 = start_parameters["t1"]
    s1 = start_parameters["s1"]
    # Определение погрешности измерений
    for p2 in base_parameters.parameters["p_end_coef"]:
        parameters_dict = base_functions.all_parameters(start_parameters, p2)
        for formula in formulas_dict.formula_dict:
            for avg in formula["averaging"]:
                error_dict = avg(parameters_dict, formula["func"], base_parameters.parameters["gas_name"])
                t_err = error_dict["t_err"].reshape(lt, ls)
                d_err = error_dict["d_err"].reshape(lt, ls)
                logger.info(f'Pressure ratio = {p2}, Formula = {formula["name"]}, '
                            f'Averaging function = {avg.__name__} is calculated!')
                # Отрисовка полученных погрешностей
                drawing(t_err, entropy_range/1000, temperature_range,
                        f'Погрешность температуры при отношении давлений {p2} по формуле {formula["name"]}')

                plt.show()