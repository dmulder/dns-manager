# encoding: utf-8



from libyui import *

class ComboBox1Client:
    def main(self):
      UI.OpenDialog(
        VBox(
          ComboBox("Select your Pizza:", ["Napoli", "Funghi", "Salami"]),
          PushButton("&OK")
        )
      )
      UI.UserInput()
      UI.CloseDialog()

ComboBox1Client().main()
