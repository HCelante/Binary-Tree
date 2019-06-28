


class No:
     
    def __init__(self, key, dir, esq):
        self.item = key
        self.dir = dir
        self.esq = esq

class Tree:
    
    def __init__(self):
        self.root = No(None,None,None)
        self.root = None

    def inserir(self, valor):
        novo = No(valor,None,None) # instancia o novo no e ja insere o valor
        if (self.root == None): # se o no raiz for nulo
            self.root = novo # insere o no na raiz
        else: # se o nó a ser inserido nao for raiz
            atual = self.root # variavel para percorrer os nos da arvore
            while True:
                anterior = atual # variavel para guardar a posicao anterior
                if valor <= atual.item: # caminha para a esquerda
                    atual = atual.esq # variavel que percorre a arvore recebe o no da esquerda
                    if atual == None: # se for vazio
                        anterior.esq = novo # insere na esquerda
                        print("inserido a esquerda do", anterior.item)
                        return 
                else: # caminha para a direita
                    atual = atual.dir #variavel que percorre a arvore recebe o no da direita
                    if atual == None: # se for vazio insere
                        anterior.dir = novo
                        print("inserido a direita do", anterior.item)
                        return

    def insererecB(self,valor,atual,anterior,novo):
        if valor <= atual.item: # caminha para a esquerda
            atual = atual.esq # variavel que percorre a arvore recebe o no da esquerda
            if atual == None: # se for vazio
                anterior.esq = novo # insere na esquerda
                return 
        else: # caminha para a direita
            atual = atual.dir #variavel que percorre a arvore recebe o no da direita
            if atual == None: # se for vazio insere
                anterior.dir = novo
                return

        self.insererecB(valor,atual,anterior,novo)

    def insererec(self,valor):
        novo = No(valor,None,None) # instancia o novo no e ja insere o valor
        if (self.root == None): # se o no raiz for nulo
            self.root = novo # insere o no na raiz
        else: # se o nó a ser inserido nao for raiz
            atual = self.root
            anterior = atual # variavel para guardar a posicao anterior
            self.insererecB(valor,atual,anterior,novo)
            return

    def buscar(self, chave):
        if (self.root == None):# se a arvore for vazia retorna falso
            return False
        esquilo = self.root # inicia pela raiz e percorre a arvore procurando o item
        while (esquilo.item != chave): # enquanto o item que esta em 'esquilo' nao for o desejado, faz 
            if (chave > esquilo.item):
                esquilo = esquilo.dir # procura a direita
            else:
                esquilo = esquilo.esq # procura a esquerda
            # se for nulo    
            if (esquilo == None):
                return False
        return esquilo

    def isHeap(self,i,n):
        pass


if __name__ == "__main__":
    arvere = Tree()
    n = int(input(" Informe o numero de itens q deseja inserir -> "))
    for i in range(n):
        x = int(input(" Informe o valor -> "))
        print (i)
        arvere.inserir(x)
    a = arvere.buscar(x)
    print("a busca retornou ",a.item)
        #arvere.isHeap(0,99)