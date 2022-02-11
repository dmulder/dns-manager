# encoding: utf-8


from libyui import *

class ComboBoxEmptyClient:
    def main(self):
      UI.OpenDialog(
        VBox(ComboBox("Select your Pizza:", [""]), PushButton("&OK"))
      )
      UI.UserInput()
      UI.CloseDialog()

ComboBoxEmptyClient().main()
