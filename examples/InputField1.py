# encoding: utf-8



from libyui import *
class InputField1Client:
    def main(self):
      UI.OpenDialog(VBox(InputField("Name:"), PushButton("&OK")))
      UI.UserInput()
      UI.CloseDialog()


InputField1Client().main()

