from abc import ABCMeta,abstractmethod

class Computador(metaclass=ABCMeta):

    @property
    def modelo(self):
        pass

    @modelo.setter
    def modelo (self,valor):
        pass

    @property
    def cor(self):
        pass

    @cor.setter  
    def modelo (cor,valor):
        pass

    @property
    def preco(self):
        pass

    @preco.setter
    def preco (self,valor):
        pass

    def getImprimir(self):
        print("modelo:",self.modelo)
        print("cor:",self.cor)
        print("preco:",self.preco)

    
    @abstractmethod
    def cadastrar(self,v1,v2,v3,v4):
        pass
        
