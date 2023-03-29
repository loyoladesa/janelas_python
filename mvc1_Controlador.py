import mvc1_Visao as vis
import mvc1_Modelo as model

class Controller:
    def __init__(self, model, view):
        self.sorteio = model
        self.view = view
        self.set_sorteio(model.get_sorteio(),model.get_sorteados())
        self.jogos = []


    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.sorteio.email = email
            self.sorteio.save()

            # show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def mainloop(self):
        self.view.mainloop()

    def set_sorteio(self,numeroSorteio,numerosSorteados):
        self.sorteio = model.Sorteio(numeroSorteio, numerosSorteados)
        self.view.set_sorteio(numeroSorteio,numerosSorteados)

    def set_jogos(self,filename):
        try:
            with open(filename, 'r') as infile:
                # Para cada linha do arquivo de entrada
                print("Arquivo Aberto")
                for linha in infile.readlines():
                    print("linha lida")
                    dezenas = []
                    numeros = linha.split('-')
                    for numero in numeros:
                        dezenas.append(numero)
                    jogo = model.Jogo(sorteio.get_sorteio(),dezenas)
                    self.jogos.append(jogo)
                    print("jogo adicionado")
        except:
            print("Ocorreu uma exceção")

        self.view.set_jogos(len(self.jogos))

    def verificarResultados(self):
        jogosCom6Acertos = []
        jogosCom5Acertos = []
        jogosCom4Acertos = []
        jogosCom3Acertos = []
        jogosCom2Acertos = []
        jogosCom1Acertos = []


        for jogo in self.jogos:
            numerosAcertados = jogo.verificar(self.sorteio.get_sorteados())

            if len(numerosAcertados) == 6:
                jogosCom6Acertos.append(jogo)
            if len(numerosAcertados) == 5:
                jogosCom5Acertos.append(jogo)
            if len(numerosAcertados) == 4:
                jogosCom4Acertos.append(jogo)
            if len(numerosAcertados) == 3:
                jogosCom3Acertos.append(jogo)
            if len(numerosAcertados) == 2:
                jogosCom2Acertos.append(jogo)
            if len(numerosAcertados) == 1:
                jogosCom1Acertos.append(jogo)

        mensagem = "Resultados: "+ "\n"

        mensagem = mensagem + 'Jogos com 6 Acertos: ' + str(len(jogosCom6Acertos)) + "\n"
        for jogo in jogosCom6Acertos:
            mensagem = mensagem + jogo.imprimir() + "\n"
        mensagem = mensagem + "\n"
        mensagem = mensagem + 'Jogos com 5 Acertos: ' + str(len(jogosCom5Acertos)) + "\n"
        for jogo in jogosCom5Acertos:
            mensagem = mensagem + jogo.imprimir() + "\n"
        mensagem = mensagem + "\n"
        mensagem = mensagem + 'Jogos com 4 Acertos: ' + str(len(jogosCom4Acertos)) + "\n"
        for jogo in jogosCom4Acertos:
            mensagem = mensagem + jogo.imprimir() + "\n"
        mensagem = mensagem + "\n"
        mensagem = mensagem + 'Jogos com 3 Acertos: ' + str(len(jogosCom3Acertos)) + "\n"
        for jogo in jogosCom3Acertos:
            mensagem = mensagem + jogo.imprimir() + "\n"
        mensagem = mensagem + "\n"
        mensagem = mensagem + 'Jogos com 2 Acertos: ' + str(len(jogosCom2Acertos)) + "\n"
        for jogo in jogosCom2Acertos:
            mensagem = mensagem + jogo.imprimir() + "\n"
        mensagem = mensagem + "\n"
        mensagem = mensagem + 'Jogos com 1 Acertos: ' + str(len(jogosCom1Acertos)) + "\n"
        for jogo in jogosCom1Acertos:
            mensagem = mensagem + jogo.imprimir() + "\n"

        self.view.set_resultados(mensagem)





if __name__ == '__main__':

    sorteio = model.Sorteio(2532, ['28', '36', '39', '44', '56', '60'])
    visao = vis.Visao("MegaSena")

    controller = Controller(sorteio,visao)
    visao.set_controller(controller)
    controller.mainloop()






