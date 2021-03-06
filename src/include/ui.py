from libyui import *

have_advanced_gui = UI.HasSpecialWidget('Wizard')

def CreateMenu(menu):
    '''Add a file menu

    Parameters
    list menu   A list of dictionaries, each dictionary describing a new menu entry
        For example:
            [{'title': 'File', 'id': 'file', 'type': 'Menu'},
             {'title': 'Save', 'id': 'save', 'type': 'SubMenu', 'parent': 'file'},
             {'title': 'Save as', 'id': 'save_as', 'type', 'MenuEntry', 'parent': 'save'},
             {'title': 'Close', 'id': 'close', 'type': 'MenuEntry', 'parent': 'file'}]
        Each menu entry must provide a title, id, and type. The entry can optionally
        provide a parent, meaning the parent menu to append this entry to.
    '''
    if have_advanced_gui:
        UI.WizardCommand(Term('DeleteMenus'))
        for m in menu:
            if m['type'] == 'Menu':
                UI.WizardCommand(Term('AddMenu', m['title'], m['id']))
            elif m['type'] == 'MenuEntry':
                UI.WizardCommand(Term('AddMenuEntry', m['parent'], m['title'], m['id']))
            elif m['type'] == 'SubMenu':
                UI.WizardCommand(Term('AddSubMenu', m['parent'], m['title'], m['id']))
    else:
        Wizard.CreateMenu(menu)

def DeleteButtonBox():
    '''Hide the Wizard button box from the bottom of the window
    '''
    Wizard.HideBackButton()
    Wizard.HideNextButton()
    Wizard.HideAbortButton()
    if UI.WidgetExists(Id('rep_help')):
        UI.ReplaceWidget(Id('rep_help'), Empty())
