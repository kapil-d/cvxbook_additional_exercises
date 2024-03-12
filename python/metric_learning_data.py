"""
Data for learning a quadratic metric from pairs of similar and dissimilar data
You should use X, S, D, as well as S_test, D_test
n: dimension of the data
N: number of data points

X: (N, n) array of data points
S: 2d array of similar pairs
D: 2d array of dissimilar pairs
S_test: 2d array of similar pairs for testing
D_test: 2d array of dissimilar pairs for testing
"""

import numpy as np

n = 5
N = 50


X = np.array(
    [
        [
            2.94192455e-01,
            3.61758698e-01,
            2.71811663e-01,
            4.65784384e-01,
            6.71933145e-01,
        ],
        [
            2.35233613e-01,
            -1.82930386e-01,
            1.15694179e-01,
            6.21828122e-03,
            -1.54771623e-01,
        ],
        [
            4.48959403e-01,
            1.86242077e-01,
            2.92479610e-01,
            3.32690528e-01,
            3.81032807e-01,
        ],
        [
            1.52782792e-01,
            1.83392366e-01,
            5.22575411e-02,
            2.09086302e-01,
            8.54044961e-02,
        ],
        [
            2.14648350e-01,
            -2.39282553e-01,
            1.50718093e-01,
            -7.59464644e-02,
            -7.41994918e-02,
        ],
        [
            1.31958525e-01,
            -5.56889701e-02,
            1.63147504e-01,
            1.09702807e-01,
            1.69609056e-01,
        ],
        [
            -7.60760497e-02,
            -1.96945244e-01,
            -2.01081235e-01,
            -2.04107225e-01,
            -5.09498615e-01,
        ],
        [
            2.97239310e-01,
            1.15310760e-01,
            1.90507330e-01,
            1.25151700e-01,
            2.18264913e-01,
        ],
        [
            -2.93432633e-01,
            -7.48841080e-02,
            -1.38791240e-01,
            -1.07954641e-01,
            -1.35209976e-01,
        ],
        [
            -2.02922200e-01,
            -2.69267691e-01,
            -1.42808522e-01,
            -4.04737529e-01,
            -3.40724726e-01,
        ],
        [
            -4.38487850e-02,
            -3.61924431e-01,
            -1.41356622e-01,
            -3.05952960e-01,
            -5.89006749e-01,
        ],
        [
            -2.03799827e-02,
            3.56813938e-02,
            -7.97415945e-02,
            -9.82954448e-02,
            -1.02838159e-01,
        ],
        [
            -1.54806990e-01,
            -3.59145915e-01,
            -2.14617256e-01,
            -3.48328986e-01,
            -6.08152539e-01,
        ],
        [
            -2.71525762e-01,
            -2.51842774e-01,
            -1.52224245e-01,
            -3.86474375e-01,
            -2.77239525e-01,
        ],
        [
            1.93051012e-01,
            4.86302607e-02,
            9.60850388e-02,
            2.98739810e-02,
            1.28418929e-01,
        ],
        [
            -3.44535338e-01,
            -3.56974757e-01,
            -2.41059436e-01,
            -4.00401342e-01,
            -5.15939937e-01,
        ],
        [
            2.52464205e-01,
            -2.24484908e-01,
            1.09722070e-01,
            -6.54820451e-02,
            -1.61943745e-01,
        ],
        [
            2.94060872e-01,
            2.04707495e-01,
            9.70122516e-02,
            3.16057718e-01,
            1.95676952e-01,
        ],
        [
            3.34442653e-01,
            1.48553935e-01,
            2.60927332e-01,
            3.16557395e-01,
            3.48903739e-01,
        ],
        [
            2.40410775e-01,
            2.23328092e-01,
            2.42562671e-01,
            1.92880938e-01,
            5.22079052e-01,
        ],
        [
            -2.70212208e-01,
            1.95548454e-01,
            -1.72610352e-01,
            6.17951724e-02,
            5.57183549e-02,
        ],
        [
            1.17684984e-01,
            3.19659715e-01,
            1.15247387e-01,
            4.04225312e-01,
            4.72549611e-01,
        ],
        [
            1.04238407e-01,
            3.76659540e-01,
            7.76627528e-02,
            4.12925053e-01,
            4.03867719e-01,
        ],
        [
            3.88615496e-01,
            3.17694137e-01,
            2.42077265e-01,
            5.12364842e-01,
            4.88246266e-01,
        ],
        [
            -2.35883624e-01,
            1.69377515e-01,
            -3.33261685e-02,
            9.56925663e-03,
            2.61190595e-01,
        ],
        [
            1.36419556e-01,
            1.06685267e-01,
            2.27841214e-01,
            6.84258128e-02,
            4.52582214e-01,
        ],
        [
            -1.26862573e-01,
            -2.03209587e-01,
            -1.39544216e-01,
            -1.86340515e-01,
            -4.36590246e-01,
        ],
        [
            -5.44032080e-02,
            2.42229489e-01,
            -5.71334114e-02,
            1.41435027e-01,
            9.32424986e-02,
        ],
        [
            2.60867675e-01,
            -9.32940584e-02,
            2.08720934e-01,
            1.22567460e-01,
            1.48430016e-01,
        ],
        [
            -1.04524566e-01,
            5.79166132e-03,
            -7.51208212e-02,
            -1.64439748e-01,
            -2.59956442e-02,
        ],
        [
            1.98234151e-01,
            -4.07514417e-02,
            -3.94448867e-04,
            8.62068854e-02,
            -2.22206809e-01,
        ],
        [
            -3.33637809e-03,
            -2.22980161e-01,
            -1.38217330e-01,
            -1.55332959e-01,
            -5.09306753e-01,
        ],
        [
            1.71318752e-01,
            5.20542318e-02,
            1.10235179e-01,
            4.46185572e-02,
            5.69392627e-02,
        ],
        [
            -1.68481034e-01,
            1.36347986e-01,
            -1.00055783e-01,
            1.45716206e-01,
            8.57655245e-02,
        ],
        [
            3.62060709e-03,
            1.49853452e-01,
            -1.97140019e-02,
            -8.97430151e-03,
            7.70383660e-02,
        ],
        [
            -2.58072384e-01,
            -1.40710821e-02,
            -2.35032736e-01,
            -9.32153299e-02,
            -2.20718485e-01,
        ],
        [
            -1.81001581e-01,
            -3.00952439e-01,
            -1.97517209e-01,
            -3.25495319e-01,
            -4.70861861e-01,
        ],
        [
            -3.24941978e-02,
            -3.19222514e-01,
            -7.29554054e-03,
            -2.39742380e-01,
            -2.37337345e-01,
        ],
        [
            4.97711713e-02,
            -3.72034062e-01,
            -3.00656790e-02,
            -2.77721781e-01,
            -4.34612424e-01,
        ],
        [
            3.02368735e-01,
            2.21874171e-01,
            3.01221544e-01,
            3.65598121e-01,
            5.60338480e-01,
        ],
        [
            1.82885006e-01,
            6.68499651e-02,
            2.57768277e-01,
            1.05263794e-01,
            4.43117868e-01,
        ],
        [
            -1.54118721e-01,
            -3.15688528e-01,
            -9.74717604e-02,
            -2.61052179e-01,
            -4.02915702e-01,
        ],
        [
            1.56177683e-02,
            1.84582287e-01,
            -4.80063406e-03,
            2.84678779e-02,
            1.27744059e-01,
        ],
        [
            3.79797803e-02,
            1.74539183e-01,
            1.55900450e-01,
            1.91036315e-01,
            4.04037330e-01,
        ],
        [
            -3.54437960e-01,
            -1.66786731e-01,
            -2.05735080e-01,
            -3.15271840e-01,
            -3.54900296e-01,
        ],
        [
            1.23690454e-02,
            -1.14488644e-01,
            -7.34367860e-02,
            -2.01146677e-01,
            -2.65966909e-01,
        ],
        [
            -3.41486252e-01,
            -2.59409900e-01,
            -1.94073595e-01,
            -3.63166810e-01,
            -4.16319750e-01,
        ],
        [
            1.59715230e-01,
            1.33574828e-01,
            1.16427790e-02,
            3.05257381e-01,
            2.10292201e-02,
        ],
        [
            -3.52083435e-01,
            -4.03340812e-01,
            -2.37865513e-01,
            -5.12567442e-01,
            -5.88033579e-01,
        ],
        [
            -2.59127652e-03,
            -1.99529142e-01,
            -7.57733842e-03,
            -2.58088075e-01,
            -2.63267258e-01,
        ],
    ]
)

