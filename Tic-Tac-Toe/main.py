import pygame

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

def showBoard (screen, board):
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
    global grid,winner
    
    for row in range(3):
        if (grid[row][0]==grid[row][1]==grid[row][2]) and (grid[row][0] is not None):
            winner=grid[row][0]
            pygame.draw.line(board,(255,0,0), (10,(row*screen_height/3)+screen_height/6),(screen_width-10,(row*screen_height/3)+screen_height/6),5)
            break
    for col in range(3):
        if (grid[0][col]==grid[1][col]==grid[2][col]) and (grid[0][col] is not None):
            winner=grid[0][col]
            pygame.draw.line(board,(255,0,0), ((col*screen_width/3)+screen_width/6,10),((col*screen_width/3)+screen_width/6,screen_height-10),5)
            break
    if (grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] is not None):
        # game won diagonally left to right
        winner = grid[0][0]
        pygame.draw.line (board, (250,0,0), (10, 10), (screen_width-10,screen_height-10), 5)

    if (grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] is not None):
        # game won diagonally right to left
        winner = grid[0][2]
        pygame.draw.line (board, (250,0,0), (screen_width-10, 10), (10, screen_height-10), 5)

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

