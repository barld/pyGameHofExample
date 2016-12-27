import sys, pygame
from LinkedList import *
pygame.init()

l = Node(2,Node(3,(Node(4,Node(5,Node(6,Empty()))))))
f = lambda x : x*2
state = MapperState(l, f)

size = width, height = 1520, 240
black = 0, 0, 0
myfont = pygame.font.SysFont("monospace", 25)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

clock.tick(3000)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    dt = clock.tick(10)/1000.0
    state.Update(dt)

    screen.fill(black)
    # render text
    label = myfont.render(state.s, 2, (255, 255, 0))
    screen.blit(label, (100, 100))
    pygame.display.flip()