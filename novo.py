

class No:
     
    def __init__(self, key, dir, esq):
        self.item = key
        self.dir = dir
        self.esq = esq


class AVLPronta:
    def __init__(self):
        self.root = No(55, No(21,       No(13,None,None),      No(8,None,None))    ,                          No(34,      No(21,None,None)    , No(13,None,None) ))
                #raiz, filhodireito(filho direito , filho esquerdo), filho esquerdo(filho direito, filho esquerdo)

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
    
    def remover(self, v):
        if self.root == None:
                return False # se arvore vazia
        atual = self.root
        pai = self.root
        filho_esq = True
        while atual.item != v: # enquanto nao encontrou
            pai = atual
            if v < atual.item: # caminha para esquerda
                atual = atual.esq
                filho_esq = True # é filho a esquerda? sim
            else: # caminha para direita
                atual = atual.dir 
                filho_esq = False # é filho a esquerda? NAO
            if atual == None:
                return False # encontrou uma folha -> sai
        
        if atual.esq == None and atual.dir == None:
            if atual == self.root:
                self.root = None # se raiz
            else:
                if filho_esq:
                    pai.esq =  None # se for filho a esquerda do pai
                else:
                    pai.dir = None # se for filho a direita do pai

         # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
        elif atual.dir == None:
            if atual == self.root:
                self.root = atual.esq # se raiz
            else:
                if filho_esq:
                    pai.esq = atual.esq # se for filho a esquerda do pai
                else:
                    pai.dir = atual.esq # se for filho a direita do pai
         
         # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
        elif atual.esq == None:
            if atual == self.root:
                self.root = atual.dir # se raiz
            else:
                if filho_esq:
                    pai.esq = atual.dir # se for filho a esquerda do pai
                else:
                    pai.dir = atual.dir # se for  filho a direita do pai

         # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
        else:
            sucessor = self.nosucessor(atual)
               # Usando sucessor que seria o Nó mais a esquerda da subarvore a direita do No que deseja-se remover
            if atual == self.root:
                self.root = sucessor # se raiz
            else:
                if filho_esq:
                    pai.esq = sucessor # se for filho a esquerda do pai
                else:
                        pai.dir = sucessor # se for filho a direita do pai
            sucessor.esq = atual.esq # acertando o ponteiro a esquerda do sucessor agora que ele assumiu 
                                        # a posição correta na arvore   

        return True
    
    
    
    #def buscar(self, chave):
    #    if self.root == None:
    #        return None # se arvore vazia
    #    atual = self.root # comeca a procurar desde raiz
    #    while atual.item != chave: # enquanto nao encontrou
    #        if chave < atual.item:
    #            atual = atual.esq # caminha para esquerda
    #        else:
    #            atual = atual.dir # caminha para direita
    #        if atual == None:
    #            return None # encontrou uma folha -> sai
    #    return atual  # terminou o laco while e chegou aqui pq encontrou item
#
    #def buscarRec(self,chave,atual):
    #    if atual == None:
    #        return
    #    atual.item = int(atual.item)
    #    chave = int(chave)
    #    if atual.item == chave:
    #        return True
    #    else:
    #        return self.buscarRec(chave,atual.esq) and self.buscarRec(chave,atual.dir)
            


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
        
        if ((atual.item > filhoEsq.item) or (atual.item > filhoDir.item)):
            return True
        return True and (self.maxHeap(filhoEsq) and self.maxHeap(filhoDir)) 
        

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
            return True
        elif(filhoEsq == None) and (filhoDir.item > atual.item):
            return True
        elif(filhoDir == None) and (filhoEsq.item < atual.item):
            return True
        elif(filhoEsq == None) and (filhoDir.item < atual.item):
            return False
        elif(filhoDir == None) and (filhoEsq.item > atual.item):
            return False
        elif(filhoEsq.item > atual.item) or (filhoDir.item < atual.item):    
            return False
        else:
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
        if (abs(alturaEsq - alturaDir) <= 1) and (self.isAVL(atual.esq) is True) and (self.isAVL(atual.dir) is True): 
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

    #def isSum(self,atual):
