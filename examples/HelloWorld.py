# encoding: utf-8



from libyui import *
class HelloWorldClient:
    def main(self):
      UI.OpenDialog(
        VBox(Label("Hello, World!"), PushButton(Opt("default"), "&OK"))
      )
      UI.UserInput()
      UI.CloseDialog()


HelloWorldClient().main()

