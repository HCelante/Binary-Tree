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
        else: # se o no a ser inserido nao for raiz
            atual = self.root # variavel para percorrer os nos da arvore
            while True:
                anterior = atual # variavel para guardar a posicao anterior
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

    def buscar(self, chave):
        if self.root == None:
            return None # se arvore vazia
        atual = self.root # comeca a procurar desde raiz
        while atual.item != chave: # enquanto nao encontrou
            if chave < atual.item:
                atual = atual.esq # caminha para esquerda
            else:
                atual = atual.dir # caminha para direita
            if atual == None:
                return None # encontrou uma folha -> sai
        return atual  # terminou o laco while e chegou aqui e pq encontrou item

    def maxHeap(self, atual):
        if atual == None:
            return None # se arvore vazia   
        
        if(atual.esq == None):
            return False
        else:
            filhoEsq = atual.esq
        
        if(atual.dir == None):
            return False
        else:
            filhoDir = atual.dir
        
        if ((atual.item <= filhoEsq.item) or (atual.item <= filhoDir.item)):
            return False
        return self.maxHeap(filhoEsq) and self.maxHeap(filhoDir) 
        

    def minHeap(self, root):
        if root == None:
            return None # se arvore vazia   
        atual = root
        
        if(atual.esq == None):
            return False
        else:
            filhoEsq = atual.esq
        
        if(atual.dir == None):
            return False
        else:
            filhoDir = atual.dir
        
        if ((atual.item >= filhoEsq.item) or (atual.item >= filhoDir.item)):
            return False
        return self.minHeap(filhoEsq) and self.minHeap(filhoDir) 
    

    def isBST(self, atual):
        if atual == None:
            return None # se arvore vazia
        filhoEsq = atual.esq
        filhoDir = atual.dir
        
        if(filhoEsq == None and filhoDir == None):
            print("is BST")
            return True
        elif(filhoEsq == None) and (filhoDir.item < atual.item):
            return False
        elif(filhoDir == None) and (filhoEsq.item > atual.item):
            return False
        elif((filhoEsq.item > atual.item) or (filhoDir.item < atual.item)):    
            return False
        else:
            print("is BST")
            return self.isBST(filhoEsq) and self.isBST(filhoDir)
 
    def altura(self, atual): 
        if atual is None: 
            return 0
        return max(self.altura(atual.esq), self.altura(atual.dir)) + 1

    def isAVL(self, atual):
        if atual == None:
            return False # se arvore vazia
        alturaEsq = self.altura(atual.esq)
        print(alturaEsq)
        alturaDir = self.altura(atual.dir)
        print(alturaDir)
        if (abs(alturaEsq - alturaDir) <= 1): 
            return True
        return False

    def contadorNos(self, atual): 
        if atual == None: 
            return 0 
        return (1+ self.contadorNos(atual.esq) + self.contadorNos(atual.dir)) 
  
    def isComplete(self, atual, index, qtdeNos): 
        
        if atual == None: 
            return True
        
        if index >= qtdeNos : 
            return False
        
        return (self.isComplete(atual.esq , 2*index+1 , qtdeNos) and self.isComplete(atual.dir, 2*index+2, qtdeNos)) 
             
    
    
    def highestValue(self, atual):
        if atual == None:
            return None
        maior = atual.item
        filhoDir = atual.dir
        if(filhoDir == None):
            return maior
        return self.highestValue(filhoDir)


    def lowestValue(self, atual):
        if atual == None:
            return None
        menor = atual.item
        filhoEsq = atual.esq
        if(filhoEsq == None):
            return menor
        return self.lowestValue(filhoEsq)
    
    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esq)
            print(atual.item)
            self.inOrder(atual.dir)
  
    def preOrder(self, atual):
        if atual != None:
            print(atual.item,)
            self.preOrder(atual.esq)
            self.preOrder(atual.dir)
       
    def posOrder(self, atual):
        if atual != None:
            self.posOrder(atual.esq)
            self.posOrder(atual.dir)
            print(atual.item)
    
    def caminhar(self):
        print(" Exibindo em ordem: ")
        self.inOrder(self.root)
        print("\n Exibindo em pos-ordem: ")
        self.posOrder(self.root)
        print("\n Exibindo em pre-ordem: ")
        self.preOrder(self.root)

    def isSum(self,atual):
        if ((atual.dir == None) and (atual.esq == None)):
            return True
        if (atual.item == (atual.dir.item + atual.esq.item)):
            return self.isSum(atual.dir) and self.isSum(atual.esq)
        else:
            return False
            


arv = Tree()
opcao = 0
while opcao != 3:
    print("\n Entre com a opcao:")
    print("1: Inserir")
    print("2: Exibir")
    print("3: Maior")
    print("4: Menor")
    print("5: AVL")
    print("6: Completo")
    print("7: Sair do programa")
    opcao = int(input("-> "))
    if opcao == 1:
        x = int(input("Informe o valor: "))
        arv.inserir(x)
    elif opcao == 2:
        arv.caminhar()
    elif opcao == 3:
        maior = arv.highestValue(arv.root)
        print(maior)
    elif opcao == 4:
        menor = arv.lowestValue(arv.root)
        print(menor)
    elif opcao == 5:
        avrl = arv.isAVL(arv.root)
        print(avrl)
    elif opcao == 6:
        qtdeNos = arv.contadorNos(arv.root)
        index = 0
        complet = arv.isComplete(arv.root, index, qtdeNos)
        print(complet)
    elif opcao == 7:
        break
