from tkinter import Tk, Canvas, Frame, BOTH

def main():
    root = Tk()

    frame = Frame()
    frame.master.title("Spinograph")
    frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(frame)
    canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
    canvas.pack(fill=BOTH, expand=1)

    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
