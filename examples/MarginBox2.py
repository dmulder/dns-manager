# encoding: utf-8



from libyui import *
class MarginBox2Client:
    def main(self):
      UI.OpenDialog(
        VBox(
          MarginBox(
            Term("leftMargin", 10),
            Term("rightMargin", 20),
            Term("topMargin", 2),
            Term("bottomMargin", 3.5),
            Label("Hello, World!")
          ),
          PushButton(Opt("default"), "&OK")
        )
      )
      UI.UserInput()
      UI.CloseDialog()


MarginBox2Client().main()

