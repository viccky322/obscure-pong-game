import pygame, sys ,random
from pygame.constants import  K_UP ,K_DOWN
from pygame import mixer 

#inputs
ball_speed_x=8* random.choice((1,-1))
ball_speed_y=8* random.choice((1,-1))
player_speed = 0 
opponent_speed= 20
player_score=0
opponent_score=0


#animations
def ball_speed(): 
    global ball_speed_x,ball_speed_y,player_score,opponent_score
    
    ball.x=ball.x+ball_speed_x
    
    ball.y=ball.y+ball_speed_y
    
    if ball.top<= 0 or ball.bottom>=screen_height:
        
        ball_speed_y=ball_speed_y *-1
    if ball.left<=0 :
        pygame.mixer.Sound.play(score_sound)
        opponent_score= opponent_score +1
        ball_reset()
    if ball.right>= screen_width:
        pygame.mixer.Sound.play(score_sound)
        player_score= player_score +1
        ball_reset()
        #bug ,frame skips when both the ball and the rect are moving ?
    if ball.colliderect(player) and ball_speed_x<0:
        pygame.mixer.Sound.play(collision_sound)
        if abs(ball.left - player.right) < 10: 
            ball_speed_x= ball_speed_x *-1
        elif abs(ball.bottom- player.top) <8 and ball_speed_y>0:
            ball_speed_y=ball_speed_y* -1
            print(ball.bottom-player.top)
        elif abs(ball.top- player.bottom) < 8 and ball_speed_y<0:
            ball_speed_y=ball_speed_y* -1
        
    if ball.colliderect(opponent) and ball_speed_x>0:
        pygame.mixer.Sound.play(collision_sound)
        if abs(ball.right - opponent.left) < 10: 
            ball_speed_x= ball_speed_x *-1
            
        elif abs(ball.bottom- opponent.top) <10 and ball_speed_y>0:
            ball_speed_y=ball_speed_y* -1
            print(ball.bottom- opponent.top)
        elif abs(ball.top- opponent.bottom) <10  and ball_speed_y<0:
            ball_speed_y=ball_speed_y* -1      
        
def player_animation():
    player.y= player.y + player_speed
    if player.top <=0 :
        player.top = 0 
    if player.bottom>= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top <ball.y :
        opponent.top =opponent.top + opponent_speed
    if opponent.bottom>= ball.y:
        opponent.bottom = opponent.bottom- opponent_speed
    if opponent.top <=0 :
        opponent.top = 0 
    if opponent.bottom>= screen_height:
        opponent.bottom = screen_height

def ball_reset():
    global ball_speed_x ,ball_speed_y
    ball.center= (screen_width/2,screen_height/2)    
    ball_speed_y= ball_speed_y * random.choice((1,-1))
    ball_speed_x= ball_speed_x * random.choice((1,-1))


        
#setup   
pygame.mixer.pre_init(44100,-16,2,512)     
pygame.init()
clock = pygame.time.Clock()
my_font=pygame.font.Font("freesansbold.ttf",45)

#window
screen_width=1280
screen_height=720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('pong ponginon')

#rectangles   (x,y,dimensão x,dimensão y)
ball = pygame.Rect(screen_width/2-(20/2),  screen_height/2,20,20)
player=pygame.Rect(20,screen_height/2-50,8,100)
opponent=pygame.Rect(screen_width-20,screen_height/2-50,8,100)

#colors
white_color=(255,255,255)
black_color=(0,0,0)
red_color=(255,0,0)
blue_color=(0,0,255)
green_color=(0,255,0)
background= pygame.image.load('..\images\\tennis_battle.png')

#sound
collision_sound=pygame.mixer.Sound('..\sound\collision_sound_effect.ogg')
score_sound=pygame.mixer.Sound('..\sound\score_sound_effect.ogg')



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 #Since Pygame doest recognize key holdings,you can assign a speed to your object that is going to change every frame 
 #and increment a number value for the movement as you press or release a button.      
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_s:
                player_speed= player_speed +7
            if event.key ==pygame.K_w:
                player_speed=player_speed - 7 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed=player_speed +7
            if event.key ==pygame.K_s:
                player_speed=player_speed - 7 
            
    ball_speed()
    player_animation()
    opponent_animation()
   
            
    #colors (surface,color,object)
    screen.fill(black_color)
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,black_color,player)
    pygame.draw.rect(screen,black_color,opponent)
    pygame.draw.ellipse (screen,green_color,ball)
    #pygame.draw.aaline(screen,black_color,(screen_width/2,0),(screen_width/2,screen_height))
    p1_text= my_font.render(f"{player_score}",False,black_color)
    screen.blit(p1_text,(400,300))
    p2_text=my_font.render(f"{opponent_score}",False,black_color)
    screen.blit(p2_text,(900,300))
    
    #window update
    pygame.display.flip()
    clock.tick(120)