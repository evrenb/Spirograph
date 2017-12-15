import math
from tkinter import Tk, Canvas, Frame, BOTH

def lcm(x, y):
   lcm = (x*y)//math.gcd(x,y)
   return lcm

def main():
    window = Tk()
    window.geometry("1000x1000+0+0")

    # frame = Frame()
    # frame.master.title("Spirograph")
    # frame.pack(fill=BOTH, expand=1)

    R = 50
    r = 20
    l = 6
    rot = lcm(R,r)/R
    print (rot)

    c = (R-r)/r

    positions = []
    for i in range(0,(int)(360*rot)+1):
        positions.append((40+(R-r)*math.sin(math.radians(i))-(l*math.sin(math.radians(c*i))))*10)
        positions.append((40+(R-r)*math.cos(math.radians(i))+(l*math.cos(math.radians(c*i))))*10)

    print(positions)

    canvas = Canvas()
    canvas.create_line(positions, fill='#ff0000')
    canvas.pack(fill=BOTH, expand=1)

    window.mainloop()

if __name__ == '__main__':
    main()
