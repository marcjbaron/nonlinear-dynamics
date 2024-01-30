import matplotlib.pyplot as plt
import numpy as np

from functions import logistic_map

plt.rcParams['text.usetex'] = True


def initial_conditions_logistic_map(x0_1, x0_2, r, n):
    """Creates a plot showing the difference in iterations of the logistic map
    when you slightly change the initial conditions"""

    steps, x1 = logistic_map(x0_1, r, n)
    steps, x2 = logistic_map(x0_2, r, n)

    diff = abs(np.array(x1)-np.array(x2))

    fig, ax = plt.subplots()
    plt.scatter(steps, diff, s=2)
    plt.plot(steps, diff, linewidth=0.5, alpha=0.2) 
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"$| x_n - \hat{x_n}|$")
    plt.savefig(f"../images/initial_conditions_logistic_r = {r}.png")




