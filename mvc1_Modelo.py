


class Jogo:
    def __init__(self,numeroConcurso,dezenas):
        self.numeroConcurso = numeroConcurso
        self.dezenas = dezenas

    def imprimir(self):
        tamanho = len(self.dezenas)
        cont = 1
        #print('Sorteio: ',self.numeroConcurso,' dezenas: ',end='')
        mensagem = 'Sorteio: '+ self.numeroConcurso + ' dezenas: ' + '\n'
        for dezena in self.dezenas:
            if(cont < tamanho):
                #print(dezena,end='-')
                mensagem = mensagem + dezena + '-'
                cont = cont + 1
            else:
                #print(dezena)
                mensagem = mensagem + dezena
        return mensagem

class MegaSena:
    def __init__(self,numeroConcurso,numerosSorteados):
        self.numeroConcurso = numeroConcurso
        self.numerosSorteados = numerosSorteados

    def imprimir(self):
        tamanho = len(self.dezenas)
        cont = 1
        #print('Sorteio: ',self.numeroConcurso,' dezenas: ',end='')
        mensagem = 'Sorteio: '+ self.numeroConcurso + ' dezenas: ' + '\n'
        for dezena in self.dezenas:
            if(cont < tamanho):
                #print(dezena,end='-')
                mensagem = mensagem + dezena + '-'
                cont = cont + 1
            else:
                #print(dezena)
                mensagem = mensagem + dezena
        return mensagem

    def get_sorteio(self):
        return self.numeroConcurso

    def get_sorteados(self):
        return self.numerosSorteados