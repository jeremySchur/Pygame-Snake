import pygame, random, time

pygame.init()

#Color      R      G      B
Black    = (0,     0,     0)
White    = (255,  255,   255)
Green    = (0,    255,    0)
Red      = (255,   0,     0)
DarkGrey = (40,    40,    40)
Orange   = (255,  165,    0)
Blue     = (0,     0,    255)
Yellow   = (255,  255,    0)

screen_size = width, height = 640, 480
cell_size = cellwidth, cellheight = (width/20), (height/20)
screen = pygame.display.set_mode(screen_size)
Clock = pygame.time.Clock()
apple = pygame.image.load("apple.png").convert()
startscreen = pygame.image.load("startscreen.png").convert()
lightning = pygame.image.load("SpeedUp.png").convert()
xlogo = pygame.image.load("xlogo.gif").convert()
reverse = pygame.image.load("reverse.png").convert()
ice = pygame.image.load("slow.png").convert()
BlueDot = pygame.image.load("bluedot.png").convert()
GreenDot = pygame.image.load("greendot.png").convert()
YellowDot = pygame.image.load("yellowdot.png").convert()
WhiteDot = pygame.image.load("whitedot.png").convert()
Trap = pygame.image.load("trap.png").convert()
finalscreen = pygame.image.load("gameover.png").convert()
Font = pygame.font.Font('freesansbold.ttf', 25)
pickupsound = pygame.mixer.music.load("pickup.wav")
YellowWins = pygame.image.load("yellowwins.png").convert()
GreenWins = pygame.image.load("greenwins.png").convert()
Tie = pygame.image.load("tie.png").convert()
fin = open("highscore.txt", 'r')
global HighScore
HighScore = int(fin.read())
applelist = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620]
LenOfSnakeList = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
Walls = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
PowerUp = [1, 2, 8, 1, 4, 1, 5, 6, 7, 8, 1]
SecretList = [5, 15, 30, 40, 45, 60, 72, 81, 99, 115]




def main():
    hello = True
    hello2 = True
    global HighScore
    begin = beginscreen()
    if begin:
        while hello:
            pygame.mixer.music.load("backgroundmusic.mp3")
            pygame.mixer.music.play(-1)
            if run() == False:
                pygame.mixer.music.stop()
                if Score > HighScore:
                    HighScore = Score
                end = endscreen()
                if end == False:
                    hello = False
                    pyquit()
    if not begin:
        while hello2:
            pygame.mixer.music.load("backgroundmusic.mp3")
            pygame.mixer.music.play(-1)
            if run2() == False:
                pygame.mixer.music.stop()
                if Score1 == Score2:
                    tie()
                elif Score1 > Score2:
                    gameover()
                elif Score1 < Score2:
                    gameover2()
        

                     
