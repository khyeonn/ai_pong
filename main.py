import threading
import time
import pygame
import pong



#starts a function as a thread so it can run synchronously
def startThread(function, arguments):
    t = threading.Thread(target = function, args = arguments)
    t.start()

#moves a paddle for a certain number of seconds, must be called through a thread
def move_paddle(direction, seconds):
    k = pygame.event.Event(pygame.KEYDOWN)
    k.key = direction
    
    pong.keydown(k)
    time.sleep(seconds)
    pong.keyup(k)
    return

right_up = pygame.K_UP
right_down = pygame.K_DOWN
left_up = pygame.K_w
left_down = pygame.K_s
    
startThread(move_paddle, (right_up, 0.2))
startThread(move_paddle, (left_down, 0.2))

pong.game_loop()