S = np.array(
    [
        [0, 3],
        [0, 5],
        [0, 14],
        [0, 17],
        [0, 19],
        [0, 20],
        [0, 23],
        [0, 27],
        [0, 28],
        [0, 33],
        [0, 40],
        [0, 43],
        [1, 4],
        [1, 5],
        [1, 6],
        [1, 7],
        [1, 10],
        [1, 16],
        [1, 18],
        [1, 23],
        [1, 26],
        [1, 30],
        [1, 32],
        [1, 41],
        [1, 45],
        [1, 46],
        [1, 47],
        [2, 14],
        [2, 16],
        [2, 17],
        [2, 18],
        [2, 19],
        [2, 23],
        [2, 28],
        [2, 31],
        [2, 34],
        [2, 39],
        [2, 40],
        [2, 49],
        [3, 7],
        [3, 18],
        [3, 20],
        [3, 26],
        [3, 27],
        [3, 31],
        [3, 32],
        [3, 39],
        [3, 44],
        [3, 46],
        [3, 47],
        [3, 49],
        [4, 9],
        [4, 12],
        [4, 15],
        [4, 16],
        [4, 18],
        [4, 25],
        [4, 26],
        [4, 36],
        [4, 40],
        [4, 41],
        [5, 8],
        [5, 18],
        [5, 21],
        [5, 23],
        [5, 25],
        [5, 28],
        [5, 33],
        [5, 38],
        [5, 40],
        [5, 41],
        [6, 7],
        [6, 9],
        [6, 29],
        [6, 30],
        [6, 34],
        [6, 36],
        [6, 42],
        [7, 9],
        [7, 11],
        [7, 14],
        [7, 25],
        [7, 27],
        [7, 29],
        [7, 31],
        [7, 32],
        [7, 34],
        [7, 38],
        [7, 40],
        [7, 42],
        [8, 15],
        [8, 20],
        [8, 22],
        [8, 24],
        [8, 26],
        [8, 27],
        [8, 28],
        [8, 35],
        [8, 41],
        [8, 46],
        [8, 48],
        [9, 11],
        [9, 25],
        [9, 29],
        [9, 35],
        [9, 36],
        [9, 37],
        [9, 40],
        [9, 42],
        [9, 44],
        [10, 13],
        [10, 14],
        [10, 26],
        [10, 31],
        [10, 32],
        [10, 36],
        [10, 38],
        [10, 44],
        [10, 45],
        [10, 47],
        [11, 12],
        [11, 19],
        [11, 29],
        [11, 30],
        [11, 31],
        [11, 32],
        [11, 35],
        [11, 36],
        [11, 42],
        [11, 49],
        [12, 13],
        [12, 14],
        [12, 15],
        [12, 17],
        [12, 26],
        [12, 30],
        [12, 31],
        [12, 38],
        [12, 45],
        [12, 46],
        [12, 47],
        [12, 48],
        [12, 49],
        [13, 15],
        [13, 24],
        [13, 29],
        [13, 36],
        [13, 40],
        [13, 41],
        [13, 45],
    ],
)

