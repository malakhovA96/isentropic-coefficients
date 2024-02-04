import matplotlib.pyplot as plt
from CoolProp.Plots import PropertyPlot
import CoolProp
import matplotlib as mpl
import numpy as np
from conditions.base_parameters import parameters
from matplotlib import cm, ticker


# Отрисовка тепловой карты
def drawing(gas, z, x, y, title):
    ax = draw_cool_prop_plots(gas)
    map = cm.PuBu
    map = mpl.colormaps['gist_rainbow']
    cs = ax.contourf(x/1000, y, z, locator=ticker.LogLocator(),
                         cmap=map, levels=np.arange(z.min(), z.max(), 1)) #levels=np.arange(z.min(), z.max(), 0.01)
    print('min max' , z.min(), z.max())
    plt.colorbar(cs)
    plt.title(title)
# def drawing(diagramtype, gas, z, x, y, title, minlvl = 0, maxlvl = 0, steplvl=0):
#     ax = drawCoolPropPlots(diagramtype, gas)
#     # X, Y = np.meshgrid(x, y)
#     from matplotlib import cm, ticker
#     map = cm.PuBu
#     map = mpl.colormaps['tab20c']
#     # map = mpl.colormaps['Accent']
#     # cs = ax.contourf(x, y, z, 30)
#     if  minlvl==0 or maxlvl==0 or steplvl==0:
#         cs = ax.contourf(x, y, z, 30, locator=ticker.LogLocator(), cmap=map)
#     else:
#         cs = ax.contourf(x, y, z, 30, locator=ticker.LogLocator(),
#                          cmap=map, levels=np.arange(minlvl, maxlvl, steplvl))
#     plt.colorbar(cs)
#     plt.title(title)

# Отрисовка диаграммы состояния
def draw_cool_prop_plots(gas_name):
    plot = PropertyPlot(gas_name, 'TS', unit_system='KSI', tp_limits='DEF')
    plot.calc_isolines(CoolProp.iQ, num=10)
    plot.calc_isolines(CoolProp.iP, num=25)
    plot.draw()  # обязательно, не удалять
    return plot.axis
