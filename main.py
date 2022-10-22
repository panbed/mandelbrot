import pygame

MAX_ITERATE = 150
CONVERGENCE_CUTOFF = 50
SIZE = 500

def converge(c):
    z = 0
    for i in range(MAX_ITERATE):
        z = z ** 2 + c
        if(abs(z) > CONVERGENCE_CUTOFF):
            break

    return abs(z) <= 5

def pixel_to_zoom(center_coord, bound, zoom_factor = 1, size = SIZE):
    displacement = bound[2]/zoom_factor

    x = (bound[0] - (center_coord[0]/size)*bound[2]) + displacement/2
    y = (bound[1] - (center_coord[1]/size)*bound[2]) + displacement/2

    return(x, y, displacement)

def zoom_to_mouse(x, y):
    return (pygame.mouse.get_pos[0], pygame.mouse.get_pos[1])

def make_view(bound, size = SIZE):
    view = [[0 for i in range(size)] for j in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            if(converge(complex(bound[0] - bound[2]/size * j, bound[1] - bound[2]/size * i))):
                window.set_at((SIZE-1-j, i), (0, 0, 0))

pygame.init()

window = pygame.display.set_mode([SIZE, SIZE])

bound = (2, 2, 4)
counter = 0

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))

    make_view(bound, SIZE)

    # 475 with 750 goes crazy
    if(counter <= 200):
        bound = pixel_to_zoom((500, 500), bound, SIZE, 2)

    pygame.display.update()
    counter = counter + 1
