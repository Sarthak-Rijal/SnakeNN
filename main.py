import math
import random
import pygame
from snake import *
from cube import *
import math



def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
        

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    #s.draw(surface)
    #snack.draw(surface)
    drawGrid(width,rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(1,rows-1)
        y = random.randrange(1,rows-1)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
        
    return (x,y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, s, snack

    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    
    #s = snake((255,0,0), (10,10))
    test = snake((255,0,0,), (1,0))
    #snack = cube(randomSnack(rows, s), color=(0,255,0))

    flag = True
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(100)
        clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #s.move(snack.pos)

        #if s.body[0].pos == snack.pos:
          #  s.addCube()
         #   snack = cube(randomSnack(rows, s), color=(0,255,0))


        #print(s.seeingAlgo(snack.pos))

        #print(s.dead()) #check for death
        
        win.fill((0,0,0))
        test.update(win)
        #snack.draw(surface)
        drawGrid(width,rows, win)
        pygame.display.update()
        
        
        #redrawWindow(win)

main()