from tkinter import *		
from tkinter import messagebox  
from functools import partial
from PIL import Image,ImageTk
menu = Tk()
menu.geometry("400x425")
menu.title("XOXO")
menu.configure(background='black')

nbr=0
def resultat():
    global nbr,b1,b2,b3,b4,b5,b6,b7,b8,b9
    gagne=False 

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
        b1.config(bg="Purple")
        b2.config(bg="Purple")
        b3.config(bg="Purple")
        n=float(playerxx.get())
        score=(n+1)
        playerxx.set(score)
        messagebox.showinfo("resultat","player 1 a gagné!!")
        nbr=0
        gagne=True
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
        b4.config(bg="Purple")
        b5.config(bg="Purple")
        b6.config(bg="Purple")
        n=float(playerxx.get())
        score=(n+1)
        playerxx.set(score)
        messagebox.showinfo("resultat","player 1 a gagné!!")
        nbr=0
        gagne=True
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
        b7.config(bg="Purple")
        b8.config(bg="Purple")
        b9.config(bg="Purple")
        n=float(playerxx.get())
        score=(n+1)
        playerxx.set(score)
        messagebox.showinfo("resultat","player 1 a gagné!!")
        nbr=0
        gagne=True
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
        b1.config(bg="Purple")
        b4.config(bg="Purple")
        b7.config(bg="Purple")
        n=float(playerxx.get())
        score=(n+1)
        playerxx.set(score)
        messagebox.showinfo("resultat","player 1 a gagné!!")
        nbr=0
        gagne=True
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
        b2.config(bg="Purple")
        b5.config(bg="Purple")
        b8.config(bg="Purple")
        n=float(playerxx.get())
        score=(n+1)
        playerxx.set(score)
        messagebox.showinfo("resultat","player 1 a gagné!!")
        nbr=0
        gagne=True
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
        b3.config(bg="Purple")
        b6.config(bg="Purple")
        b9.config(bg="Purple")
        n=float(playerxx.get())
        score=(n+1)
        playerxx.set(score)
        messagebox.showinfo("resultat","player 1 a gagné!!")
        nbr=0
        gagne=True
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
        b1.config(bg="Purple")
        b5.config(bg="Purple")
        b9.config(bg="Purple")
        n=float(playerxx.get())
        score=(n+1)
        playerxx.set(score)
        messagebox.showinfo("resultat","player 1 a gagné!!")
        nbr=0
        gagne=True
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
        b3.config(bg="Purple")
        b5.config(bg="Purple")
        b7.config(bg="Purple")
        n=float(playerxx.get())
        score=(n+1)
        playerxx.set(score)
        messagebox.showinfo("resultat","player 1 a gagné!!")
        nbr=0
        gagne=True
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
        b1.config(bg="Purple")
        b2.config(bg="Purple")
        b3.config(bg="Purple")
        m=float(playeroo.get())
        scorem=(m+1)
        playeroo.set(scorem)
        messagebox.showinfo("resultat","player 2 a gagné!!")
        nbr=0
        gagne=True
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
        b4.config(bg="Purple")
        b5.config(bg="Purple")
        b6.config(bg="Purple")
        m=float(playeroo.get())
        scorem=(m+1)
        playeroo.set(scorem)
        messagebox.showinfo("resultat","player 2 a gagné!!")
        nbr=0
        gagne=True
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
        b7.config(bg="Purple")
        b8.config(bg="Purple")
        b9.config(bg="Purple")
        m=float(playeroo.get())
        scorem=(m+1)
        playeroo.set(scorem)
        messagebox.showinfo("resultat","player 2 a gagné!!")
        nbr=0
        gagne=True
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
        b1.config(bg="Purple")
        b4.config(bg="Purple")
        b7.config(bg="Purple")
        m=float(playeroo.get())
        scorem=(m+1)
        playeroo.set(scorem)
        messagebox.showinfo("resultat","player 2 a gagné!!")
        nbr=0
        gagne=True
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
        b5.config(bg="Purple")
        b2.config(bg="Purple")
        b8.config(bg="Purple")
        m=float(playeroo.get())
        scorem=(m+1)
        playeroo.set(scorem)
        messagebox.showinfo("resultat","player 2 a gagné!!")
        nbr=0
        gagne=True
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
        b6.config(bg="Purple")
        b9.config(bg="Purple")
        b3.config(bg="Purple")
        m=float(playeroo.get())
        scorem=(m+1)
        playeroo.set(scorem)
        messagebox.showinfo("resultat","player 2 a gagné!!")
        nbr=0
        gagne=True
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
        b1.config(bg="Purple")
        b5.config(bg="Purple")
        b9.config(bg="Purple")
        m=float(playeroo.get())
        scorem=(m+1)
        playeroo.set(scorem)
        messagebox.showinfo("resultat","player 2 a gagné!!")
        nbr=0
        gagne=True
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
        b5.config(bg="Purple")
        b7.config(bg="Purple")
        b3.config(bg="Purple")
        m=float(playeroo.get())
        scorem=(m+1)
        playeroo.set(scorem)
        messagebox.showinfo("resultat","player 2 a gagné!!")
        nbr=0
        gagne=True
    elif nbr==9 and gagne==False:
        messagebox.showinfo("resultat","aucun a gagne !! match nul ") 
        nbr=0
 
