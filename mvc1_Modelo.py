


class Jogo:
    def __init__(self,numeroConcurso,dezenas):
        self.numeroConcurso = numeroConcurso
        self.dezenas = dezenas

    def imprimir(self):
        tamanho = len(self.dezenas)
        cont = 1
        #print('Sorteio: ',self.numeroConcurso,' dezenas: ',end='')
        mensagem = 'Sorteio: '+ str(self.numeroConcurso) + '\n' + 'Dezenas: ' + '\n'
        for dezena in self.dezenas:
            if(cont < tamanho):
                #print(dezena,end='-')
                mensagem = mensagem + dezena + '-'
                cont = cont + 1
            else:
                #print(dezena)
                mensagem = mensagem + dezena
        return mensagem

    def verificar(self,numerosSorteados):
        numerosAcertados = []

        for numero in numerosSorteados:

            if numero in self.dezenas:
                numerosAcertados.append(numero)
        return numerosAcertados

class Sorteio:
    def __init__(self,numeroConcurso,numerosSorteados):
        self.numeroConcurso = numeroConcurso
        self.numerosSorteados = numerosSorteados

    def get_sorteio(self):
        return self.numeroConcurso

    def get_sorteados(self):
        return self.numerosSorteados