def run():
    global Score
    Score = 0
    myRect = pygame.Rect(20, 380, 20, 20)
    Color = Green
    BackGround = Black
    myRect_location = [20,20]
    xspeed = 20
    yspeed = 20
    RSpeed = [xspeed,0]
    applenumber = False
    running = True
    pause = 15
    NumberOfRects = 0
    Rects = []
    final = 0
    lightningposition = 0
    WallNumber = 0
    WallPosition = []
    WallList = []
    WidthList = [1,2]
    LLposition = (1000,1000)
    Light = False
    randomT = True
    myTrap = False
    locT = True
    Uses = 0
    li = 0
    while running:
        getmovement(RSpeed, xspeed, yspeed)
        myRect = myRect.move(RSpeed)
        pygame.display.flip()
        screen.fill(BackGround)
        drawcords()
        pygame.draw.rect(screen, Color, myRect)
        Clock.tick(pause)
        pygame.display.flip()
        while len(Rects)>NumberOfRects:
            Rects=Rects[1:]
        if NumberOfRects!=0:
            Rects.append(myRect)
        printrects = NumberOfRects
        final = len(Rects)-1
        if NumberOfRects!=0:
            while printrects!=-1:
                pygame.draw.rect(screen, Color, Rects[final])
                final-=1
                printrects-=1
        if NumberOfRects == Walls[WallNumber]:
            a = random.randint(1,2)
            WallPosition.append([randomlocation(myRect, Rects, WallList), a])
            WallNumber += 1
        WallSpot = 0
        if NumberOfRects >= Walls[0]:
            while WallSpot <= len(WallPosition)-1:
                if WallPosition[WallSpot][1] == 1:
                    x = 20
                    y = 60
                elif WallPosition[WallSpot][1] == 2:
                    x = 60
                    y = 20
                wall = pygame.Rect(WallPosition[WallSpot][0][0], WallPosition[WallSpot][0][1], x, y)
                WallList.append(wall)
                pygame.draw.rect(screen, Orange, wall)
                WallSpot += 1
        WallSpot = 0
        while WallSpot <= len(WallList)-1:
            if myRect.colliderect(WallList[WallSpot]):
                running = False
            WallSpot += 1
        if Light == False:
            if NumberOfRects == LenOfSnakeList[lightningposition]:
                LLposition = randomlocation(myRect, Rects, WallList)
                lightningposition += 1
                Light = True
        if Light:
            if randomT:
                myrandom = random.randint(0, len(PowerUp)-1)
                randomT = False
            if PowerUp[myrandom] == 1:
                image = 1
                screen.blit(lightning, (LLposition[0]+5, LLposition[1]+3))
            if PowerUp[myrandom] == 2:
                image = 2
                screen.blit(xlogo, (LLposition[0], LLposition[1]))
            if PowerUp[myrandom] == 4:
                image = 4
                screen.blit(reverse, (LLposition[0]+5, LLposition[1]))
            if PowerUp[myrandom] == 5:
                image = 5
                screen.blit(BlueDot, (LLposition[0], LLposition[1]))
            if PowerUp[myrandom] == 6:
                image = 6
                screen.blit(GreenDot, (LLposition[0], LLposition[1]))
            if PowerUp[myrandom] == 7:
                image = 7
                screen.blit(YellowDot, (LLposition[0], LLposition[1]))
            if PowerUp[myrandom] == 8:
                image = 8
                screen.blit(WhiteDot, (LLposition[0], LLposition[1]))
        pygame.display.flip()
        if RSpeed[0] == xspeed:
            myRect_location[0] += xspeed
        elif RSpeed[0] == -xspeed:
            myRect_location[0] -= xspeed
        elif RSpeed[1] == yspeed:
            myRect_location[1] += yspeed
        elif RSpeed[1] == -yspeed:
            myRect_location[1] -= yspeed
        if applenumber==False:
            applelocation = randomlocation(myRect, Rects, WallList)
            applenumber = True
        screen.blit(apple, applelocation)
        if collide(myRect, applelocation):
            pickupsound = pygame.mixer.Sound("pickup.wav")
            pygame.mixer.Sound.play(pickupsound)
            applenumber = False
            NumberOfRects+=1
            Score+=1
        if collide(myRect, LLposition):    #Power-Up Collide
            Light = False
            randomT = True
            if image == 1:
                pause += 5
            if image == 2:
                clearwalls(WallPosition, WallList, WallNumber)
                pause = 15
                xspeed = 20
                yspeed = 20
                BackGround = Black
                Color = Green
            if image == 4:
                yspeed = -yspeed
                xspeed = -xspeed
            if image == 5:
                Color = Blue
            if image == 6:
                Color = Green
            if image == 7:
                Color = Yellow
            if image == 8:
                if BackGround == Black:
                    BackGround = White
                    Color = Black
                else:
                    BackGround = Black
                    Color = White
        if myRect.right>width or myRect.left<0:
            running = False
        elif myRect.top<0 or myRect.bottom>height:
            running = False
        elif snakecollide(myRect, Rects):
            running = False
        if NumberOfRects == SecretList[li]:
            myTrap = True
            if locT == True:
                loc = randomlocation(myRect, Rects, WallList)
                locT = False
        if myTrap == True:
            screen.blit(Trap, [loc[0]+3, loc[1]])
            if myRect.collidepoint(loc[0], loc[1]):
                Uses += 1
                extraloc = randomlocation(myRect, Rects, WallList)
                myRect.x = extraloc[0]
                myRect.y = extraloc[1]
                if Uses == 3:
                    li += 1
                    locT = True
                    myTrap = False
        pygame.display.flip()
    return False

