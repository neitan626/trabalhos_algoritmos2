from Computador import Computador

class Desktop(Computador):

    def __init__(self,modelo=None,cor=None,preco=None,potenciaDaFonte=None):
        self._modelo = modelo
        self._cor = cor
        self._preco = preco
        self._potenciaDaFonte = potenciaDaFonte
        

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
        return self._potenciaDaFonte

    @modelo.setter
    def modelo(self,valor):
        self._potenciaDaFonte = valor

    def getImprimir(self):
        print("--Desktop--")
        super().getImprimir()
        print("potencia da fonte:",self._potenciaDaFonte)
        print("-------------")
        
   
    def cadastrar(self, v1=None, v2=None, v3=None, v4=None):
        print("cadastrando um novo Desktop")
        v1 = str(input("Insira o nome do modelo:"))
        v2 = str(input("Insira uma cor:"))
        v3 = float(input("Insira o preço:"))
        v4 = str(input("Insira o potencia da fonte:"))
        print("---Desktop Cadstrado!---")
        print(" ")
        self._modelo = v1
        self._cor = v2
        self._preco = v3
        self._potenciaDaFonte = v4
        
    