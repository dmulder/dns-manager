# encoding: utf-8



from libyui import *
class SmallDecorationsClient:
    def main(self):
      UI.OpenDialog(
        Opt("smallDecorations"),
        VBox(Label("Hello, World!"), PushButton(Opt("default"), "&OK"))
      )
      UI.UserInput()
      UI.CloseDialog()


SmallDecorationsClient().main()

