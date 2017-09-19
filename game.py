import pygame,sys
from pygame.locals import *
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
color = (0,40,40)
height = 600
width = 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Air Hockey')
screen.fill(color)
clock = pygame.time.Clock()

paddle_color = (255,215,0)
paddle1 = 300
paddle2 = 300
ball_x = 400
ball_y = 300
direction_x = 5
direction_y = -5
score1,score2 = 0,0

def collision(ball_x,ball_y,direction_x,direction_y,paddle1,paddle2,width,height):
    if (ball_x == 30 and ball_y+10 >= paddle1 and ball_y <= paddle1+50):
        direction_x *= -1
    elif (ball_x == width-30 and ball_y >= paddle2 and ball_y <= paddle2+50):
        direction_x *= -1
    if (ball_y <= 0 or ball_y >= height):
        direction_y *= -1
    return direction_x,direction_y

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(color)
    pygame.draw.rect(screen,paddle_color,pygame.Rect(20,paddle1,10,50))
    pygame.draw.rect(screen,paddle_color,pygame.Rect(width-30,paddle2,10,50))
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(width//2 ,0,2,height))
    pygame.draw.circle(screen, (255,255,255), (ball_x,ball_y) , 10)
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_UP] and paddle1 >= 10):
        paddle1 -= 6
    if (pressed[pygame.K_DOWN] and paddle1 <= height-60):
        paddle1 += 6

    score_1 = myfont.render(str(score1), False, (255, 255, 0))
    score_2 = myfont.render(str(score2), False, (255, 255, 0))
    direction_x,direction_y = collision(ball_x,ball_y,direction_x,direction_y,paddle1,paddle2,width,height)
    ball_x += direction_x
    ball_y += direction_y
    if (ball_x >= 300 and ball_y - paddle2 >= 0 and paddle2 <= 540):
        paddle2 += 6
    if (ball_x >= 300 and ball_y - paddle2 <= 0 and paddle2 >= 10):
        paddle2 -= 6
    if (ball_x >= width):
        score1 += 1
        paddle1,paddle2 = 300,300
        ball_x = width//2
        ball_y = height//2
    if (ball_x <= 0):
        score2 += 1
        paddle1,paddle2 = 300,300
        ball_x = width//2
        ball_y = height//2
    screen.blit(score_1,(350,300))
    screen.blit(score_2,(450,300))
    clock.tick(60)
    pygame.display.update()
