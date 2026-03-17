import random

class Model(object):
    def __init__(self):
        self._Nmax = 100
        self._Tmax = 6
        self._T = self._Tmax
        self._segreto = None

    def reset(self):
        #Resetta lo stato del gioco, dà un numero da indovinare e ripristina tentativi
        self._segreto = random.randint(0,self._Nmax)
        self._T = self._Tmax
        print(self._segreto)

    def play(self, tentativo):
        #Questo metodo riceve come argomento un valore intero che è il tentativo del giocatore e viene confrontato con il segreto
        #-1 se segreto minore del tentativo, 0 uguale, 1 più grande
        #2 se vite finite
        self._T -= 1
        if tentativo == self._segreto:
            return 0 #vittoria
        #tentativi successivi da fare solo se ho ancora vite
        if self._T == 0:
            return 2
        if tentativo > self._segreto:
            return -1
        else:
            return 1

    @property
    def Nmax(self):
        return self._Nmax

    @property
    def Tmax(self):
        return self._Tmax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto

if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(50))
    print(m.play(20))
    print(m.play(30))
    print(m.play(40))
    print(m.play(60))
    print(m.play(70))
    print(m.play(80))