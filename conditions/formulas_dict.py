from formulas import istomin, constant, shekhtman, definition
from averaging import start_value, middle_value, istomin_value


formula_dict = [
    {"name": "k_const",
     "averaging": [start_value.avg_start_value],
     "func": constant.k_const},
    {"name": "k_cpcv",
     "averaging": [middle_value.avg_middle_value],
     "func": definition.k_cpcv},
    {"name": "k_istomin",
     "averaging": [istomin_value.istomin_value],
     "func": istomin.k_istomin},
    {"name": "k_shekhtman",
     "averaging": [middle_value.avg_middle_value],
     "func": shekhtman.k_shekhtman}
]
