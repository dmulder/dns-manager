from dnsmanager.dialogs import DNS
from libyui import Wizard, UI, Sequencer, Symbol

def DNSSequence():
    aliases = {
        'dns' : [(lambda: DNS().Show())],
    }

    sequence = {
        'ws_start' : 'dns',
        'dns' : {
            Symbol('abort') : Symbol('abort'),
            Symbol('next') : Symbol('next'),
        },
    }

    Wizard.CreateDialog()
    Wizard.SetTitleIcon('dns-manager')

    ret = Sequencer.Run(aliases, sequence)

    UI.CloseDialog()
    return ret

