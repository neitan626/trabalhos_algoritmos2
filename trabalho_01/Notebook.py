from Computador import Computador

class Notebook(Computador):

    def __init__(self,modelo=None,cor=None,preco=None,tempoDeBateria=None):
        self._modelo = modelo
        self._cor = cor
        self._preco = preco
        self.__tempoDeBateria = tempoDeBateria
        

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self,valor):
        self._modelo = valor


    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self,valor):
        self._modelo = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self,valor):
        self._preco = valor


    @property
    def modelo(self):
        return self.__tempoDeBateria

    @modelo.setter
    def modelo(self,valor):
        self.__tempoDeBateria = valor

    def getImprimir(self):
        print("Notebook")
        super().getImprimir()
        print("potencia da fonte:",self.__tempoDeBateria)
        
   
    def cadastrar(self, v1=None, v2=None, v3=None, v4=None):
        print("cadastrando um Notebook")
        v1 = str(input("Insira o nome do modelo:"))
        v2 = str(input("Insira uma cor:"))
        v3 = float(input("Insira o preço:"))
        v4 = str(input("Insira o tempo de bateria:"))
        print(" ")
        print("---Notebook Cadstrado!---")
        print(" ")
        self._modelo = v1
        self._cor = v2
        self._preco = v3
        self.__tempoDeBateria = v4
        
    