import tkinter

window = tkinter.Tk()
window.title("GUI Graphical user interface")
window.minsize(width=400, height=300)

#Label
label = tkinter.Label(text="Just die (shine)", font=("Arial", 25, "bold"))
label.grid(row=0, column=0)
label.config(padx=20, pady=20)

def click():
    new_text = input.get()
    label.config(text=new_text)

#entry
input = tkinter.Entry(width=15)
input.grid(column=3,row=3)


#button
button = tkinter.Button(text="click here", command=click)
button.grid(column=0, row=1)



window.mainloop()