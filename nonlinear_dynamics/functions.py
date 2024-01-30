def logistic_map(x0, r, N):
    """Computes an iteration of the logistic map"""
    x = x0
    iter_list = []
    x_list = []
    for i in range(0, N):
        x = r * x * (1 - x) 
        iter_list.append(i+1)
        x_list.append(x)
    return iter_list, x_list
    