#
    #    if ((atual == None) or (atual.dir == None) or (atual.esq == None)):
    #        return
    #    #print (atual.item )
    #    #print (atual.dir.item + atual.esq.item)
    #    if(atual.item == (atual.dir.item + atual.esq.item)):
    #        
    #        return True and (self.isSum(atual.dir) and self.isSum(atual.esq))
#
    #    else:
    #        return 


    #def isSum(self,atual):
        #if(atual == None):
            #return
        #if ((atual.dir == None) or (atual.esq == None)):
            #return 
        #elif(atual.item == (self.isSum(atual.dir) + self.isSum(atual.esq))):
            #return True
        #else: 
            #return False

    def sum(self, atual):
        if(atual == None):
            return False
        return self.sum(atual.esq) + atual.item + self.sum(atual.dir)

    def isSum(self, atual):
        if(atual == None or (atual.esq == None and atual.dir == None)):
            return True
        somaEsq = self.sum(atual.esq)
        somaDir = self.sum(atual.dir)
        if((atual.item == somaEsq + somaDir) and self.isSum(atual.esq) and self.isSum(atual.dir)):
            return True
        return False


    def mirrorTree(self,atual):
        if atual == None:
            return
        temp = No(None,None,None)
        temp = atual.dir 
        atual.dir = atual.esq
        atual.esq = temp
        self.mirrorTree(atual.dir)
        self.mirrorTree(atual.esq)

    #    
    #    if ((atual.dir == None) and (atual.esq == None)):# quando chega na folha retorna true pois a condicao se manteve verdadeira
    #        return # em toda a arvore
    #    if (atual.item == (atual.dir.item + atual.esq.item)):# só avaça na arvore se a condicao se manter verdadeira
    #        return True and (self.isSum(atual.dir) and self.isSum(atual.esq)) # retorna um and do resultado da subarvore esquerda e da direita
    #    else:
    #        return False
            
    #def areCousins(self,p1,p2, avo):
    #    if(avo == None):
    #        return False
    #    avo = avo
    #    filhoesq = avo.esq
    #    filhodir = avo.dir
    #    neto1 = filhoesq.esq.item
    #    neto2 = filhoesq.dir.item
    #    neto3 = filhodir.esq.item
    #    neto4 = filhodir.dir.item
#
    #    if((p1 == (neto1 or neto2)) and (p2 == (neto3 or neto4))):
    #        return True
    #    if((p1 == (neto1 or neto2)) and (p2 != (neto3 or neto4))) or ((p1 != (neto1 or neto2)) and (p2 == (neto3 or neto4))):
    #        return False
    #    else:
    #        return self.areCousins(p1,p2,avo.dir) and self.areCousins(p1,p2,avo.esq)

    def areCousins(self,p1,p2,raiz):
        if(raiz == None or raiz.esq == None or raiz.dir == None or raiz.dir.esq == None or raiz.dir.dir == None):
            print("retorna")
            return
        print("                             avo = ", raiz.item)
        print("                             /  \   ")

        Avo = raiz
        filhoesq = Avo.esq
        filhodir = Avo.dir
        print("                filho esq", filhoesq.item,"   " ,filhodir.item,"filho dir")
        print("                         / \     / \ ")
                                       
        neto1 = int(filhoesq.esq.item)
        neto2 = int(filhoesq.dir.item)
        print("                       ", filhoesq.esq.item," ", filhoesq.dir.item,"",filhodir.esq.item, "",filhodir.dir.item)
        
        print("filho dir do filho esq")
        neto3 = int(filhodir.esq.item)
        neto4 = int(filhodir.dir.item)
        if((p1 == neto1 or p1 == neto2) and (p2 == neto3 or p2 == neto4)):
            return True
        if((p1 == neto3 or p1 == neto4) and (p2 == neto1 or p2 == neto2)):
            return True
        else:
            self.areCousins(p1,p2,filhoesq)
            self.areCousins(p1,p2,filhodir)


