from tkinter import *
import scrip_limpar


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()

        self.fontePadrao2 = ("Arial", "15")
        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 40
        self.segundoContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 100
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="SuperClear")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.titulo2 = Label(self.segundoContainer, text="É NECESSARIO ME EXECUTAR EM MODO ADM,\n OBRIGADO!")
        self.titulo2["font"] = ("Arial", "20", "bold")
        self.titulo2.pack()

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Executar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 19
        self.autenticar["command"] = self.realizarlimpeza
        self.autenticar.pack()

        imagem = PhotoImage(master=root, file=".img\\ccleaner_copy.png")
        w = Label(root, image=imagem)
        w.imagem = imagem
        w.pack()

    # Método realizar limpeza
    def realizarlimpeza(self):
        scrip_limpar.realizar_limpeza()
        self.autenticar["text"] = "Finalizado!"




root = Tk()
Application(root)
root.mainloop()