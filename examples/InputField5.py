# encoding: utf-8



from libyui import *
class InputField5Client:
    def main(self):
      UI.OpenDialog(
        VBox(
          Frame(
            "Shrinkable Textentries",
            HBox(
              InputField(Opt("shrinkable"), "1"),
              InputField(Opt("shrinkable"), "2"),
              InputField(Opt("shrinkable"), "321"),
              InputField(Opt("shrinkable"), "4")
            )
          ),
          PushButton(Opt("default"), "&OK")
        )
      )
      UI.UserInput()
      UI.CloseDialog()


InputField5Client().main()

