import tkinter as tk


def show_stock():
    label.config(text="Spekboom - R35.00")


window = tk.Tk()
window.title("GreenLeaf Nursery Stock")

label = tk.Label(window, text="GreenLeaf Nursery Stock")
label.pack(padx=20, pady=10)

button = tk.Button(window, text="Show Stock", command=show_stock)
button.pack(pady=10)

window.mainloop()