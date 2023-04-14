from tkinter import *
from tkinter.messagebox import *
import random


root=Tk('jigsaw puzzle')
root.title("puzzle")
# load external image
Pics=[]
for i in range(9):
    filename='t_picture\\cute_'+str(i+1)+'.png'
    Pics.append(PhotoImage(file=filename))
# define constants
# The size of the canvas
WIDTH=1500
HEIGHT=810
# The side length of the image block
IMAGE_WIDTH=WIDTH//3
IMAGE_HEIGHT=HEIGHT//3

# Number of rows and columns of the board
ROWS=3
COLS=3
# number of moving steps
steps=0
# save a list of all image blocks
board= [[0,1,2],
        [3,4,5],
        [6,7,8]]
#ImageBlock class
class Square:
    def __init__(self,orderID):
        self.orderID=orderID
    def draw(self,canvas,board_pos):
        img=Pics[self.orderID]
        canvas.create_image(board_pos,image=img)
# Initialize the puzzle
def init_board():
    # Scramble image block coordinates
    L=list(range(8))
    L.append(None)
    random.shuffle(L)
    # Fill the puzzle board
    for i in range(ROWS):
        for j in range(COLS):
            idx=i*ROWS+j
            orderID=L[idx]
            if orderID is None:
                board[i][j]=None
            else:
                board[i][j]=Square(orderID)
# reset game
def play_game():
    global steps
    steps=0
    init_board()

# Draw the elements of the game interface
def drawBoard(canvas):
    # draw black frame
    canvas.create_polygon((0,0,WIDTH,0,WIDTH,HEIGHT,0,HEIGHT),width=1,outline='Black',fill='white')
    # draw image blocks
    
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None:
                board[i][j].draw(canvas,(IMAGE_WIDTH*(j+0.5),IMAGE_HEIGHT*(i+0.5)))
def mouseclick(pos):
    global  steps
    # Convert the click position to coordinates on the puzzle board
    r=int(pos.y//IMAGE_HEIGHT)
    c=int(pos.x//IMAGE_WIDTH)
    print(r,c)
    if r<3 and c<3:
        if board[r][c] is None:
            return
        else:
            current_square=board[r][c]
            if r-1>=0 and board[r-1][c] is None:
                board[r][c]=None
                board[r-1][c]=current_square
                steps+=1
            elif c+1<=2 and board[r][c+1] is None:
                board[r][c] = None
                board[r][c+1] = current_square
                steps += 1
            elif r+1<=2 and board[r+1][c] is None:
                board[r][c] = None
                board[r+1][c] = current_square
                steps += 1
            elif c-1>=0 and board[r][c-1] is None:
                board[r][c] = None
                board[r][c-1] = current_square
                steps += 1
            #print(board)
            label1["text"]=str(steps)
            cv.delete('all')
            drawBoard(cv)
    if win():
        showinfo(title="Congratulations",message="You succeeded!")

def win():
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None and  board[i][j].orderID!=i*ROWS+j:
                return False
    return  True

def callBack2():
    print("restart")
    play_game()
    cv.delete('all')
    drawBoard(cv)

# set window
cv=Canvas(root,bg='white',width=WIDTH,height=HEIGHT)
b1=Button(root,text="restart",command=callBack2,width=20)
label1=Label(root,text="0",fg="red",width=20)
label1.pack()
cv.bind("<Button-1>",mouseclick)

cv.pack()
b1.pack()
play_game()
drawBoard(cv)
root.mainloop()