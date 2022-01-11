import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.title("Aplicação GUI")
ttk.Label(janela, text="Componente Label").grid(column=0, row=0)
# janela.resizable(False, False)
janela.mainloop()