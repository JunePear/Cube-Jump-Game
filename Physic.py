import pygame
import time

#monitor_info = pygame.display.Info()
#screen_width = monitor_info.current_w
#screen_height = monitor_info.current_h

pygame.init()
WIDTH = 1000
HEIGHT = 1000
#WINDOW = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulation")

Blue = (0, 120, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
White = (255, 255, 255)
Yellow = (255, 210, 150)
Dark_Blue = (50, 55, 180)

SPEED  = 20

all_bullets  = []


#_______________________________________________________________________________

def main():
    clock = pygame.time.Clock()
    
    run = True
    
    length = 50

    xA = 480
    yA = 480

    xB = 100
    yB = 100

    
    #candouble = False
    #candouble_check = False

    upVelSub = 0.5
    i=0

    upVel = 10
    downVel = 0

    BulletVel = 0

    x = 0

    XForce = 0

    JumpC = False
    canFall = True

    while run:
        clock.tick(80)
        


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                run = False

        WINDOW.fill(Blue)

        Cube_A = pygame.draw.rect(WINDOW, (Yellow), (xA, yA, 20, 20))
        Cube_B = pygame.draw.rect(WINDOW, (White), (xB, yB, 20, 20))
        Platform = pygame.draw.rect(WINDOW, (Black), (0, 720, 1000, 100))
        Jump_Fuel = pygame.draw.rect(WINDOW, (Yellow), (50, 190, 60, (9*(25-x))))
        pygame.display.flip()

        

        if canFall == True:
            yA += downVel
            downVel = downVel + 0.2
            
        if yA >= 700:
            canFall = False
            canJump = True

        if yA >= 700:
            yA = 700
            x = 0
            
            #candouble_check = True

        if yA < 700:
            canFall = True

        if xA < 0:
            xA = 0

        if xA > 980:
            xA = 980
            
        
        if xA == 0:
            XForce = XForce * -0.2
        
        if xA == 980:
            XForce = XForce * -0.2
            
            
        if JumpC == True:
            downVel = upVel * -0.5


        JumpC = False
        
        if keys[pygame.K_w]:
            
            if canJump ==  True:
                canFall = False
                yA -= upVel
                upVel = upVel - 0.2

                x = x + 1
                JumpC = True

                if x == 25:
                    canJump = False
                    canFall = True
                    upVel = 10
                    #downVel = upVel * -0.2
                    #if candouble_check == True:
                        #candouble = True
            
        
            #if candouble == True:
                #canJump = True
                #candouble = False
                #candouble_check = False

        xA = xA + XForce

        if keys[pygame.K_a] and yA >= 700:
            XForce = XForce - 0.2
            

        if keys[pygame.K_d] and yA >= 700:
            XForce = XForce + 0.2
        
        if XForce > 0 and yA >= 700:
            XForce = XForce - 0.1
        
        if XForce < 0 and yA >= 700:
            XForce = XForce + 0.1

        Cube_A = pygame.draw.rect(WINDOW, (Yellow), (xA, yA, 20, 20))
        Cube_B = pygame.draw.rect(WINDOW, (White), (xB, yB, 20, 20))
        pygame.display.flip()

        
        #if keys[pygame.K_a]:
            #if canJump == True:
                #xA -= XForce
                #XForce += 0.1
                #if XForce >= 7:
                    #XForce = 7
            
            
        #if keys[pygame.K_d]:
            #X

        start_can = pygame.math.Vector2(Cube_A.center)
        end = start_can
        
        if event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            end = start_can + (mouse - start_can).normalize() * length
        
        pygame.MOUSEBUTTONDOWN  
        if event.type == pygame.MOUSEBUTTONDOWN:
                
            mouse = pygame.mouse.get_pos()
            distance = mouse - start_can
            position = pygame.math.Vector2(Cube_A.center) # duplicate # start position in start of canon
            #position = pygame.math.Vector2(end)   # duplicate # start position in end of canon
            speed = distance.normalize() * SPEED
            all_bullets.append([position, speed])
                    
            

            mouse = pygame.mouse.get_pos()
            distance = mouse - start_can
            position = pygame.math.Vector2(Cube_A.center) # duplicate # start position in start of canon
            #position = pygame.math.Vector2(end)   # duplicate # start position in end of canon
            speed = distance.normalize() * SPEED
            all_bullets.append([position, speed])

        for position, speed in all_bullets:
            position += speed

        pygame.draw.line(WINDOW, (Red), start_can, end)

        for position, speed in all_bullets:
                
            pos_x = int(position.x)
            pos_y = int(position.y)
            def line_Bullet():
                pygame.draw.rect(WINDOW, (255, 255, 255), (pos_x, pos_y, 5, 5))
            line_Bullet()

        
            
            

        pygame.display.flip()


        pygame.display.update()
        
    pygame.quit()


if __name__ == "__main__":
    main()