D = np.array(
    [
        [0, 8],
        [0, 9],
        [0, 10],
        [0, 11],
        [0, 15],
        [0, 16],
        [0, 26],
        [0, 29],
        [0, 31],
        [0, 35],
        [0, 36],
        [0, 37],
        [0, 38],
        [0, 46],
        [0, 48],
        [1, 13],
        [1, 17],
        [1, 24],
        [1, 27],
        [1, 34],
        [1, 36],
        [2, 6],
        [2, 10],
        [2, 12],
        [2, 13],
        [2, 24],
        [2, 26],
        [2, 29],
        [2, 37],
        [2, 46],
        [2, 48],
        [3, 8],
        [3, 12],
        [3, 13],
        [3, 16],
        [3, 21],
        [3, 25],
        [3, 29],
        [3, 35],
        [3, 36],
        [3, 41],
        [3, 48],
        [4, 6],
        [4, 8],
        [4, 11],
        [4, 20],
        [4, 22],
        [4, 24],
        [4, 33],
        [4, 43],
        [4, 46],
        [5, 7],
        [5, 11],
        [5, 13],
        [5, 17],
        [5, 19],
        [5, 29],
        [5, 30],
        [5, 31],
        [5, 32],
        [5, 34],
        [5, 35],
        [5, 36],
        [5, 42],
        [6, 20],
        [6, 21],
        [6, 23],
        [6, 24],
        [6, 28],
        [6, 40],
        [6, 41],
        [6, 43],
        [6, 46],
        [7, 8],
        [7, 12],
        [7, 13],
        [7, 15],
        [7, 21],
        [7, 24],
        [7, 33],
        [7, 36],
        [7, 41],
        [7, 43],
        [7, 46],
        [7, 47],
        [7, 48],
        [8, 9],
        [8, 11],
        [8, 14],
        [8, 16],
        [8, 17],
        [8, 23],
        [8, 29],
        [8, 30],
        [8, 32],
        [8, 34],
        [8, 42],
        [8, 45],
        [8, 49],
        [9, 17],
        [9, 18],
        [9, 20],
        [9, 21],
        [9, 30],
        [9, 31],
        [9, 39],
        [9, 43],
        [9, 47],
        [10, 19],
        [10, 24],
        [10, 27],
        [10, 29],
        [10, 34],
        [10, 40],
        [10, 42],
        [11, 21],
        [11, 23],
        [11, 24],
        [11, 28],
        [11, 37],
        [11, 39],
        [11, 40],
        [11, 41],
        [11, 44],
        [11, 47],
        [12, 19],
        [12, 20],
        [12, 22],
        [12, 23],
        [12, 25],
        [12, 32],
        [12, 33],
        [12, 34],
        [12, 39],
        [12, 43],
        [13, 17],
        [13, 20],
        [13, 22],
        [13, 27],
        [13, 28],
        [13, 30],
        [13, 31],
        [13, 32],
        [14, 15],
        [14, 21],
        [14, 31],
        [14, 41],
        [14, 44],
        [14, 47],
        [15, 17],
    ]
)

