from solver import equation1, equation2, equation3, equation4
import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse
from script import getValue
from formater import multiple_formatter

def help():
    print("""
# Interactive Python Pendulum

displays 4 graphs of the angle of a pendulum with time

## Usage

to launch User interface
python script.py [-h]

to generate graph
python shower.py [options]

 - --file path_to_graph
 - -G float Gravity constant
 - -L float Length of chord
 - -M float Mass of pendulum
 - -K float Air resistrance coefficient
 - -T float Time span
 - -N integer Number of interations
 - -A float Initial angle
 - -S float Initial speed

The default values can be modifed in default.conf


todo:
 - add config file for default values and range

    """)

# the function that describes the motion of a pendulum 
def fun(t, theta, g=9.81, l=1, m=1, k=0):
    theta_1 = theta[0]
    theta_2 = theta[1]

    d_theta_1 = theta_2
    d_theta_2 = - g / l * np.sin(theta_1) - k / m * theta_2

    return np.array([d_theta_1, d_theta_2])

# a function that splits the graph when the angle depasses the top so that it stays betwwen -pi and pi
def split_Y(Y, T):
    acc = 100
    indexes = [0, 1]
    for i in range(len(Y)-1):
        d = Y[i]/Y[i+1]
        if np.round(d * acc) == -acc:
            indexes.append(i)
            indexes.append(i+1)

    indexes.append(len(T))
    return indexes


# function that generates each graph
def generateGraph(imgfile, G, L, M, K, T, N, A, S):
    plt.style.use('dark_background')
    generatePlot(G, L, M, K, T, N, A, S, equation1, "RK43", 'w', fun)
    generatePlot(G, L, M, K, T, N, A, S, equation2, "RK1", 'b', fun)
    generatePlot(G, L, M, K, T, N, A, S, equation3, "RK2", 'r', fun)
    generatePlot(G, L, M, K, T, N, A, S, equation4, "exact", 'g', lambda t, y: np.exp(-K/M*t/2) * (y[0] * np.cos(np.sqrt(G/L - ((K/M)**2)/4)*t) + (y[1] + K/M*y[0]/2)/(np.sqrt(G/L - ((K/M)**2)/4))*np.sin(np.sqrt(G/L - ((K/M)**2)/4)*t)))
    
    plt.title("Motion of a Pendulum", loc="left")
    plt.xlabel("time  s", loc="left")
    plt.ylabel("angle  rad", loc="bottom")
    plt.legend()
    ax = plt.gca()
    ax.xaxis.set_major_locator(plt.MultipleLocator())
    ax.xaxis.set_minor_locator(plt.MultipleLocator())
    ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))

    plt.savefig(imgfile)



# function that plots each graph
def generatePlot(G, L, M, K, T, N, A, S, eq, lb, c, fun):
    X, Y = eq(fun, (G, L, M, K), t_max=T, n=N, theta_0=np.array([A, S]))
    splits = split_Y(Y, X)
    for i in range(1, len(splits)-1):
        i1 = splits[i-1]
        i2 = splits[i]
        i3 = splits[i+1]
        plt.plot(X[i1:i2], Y[i1:i2], c, label=lb)
        plt.plot(X[i2:i3], Y[i2:i3], c)


# main function that parses the command line for the values
def main():
    descript = "Testing"
    parser = argparse.ArgumentParser(
            prog="Pendulum Simulator",
            description="This is the file that creates a image ('graph.png') from the given parameters. If no parameters are given defaults to those in config.",
            epilog="todo\n- add config file",
            add_help=False)

    parser.add_argument('--file', dest='imgfile', required=False)
    parser.add_argument('-G', dest='G', required=False)
    parser.add_argument('-L', dest='L', required=False)
    parser.add_argument('-M', dest='M', required=False)
    parser.add_argument('-K', dest='K', required=False)
    parser.add_argument('-T', dest='T', required=False)
    parser.add_argument('-N', dest='N', required=False)
    parser.add_argument('-A', dest='A', required=False)
    parser.add_argument('-S', dest='S', required=False)
    parser.add_argument('--help', dest='H', required=False, help="displays this help", action="store_true")

    args = parser.parse_args()

    imgfile = "graph.png"
    G = float(getValue("G", 0))
    L = float(getValue("L", 0))
    M = float(getValue("M", 0))
    K = float(getValue("K", 0))
    T = float(getValue("T", 0))
    N = int(getValue("N", 0))
    A = float(getValue("A", 0))
    S = float(getValue("S", 0))


    if args.H:
        help()


    if args.imgfile:
        imgfile = args.imgfile

    if args.G:
        G = float(args.G)

    if args.L:
        L = float(args.L)

    if args.M:
        M = float(args.M)

    if args.K:
        K = float(args.K)

    if args.T:
        T = float(args.T)

    if args.N:
        N = int(args.N)

    if args.S:
        S = float(args.S)

    if args.A:
        A = float(args.A)

    generateGraph(imgfile, G, L, M, K, T, N, A, S)


if __name__ == '__main__':
    main()
