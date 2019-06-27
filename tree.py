


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
            atual = self.root
            while True:
                anterior = atual # variavel para percorrer os nos da arvore
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
