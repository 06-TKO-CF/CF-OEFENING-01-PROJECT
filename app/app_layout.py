import FreeSimpleGUI as sg

from . import init_layout

def appLayout():
    fontTitel = init_layout.fontApp[:]
    fontTitel[1] = 24
    fontTitel.append('bold')

    fontBedrag = init_layout.fontApp[:]
    fontBedrag[1] = 48
    fontBedrag.append('bold')

    return [
        # RIJ 1
        [
            sg.Push(),
            sg.Image(
                source = 'assets/logo.png'
            ),
            sg.Text(
                text = 'PAKJES VERZENDKOSTEN CALCULATOR',
                font = tuple(fontTitel)
            ),
            sg.Push()
        ],

        # RIJ 2
        [
            sg.Column(
                layout = [
                    [
                        sg.Frame(
                            title = 'Info pakje',
                            pad = (15,15),
                            layout = [
                                [
                                    sg.Text(
                                        text = 'Maximale afmetingen: 100 x 50 x 50 cm',
                                        pad = (15, 15)
                                    )
                                ],
                                [
                                    sg.Text(
                                        text = 'Land bestemming',
                                        size = (18, 1),
                                        pad = (15, 15)
                                    ),
                                    sg.Combo(
                                        values = [],
                                        key = '-CBB-BESTEMMING-',
                                        enable_events = True,
                                        size = (15,1),
                                        pad = (15, 15)
                                    )
                                ],
                                [
                                    sg.Text(
                                        text = 'Gewicht pakje',
                                        size = (18, 1),
                                        pad = (15, 15)
                                    ),
                                    sg.Combo(
                                        values = [],
                                        key = '-CBB-GEWICHT-',
                                        enable_events = True,
                                        size = (15,1),
                                        pad = (15, 15)
                                    )
                                ],                                
                                [
                                    sg.Text(
                                        text = '',
                                        size = (18, 1),
                                        pad = (15, 15)
                                    ),
                                    sg.Checkbox(
                                        text = 'verzekerd tot € 500,-',
                                        pad = (15,15),
                                        key = '-CHB-VERZEKERD-',
                                        enable_events = True
                                    )
                                ],                               
                                [
                                    sg.Text(
                                        text = '',
                                        size = (18, 1),
                                        pad = (15, 15)
                                    ),
                                    sg.Checkbox(
                                        text = 'Standaard track & trace',
                                        pad = (15,15),
                                        disabled = True,
                                        default = True
                                    )
                                ],
                                [
                                    sg.Button(
                                        button_text = 'Bereken verzendkosten',
                                        size = (41,2),
                                        pad = (15,15),
                                        key = '-BTN-BEREKEN-'
                                    )
                                ]
                            ]
                        )
                    ]
                ]
            ),

            sg.Column(
                expand_y = True,
                layout = [
                    [
                        sg.Frame(
                            title = 'Verzendkosten',
                            pad = (15,15),
                            expand_y = True,
                            layout = [
                                [
                                    sg.VPush()
                                ],
                                [
                                    sg.Text(
                                        text = '0',
                                        pad = (15, 15),
                                        justification = 'center',
                                        font = fontBedrag,
                                        size = (10,1),
                                        key = '-TXT-BEDRAG-'
                                    )
                                ],
                                [
                                    sg.VPush()
                                ]
                            ]
                        )
                    ]
                ]
            )
        ]
    ]