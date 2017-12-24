import math
from tkinter import *
from PIL import Image, ImageTk

windowSize = 1000
spirographSet = []
canvas = 'null'

def lcm(x, y):
   lcm = (x*y)//math.gcd(x,y)
   return lcm

class Spirograph():
    def __init__(self, R = 0, r = 0, l = 0, theta = 0, c = 'red', spiroType = 0):
        self.R = R
        self.r = r
        self.l = l
        self.theta = theta
        self.color = c
        self.spiroType = spiroType
        if(self.spiroType==1):
            self.ownScale = windowSize/(2*R)*.9
        if(self.spiroType==2):
            self.ownScale = windowSize/(2*(R+2*r))*.9
        if(self.spiroType==3):
            self.ownScale = windowSize/(2*(2*R-r+l))*.9
        self.positions = []
    def updatePositions(self, scale):
        offset = windowSize/2
        self.positions = []
        if(self.spiroType==1):
            rot = lcm(self.R,self.r)/self.R
            c = (self.R-self.r)/self.r
            for i in range(0,(int)(360*rot)+1):
                self.positions.append(offset+((self.R-self.r)*math.sin(math.radians(i-self.theta))-(self.l*math.sin(math.radians(c*i))))*scale)
                self.positions.append(offset+((self.R-self.r)*math.cos(math.radians(i-self.theta))+(self.l*math.cos(math.radians(c*i))))*scale)
        if(self.spiroType==2):
            rot = lcm(self.R,self.r)/self.R
            c = (self.R+self.r)/self.r
            for i in range(0,(int)(360*rot)+1):
                self.positions.append(offset+((self.R+self.r)*math.sin(math.radians(i-self.theta))+(self.l*math.sin(math.radians(c*i))))*scale)
                self.positions.append(offset+((self.R+self.r)*math.cos(math.radians(i-self.theta))+(self.l*math.cos(math.radians(c*i))))*scale)
        if(self.spiroType==3):
            rot = lcm(self.R,self.r)/self.r
            c = (self.R-self.r)/self.R
            for i in range(0,(int)(360*rot)+1):
                self.positions.append(offset+((self.r-self.R)*math.sin(math.radians(i+self.theta))+((self.R+self.l)*math.sin(math.radians(c*i))))*scale)
                self.positions.append(offset+((self.r-self.R)*math.cos(math.radians(i+self.theta))+((self.R+self.l)*math.cos(math.radians(c*i))))*scale)

def UpdateSpirographs():
    global spirographSet
    global canvas
    scale = float('Inf')
    for spiro in spirographSet:
        if(spiro.ownScale < scale):
            scale = spiro.ownScale
    for spiro in spirographSet:
        spiro.updatePositions(scale)
    if spirographSet:
        canvas.delete(ALL)
        for spiro in spirographSet:
            canvas.create_line(spiro.positions, fill=spiro.color)

def SetInfo(e):
    correct = TRUE
    for value in e[0:5]:
        if(value.get()=='' or value.get()=='missing input'):
            value.delete(0, END)
            value.insert(INSERT, 'missing input')
            correct = FALSE
    if(e[5].get()==0):
        correct = FALSE
    if(correct):
        if(e[6].get()==0):
            ClearCanvas()
        newSprirograph = Spirograph(int(e[0].get()),int(e[1].get()),int(e[2].get()),int(e[3].get()),e[4].get(),int(e[5].get()))
        spirographSet.append(newSprirograph)
        UpdateSpirographs()

def ClearCanvas():
    global spirographSet
    spirographSet = []
    canvas.delete(ALL)

def main():
    root = Tk()
    root.geometry('{}x{}+0+0'.format((int)(windowSize*1.2),windowSize))
    root.title("Spirograph");

    app = Frame(root)

    global spirographSet
    global canvas
    canvas = Canvas(app)
    canvas.pack(fill=BOTH, expand=1, side= LEFT)

    frame = Frame(app)

    Label(frame, text="R").grid(row=0, sticky= W+E+N+S)
    Label(frame, text="r").grid(row=1, sticky= W+E+N+S)
    Label(frame, text="l").grid(row=2, sticky= W+E+N+S)
    Label(frame, text="theta").grid(row=3, sticky= W+E+N+S)
    Label(frame, text="color").grid(row=4, sticky= W+E+N+S)

    e1 = Entry(frame)
    e2 = Entry(frame)
    e3 = Entry(frame)
    e4 = Entry(frame)
    e5 = Entry(frame)

    e1.grid(row=0, column=1, sticky= W+E+N+S)
    e2.grid(row=1, column=1, sticky= W+E+N+S)
    e3.grid(row=2, column=1, sticky= W+E+N+S)
    e4.grid(row=3, column=1, sticky= W+E+N+S)
    e5.grid(row=4, column=1, sticky= W+E+N+S)

    image1 = Image.open("Picture1.png")
    photo1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("Picture2.png")
    photo2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("Picture3.png")
    photo3 = ImageTk.PhotoImage(image3)

    spirographType = IntVar()
    spirographType.set(1)
    rb1 = Radiobutton(frame, text="Type One", image=photo1, variable=spirographType, value=1).grid(row=5, columnspan=2, sticky= W+E+N+S)
    rb2 = Radiobutton(frame, text="Type Two", image=photo2, variable=spirographType, value=2).grid(row=6, columnspan=2, sticky= W+E+N+S)
    rb3 = Radiobutton(frame, text="Type Three", image=photo3, variable=spirographType, value=3).grid(row=7, columnspan=2, sticky= W+E+N+S)

    clear = IntVar()
    c = Checkbutton(frame, text="Keep figure", variable=clear).grid(row=8, columnspan=2, sticky= W+E+N+S)

    e = [e1,e2,e3,e4,e5,spirographType,clear]
    drawButton = Button(frame, text="Draw", command=lambda : SetInfo(e)).grid(row=9, columnspan=2, sticky= W+E+N+S)
    drawButton = Button(frame, text="Clear", command=lambda : ClearCanvas()).grid(row=10, columnspan=2, sticky= W+E+N+S)

    frame.place(x=windowSize, y=0, height= windowSize, width= windowSize*0.2)

    app.pack(fill=BOTH, expand=1)
    root.mainloop()

if __name__ == '__main__':
    main()
