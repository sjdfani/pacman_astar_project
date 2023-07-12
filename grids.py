# 40x21

grid_1_Forages = [
    "++++++++++++++++++++++++++++++++++++++++",
    "+s               +++++++               +",
    "+ ++++++ +++++++ +++++++ +++++++ +++++ +",
    "+                                      +",
    "+ ++++++ ++ +++++++++++++++++ ++ +++++ +",
    "+        ++      +++++++      ++       +",
    "++++++++ +++++++ +++++++ +++++++ +++++++",
    "++++++++ ++                   ++ +++++++",
    "++++++++ ++ ++++++++ ++++++++ ++ +++++++",
    "+                                      +",
    "++++++++ ++ ++++++++ ++++++++ ++ +++++++",
    "++++++++ ++                   ++ +++++++",
    "++++++++ ++ +++++++++++++++++ ++ +++++++",
    "+               f+++++++               +",
    "+ ++++++ +++++++ +++++++ +++++++ +++++ +",
    "+     ++                         ++    +",
    "+++++ ++ +++++++ +++++++ +++++++ ++ ++++",
    "+        +++++++    +    +++++++       +",
    "+ +++++++++++++++++ + ++++++++++++++++ +",
    "+                                      +",
    "++++++++++++++++++++++++++++++++++++++++",
]

grid_2_Forages = [
    "++++++++++++++++++++++++++++++++++++++++",
    "+s               +++++++               +",
    "+ ++++++ +++++++ +++++++ +++++++ +++++ +",
    "+                                      +",
    "+ ++++++ ++ +++++++++++++++++ ++ +++++ +",
    "+        ++      +++++++      ++       +",
    "++++++++ +++++++ +++++++ +++++++ +++++++",
    "++++++++ ++                   ++ +++++++",
    "++++++++ ++ ++++++++ ++++++++ ++ +++++++",
    "+                                      +",
    "++++++++ ++ ++++++++f++++++++ ++ +++++++",
    "++++++++ ++                   ++ +++++++",
    "++++++++ ++ +++++++++++++++++ ++ +++++++",
    "+                +++++++               +",
    "+ ++++++ +++++++ +++++++ +++++++ +++++ +",
    "+     ++                         ++    +",
    "+++++ ++ +++++++ +++++++ +++++++ ++ ++++",
    "+        +++++++    +    +++++++       +",
    "+ +++++++++++++++++ + ++++++++++++++++ +",
    "+f                                     +",
    "++++++++++++++++++++++++++++++++++++++++",
]

grid_3_Forages = [
    "++++++++++++++++++++++++++++++++++++++++",
    "+s               +++++++              f+",
    "+ ++++++ +++++++ +++++++ +++++++ +++++ +",
    "+                                      +",
    "+ ++++++ ++ +++++++++++++++++ ++ +++++ +",
    "+        ++      +++++++      ++       +",
    "++++++++ +++++++ +++++++ +++++++ +++++++",
    "++++++++ ++                   ++ +++++++",
    "++++++++ ++ ++++++++ ++++++++ ++ +++++++",
    "+                                      +",
    "++++++++ ++ ++++++++ ++++++++ ++ +++++++",
    "++++++++ ++                   ++ +++++++",
    "++++++++ ++ +++++++++++++++++ ++ +++++++",
    "+                +++++++               +",
    "+ ++++++ +++++++ +++++++ +++++++ +++++ +",
    "+     ++                         ++    +",
    "+++++ ++ +++++++ +++++++ +++++++ ++ ++++",
    "+        +++++++    +    +++++++       +",
    "+ +++++++++++++++++ + ++++++++++++++++ +",
    "+f                                    f+",
    "++++++++++++++++++++++++++++++++++++++++",
]

grid_4_Forages = [
    "++++++++++++++++++++++++++++++++++++++++",
    "+s               +++++++              f+",
    "+ ++++++ +++++++ +++++++ +++++++ +++++ +",
    "+                                      +",
    "+ ++++++ ++ +++++++++++++++++ ++ +++++ +",
    "+        ++      +++++++      ++       +",
    "++++++++ +++++++ +++++++ +++++++ +++++++",
    "++++++++ ++                   ++ +++++++",
    "++++++++ ++ ++++++++ ++++++++ ++ +++++++",
    "+                                      +",
    "++++++++ +f ++++++++ ++++++++ ++ +++++++",
    "++++++++ ++                   ++ +++++++",
    "++++++++ ++ +++++++++++++++++ ++ +++++++",
    "+                +++++++               +",
    "+ ++++++ +++++++ +++++++ +++++++ +++++ +",
    "+     ++                         ++    +",
    "+++++ ++ +++++++ +++++++ +++++++ ++ ++++",
    "+        +++++++    +    +++++++       +",
    "+ +++++++++++++++++ + ++++++++++++++++ +",
    "+f                                    f+",
    "++++++++++++++++++++++++++++++++++++++++",
]


def get_grid(count_foods):
    grids = [grid_1_Forages, grid_2_Forages, grid_3_Forages, grid_4_Forages]
    return grids[count_foods-1]