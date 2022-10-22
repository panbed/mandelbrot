#H I! 
# helo :3
import pygame
import PySimpleGUI as gui

# gui.theme() # set pysimplegui theme

pygame.init()

MAX_ITERATE = 30
CONVERGENCE_CUTOFF = 250
SIZE = 500

def converge(c):
    z = 0
    for i in range(MAX_ITERATE):
        z = z ** 2 + c
        if(abs(z) > CONVERGENCE_CUTOFF):
            break

    return abs(z) <= 5

def make_view(window, size, upper_x = 1, upper_i = 1, displacement = 2):
    view = [[0 for i in range(size)] for j in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            if(converge(complex(upper_x - displacement/size * j, upper_i - displacement/size * i))):
                window.set_at((SIZE-1-j, i), (0, 0, 0))



def display_mandelbrot():

    window = pygame.display.set_mode([SIZE, SIZE])

    x = 1
    y = 1

    run = True
    while run:

        zoom_factor = 0.75
        inv_factor = 0.25

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill((255, 255, 255))

        make_view(window, SIZE, 1, 1, 2)

        pygame.display.update()

def display_gui():
    # layout of the menubar at top of gui
    menu = [
        ["&Help", ["&Mandelbrots"]],
        ["&About"]
    ]

    # actual layout of the main gui
    layout = [
        [gui.Menu(menu)],
        [gui.Text("Resolution: "), gui.Input(size = (5, 1), key="_RES_")],
        [gui.Text("i-coordinate: "), gui.Input(size = (5, 1), key="_ICORD_")],
        [gui.Text("x-coordinate: "), gui.Input(size = (5, 1), key="_XCORD_")],
        [gui.Text("Displacement: "), gui.Input(size = (5, 1), key="_DIS_")],
    ]

    sg_window = gui.Window("Mandelbrots!", layout)

    run = True
    while run:
        event, values = sg_window.read()
        if event in (gui.WIN_CLOSED, 'Exit'):
            break

        if event == "Mandelbrots":
            print("help feature")
        elif event == "About":
            print("about feature")

    sg_window.close()



display_gui()
#display_mandelbrot()