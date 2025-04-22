import tkinter as tk

app = tk.Tk()
app.title("Rechthoek")
app.geometry("800x600")

def tick(x1, x2):
    #canvas.create_rectangle(50, 0, 100, 50, fill='red')
    canvas.create_rectangle(50, 0, x1 * 50, 50, fill='red')
    if x1 < 5:
        app.after(1000, tick, x1 + 1, x2 - 100)
    else:
        app.after(1000, tick2, x1 + 1, 300, 1)

def tick2(x1, x2, y1):
    #canvas.create_rectangle(50, 0, 100, 50, fill='red')
    canvas.create_rectangle(250, 0, 300, y1 * 50, fill='red')
    if y1 < 4:
        app.after(1000, tick2, x1 + 1, x2, y1 + 1)
    else:
        app.after(1000, tick3, x1 + 1, 300)


def tick3(x1, x2):
    #canvas.create_rectangle(50, 0, 100, 50, fill='red')
    canvas.create_rectangle(250, 200, x2, 250, fill='red')
    if x2 > 0:
        app.after(1000, tick3, x1 + 1, x2 - 50)
    else:
        app.after(1000, tick4, x1 + 1, 300, 0, 5)

def tick4(x1, x2, y1, y2):
    #canvas.create_rectangle(50, 0, 100, 50, fill='red')
    canvas.create_rectangle(0, 200, 50, y2 * 50, fill='red')
    if y2 > 0:
        app.after(1000, tick4, x1 + 1, x2, 0, y2 - 1)

canvas = tk.Canvas(app)
tick(2, 200)

canvas.pack(expand= 1)
app.mainloop()