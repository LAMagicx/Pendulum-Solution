import tkinter as tk
from PIL import Image, ImageTk
import os, time, sys

background_colour = '#000000'
text_colour = '#EEEEEE'

def Create():
    returned = os.system('python shower.py --file graph.png  -G {0} -L {1} -M {2} -K {3} -T {4} -N {5} -A {6} -S {7}'.format(
                                                                                            float(G_var.get()), 
                                                                                            float(L_var.get()),
                                                                                            float(M_var.get()),
                                                                                            float(K_var.get()),
                                                                                            float(T_var.get()),
                                                                                            int(N_var.get()),
                                                                                            float(A_var.get()),
                                                                                            float(S_var.get())
                                                                                            ))
    image2 = Image.open("graph.png")
    image2 = image2.resize((640, 480), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(image2)
    image.configure(image=img2)
    image.image = img2  

def slide_g(arg):
    select = 'G: ' + str(G_var.get())
    G_Value.config(text=select)

def slide_L(arg):
    select = 'L: ' + str(L_var.get())
    L_Value.config(text=select)

def slide_M(arg):
    select = 'M: ' + str(M_var.get())
    M_Value.config(text=select)

def slide_K(arg):
    select = 'K: ' + str(K_var.get())
    K_Value.config(text=select)

def slide_T(arg):
    select = 'T: ' + str(T_var.get())
    T_Value.config(text=select)

def slide_N(arg):
    select = 'N: ' + str(N_var.get())
    N_Value.config(text=select)

def slide_A(arg):
    select = 'A: ' + str(A_var.get())
    A_Value.config(text=select)

def slide_S(arg):
    select = 'S: ' + str(S_var.get())
    S_Value.config(text=select)

def Open():
    os.system("graph.png")


def main():
    window = tk.Tk()

    window.title("APP")

    img = Image.open("graph.png")
    img = img.resize((640, 480), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    window.configure(background=background_colour)

    # sidebar
    sidebar = tk.Frame(window, width=200, bg='white', height=500, borderwidth=2, )
    sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
    sidebar.configure(background=background_colour)

    # main content area
    mainarea = tk.Frame(window, bg='#CCC', width=500, height=500)
    mainarea.pack(expand=True, fill='both', side='right')
    mainarea.configure(background=background_colour)


    image = tk.Label(mainarea, image=img, bg=background_colour)
    image.pack()


    button = tk.Button(sidebar, text="Generate", width=25,  command=Create)
    button.grid(row=19, column=0, sticky='S')

    G_var = tk.DoubleVar()

    G_slider = tk.Scale(sidebar, bg=background_colour, fg=text_colour, from_ = 0, to=25, resolution=0.1, orient='horizontal', command=slide_g, variable=G_var, showvalue=0, activebackground="#FFFFFF", highlightbackground=background_colour, highlightcolor=background_colour, sliderlength=20, length=180)
    G_slider.grid(row=0, column=0, sticky='S')
    G_slider.set(9.81)


    G_Value = tk.Label(sidebar, bg=background_colour, fg=text_colour)
    G_Value.grid(row=1, column=0, sticky='N')

    L_var = tk.DoubleVar()

    L_slider = tk.Scale(sidebar, bg=background_colour, fg=text_colour, from_ = 0.1, to=10, resolution=0.1, orient='horizontal', command=slide_L, variable=L_var, showvalue=0, activebackground="#FFFFFF", highlightbackground=background_colour, highlightcolor=background_colour, sliderlength=20, length=180)
    L_slider.grid(row=2, column=0, sticky='S')
    L_slider.set(1)


    L_Value = tk.Label(sidebar, bg=background_colour, fg=text_colour)
    L_Value.grid(row=3, column=0, sticky='N')

    M_var = tk.DoubleVar()

    M_slider = tk.Scale(sidebar, bg=background_colour, fg=text_colour, from_ = 0.1, to=100, resolution=0.1, orient='horizontal', command=slide_M, variable=M_var, showvalue=0, activebackground="#FFFFFF", highlightbackground=background_colour, highlightcolor=background_colour, sliderlength=20, length=180)
    M_slider.grid(row=4, column=0, sticky='S')
    M_slider.set(1)


    M_Value = tk.Label(sidebar, bg=background_colour, fg=text_colour)
    M_Value.grid(row=5, column=0, sticky='N')

    K_var = tk.DoubleVar()

    K_slider = tk.Scale(sidebar, bg=background_colour, fg=text_colour, from_ = 0, to=10, resolution=0.1, orient='horizontal', command=slide_K, variable=K_var, showvalue=0, activebackground="#FFFFFF", highlightbackground=background_colour, highlightcolor=background_colour, sliderlength=20, length=180)
    K_slider.grid(row=6, column=0, sticky='S')
    K_slider.set(0)


    K_Value = tk.Label(sidebar, bg=background_colour, fg=text_colour)
    K_Value.grid(row=7, column=0, sticky='N')

    T_var = tk.DoubleVar()

    T_slider = tk.Scale(sidebar, bg=background_colour, fg=text_colour, from_ = 0, to=1000, resolution=0.1, orient='horizontal', command=slide_T, variable=T_var, showvalue=0, activebackground="#FFFFFF", highlightbackground=background_colour, highlightcolor=background_colour, sliderlength=20, length=180)
    T_slider.grid(row=8, column=0, sticky='S')
    T_slider.set(6.28)


    T_Value = tk.Label(sidebar, bg=background_colour, fg=text_colour)
    T_Value.grid(row=9, column=0, sticky='N')

    N_var = tk.IntVar()

    N_slider = tk.Scale(sidebar, bg=background_colour, fg=text_colour, from_ = 0, to=500, resolution=1, orient='horizontal', command=slide_N, variable=N_var, showvalue=0, activebackground="#FFFFFF", highlightbackground=background_colour, highlightcolor=background_colour, sliderlength=20, length=180)
    N_slider.grid(row=10, column=0, sticky='S')
    N_slider.set(50)


    N_Value = tk.Label(sidebar, bg=background_colour, fg=text_colour)
    N_Value.grid(row=11, column=0, sticky='N')

    A_var = tk.DoubleVar()

    A_slider = tk.Scale(sidebar, bg=background_colour, fg=text_colour, from_ = -1.57, to=1.57, resolution=0.1, orient='horizontal', command=slide_A, variable=A_var, showvalue=0, activebackground="#FFFFFF", highlightbackground=background_colour, highlightcolor=background_colour, sliderlength=20, length=180)
    A_slider.grid(row=12, column=0, sticky='S')
    A_slider.set(1.8)


    A_Value = tk.Label(sidebar, bg=background_colour, fg=text_colour)
    A_Value.grid(row=13, column=0, sticky='N')

    S_var = tk.DoubleVar()

    S_slider = tk.Scale(sidebar, bg=background_colour, fg=text_colour, from_ = -10, to=10, resolution=0.1, orient='horizontal', command=slide_S, variable=S_var, showvalue=0, activebackground="#FFFFFF", highlightbackground=background_colour, highlightcolor=background_colour, sliderlength=20, length=180)
    S_slider.grid(row=14, column=0, sticky='S')
    S_slider.set(1)


    S_Value = tk.Label(sidebar, bg=background_colour, fg=text_colour)
    S_Value.grid(row=15, column=0, sticky='S')

    open_button = tk.Button(sidebar, text="Open", command=Open, bg=background_colour, fg=text_colour, width=25)
    open_button.grid(row=20, column=0, sticky='S')


    window.mainloop()


if __name__ == "__main__":

    if len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            os.system('python shower.py --help')
        else:
            print("python shower.py\n  -h for help\n")
    else:
        main()
