#H I! 
# helo :3
import pygame

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
        
def pixel_to_coord(x, y):
    return -1

def zoom_to_mouse(x, y):
    pygame.mouse.get_pos[0] #x

def make_view(size, upper_x = 1, upper_i = 1, displacement = 2):
    view = [[0 for i in range(size)] for j in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            if(converge(complex(upper_x - displacement/size * j, upper_i - displacement/size * i))):
                window.set_at((SIZE-1-j, i), (0, 0, 0))

pygame.init()

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

    make_view(SIZE, 1, 1, 2)

    #(2.5 * zoom_factor)

    #zoom_to_mouse(x, y)

    pygame.display.update()
