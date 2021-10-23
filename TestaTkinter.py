from tkinter import *

window = Tk()
btn = Button(window, text="Este é um componente Botão", fg='blue')
btn.place(x=80, y=100)
lbl = Label(window, text="Este é um componente de Rótulo", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld = Entry(window, text="Este é um componente de Entrada de Texto", bd=5)
txtfld.place(x=80, y=150)
window.title('Bem-vindo ao Python')
window.geometry("300x200+10+10")
window.mainloop()
