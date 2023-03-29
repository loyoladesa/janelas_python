import mvc1_Visao as vis
import mvc1_Modelo as model

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.set_sorteio(model.get_sorteio(),model.get_sorteados())


    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

    def mainloop(self):
        self.view.mainloop()

    def set_sorteio(self,numeroSorteio,numerosSorteados):
        self.model = model.MegaSena(numeroSorteio,numerosSorteados)
        self.view.set_sorteio(numeroSorteio,numerosSorteados)

if __name__ == '__main__':

    sorteio = model.MegaSena(2532,['28','36','39','44','56','60'])
    visao = vis.Visao("MegaSena")

    controller = Controller(sorteio,visao)
    visao.set_controller(controller)
    controller.mainloop()






