import tkinter as tk
from tkinter import ttk

import mvc1_Modelo
import mvc1_Controlador as control


class Visao():
    def __init__(self,titulo):
        self.janela = tk.Tk()
        self.janela.title(titulo)
        self.janela.geometry('600x400')

        # Mensagem a ser exibida no menu Sobre
        self.sobre = "Comissão Nacional de Energia Nuclear" + "\n" + "@DISOL. Todos os direitos reservados" + "\n" + "Versão: 1.0" + "\n" + "disol@cnen.gov.br"

        # Cria os menus
        self.menubar = tk.Menu(self.janela)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Novo", command=None)
        self.filemenu.add_command(label="Abrir", command=None)
        self.filemenu.add_command(label="Salvar", command=None)
        self.filemenu.add_command(label="Salvar Como", command=None)
        self.filemenu.add_separator()

        self.filemenu.add_command(label="Sair", command=self.janela.quit)
        self.menubar.add_cascade(label="Arquivo", menu=self.filemenu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Índice Ajuda", command=lambda: self.funcaoAlerta(self.sobre))
        self.helpmenu.add_command(label="Sobre...", command=lambda: self.funcaoAlerta(self.sobre))
        self.menubar.add_cascade(label="Ajuda", menu=self.helpmenu)

        self.janela.config(menu=self.menubar)

        self.textoTopo = ttk.Label(self.janela, text="Exemplo de Janela Python")
        self.textoTopo.grid(column=0, row=0, padx=10, pady=10)

        # cria o botao
        mensagem = "Executou  a Função de Alerta"
        self.botao = ttk.Button(self.janela, text='Carregar Sorteio', command=lambda: self.funcaoCarregarSorteio())
        self.botao.grid(column=0, row=2, padx=10, pady=10)
        # btn.pack(side = 'top')

        # cria o botao
        mensagem2 = "Executou  a Função de Alerta 2"
        self.botao2 = ttk.Button(self.janela, text='Exibir Mensagem 2', command=lambda: self.funcaoAlerta(mensagem2))
        self.botao2.grid(column=1, row=2, padx=10, pady=10)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller


    def funcaoAlerta(self,mensagem):
        filewin = tk.Toplevel(self.janela)
        filewin.geometry('400x150')
        textoMensagem = ttk.Label(filewin, text=mensagem)
        textoMensagem.grid(column=0, row=0, padx=10, pady=10)
        self.center(filewin)

    def center(self,win):
        # :param win: the main window or Toplevel window to center

        # Apparently a common hack to get the window size. Temporarily hide the
        # window to avoid update_idletasks() drawing the window in the wrong
        # position.
        win.update_idletasks()  # Update "requested size" from geometry manager

        # define window dimensions width and height
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width

        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width

        # Get the window position from the top dynamically as well as position from left or right as follows
        # x = win.winfo_screenwidth() // 2 - win_width // 2
        # y = win.winfo_screenheight() // 2 - win_height // 2

        x = self.janela.winfo_rootx()
        y = self.janela.winfo_rooty()

        # this is the line that will center your window
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        # This seems to draw the window frame immediately, so only call deiconify()
        # after setting correct window position
        win.deiconify()

    def mainloop(self):
        self.janela.mainloop()

    def set_sorteio(self,numeroSorteio,numerosSorteados):
        mensagem = "Número do Sorteio : " + str(numeroSorteio) + "\n" + "Números Sorteados: [ "

        for numero in numerosSorteados:
            mensagem = mensagem + numero + " , "
        mensagem = mensagem[:-2]
        mensagem = mensagem + "]"

        #self.textoTopo = ttk.Label(self.janela, text=mensagem)
        #self.textoTopo.grid(column=0, row=0, padx=10, pady=10)

        self.textoTopo['text']=mensagem

    def funcaoCarregarSorteio(self):
        filewin = tk.Toplevel(self.janela)
        filewin.geometry('400x150')
        #textoMensagem = ttk.Label(filewin, text=mensagem)
        #textoMensagem.grid(column=0, row=0, padx=10, pady=10)

        # create widgets
        # label
        label = ttk.Label(filewin, text='Número do Sorteio:')
        label.grid(column=0, row=0, padx=10, pady=10)

        # email entry
        numero_sorteio = tk.StringVar()
        numero_sorteio_entry = ttk.Entry(filewin, textvariable=numero_sorteio, width=4)
        numero_sorteio_entry.grid(row=0, column=1, sticky=tk.NSEW)

        label_1 = ttk.Label(filewin, text='Números Sorteados:')
        label_1.grid(column=0, row=1, padx=10, pady=10)

        # email entry
        dezena1 = tk.StringVar()
        dezena1_entry = ttk.Entry(filewin, textvariable=dezena1, width=4)
        dezena1_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # email entry
        dezena2 = tk.StringVar()
        dezena2_entry = ttk.Entry(filewin, textvariable=dezena2, width=4)
        dezena2_entry.grid(row=1, column=2, sticky=tk.NSEW)

        # email entry
        dezena3 = tk.StringVar()
        dezena3_entry = ttk.Entry(filewin, textvariable=dezena3, width=4)
        dezena3_entry.grid(row=1, column=3, sticky=tk.NSEW)
        # email entry

        dezena4 = tk.StringVar()
        dezena4_entry = ttk.Entry(filewin, textvariable=dezena4, width=4)
        dezena4_entry.grid(row=1, column=4, sticky=tk.NSEW)

        # email entry
        dezena5 = tk.StringVar()
        dezena5_entry = ttk.Entry(filewin, textvariable=dezena5, width=4)
        dezena5_entry.grid(row=1, column=5, sticky=tk.NSEW)

        # email entry
        dezena6 = tk.StringVar()
        dezena6_entry = ttk.Entry(filewin, textvariable=dezena6, width=4)
        dezena6_entry.grid(row=1, column=6, sticky=tk.NSEW)

        numeros_sorteados = []
        numeros_sorteados.append(dezena1.get())
        numeros_sorteados.append(dezena2.get())
        numeros_sorteados.append(dezena3.get())
        numeros_sorteados.append(dezena4.get())
        numeros_sorteados.append(dezena5.get())
        numeros_sorteados.append(dezena6.get())

        print(numeros_sorteados)

        # save button
        save_button = ttk.Button(filewin, text='Save', command=lambda: self.save_button_clicked(numero_sorteio.get(),dezena1.get(),filewin))
        save_button.grid(row=2, column=0, padx=10)


        self.center(filewin)

    def save_button_clicked(self,numeroSorteio,numerosSorteados,filewin):
        """
        Handle button click event
        :return:
        """

        #filewin.

        if self.controller:
            self.controller.set_sorteio(numeroSorteio,numerosSorteados)
        filewin.destroy()