S_test = np.array(
    [
        [13, 46],
        [13, 48],
        [14, 16],
        [14, 17],
        [14, 19],
        [14, 29],
        [14, 32],
        [14, 35],
        [14, 37],
        [14, 40],
        [14, 49],
        [15, 20],
        [15, 24],
        [15, 31],
        [15, 33],
        [15, 36],
        [15, 48],
        [16, 17],
        [16, 19],
        [16, 23],
        [16, 30],
        [16, 31],
        [16, 36],
        [16, 38],
        [16, 49],
        [17, 19],
        [17, 21],
        [17, 22],
        [17, 23],
        [17, 27],
        [17, 35],
        [17, 36],
        [18, 19],
        [18, 21],
        [18, 23],
        [18, 28],
        [18, 40],
        [18, 43],
        [18, 49],
        [19, 23],
        [19, 34],
        [19, 39],
        [19, 40],
        [19, 49],
        [20, 22],
        [20, 34],
        [20, 42],
        [20, 44],
        [20, 46],
        [21, 22],
        [21, 23],
        [21, 24],
        [21, 28],
        [21, 33],
        [21, 40],
        [21, 47],
        [22, 34],
        [22, 39],
        [23, 27],
        [23, 28],
        [23, 33],
        [23, 39],
        [23, 47],
        [24, 25],
        [24, 27],
        [24, 33],
        [24, 35],
        [24, 39],
        [24, 43],
        [25, 29],
        [25, 32],
        [25, 37],
        [25, 42],
        [25, 43],
        [25, 49],
        [26, 27],
        [26, 30],
        [26, 32],
        [26, 38],
        [26, 43],
        [26, 46],
        [27, 30],
        [27, 31],
        [27, 43],
        [27, 46],
        [27, 47],
        [27, 49],
        [28, 37],
        [28, 41],
        [28, 43],
        [28, 47],
        [29, 34],
        [29, 35],
        [29, 36],
        [29, 42],
        [29, 48],
        [30, 32],
        [30, 34],
        [30, 42],
        [30, 45],
        [30, 47],
        [31, 34],
        [31, 36],
        [31, 38],
        [31, 41],
        [31, 44],
        [31, 45],
        [31, 47],
        [31, 48],
        [32, 34],
        [32, 38],
        [32, 39],
        [32, 40],
        [32, 41],
        [32, 42],
        [32, 44],
        [32, 46],
        [33, 35],
        [33, 47],
        [34, 45],
        [34, 49],
        [35, 37],
        [35, 45],
        [36, 37],
        [36, 41],
        [36, 45],
        [36, 48],
        [37, 38],
        [37, 41],
        [37, 46],
        [37, 48],
        [38, 41],
        [38, 45],
        [38, 46],
        [38, 48],
        [38, 49],
        [39, 43],
        [40, 49],
        [41, 43],
        [41, 46],
        [41, 47],
        [41, 48],
        [41, 49],
        [43, 44],
        [44, 46],
        [44, 48],
        [45, 48],
        [45, 49],
        [46, 49],
        [48, 49],
    ]
)

