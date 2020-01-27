import tkinter

round = 1

def next_round():
    global round
    round += 1
    if round%2==0:
        X_label['text']="X"
        Y_label['text']="O is playing"
    else:
        X_label['text']="X is playing"
        Y_label['text']="O"

def restart():
    global round
    round = 1
    X_label['text'] = "X is playing"
    Y_label['text'] = "O"
    [[buttons[i][j].config(text="") for i in range(3)] for j in range(3)]

def click(i,j):
    if round%2 == 0:
        buttons[j][i].config(text="O")
    else:
        buttons[j][i].config(text="X")
    next_round()


window = tkinter.Tk()
window.title('Tic')

board = tkinter.Frame(window)
board.pack()

buttons = [[tkinter.Button(board, text='', width = 3,borderwidth=3, command = lambda i=i, j=j: click(i,j)) for i in range(3)] for j in range(3)]
[[ buttons[i][j].grid(row=j,column=i) for i in range(3)] for j in range(3)]

UI =  tkinter.Frame(window)
UI.pack()

X_label = tkinter.Label(UI, text='X is playing', width=10)
X_label.pack(side = "left")
button = tkinter.Button(UI, text='New', width=10, command=restart)
button.pack(side = "left")
Y_label = tkinter.Label(UI, text='O', width=10)
Y_label.pack()

window.mainloop()
