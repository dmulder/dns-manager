# encoding: utf-8



from libyui import *
class Slider1Client:
    def main(self):
      if not UI.HasSpecialWidget("Slider"):
        UI.OpenDialog(
          VBox(
            Label("Error: This UI doesn't support the Slider widget!"),
            PushButton(Opt("default"), "&OK")
          )
        )
        UI.UserInput()
        UI.CloseDialog()

        return

      UI.OpenDialog(
        VBox(Slider("Percentage", 0, 100, 50), PushButton(Opt("default"), "&OK"))
      )
      UI.UserInput()
      UI.CloseDialog()


Slider1Client().main()

