# encoding: utf-8

# Label example using bold font


from libyui import *
class Label4Client:
    def main(self):
      UI.OpenDialog(
        VBox(
          Label("Label using normal font"),
          Label(Opt("boldFont"), "Label using bold font"),
          Label("Label using normal font"),
          PushButton(Opt("default"), "&OK")
        )
      )

      UI.UserInput()
      UI.CloseDialog()


Label4Client().main()

