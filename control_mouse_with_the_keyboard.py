from pynput.mouse import Button, Controller
from time import sleep
import pygame


mouse = Controller()
print("controls: \n up=w \n down=s \n left=a \n right=d \n leftclick=q \n rightclick=e")
print("clicking on athother window will make it stop working click on the pygame window to fix it")

print("press enter")
input()

screen = pygame.display.set_mode((600,600))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mouse.move(0, -100)
            if event.key == pygame.K_a:
                mouse.move(-100,0)
            if event.key == pygame.K_s:
                mouse.move(0, 100)
            if event.key == pygame.K_d:
                mouse.move(100, 0)
            if event.key == pygame.K_q:
                mouse.click(Button.left, 1)
            if event.key == pygame.K_e:
                mouse.click(Button.right, 1)





