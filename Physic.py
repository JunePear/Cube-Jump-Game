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
    
    canJump = True
    is_grounded = False

    platforms = [
        pygame.Rect(0, 720, 1000, 100),
        pygame.Rect(0, 140, 1000, 20),
        pygame.Rect(350, 550, 300, 20),  
        pygame.Rect(150, 400, 250, 20),   
        pygame.Rect(600, 400, 250, 20)     
    ]

    while run:
        clock.tick(60)
        
       
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

           
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_can = pygame.math.Vector2(xA + 10, yA + 10) 
                mouse = pygame.mouse.get_pos()
                distance = mouse - start_can
                if distance.length() > 0:
                   
                    bullet_dir = distance.normalize()
                    
                   
                    XForce -= bullet_dir.x * 10.0
                    downVel -= bullet_dir.y * 12.0
                    is_grounded = False 
                    
                    position = pygame.math.Vector2(start_can) # duplicate # start position in start of canon
                    #position = pygame.math.Vector2(end)   # duplicate # start position in end of canon
                    speed = bullet_dir * SPEED
                    all_bullets.append([position, speed])
                    
                    mouse = pygame.mouse.get_pos()
                    distance = mouse - start_can
                    position = pygame.math.Vector2(start_can) # duplicate # start position in start of canon
                    #position = pygame.math.Vector2(end)   # duplicate # start position in end of canon
                    speed = bullet_dir * SPEED
                    all_bullets.append([position, speed])


      
        if keys[pygame.K_a]:
            XForce = XForce - 0.9  
        if keys[pygame.K_d]:
            XForce = XForce + 0.9  
        
        if is_grounded:
            XForce = XForce * 0.82
        else:
            XForce = XForce * 0.95

        xA = xA + XForce

        
        if xA < 0:
            xA = 0
            XForce = -XForce * 0.75  

        if xA > 980:
            xA = 980
            XForce = -XForce * 0.75  
        

       
        if not is_grounded:
            downVel += 0.6  
            yA += downVel
            
     
        if keys[pygame.K_w]:
            if canJump == True:
                is_grounded = False
                yA -= 6         
                downVel = -4.5  
                
                x = x + 1.5     
                JumpC = True

                if x >= 15:     
                    canJump = False
                    upVel = 10
                    #downVel = upVel * -0.2
                    #if candouble_check == True:
                        #candouble = True
        else:
            if not is_grounded:
                canJump = False

     
        player_rect = pygame.Rect(xA, yA, 20, 20)
        is_grounded = False  

        for plat in platforms:
            if player_rect.colliderect(plat):
                if downVel >= 0 and player_rect.bottom - downVel <= plat.top + 10:
                    yA = plat.top - 20
                    downVel = 0
                    is_grounded = True
                    canJump = True
                    x = 0
                    #candouble_check = True
                elif downVel < 0 and player_rect.top - downVel >= plat.bottom - 10:
                    yA = plat.bottom
                    downVel = 0.5
                elif XForce > 0:
                    xA = plat.left - 20
                    XForce = -XForce * 0.5
                elif XForce < 0:
                    xA = plat.right
                    XForce = -XForce * 0.5

        if yA < 700 and is_grounded == False:
            pass 

        if JumpC == True:
            pass

        JumpC = False


        #if keys[pygame.K_a]:
            #if canJump == True:
                #xA -= XForce
                #XForce += 0.1
                #if XForce >= 7:
                    #XForce = 7
            
            
        #if keys[pygame.K_d]:
            #X


        #render pipleline
        WINDOW.fill(Blue)
        
        for plat in platforms:
            pygame.draw.rect(WINDOW, Black, plat)
            

        Cube_A = pygame.draw.rect(WINDOW, (Yellow), (xA, yA, 20, 20))
        Cube_B = pygame.draw.rect(WINDOW, (White), (xB, yB, 20, 20))

        start_can = pygame.math.Vector2(Cube_A.center)
        mouse = pygame.mouse.get_pos()
        dir_vector = mouse - start_can
        if dir_vector.length() > 0:
            end = start_can + dir_vector.normalize() * length
        else:
            end = start_can
        
        pygame.MOUSEBUTTONDOWN  

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
