import FreeSimpleGUI as sg

from .app_layout import appLayout
from entiteit.pakjesdienst import Pakjesdienst

class App:
    def __init__(self):
        self._pakjesdienst = Pakjesdienst()

    def toon(self):
        venster = sg.Window(
            title = 'PAKJES VERZENDKOSTEN CALCULATOR',
            icon = 'assets/favicon.ico',
            layout = appLayout(),
            resizable = False,
            finalize = True
        )

        landen = self._pakjesdienst.landen()
        venster['-CBB-BESTEMMING-'].update(values = landen)
        venster['-CBB-BESTEMMING-'].update(set_to_index = 0)

        categorieen = self._pakjesdienst.categorieen()
        venster['-CBB-GEWICHT-'].update(values = categorieen)
        venster['-CBB-GEWICHT-'].update(set_to_index = 0)

        bedrag = self._pakjesdienst.bereken(land=landen[0], gewicht=categorieen[0], verzekerd=False)
        venster['-TXT-BEDRAG-'].update(f'€ {bedrag:0.2f}')


        while True:
            evt, vals = venster.read()

            match evt:
                case sg.WIN_CLOSED:
                    break

                case '-BTN-BEREKEN-' | '-CBB-BESTEMMING-' | '-CBB-GEWICHT-' | '-CHB-VERZEKERD-':
                    bestemming = vals['-CBB-BESTEMMING-']
                    gewicht = vals['-CBB-GEWICHT-']
                    verzekerd = vals['-CHB-VERZEKERD-']

                    bedrag = self._pakjesdienst.bereken(land = bestemming, gewicht = gewicht, verzekerd = verzekerd)

                    venster['-TXT-BEDRAG-'].update(f'€ {bedrag:0.2f}')

        venster.close()