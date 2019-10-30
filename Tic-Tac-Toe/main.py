import pygame
from pygame.locals import *

pygame.init()

screen_width=600
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Tic-Tac-Toe")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

grid=[[None,None,None],[None,None,None],[None,None,None]]
symbol='X'
winner=None


def intro():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                introduction=False

        screen.fill((255,208,23))
        background=pygame.image.load('background.jpeg')
        background=pygame.transform.scale(background,(screen_width,screen_height))
        screen.blit(background,(0,0))

        click=pygame.mouse.get_pressed()
        mouse=pygame.mouse.get_pos()

        text=pygame.font.Font('freesansbold.ttf',45)

        intro_text=text.render('JEU DE MORPION',True,(120,32,42))
        screen.blit(intro_text,(int(screen_height/6),screen_width/3))
        
        if(screen_width/6 < mouse[0] < screen_width/6+int(screen_width/7) and 2*screen_height/3 < mouse[1] < 2*screen_height/3+screen_height/12):
            pygame.draw.rect(screen, (0,255,0),(screen_width/6,2*screen_height/3,int(screen_width/7),screen_height/12))
            if(click[0]==1):
                winner=None
                gameloop()
        else:
            pygame.draw.rect(screen, (0,200,0),(screen_width/6,2*screen_height/3,int(screen_width/7),screen_height/12))
        
        if(screen_width-screen_width/6-int(screen_width/7) < mouse[0] < screen_width-screen_width/6 and 2*screen_height/3<mouse[1] < 2*screen_height/3+screen_height/12):
            pygame.draw.rect(screen, (255,0,0),(screen_width-screen_width/6-int(screen_width/7),2*screen_height/3,int(screen_width/7),screen_height/12))
            if(click[0]==1):
                introduction=False
                break
        else:
            pygame.draw.rect(screen, (200,0,0),(screen_width-screen_width/6-int(screen_width/7),2*screen_height/3,int(screen_width/7),screen_height/12))
        
        if(screen_width/2-int(screen_width/10)-10 < mouse[0] < screen_width/2+int(screen_width/10)+10 and 4*screen_height/5 < mouse[1] < 4*screen_height/5+screen_height/16):
            pygame.draw.rect(screen, (245,176,65),(screen_width/2-int(screen_width/10)-10,4*screen_width/5,int(screen_width/5)+20,screen_height/16))
            if(click[0]==1):
                instructions()
        else:
            pygame.draw.rect(screen, (200,176,65),(screen_width/2-int(screen_width/10)-10,4*screen_width/5,int(screen_width/5)+20,screen_height/16))
        
        text1=pygame.font.Font('freesansbold.ttf',15)
        start=text1.render('Let\'s GO!',True,(0,0,0))
        screen.blit(start,(9*screen_width/50,7*screen_height/10))

        stop=text1.render('QUIT',True,(0,0,0))
        screen.blit(stop,(screen_width-screen_width/8-int(screen_width/7),7*screen_height/10))

        instruc=text1.render('INSTRUCTIONS',True,(0,0,0))
        screen.blit(instruc,(screen_width/2-int(screen_width/10),0.82*screen_height))

        pygame.display.update()

def instructions():
    instruct=True
    while instruct:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                instruct=False

        click=pygame.mouse.get_pressed()
        mouse=pygame.mouse.get_pos()
        screen.fill((255,255,255))
        background=pygame.image.load('instructions.jpeg')
        background=pygame.transform.scale(background,(screen_width,screen_height))
        screen.blit(background,(0,0))

        multi_text=['The object of Tic Tac Toe is to get three in a row.',
                    'You play on a three by three game board.',
                    'The first player is known as X and the second is O.',
                    'Players alternate placing Xs and Os on the game board ',
                    'until either oppent has three in a row or all nine squares',
                    'are filled. X always goes first, and in the event that no',
                    'one has three in a row, the stalemate is called a CAT GAME']

        text=pygame.font.Font('freesansbold.ttf',20)

        for i in range(7):
            intro_text=text.render(multi_text[i],True,(66,33,0))
            screen.blit(intro_text,(15,30+i*30))

        if(8*screen_width/20<mouse[0]<8*screen_width/20+int(screen_width/7) and 2*screen_height/3<mouse[1]<2*screen_height/3+screen_height/12):
            pygame.draw.rect(screen, (255,0,0),(8*screen_width/20,2*screen_height/3,int(screen_width/7),screen_height/12))
            if(click[0]==1):
                instruct=False
                break
        else:
             pygame.draw.rect(screen, (200,0,0),(8*screen_width/20,2*screen_height/3,int(screen_width/7),screen_height/12))        

        text1=pygame.font.Font('freesansbold.ttf',15)
        back=text1.render('Back',True,(0,0,0))
        screen.blit(back,(44*screen_width/100,7*screen_height/10))
        pygame.display.update()
   


