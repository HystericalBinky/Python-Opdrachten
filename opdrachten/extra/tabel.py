import tkinter as tk
from tkinter import ttk
import json

app = tk.Tk()
app.title("Game Data")

# Create a Treeview widget
table = ttk.Treeview(app)

# Define the columns
table['columns'] = ('title', 'developer', 'release date')

# Format the columns
table.column('#0', width=0, stretch=tk.NO)
table.column('title', anchor=tk.W, width=150)
table.column('developer', anchor=tk.W, width=200)
table.column('release date', anchor=tk.W, width=150)

# Create the headings
table.heading('#0', text='', anchor=tk.W)
table.heading('title', text='title', anchor=tk.W)
table.heading('developer', text='teveloper', anchor=tk.W)
table.heading('release date', text='release Date', anchor=tk.W)

# Sample data
with open('data.json', 'r') as file:
        data = json.load(file)

# Configure alternating row colors
table.tag_configure('oddrow', background='#FF0000')
table.tag_configure('evenrow', background='#00FF00')

# Add data with alternating row colors
for i in range(len(data)):
    if i % 2 == 0:
        table.insert(parent='', index=i, values=data[i], tags=('evenrow',))
    else:
        table.insert(parent='', index=i, values=data[i], tags=('oddrow',))

# Pack the table
table.pack(expand=True, fill=tk.BOTH)

app.mainloop()