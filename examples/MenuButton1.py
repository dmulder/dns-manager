# encoding: utf-8

# Build a dialog with one menu button.
# Wait the user selects a menu entry,
# then close the dialog and terminate.
#
# Please note that it's pretty pointless to create menu entries without an ID:
# You'd never know what entry the user selected.


from libyui import *
class MenuButton1Client:
    def main(self):
      UI.OpenDialog(
        MenuButton(
          "&Create",
          [
            Item(Id("folder"), "&Folder"),
            Item(Id("text"), "&Text File"),
            Item(Id("image"), "&Image")
          ]
        )
      )

      id = UI.UserInput()
      UI.CloseDialog()

      ycpbuiltins.y2milestone("Selected: %1", id)


MenuButton1Client().main()