def click(b):
    global nbr
    if b["text"] == " " and nbr%2==0:
        b["text"] = "X"
        nbr += 1
        l1.config(state=DISABLED)
        l2.config(state=ACTIVE)
        resultat()
    elif b["text"] == " " and nbr%2!=0:       
        b["text"] = "O"
        nbr += 1
        l2.config(state=DISABLED)
        l1.config(state=ACTIVE)
        resultat()
    else:
        messagebox.showwarning("erreur","box is full") 
        
        
def reset():
    b1['text']=" "
    b2['text']=" "
    b3['text']=" "
    b4['text']=" "
    b5['text']=" "
    b6['text']=" "
    b7['text']=" "
    b8['text']=" "
    b9['text']=" "
    b1.configure(background='white')
    b2.configure(background='white')
    b3.configure(background='white')
    b4.configure(background='white')
    b5.configure(background='white')
    b6.configure(background='white')
    b7.configure(background='white')
    b8.configure(background='white')
    b9.configure(background='white')
   
    
    
def newgame():
    reset()
    playerxx.set(0)
    playeroo.set(0)

    
def XO(g):
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,l1,l2,playerxx,playeroo
    g.destroy()
    g = Tk()
    g.title("XOXO")
    playerxx=IntVar()
    playeroo=IntVar()
    playerxx.set(0)
    playeroo.set(0)
    frame0=Frame(g,bd=10,width=1000,height=1000,pady=2,padx=10,bg="plum",relief=RIDGE)
    frame0.grid(row=0,column=0)
    frame1=Frame(frame0,bd=10,width=300,height=300,pady=2,padx=10,bg="plum",relief=RIDGE)
    frame1.pack(side=LEFT)
    frame2=Frame(frame0,bd=10,width=200,height=286,pady=2,padx=10,bg="plum",relief=RIDGE)
    frame2.pack(side=RIGHT)
    frame3=Frame(frame2,bd=10,width=250,height=200,pady=2,padx=10,bg="plum",relief=RIDGE)
    frame3.grid(row=0,column=0)
    frame4=Frame(frame2,bd=10,width=250,height=200,pady=2,padx=10,bg="plum",relief=RIDGE)
    frame4.grid(row=1,column=0)
    playerX=Label(frame3,text="X:",bg='white')
    playerX.grid(row=0,column=0,sticky=W)
    txtplayerX=Entry(frame3,bd=2,fg="black",textvariable=playerxx,width=20,justify=LEFT).grid(row=0,column=1)
    playerO=Label(frame3,text="O:",bg='white')
    playerO.grid(row=1,column=0,sticky=W)
    txtplayerO=Entry(frame3,bd=2,fg="black",textvariable=playeroo,width=20,justify=LEFT).grid(row=1,column=1)
    
    resetbutton=Button(frame4,text="reset",height=5,width=8,bg='dark magenta',command=reset)
    resetbutton.grid(row=0,column=0,sticky=S+N+E+W)
    newgamebutton=Button(frame4,text="new game",height=5,width=8,bg='dark magenta',command=newgame)
    newgamebutton.grid(row=1,column=1,sticky=S+N+E+W)
    
    
    
    l1 = Button(frame1, text = "player 1 : X", width = 10)   
    l1.grid(row = 1, column = 1)
    l2 = Button(frame1, text = "Player 2 : O", width = 10,state=DISABLED) 
    l2.grid(row = 2, column = 1)

    b1 = Button(frame1, text=" ",bd=9,bg='white', height=3, width=6,  command=lambda: click(b1))
    b1.grid(row=3, column=0)
    b2 = Button(frame1, text=" ",bd=9,bg='white', height=3, width=6,  command=lambda: click(b2))
    b2.grid(row=3, column=1)
    b3 = Button(frame1, text=" ",bd=9,bg='white', height=3, width=6,  command=lambda: click(b3))
    b3.grid(row=3, column=2)
    b4 = Button(frame1, text=" ",bd=9,bg='white', height=3, width=6,  command=lambda: click(b4))
    b4.grid(row=4, column=0)
    b5 = Button(frame1, text=" ",bd=9,bg='white', height=3, width=6,  command=lambda: click(b5))
    b5.grid(row=4, column=1)
    b6 = Button(frame1, text=" ",bd=9,bg='white', height=3, width=6, command=lambda: click(b6))
    b6.grid(row=4, column=2)
    b7 = Button(frame1, text=" ", bd=9,bg='white', height=3, width=6, command=lambda: click(b7))
    b7.grid(row=5, column=0)
    b8 = Button(frame1, text=" ", bd=9,bg='white',height=3, width=6, command=lambda: click(b8))
    b8.grid(row=5, column=1)
    b9 = Button(frame1, text=" ", bd=9,bg='white',height=3, width=6, command=lambda: click(b9))
    b9.grid(row=5, column=2)


    
def play():
    xd=partial(XO,menu)
    B2 = Button(menu, text = "Play",command=xd ,
                activeforeground = 'pink',
                activebackground = "black",
                bg = "purple",fg = "white",cursor="gumby",
                width =20,height=1, font = 'summer', bd = 9)

    B3 = Button(menu, text = "Exit", command = menu.destroy,
                activeforeground = 'pink',
                activebackground = "black",
                bg = "purple", fg = "white",cursor="pirate",
                width = 20,height=1, font = 'summer', bd = 9)
    load=Image.open("caca.png")
    render=ImageTk.PhotoImage(load)
    mylabel=Label(menu,image=render)
    mylabel.image=render
    
    B2.pack(side = 'top',padx=5,pady=5)
    mylabel.pack()
    B3.pack(side = 'bottom',padx=5,pady=5)
    menu.mainloop()

    

if True:
    play()


