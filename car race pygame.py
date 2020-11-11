import pygame,math

pygame.init()

#pygame.mixer_music.load("travis.wav")
#pygame.mixer_music.play(-1)

white = [255, 255, 255]
red = [255, 0, 0]

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PFE Race')

clock = pygame.time.Clock()

bg = pygame.image.load('bg.jpg')
carImg = pygame.image.load('racecar.png')
enemyCar = pygame.image.load('enemy.png')
carImg = pygame.transform.scale(carImg,(30,50))
enemyCar = pygame.transform.scale(enemyCar,(30,50))


#501 x 737
x = (display_width * 0.45)
y = (display_height * 0.1)
en_x = (display_width * 0.05)
en_y = (display_height * 0.05)
prevx = en_x
prevy = en_y - 1

x_change = 0
y_change = 0
y_b = False


o = math.pi / 2
o2 = math.pi / 2

def car(Sur, x, y, rot):
    Hajde = pygame.transform.rotate(Sur, math.degrees(rot+math.pi/2))
    okej = Hajde.get_rect()
    okej.center = (x, y)
    gameDisplay.blit(Hajde, okej)
def stay(x, y):
    if x > 740:
        x = 740
    if x < 60:
        x = 60
    if y > 540:
        y = 540
    if y < 60:
        y = 60
    return x,y
def check_collision(x,y,a,b):
    #30,50
    l1=(x-15,y-25)
    r1=(x+15,y+25)
    l2=(a-15,b-25)
    r2=(a+15,b+25)

    if (l1[0] > r2[0] or l2[0] > r1[0]):
        return False
    if (l1[1] > r2[1] or l2[1] > r1[1]):
        return False

    return True
def calc(x,y,o,dx,dy):
    dt = 1 / 60

    y = y + 100 * dt * math.cos(o-math.pi/2) * dy
    if (dy == 0):
        return [x,y,o]
    x = x + 100 * dt * math.sin(o-math.pi/2) * dy
    o = o - dt*dx
    return [x,y,o]
def enemy(x,y,o,dx,dy):
    dt = 1 / 60

    y = y + 100 * dt * math.cos(o-math.pi/2) * dy
    x = x + 100 * dt * math.sin(o-math.pi/2) * dy
    return [x,y,o]

def side(a,b,c):
    return ((c[0]-a[0])*(b[1]-a[1]) - (c[1]-a[1])*(b[0]-a[0])) > 0

def promeni(en_x,en_y,o2,x,y,o,prevx,prevy):
    dt = 1 / 60


    if side((en_x,en_y),(prevx,prevy),(x,y)):
        x,y,o = enemy(en_x,en_y,o2-dt,1,1)
        return [x,y,o]
    else:
        x,y,o = enemy(en_x,en_y,o2+dt,-1,1)
        return [x,y,o]

crashed = False
dx = 0
dy = 0
dx1 = 0
dy1 = 1
dt = 1 / 60

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #Kretanje user automobila
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            if event.key == pygame.K_RIGHT:
                dx = 1
            if event.key == pygame.K_UP:
                dy = 1
            if event.key == pygame.K_DOWN:
                dy = -1
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                dx = 0
            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                dy = 0
    f = en_x
    g = en_y

    x,y,o = calc(x,y,o,dx,dy)
    en_x,en_y,o2 = promeni(en_x,en_y,o2,x,y,o,prevx,prevy)

    prevx = f
    prevy = g

    x,y=stay(x,y)
    en_x,en_y=stay(en_x,en_y)

    gameDisplay.fill(red)
    gameDisplay.blit(bg,(0,0))
    car(carImg, x, y,o)
    car(enemyCar,en_x,en_y,o2)
    if check_collision(x,y,en_x,en_y) == True:
        pygame.quit()
        quit()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