arv = Tree()
opcao = 0

while opcao != 3:
    print("\n Entre com a opcao:")
    print("1: Inserir")
    print("2: Remover")
    print("3: Exibir")
    print("4: Maior")
    print("5: Menor")
    print("6: BST")
    print("7: AVL")
    print("8: Completo")
    print("9: Sair do programa")
    print("10: Se for Soma")
    print("11: Bateria de testes usando arvore soma de 3 niveis")
    opcao = int(input("-> "))
    if opcao == 1:
        x = int(input("Informe o valor: "))
        arv.inserir(x)
    elif opcao == 2:
        x = int(input(" Informe o valor -> "))
        if arv.remover(x) == False:
            print(" Valor nao encontrado!")
    elif opcao == 3:
        arv.caminhar()
    elif opcao == 4:
        maior = arv.highestValue(arv.root)
        print(maior)
    elif opcao == 5:
        menor = arv.lowestValue(arv.root)
        print(menor)
    elif opcao == 6:
        bst = arv.isBST(arv.root)
        print(bst)
    elif opcao == 7:
        avrl = arv.isAVL(arv.root)
        print(avrl)
    elif opcao == 8:
        qtdeNos = arv.contadorNos(arv.root)
        index = 0
        complet = arv.isComplete(arv.root, index, qtdeNos)
        print(complet)
    elif opcao == 9:
        break
    elif opcao == 10:
        print(arv.isSum(arv.root))
    elif opcao == 11:
        # arvore soma
        print("Teste para arvore Soma")
        #########################################################
        # TESTES
        soma = Tree()
        soma.inserir (55)
        soma.root.dir = No(34,No(21,None,None),No(13,None,None))
        soma.root.esq = No(21, No(13,None,None),No(5,None,None))
        #soma.preOrder(soma.root)
        #print(soma.isSum(soma.root))
        if (soma.isSum(soma.root)):
            print("Funcao eh Soma OK")
        else:
            print("ehSoma Falhou")
        if (soma.areCousins(21,5,soma.root)):
            print("Funcao Sao Primos Ok")
        else: 
            print("Sao Primos falhou")
        if(soma.isComplete(soma.root,0,soma.contadorNos(soma.root))):
            print("Funcao isComplete Ok")
        if False == (soma.maxHeap(soma.root)):
            print("Funcao maxHeap Ok")
        if True == (soma.isAVL(soma.root)):
            print("Funcao AVL OK")
        soma.mirrorTree(soma.root)
        print("poder da mirrorizacao")
        soma.areCousins(21,5,soma.root)
        print(soma.isAVL(soma.root))
    elif opcao == 12:
        arvoreaps = Tree()
        arvoreaps.inserir(22)
        arvoreaps.root.dir = No(3,No(1,None,None),No(2,None,None))
        arvoreaps.root.esq = No(8,No(7,None,None),No(1,None,None))
        print(arvoreaps.areCousins(2,7,arvoreaps.root))
        arvoreaps.caminhar()
        print("é avl :")
        print(arvoreaps.isAVL(arvoreaps.root))
        print("é completa?")
        print(arvoreaps.isComplete(arvoreaps.root,0,arvoreaps.contadorNos(arvoreaps.root)))
        print("é max?")
        print(arvoreaps.maxHeap(arvoreaps.root))
        print("isSUM?")
        print(arvoreaps.isSum(arvoreaps.root))
        print("é min?")
        print(arvoreaps.minHeap(arvoreaps.root))
        print("BST:")
        print(arvoreaps.isBST(arvoreaps.root))
        
        # FIM TESTES
        #############################################################################
