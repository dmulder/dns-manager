# encoding: utf-8

# Using UI::TextMode()


from libyui import *
class TextModeClient:
    def main(self):
      msg = "Text mode" if UI.TextMode() else  "GUI mode"
      UI.OpenDialog(VBox(Label(msg), PushButton(Opt("default"), "&OK")))
      UI.UserInput()
      UI.CloseDialog()


TextModeClient().main()

