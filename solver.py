import numpy as np
import scipy.integrate as spi
from RK import RK1, RK2

# function for the solve_ivp
def equation1(fun, args, theta_0=[1, 1], t_max=np.pi*2, n=50):
    t_0 = 0
    t_1 = t_max
    t = (t_0, t_1)

    theta = spi.solve_ivp(lambda t, y: fun(
        t, y, args[0], args[1], args[2], args[3]), t, theta_0, t_eval=np.linspace(t_0, t_1, n))

    return theta.t, theta.y[0, :]


# function for the RK1
def equation2(fun, args, theta_0=[1, 1], t_max=np.pi*2, n=50):
    theta = RK1(lambda t, y: fun(t, y, args[0], args[1], args[2], args[3]), np.array(
        [0, t_max]), np.array(theta_0), t_eval=np.linspace(0, t_max, n))

    return np.linspace(0, t_max, n-3), theta[0, :]

# funtion for the RK2
def equation3(fun, args, theta_0=[1, 1], t_max=np.pi*2, n=50):
    theta = RK2(lambda t, y: fun(t, y, args[0], args[1], args[2], args[3]), np.array(
        [0, t_max]), np.array(theta_0), t_eval=np.linspace(0, t_max, n))

    return np.linspace(0, t_max, n-3), theta[0, :]

# exact solution function
def equation4(fun, args, theta_0=[1, 1], t_max=np.pi*2, n=50):
    t_span = np.linspace(0, t_max, n-3)
    theta = fun(t_span, theta_0)
    return t_span, theta
