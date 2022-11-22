import pygame
from pygame.locals import *
import keyboard
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    (1, -1, 2),
    (1, 1, 2),
    (-1, -1, 2),
    (-1, 1, 2)    
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,7),
    (5,4),
    (4,8),
    (5,9),
    (6,10),
    (7,11),
    (8,9),
    (8,10),
    (9,11),
    (10,11)
    )


def Cube(framenum):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            if framenum == 0:
                glColor3f(0, 0, 1)
            else:
                glColor3f(1, 0, 0)
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -15)
    
    framenum = 0

    while True:
        framenum = (framenum + 1) % 2 
        if framenum == 1:
            glTranslatef(-0.07,0, 0)
        else:
            glTranslatef(0.07, 0, 0)
        if keyboard.is_pressed('s'):
            glTranslatef(0.0,0.0, -0.1)
        elif keyboard.is_pressed('w'):
            glTranslatef(0.0,0.0, 0.1)
        elif keyboard.is_pressed('a'):
            glTranslatef(0.1,0, 0)
        elif keyboard.is_pressed('d'):
            glTranslatef(-0.1,0, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(framenum)
        pygame.display.flip()
        pygame.time.wait(10)


main()