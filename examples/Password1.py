# encoding: utf-8



from libyui import *
class Password1Client:
    def main(self):
      UI.OpenDialog(VBox(Password("Enter password:"), PushButton("&OK")))
      UI.UserInput()
      UI.CloseDialog()


Password1Client().main()