def run2():
    global Score1
    Score1 = 0
    global Score2
    Score2 = 0
    BackGround = Black
    Color = Green
    Color2 = Yellow
    pause = 15
    myRect = pygame.Rect(20, 400, 20, 20)
    myRect2 = pygame.Rect(20, 40, 20, 20)
    xspeed = 20
    yspeed = 20
    xspeed2 = 20
    yspeed2 = 20
    RSpeed = [xspeed, 0]
    RSpeed2 = [xspeed2, 0]
    running = True
    applenumber = False
    Light = False
    randomT = True
    NumberOfRects = 0
    NumberOfRects2 = 0
    Rects = []
    Rects2 = []
    WallList = []
    WidthList = [1,2]
    WallPosition = []
    WallNumber = 0
    lightningposition = 0
    LLposition = (2000,2000)
    Uses = 0
    li = 0
    myTrap = False
    locT = True
    while running:
        move = getmovement2(RSpeed, xspeed, yspeed, RSpeed2, xspeed2, yspeed2)
        myRect = myRect.move(move[0])
        myRect2 = myRect2.move(move[1])
        screen.fill(BackGround)
        drawcords()
        pygame.draw.rect(screen, Color, myRect)
        pygame.draw.rect(screen, Color2, myRect2)
        Clock.tick(pause)
        pygame.display.flip()
        

        while len(Rects) > NumberOfRects:
            Rects = Rects[1:]
        while len(Rects2) > NumberOfRects2:
            Rects2 = Rects2[1:]   
        if NumberOfRects != 0:
            Rects.append(myRect)
        if NumberOfRects2 != 0:
            Rects2.append(myRect2)  
        printrects = NumberOfRects
        printrects2 = NumberOfRects2
        final = len(Rects)-1
        final2 = len(Rects2)-1
        if NumberOfRects != 0:
            while printrects != -1:
                pygame.draw.rect(screen, Color, Rects[final])
                final -= 1
                printrects -= 1
        if NumberOfRects2 != 0:
            while printrects2 != -1:
                pygame.draw.rect(screen, Color2, Rects2[final2])
                final2 -= 1
                printrects2 -= 1
        if not applenumber:
            applelocation = randomlocation2(myRect, myRect2)
            applenumber = True    
        if applenumber:
            screen.blit(apple, applelocation)
            pygame.display.flip()
        if collide(myRect, applelocation):
            pickupsound = pygame.mixer.Sound("pickup.wav")
            pygame.mixer.Sound.play(pickupsound)
            applelocation = [1000,1000]
            applenumber = False
            NumberOfRects += 1
        if collide(myRect2, applelocation):
            pickupsound = pygame.mixer.Sound("pickup.wav")
            pygame.mixer.Sound.play(pickupsound)
            applelocation = [1000,1000]
            applenumber = False
            NumberOfRects2 += 1
            

        if NumberOfRects == Walls[WallNumber] or NumberOfRects2 == Walls[WallNumber]:
            a = random.randint(1,2)
            WallPosition.append([randomlocation2(myRect, myRect2), a])
            WallNumber += 1
        WallSpot = 0
        if NumberOfRects >= Walls[0]:
            while WallSpot <= len(WallPosition)-1:
                if WallPosition[WallSpot][1] == 1:
                    x = 20
                    y = 60
                elif WallPosition[WallSpot][1] == 2:
                    x = 60
                    y = 20
                wall = pygame.Rect(WallPosition[WallSpot][0][0], WallPosition[WallSpot][0][1], x, y)
                WallList.append(wall)
                pygame.draw.rect(screen, Orange, wall)
                WallSpot += 1   
        WallSpot = 0
        while WallSpot <= len(WallList)-1:
            if myRect.colliderect(WallList[WallSpot]) or myRect2.colliderect(WallList[WallSpot]):
                running = False
            WallSpot += 1



        if Light == False:
            if NumberOfRects == LenOfSnakeList[lightningposition] or NumberOfRects2 == LenOfSnakeList[lightningposition]:
                LLposition = randomlocation2(myRect, myRect2)
                lightningposition += 1
                Light = True
        if Light:
            if randomT:
                myrandom = random.randint(0, len(PowerUp)-1)
                randomT = False
            if PowerUp[myrandom] == 1:
                image = 1
                screen.blit(lightning, (LLposition[0]+5, LLposition[1]+3))
            if PowerUp[myrandom] == 2:
                image = 2
                screen.blit(xlogo, (LLposition[0], LLposition[1]))
            if PowerUp[myrandom] == 4:
                image = 4
                screen.blit(reverse, (LLposition[0]+5, LLposition[1]))
            if PowerUp[myrandom] == 5:
                image = 5
                screen.blit(BlueDot, (LLposition[0], LLposition[1]))
            if PowerUp[myrandom] == 6:
                image = 6
                screen.blit(GreenDot, (LLposition[0], LLposition[1]))
            if PowerUp[myrandom] == 7:
                image = 7
                screen.blit(YellowDot, (LLposition[0], LLposition[1]))
            if PowerUp[myrandom] == 8:
                image = 8
                screen.blit(WhiteDot, (LLposition[0], LLposition[1]))
        if collide(myRect, LLposition):
            LLposition = (2000,2000)
            Light = False
            randomT = True
            if image == 1:
                pause += 5
            if image == 2:
                clearwalls(WallPosition, WallList, WallNumber)
                pause = 15
                xspeed = 20
                yspeed = 20
                xspeed2 = 20
                yspeed2 = 20
                BackGround = Black
                Color = Green
                Color2 = Yellow
            if image == 4:
                yspeed = -yspeed
                xspeed = -xspeed
            if image == 5:
                Color = Blue
            if image == 6:
                Color = Green
            if image == 7:
                Color = Yellow
            if image == 8:
                if BackGround == Black:
                    BackGround = White
                    Color = Black
                    Color2 = Black
                else:
                    BackGround = Black
                    Color = White
                    Color2 = White
        if collide(myRect2, LLposition):
            LLposition = (2000,2000)
            Light = False
            randomT = True
            if image == 1:
                pause += 5
            if image == 2:
                clearwalls(WallPosition, WallList, WallNumber)
                pause = 15
                xspeed = 20
                yspeed = 20
                xspeed2 = 20
                yspeed2 = 20
                BackGround = Black
                Color = Green
                Color2 = Yellow
            if image == 4:
                yspeed2 = -yspeed2
                xspeed2 = -xspeed2
            if image == 5:
                Color2 = Blue
            if image == 6:
                Color2 = Green
            if image == 7:
                Color2 = Yellow
            if image == 8:
                if BackGround == Black:
                    BackGround = White
                    Color = Black
                    Color2 = Black
                else:
                    BackGround = Black
                    Color = White
                    Color2 = White


        if NumberOfRects == SecretList[li] or NumberOfRects2 == SecretList[li]:
            myTrap = True
            if locT == True:
                loc = randomlocation2(myRect, myRect2)
                locT = False
        if myTrap == True:
            screen.blit(Trap, [loc[0]+3, loc[1]])
            if myRect.collidepoint(loc[0], loc[1]):
                Uses += 1
                extraloc = randomlocation2(myRect, myRect2)
                myRect.x = extraloc[0]
                myRect.y = extraloc[1]
                if Uses == 3:
                    li += 1
                    locT = True
                    myTrap = False
            elif myRect2.collidepoint(loc[0], loc[1]):
                Uses += 1
                extraloc = randomlocation2(myRect, myRect2)
                myRect2.x = extraloc[0]
                myRect2.y = extraloc[1]
                if Uses == 3:
                    li += 1
                    locT = True
                    myTrap = False

            
        if myRect.right > width or myRect.left < 0 or myRect.top < 0 or myRect.bottom > height:
            Score1 = 0
            Score2 = 1
            running = False
        if myRect2.right > width or myRect2.left < 0 or myRect2.top < 0 or myRect2.bottom > height:
            Score1 = 1
            Score2 = 0
            running = False
        if myRect.colliderect(myRect2):
            Score1 = 0
            Score2 = 0
            running = False
        if snakecollide(myRect, Rects2):
            Score1 = 0
            Score2 = 1
            running = False
        if snakecollide(myRect2, Rects):
            Score1 = 1
            Score2 = 0
            running = False
        if snakecollide(myRect, Rects):
            Score1 = 0
            Score2 = 1
            running = False
        if snakecollide(myRect2, Rects2):
            Score1 = 1
            Score2 = 0
            running = False
            
        pygame.display.flip()
    return False 

