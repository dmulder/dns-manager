# encoding: utf-8



from libyui import *
class PushButton1Client:
    def main(self):
      # Build a dialog with one button.
      # Wait until that button is clicked,
      # then close the dialog and terminate.

      UI.OpenDialog(PushButton("&OK"))

      UI.UserInput()
      UI.CloseDialog()


PushButton1Client().main()

