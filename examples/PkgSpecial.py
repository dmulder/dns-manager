# encoding: utf-8

# PkgSpecial example - not for general use!
#


from libyui import *
class PkgSpecialClient:
    def main(self):
      UI.OpenDialog(
        VBox(
          Label("Hello, world!"),
          PkgSpecial("dummy1"),
          PkgSpecial("dummy2"),
          PkgSpecial("dummy3"),
          PushButton(Opt("default"), "&Ok")
        )
      )
      UI.UserInput()
      UI.CloseDialog()


PkgSpecialClient().main()

