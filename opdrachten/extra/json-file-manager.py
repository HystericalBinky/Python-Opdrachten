import json
import tkinter as tk

master = tk.Tk()
master.geometry("600x400")

title_var = tk.StringVar()
developer_var = tk.StringVar()
release_var = tk.StringVar()

def readJson(): 
    with open('data.json', 'r') as file:
        data = json.load(file)

    print(data)

def writeJson(title, developer, release):
    dictionary = {
    "title": title,
    "developer": developer,
    "release date": release
    }
 
    with open("data.json", "w") as outfile:
        json.dump(dictionary, outfile)

def addGame():
    title = title_var.get()
    developer = developer_var.get()
    release = release_var.get()

    writeJson(title, developer, release)
    readJson()

tk.Label(master, text='Title').grid(row=0)
tk.Label(master, text='Developer').grid(row=1)
tk.Label(master, text='Release Date').grid(row=2)
e1 = tk.Entry(master, textvariable = title_var)
e2 = tk.Entry(master, textvariable = developer_var)
e3 = tk.Entry(master, textvariable = release_var)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
sub_btn=tk.Button(master,text = 'Submit', command = addGame).grid(row=4)

tk.mainloop()