def getmovement2(RSpeed, xspeed, yspeed, RSpeed2, xspeed2, yspeed2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pyquit()
            running = False
        if event.type == pygame.KEYDOWN:
            if RSpeed[0] == xspeed:
                if event.key == pygame.K_DOWN:
                    RSpeed[0] = 0
                    RSpeed[1] = yspeed
                elif event.key == pygame.K_UP:
                    RSpeed[0] = 0
                    RSpeed[1] = -yspeed
                elif event.key == pygame.K_RIGHT:
                    RSpeed[0] = xspeed
                    RSpeed[1] = 0
            if RSpeed[0] == -xspeed:
                if event.key == pygame.K_DOWN:
                    RSpeed[0] = 0
                    RSpeed[1] = yspeed
                elif event.key == pygame.K_UP:
                    RSpeed[0] = 0
                    RSpeed[1] = -yspeed
                elif event.key == pygame.K_LEFT:
                    RSpeed[0] = -xspeed
                    RSpeed[1] = 0
            if RSpeed[1] == yspeed:
                if event.key == pygame.K_DOWN:
                    RSpeed[0] = 0
                    RSpeed[1] = yspeed
                elif event.key == pygame.K_RIGHT:
                    RSpeed[0] = xspeed
                    RSpeed[1] = 0
                elif event.key == pygame.K_LEFT:
                    RSpeed[0] = -xspeed
                    RSpeed[1] = 0
            if RSpeed[1] == -yspeed:
                if event.key == pygame.K_UP:
                    RSpeed[0] = 0
                    RSpeed[1] = -yspeed
                elif event.key == pygame.K_RIGHT:
                    RSpeed[0] = xspeed
                    RSpeed[1] = 0
                elif event.key == pygame.K_LEFT:
                    RSpeed[0] = -xspeed
                    RSpeed[1] = 0
            if RSpeed2[0] == xspeed2:
                if event.key == pygame.K_s:
                    RSpeed2[0] = 0
                    RSpeed2[1] = yspeed2
                elif event.key == pygame.K_w:
                    RSpeed2[0] = 0
                    RSpeed2[1] = -yspeed2
                elif event.key == pygame.K_d:
                    RSpeed2[0] = xspeed2
                    RSpeed2[1] = 0
            if RSpeed2[0] == -xspeed2:
                if event.key == pygame.K_s:
                    RSpeed2[0] = 0
                    RSpeed2[1] = yspeed2
                elif event.key == pygame.K_w:
                    RSpeed2[0] = 0
                    RSpeed2[1] = -yspeed2
                elif event.key == pygame.K_a:
                    RSpeed2[0] = -xspeed2
                    RSpeed2[1] = 0
            if RSpeed2[1] == yspeed2:
                if event.key == pygame.K_s:
                    RSpeed2[0] = 0
                    RSpeed2[1] = yspeed2
                elif event.key == pygame.K_d:
                    RSpeed2[0] = xspeed2
                    RSpeed2[1] = 0
                elif event.key == pygame.K_a:
                    RSpeed2[0] = -xspeed2
                    RSpeed2[1] = 0
            if RSpeed2[1] == -yspeed2:
                if event.key == pygame.K_w:
                    RSpeed2[0] = 0
                    RSpeed2[1] = -yspeed2
                elif event.key == pygame.K_d:
                    RSpeed2[0] = xspeed2
                    RSpeed2[1] = 0
                elif event.key == pygame.K_a:
                    RSpeed2[0] = -xspeed2
                    RSpeed2[1] = 0    
    return [RSpeed, RSpeed2]

def getmovement(RSpeed, xspeed, yspeed):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pyquit()
            running = False
        if event.type == pygame.KEYDOWN:
            if RSpeed[0] == xspeed:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    RSpeed[0] = 0
                    RSpeed[1] = yspeed
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    RSpeed[0] = 0
                    RSpeed[1] = -yspeed
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    RSpeed[0] = xspeed
                    RSpeed[1] = 0
                break
            if RSpeed[0] == -xspeed:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    RSpeed[0] = 0
                    RSpeed[1] = yspeed
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    RSpeed[0] = 0
                    RSpeed[1] = -yspeed
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    RSpeed[0] = -xspeed
                    RSpeed[1] = 0
                break
            if RSpeed[1] == yspeed:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    RSpeed[0] = 0
                    RSpeed[1] = yspeed
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    RSpeed[0] = xspeed
                    RSpeed[1] = 0
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    RSpeed[0] = -xspeed
                    RSpeed[1] = 0
                break
            if RSpeed[1] == -yspeed:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    RSpeed[0] = 0
                    RSpeed[1] = -yspeed
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    RSpeed[0] = xspeed
                    RSpeed[1] = 0
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    RSpeed[0] = -xspeed
                    RSpeed[1] = 0
                break
    return RSpeed

def tie():
    diesound = pygame.mixer.Sound("Death.wav")
    pygame.mixer.Sound.play(diesound)
    screen.blit(Tie, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pyquit()
            if event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.stop(diesound)
                if event.key == pygame.K_h:
                    done = False
                    main()
                if event.key == pygame.K_RETURN:
                    done = False
                    return True
    
def gameover():
    diesound = pygame.mixer.Sound("Death.wav")
    pygame.mixer.Sound.play(diesound)
    screen.blit(GreenWins, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pyquit()
            if event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.stop(diesound)
                if event.key == pygame.K_h:
                    done = False
                    main()
                if event.key == pygame.K_RETURN:
                    done = False
                    return True

def gameover2():
    diesound = pygame.mixer.Sound("Death.wav")
    pygame.mixer.Sound.play(diesound)
    screen.blit(YellowWins, [0,0])
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                pyquit()
            if event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.stop(diesound)
                if event.key == pygame.K_h:
                    main()
                if event.key == pygame.K_RETURN:
                    done = False
                    return True
    

def clearwalls(WallPosition, WallList, WallNumber):
    WallPosition.clear()
    WallList.clear()
    WallNumber = 0
    
def drawcords():
    for x in range(0, width, 20):
        pygame.draw.line(screen, DarkGrey, [x,0], [x, height])
    for y in range(0, height, 20):
        pygame.draw.line(screen, DarkGrey, [0,y], [width, y])

def collide(myRect, applelocation):
    if myRect.collidepoint(applelocation[0], applelocation[1]):
        return True
    else:
        return False

def snakecollide(myRect, Rects):
    a = 0
    while a < (len(Rects)-1):
        if myRect.colliderect(Rects[a]):
            return True
        else:
            a+=1   

def randomlocation2(myRect, myRect2):
    xlocation = random.randint(0, len(applelist)-1)
    ylocation = random.randint(0, 23)
    if myRect.collidepoint(xlocation, ylocation):
        randomlocation(myRect, myRect2)
    if myRect2.collidepoint(xlocation, ylocation):
        randomlocation(myRect, myRect2)
        
    return [applelist[xlocation], applelist[ylocation]]

def randomlocation(myRect, Rects, WallList):
    xlocation = random.randint(0, len(applelist)-1)
    ylocation = random.randint(0, 23)
    a = 0
    b = 0
    if myRect.collidepoint(xlocation, ylocation):
        randomlocation(myRect, Rects, WallList)
    while a < (len(Rects)-1):
        if Rects[a].collidepoint(xlocation, ylocation):
            randomlocation(myRect, Rects, WallList)
            break
        else:
            a += 1
    while b < len(WallList)-1:
        if WallList[b].collidepoint(xlocation, ylocation):
            randomlocation(myRect, Rects, WallList)
        else:
            b += 1
    return [applelist[xlocation], applelist[ylocation]]

def beginscreen():
    pygame.mixer.music.load("startscreenmusic.mid")
    pygame.mixer.music.play(-1)
    text = Font.render("Press 1 For One Player   or   Press 2 For Two Players", True, White)
    text1 = Font.render("Press R for Rules", True, White)
    screen.blit(startscreen, [0,-100])
    screen.blit(text, [0, 400])
    screen.blit(text1, [210, 435])
    screen.blit(apple, [319, 369])
    pygame.display.flip()
    Done = False
    while not Done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Done = True
                pyquit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    rule = rules()
                    if rule:
                        return True
                    if not rule:
                        return False
                elif event.key == pygame.K_1:
                    return True
                elif event.key == pygame.K_2:
                    return False
    
def endscreen():
    global HighScore
    fout = open("highscore.txt", 'w')
    fout.write(str(HighScore))
    fout.close()
    diesound = pygame.mixer.Sound("Death.wav")
    pygame.mixer.Sound.play(diesound)
    text = Font.render("Press Enter for New Game!", True, White)
    text1 = Font.render("Score:", True, White)
    text2 = Font.render("HighScore:", True, White)
    text3 = Font.render(str(Score), True, White)
    text4 = Font.render(str(HighScore), True, White)
    text5 = Font.render("Press H For Home Screen", True, White)
    screen.blit(finalscreen, [-110,-20])
    screen.blit(text, [20,420])
    screen.blit(text1, [430,15])
    screen.blit(text3, [535, 17])
    screen.blit(text2, [430, 50])
    screen.blit(text4, [590, 52])
    screen.blit(text5, [30, 450])
    pygame.display.flip()
    Done = False
    while not Done:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                Done = True
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.Sound.stop(diesound)
                    Done = True
                    return True
                if event.key == pygame.K_h:
                    Done = True
                    main()
def rules():
    done = False
    slash = Font.render(" / ", True, White)
    text = Font.render("W / Up : Snake Moves Up", True, White)
    text1 = Font.render("A / Left : Snake Moves Left", True, White)
    text2 = Font.render("S / Down : Snake Moves Down", True, White)
    text3 = Font.render("D / Right : Snake Moves Right", True, White)
    text4 = Font.render(": Snake Speeds Up", True, White)
    text5 = Font.render(": Clears All Power-Ups and Walls", True, White)
    text6 = Font.render(": Reverse All Keys", True, White)
    text7 = Font.render(": Changes Color of Snake", True, White)
    text8 = Font.render(": Inverts Colors", True, White)
    text9 = Font.render("Press 1 For One Player   or   Press 2 For Two Players", True, White)
    text10 = Font.render("Press B To Go Back", True, White)
    text11 = Font.render(": Don't Hit These Walls", True, White)
    screen.fill(Black)
    screen.blit(text, [0,0])
    screen.blit(text1, [0, 30])
    screen.blit(text2, [0, 60])
    screen.blit(text3, [0, 90])
    screen.blit(lightning, [3, 125])
    screen.blit(text4, [20, 120])
    screen.blit(xlogo, [0, 152])
    screen.blit(text5, [30, 150])
    screen.blit(reverse, [3, 182])
    screen.blit(text6, [30, 180])
    screen.blit(BlueDot, [0, 212])
    screen.blit(slash, [20, 210])
    screen.blit(GreenDot, [40, 212])
    screen.blit(slash, [60, 210])
    screen.blit(YellowDot, [80, 212])
    screen.blit(text7, [110, 210])
    screen.blit(WhiteDot, [0, 242])
    screen.blit(text8, [20, 241])
    screen.blit(text9, [0, 435])
    screen.blit(text10, [200, 380])
    pygame.draw.rect(screen, Orange, (1, 271, 20, 20))
    screen.blit(text11, [25, 270])
    pygame.display.flip()
    while not  done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pyquit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    done = True
                    beginscreen()
                    return True
                if event.key == pygame.K_1:
                    done = True
                    return True
                if event.key == pygame.K_2:
                    done = True
                    return False
                    
def pyquit():
    pygame.quit()    

if __name__ == '__main__':
    main()
