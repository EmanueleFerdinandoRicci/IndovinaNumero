from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def getNmax(self):
        return self._model.Nmax

    def getTmax(self):
        return self._model.Tmax

    def reset(self, e): #tutti i metodi del controller associati a un pulsante devono avere un e (evento) per funzionare
        self._model.reset() #resetto gioco lato modello
        #resetto interfaccia grafica
        self._view._txtT.value = self._model.T
        self._view._lvOut.controls.clear() #visto che è una lista di controlli come per i bottoni
        self._view._lvOut.controls.append(
            ft.Text("Inizia il gioco. Indovina il numero che sto pensando")
        )
        #per aggiornare però l'interfaccia grafica serve l'update della pagina che è stato messo in un metodo di view
        self._view.update()

    def play(self, e):
        tentativoStr = self._view._txtInTentativo.value
        try:
            tentativo = int(tentativoStr)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Errore, devi inserire un valore numerico")
            )
            self._view.update()
            return

        self._view._txtT.value = self._model.T-1

        risultato = self._model.play(tentativo)
        if risultato == 0:
            #vittoria
            self._view._lvOut.controls.append(
                ft.Text(f"Hai vinto! Il valore corretto era: {tentativo}", color="red")
            )
            self._view.update()
            return
        elif risultato == 2:
            self._view._lvOut.controls.append(
                ft.Text(f"Hai perso! Il valore corretto era {self._model.segreto}")
            )
            self._view.update()
            return
        elif risultato == -1:
            self._view._lvOut.controls.append(
                ft.Text(f"Ritenta! Il segreto è più piccolo del tuo tentativo, {tentativo}")
            )
            self._view.update()
            return
        else:
            self._view._lvOut.controls.append(
                ft.Text(f"Ritenta! Il segreto è più grande del tuo tentativo, {tentativo}")
            )
            self._view.update()
            return