def gameloop(): 
    symbol='X'
    winner=None
    message=None
    def initboard(screen):
        background=pygame.Surface(screen.get_size())
        background=background.convert()
        background=pygame.image.load('background.jpeg')
        background=pygame.transform.scale(background,(screen_width,screen_height))


        pygame.draw.line (background, (0,0,0), (screen_width/3, 0), (screen_width/3, screen_height), 3)
        pygame.draw.line (background, (0,0,0), (2*screen_width/3, 0), (2*screen_width/3, screen_height), 3)

        pygame.draw.line (background, (0,0,0), (0, screen_height/3), (screen_width, screen_height/3), 3)
        pygame.draw.line (background, (0,0,0), (0, 2*screen_height/3), (screen_width, 2*screen_height/3), 3)

        return background

    def showstatus(board):
        global symbol,winner
        if (winner==None):
            if(symbol=='X'):
                message = "Player1's turn"
            else:
                message = "Player2's turn"
        else:
            if(winner=='X'):
                message = "Player1 won!!"
            else:
                message = "Player2 won!!"
            
        font=pygame.font.Font('freesansbold.ttf',15)
        status=font.render(message,True,(0,0,0))
        screen.blit(status,(10,screen_height-20))
        pygame.display.update()
    

    def showBoard (screen, board):
        showstatus(board)
        screen.blit (board, (0, 0))
        pygame.display.flip()

    def mousepos(mouseX,mouseY):
        if mouseY<screen_height/3:
            row=0
        elif mouseY<2*screen_height/3:
            row=1
        elif mouseY<screen_height:
            row=2
    
        if (mouseX < screen_width/3):
            col = 0
        elif (mouseX < 2*screen_width/3):
            col = 1
        else:
            col = 2

        return (row,col)

    def drawsymbol(board,row,column,symbol):
        x=int((column*screen_width/3)+screen_width/6)
        y=int((row*screen_height/3)+screen_width/6)

        if symbol=='O':
            pygame.draw.circle(board,(99,66,33),(x,y),int(screen_width/12),3)
        else:
            pygame.draw.line(board,(0,66,0),(x-screen_width/12,y-screen_width/12),(x+screen_width/12,y+screen_width/12),4)
            pygame.draw.line(board,(0,66,0),(x+screen_width/12,y-screen_width/12),(x-screen_width/12,y+screen_width/12),4)
        grid[row][column]=symbol

    def click(board):
        global symbol,grid
        (mouseX,mouseY)=pygame.mouse.get_pos()
        (row,col)=mousepos(mouseX,mouseY)

        if ((grid[row][col]=='X') or (grid[row][col]=='O')):
            return 
        drawsymbol(board,row,col,symbol)

        if symbol=='X':
            symbol='O'
        else:
            symbol='X'

    def gameWinner(board):
        global grid,winner,symbol
        for row in range(3):
            if (grid[row][0]==grid[row][1]==grid[row][2]) and (grid[row][0] is not None):
                winner=grid[row][0]
                pygame.draw.line(board,(200,0,0), (10,(row*screen_height/3)+screen_height/6),(screen_width-10,(row*screen_height/3)+screen_height/6),5)
                grid=[[None,None,None],[None,None,None],[None,None,None]]
                symbol='X'
                break
        for col in range(3):
            if (grid[0][col]==grid[1][col]==grid[2][col]) and (grid[0][col] is not None):
                winner=grid[0][col]
                pygame.draw.line(board,(200,0,0), ((col*screen_width/3)+screen_width/6,10),((col*screen_width/3)+screen_width/6,screen_height-10),5)
                grid=[[None,None,None],[None,None,None],[None,None,None]]
                symbol='X'
                break
        if (grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] is not None):
        # game won diagonally left to right
            winner = grid[0][0]
            pygame.draw.line (board, (200,0,0), (10, 10), (screen_width-10,screen_height-10), 5)
            symbol='X'
            grid=[[None,None,None],[None,None,None],[None,None,None]]
        if (grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] is not None):
        # game won diagonally right to left
            winner = grid[0][2]
            pygame.draw.line (board, (200,0,0), (screen_width-10, 10), (10, screen_height-10), 5)
            symbol='X'
            grid=[[None,None,None],[None,None,None],[None,None,None]]

    board=initboard(screen)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                
            elif event.type==pygame.MOUSEBUTTONDOWN:
                click(board)
    
            gameWinner(board)

            showBoard(screen,board) 

intro()