D_test = np.array(
    [
        [15, 18],
        [15, 19],
        [15, 21],
        [15, 27],
        [15, 30],
        [15, 32],
        [15, 39],
        [15, 42],
        [15, 43],
        [15, 47],
        [15, 49],
        [16, 33],
        [16, 35],
        [16, 42],
        [16, 43],
        [16, 46],
        [16, 47],
        [17, 20],
        [17, 24],
        [17, 26],
        [17, 28],
        [17, 41],
        [17, 43],
        [17, 44],
        [17, 46],
        [17, 48],
        [18, 20],
        [18, 24],
        [18, 34],
        [18, 35],
        [18, 38],
        [18, 42],
        [18, 45],
        [18, 46],
        [18, 48],
        [19, 30],
        [19, 33],
        [19, 46],
        [20, 23],
        [20, 26],
        [20, 36],
        [20, 39],
        [20, 41],
        [20, 45],
        [20, 48],
        [20, 49],
        [21, 29],
        [21, 30],
        [21, 31],
        [21, 32],
        [21, 42],
        [21, 46],
        [21, 48],
        [21, 49],
        [22, 28],
        [22, 31],
        [22, 37],
        [22, 41],
        [22, 45],
        [22, 48],
        [22, 49],
        [23, 24],
        [23, 26],
        [23, 31],
        [23, 34],
        [23, 36],
        [23, 38],
        [23, 42],
        [23, 44],
        [23, 45],
        [23, 46],
        [23, 48],
        [23, 49],
        [24, 32],
        [24, 36],
        [24, 38],
        [24, 45],
        [24, 47],
        [24, 48],
        [24, 49],
        [25, 27],
        [25, 30],
        [25, 33],
        [25, 36],
        [25, 38],
        [25, 45],
        [25, 48],
        [26, 29],
        [26, 34],
        [26, 37],
        [27, 28],
        [27, 35],
        [27, 37],
        [27, 38],
        [27, 39],
        [27, 48],
        [28, 32],
        [28, 33],
        [28, 36],
        [28, 44],
        [29, 31],
        [29, 32],
        [29, 33],
        [29, 38],
        [29, 39],
        [29, 40],
        [29, 43],
        [29, 44],
        [30, 33],
        [30, 35],
        [30, 37],
        [30, 39],
        [30, 43],
        [30, 44],
        [30, 48],
        [31, 37],
        [31, 40],
        [32, 48],
        [33, 34],
        [33, 36],
        [33, 42],
        [33, 45],
        [33, 48],
        [33, 49],
        [34, 37],
        [34, 38],
        [34, 47],
        [35, 40],
        [35, 41],
        [35, 43],
        [35, 46],
        [35, 49],
        [36, 40],
        [36, 47],
        [37, 44],
        [37, 49],
        [38, 39],
        [38, 42],
        [38, 44],
        [39, 42],
        [39, 44],
        [40, 44],
        [41, 42],
        [42, 43],
        [43, 45],
        [43, 49],
        [44, 47],
        [46, 47],
        [47, 48],
        [47, 49],
    ]
)


# # code used to generate the data
# np.random.seed(0)
# M = 300

# # Generate random data
# X = np.random.randn(N, n)
# X /= np.linalg.norm(X, axis=1, keepdims=True)

# # calculate pairwise distances
# edm = np.zeros((N, N))
# for i in range(N):
#     for j in range(i + 1, N):
#         edm[i, j] = np.sum((X[i] - X[j]) ** 2)

# # Generate similar and different pairs
# S, D = [], []
# for i in range(N):
#     for j in range(i + 1, N):
#         if edm[i, j] <= 2.0:
#             S.append((i, j))
#         else:
#             D.append((i, j))

# # transform data
# A = np.random.rand(n, n)
# A /= np.abs(np.linalg.eigvals(A)).max()
# X = X @ A

# # shuffle the pairs
# s_idx = np.sort(np.random.choice(len(S), M, replace=False))
# d_idx = np.sort(np.random.choice(len(D), M, replace=False))
# S, D = np.array(S)[s_idx], np.array(D)[d_idx]

# # Split the data into training and test sets
# S, S_test = S[: len(S) // 2], S[len(S) // 2 :]
# D, D_test = D[: len(D) // 2], D[len(D) // 2 :]
