import pygame
from pygame.locals import *
import random

size = width, height = (800,600)
road_width = int(width/1.6)
roadline_width = int(width/80)
left_lane = width/2 -  road_width/4
right_lane = width/2 +  road_width/4
speed = 1
score_value = 0
speed_accelerate = False


pygame.init()
run = True
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Car Rush")
screen.fill((156,102,31))

pygame.display.update()

car = pygame.image.load("PlayerCar.png")
car_loc = car.get_rect()
car_loc.center = left_lane,height*0.8

car2 = pygame.image.load("EnemyCar.png")
car2_loc = car2.get_rect()
car2_loc.center = right_lane,height*0.2

counter = 0

while run:
    counter += 1
    if counter == 1500:
        speed += 1
        score_value += speed
        counter = 0
        print("Level up and score" , speed,score_value)
        
    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0,1) == 0: # can be true or false both like 0,1
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 225: # pixel of both the cars should be equal unless collision won't take place
        print("GAME OVER!")
        break 
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_width/2),0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_width/2),0])
            if event.key in [K_w, K_UP]:
                car_loc = car_loc.move([0,-int(road_width/2)])
            if event.key in [K_s, K_DOWN]:
                car_loc = car_loc.move([0,int(road_width/2)])

    pygame.draw.rect(screen,(26,26,26),(width/2-road_width/2,0,road_width,height))
    pygame.draw.rect(screen,(255,215,0),(width/2-roadline_width/2,0, roadline_width,height))
    pygame.draw.rect(screen,(255,255,255),(width/2-road_width/2 + roadline_width*2,0,roadline_width,height))
    pygame.draw.rect(screen,(255,255,255),(width/2+road_width/2 - roadline_width*3,0,roadline_width,height))
    

    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("SCORE :" + str(score_value),True,(118,238,0))
    textrect = text.get_rect()
    textrect.center = ((800/10,600/10))
    

    screen.blit(text,textrect.center)
    screen.blit(car, car_loc)
    screen.blit(car2,car2_loc)
    pygame.display.update()



pygame.quit()
quit()