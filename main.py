#H I! 
# helo :3
from tkinter.tix import MAX
import pygame
import PySimpleGUI as gui

MAX_ITERATE = 150
CONVERGENCE_CUTOFF = 50
SIZE = 400

gui.theme("SystemDefaultForReal")

def converge(c, maximum = MAX_ITERATE):
    z = 0
    for i in range(maximum):
        z = z ** 2 + c
        if(abs(z) > CONVERGENCE_CUTOFF):
            break

    return abs(z) <= 5

def pixel_to_zoom(center_coord, bound, size = SIZE, zoom_factor = 1):
    displacement = bound[2]/zoom_factor
    x = (bound[0] - (center_coord[0]/size)*bound[2]) + displacement/2
    y = (bound[1] - (center_coord[1]/size)*bound[2]) + displacement/2

    return(x, y, displacement)

def zoom_to_mouse(x, y):
    return (pygame.mouse.get_pos[0], pygame.mouse.get_pos[1])

def make_view(window, bound = (2, 2, 4), size = SIZE):
    view = [[0 for i in range(size)] for j in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            if(converge(complex(bound[0] - bound[2]/size * j, bound[1] - bound[2]/size * i))):
                window.set_at((SIZE-1-j, i), (0, 0, 0))

def display_mandelbrot(bound, zoom):

    pygame.init()

    window = pygame.display.set_mode([SIZE, SIZE])

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break;

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                bound = pixel_to_zoom((SIZE - mouse_x, mouse_y), bound, SIZE, zoom)

        window.fill((255, 255, 255))

        make_view(window, bound, SIZE)

        pygame.display.update()

    pygame.quit()

def display_gui():
    # layout of the menubar at top of gui
    menu = [
        ["&Help", ["&Mandelbrots"]],
        ["&About"]
    ]

    inputs = [
        [gui.Text("Resolution: "), gui.Input(size = (5, 1), key="_RES_")],
        [gui.Text("(x, i): "), gui.Input(size = (1, 1), key="_ICORD_"), gui.Text(",", pad=(0,0)), gui.Input(size = (1, 1), key="_XCORD_")],
        #[gui.Text("x-coordinate: "), gui.Input(size = (5, 1), key="_XCORD_")],
        [gui.Text("Displacement: "), gui.Input(size = (5, 1), key="_DIS_")],
        [gui.Text("Zoom: "), gui.Slider(range=(1, 4), orientation="horizontal", default_value=2, resolution=0.1, border_width=0, enable_events=True, size=(10,10), key="_ZOOM_")],
    ]

    generate_column = [
        [gui.Button("Generate", key="_GEN_")]
    ]

    # actual layout of the main gui
    layout = [
        [gui.Menu(menu)],
        [gui.Column(inputs), gui.Column(generate_column)]
        
    ]

    sg_window = gui.Window("Mandelbrots!", layout, size=(250, 150))

    run = True
    while run:
        event, values = sg_window.read()
        if event in (gui.WIN_CLOSED, 'Exit'):
            break

        if event == "Mandelbrots":
            print(values["_ZOOM_"])
        elif event == "About":
            print("about feature")
        elif event == "_GEN_":
            print("gen")
            print(values["_XCORD_"])
            print(values["_ICORD_"])
            print(values["_ZOOM_"])
            
            x = float(values["_XCORD_"]) 
            i = float(values["_ICORD_"]) 
            displacement = float(values["_DIS_"])
            zoom = float(values["_ZOOM_"])

            bounds = x + displacement/2, i + displacement/2, displacement
            display_mandelbrot(bounds, zoom)

    sg_window.close()

display_gui()