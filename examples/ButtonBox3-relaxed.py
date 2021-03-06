# encoding: utf-8



from libyui import *

# Example for ButtonBox: Relaxed sanity check.
#
# Normally, a ButtonBox with more than one button is required to have one
# `okButton and one `cancelButton. With `opt(`relaxSanityCheck), this
# requirement is not enforced.
#
# Still, that option should only be used in very rare exceptions.

class ButtonBox3RelaxedClient:
    def main(self):
      UI.OpenDialog(
        VBox(
          HVCenter(Label("Error: Your CPU is under water.")),
          ButtonBox(
            Opt("relaxSanityCheck"),
            PushButton(Id("ok"), "&OK"),
            PushButton(Id("details"), "&Details...")
          )
        )
      )
      UI.UserInput()
      UI.CloseDialog()

ButtonBox3RelaxedClient().main()
