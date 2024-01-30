import numpy as np

from functions import logistic_map
from plotting import initial_conditions_logistic_map

rs = [2, 3.4, 3.72]

for r in rs:
    x0_1 = 0.2
    x0_2 = 0.200001
    n = 200
    initial_conditions_logistic_map(x0_1, x0_2, r, n)

for r in rs:
    x0_1 = 0.2
    x0_2 = 0.200001
    n = 500
    steps, x1 = logistic_map(x0_1, r, n)
    steps, x2 = logistic_map(x0_2, r, n)

    diff = abs(np.array(x1)-np.array(x2))
    print(f"For r = {r}, the difference between the {n}th iterate is {diff[-1]}.")
    
    if r == 3.72:
        ns = [5000, 500000]
        for n in ns:
            steps, x1 = logistic_map(x0_1, r, n)
            steps, x2 = logistic_map(x0_2, r, n)
            diff = abs(np.array(x1)-np.array(x2))
            avg_diff = (1/n)*sum(diff)
            print(f"For n = {n}, the average absolute difference for the first {n} iterates is {avg_diff}.")