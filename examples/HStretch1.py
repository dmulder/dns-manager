# encoding: utf-8



from libyui import *
class HStretch1Client:
    def main(self):
      UI.OpenDialog(
        VBox(
          Label("Some text goes here"),
          Label("This is some more text, that is quite long, as you can see."),
          HBox(PushButton("&OK"), HStretch())
        )
      )
      ret = UI.UserInput()
      UI.CloseDialog()
      deep_copy(ret)

HStretch1Client().main()

